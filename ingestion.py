"""
Ingestion de documents externes dans le curriculum Scientia.

Supporte PDF, Markdown, TXT.
Appelle Claude pour extraire des concepts pédagogiques
et les sauvegarde dans dynamic_concepts.json.
"""

from __future__ import annotations

import json
import re
import unicodedata
from datetime import datetime
from pathlib import Path

import anthropic

# ── Chemins ───────────────────────────────────────────────────────────────────

BASE_DIR     = Path(__file__).parent
DOCS_DIR     = BASE_DIR / "docs"
DYNAMIC_FILE = BASE_DIR / "dynamic_concepts.json"

# ── Client Claude ─────────────────────────────────────────────────────────────

client = anthropic.Anthropic()

# ── Extraction de texte ───────────────────────────────────────────────────────

def extraire_texte(filepath: Path) -> str:
    """Extrait le texte brut d'un fichier PDF, Markdown ou TXT."""
    ext = filepath.suffix.lower()

    if ext == ".pdf":
        return _extraire_pdf(filepath)
    elif ext in (".md", ".txt"):
        return filepath.read_text(encoding="utf-8")
    else:
        raise ValueError(f"Format non supporté : {ext}. Utilise PDF, MD ou TXT.")


def _extraire_pdf(filepath: Path) -> str:
    try:
        import pypdf
    except ImportError:
        raise ImportError(
            "pypdf n'est pas installé. Lance : pip install pypdf --break-system-packages"
        )

    texte_pages = []
    reader = pypdf.PdfReader(str(filepath))
    for page in reader.pages:
        t = page.extract_text()
        if t:
            texte_pages.append(t.strip())
    return "\n\n".join(texte_pages)


# ── Découpage en concepts ─────────────────────────────────────────────────────

PROMPT_DECOUPAGE = """Tu reçois le texte brut d'un document. Ton travail :
extraire 1 à 5 concepts pédagogiques distincts à intégrer dans Scientia,
système de révision espacée (style Anki) utilisé pour la pratique
professionnelle.

CONTEXTE D'USAGE — Dominic-André Leclerc, fondateur de Nord Paradigm
(Québec), cabinet de conseil en gouvernance d'IA. 21+ ans RCAF, auditeur
AF9000+ sur systèmes aéronautiques. Il alimente Scientia avec des textes
qu'il rencontre dans sa pratique : décisions de la CAI, articles de
règlements (Loi 25, EU AI Act, AIDA, RGPD), normes (ISO/IEC 42001,
27001, 27701), publications NIST, lignes directrices de l'AI Office,
décisions EDPB, jurisprudence, articles académiques sur la gouvernance
de l'IA et l'audit.

Chaque concept doit :
- Cibler une SEULE idée claire, mémorable, testable par des questions.
- Avoir un texte de référence de 200 à 400 mots, dense mais ACCESSIBLE.
- Porter un titre court et mémorable (3 à 8 mots).
- Privilégier les éléments DIRECTEMENT UTILISABLES en mission client :
  articles précis, seuils de sanction, calendriers, échéances,
  obligations cumulatives, cas d'application, points de friction
  fréquents avec d'autres cadres.

NIVEAU DE LANGUE — IMPORTANT :
- Dominic a un SECONDAIRE 5, pas un doctorat. Écris en FRANÇAIS QUOTIDIEN.
- Phrases COURTES. Vocabulaire COURANT.
- Pas de jargon académique inutile, pas de nominalisations empilées.
- Garde les noms techniques inévitables (Loi 25, ISO 42001, EU AI Act, RPRP, EFVP, etc.) — ils sont nécessaires pour ses missions. Mais EXPLIQUE-les en termes simples la première fois.
- Tutoiement.

Règles de découpage :
- Un long document → plusieurs concepts atomiques (max 5).
- Un court article → 1 à 2 concepts.
- Privilégie la profondeur sur la largeur : 2 bons concepts > 5 superficiels.
- Le texte de chaque concept doit être auto-suffisant.

Retourne UNIQUEMENT un tableau JSON valide. Pas de markdown, pas de backticks.
Format exact :
[
  {
    "titre": "Titre mémorable du concept",
    "texte": "Texte de référence complet (200-400 mots). Prose dense, articles précis, exemples concrets.",
    "module_suggere": "Suggestion de thème (ex: Gouvernance IA — Loi 25, Gouvernance IA — EU AI Act, Audit ISO 42001, NIST AI RMF, Jurisprudence CAI, ...)"
  }
]"""


def extraire_concepts(texte_brut: str, nom_fichier: str) -> list[dict]:
    """
    Appelle Claude pour extraire 1-5 concepts pédagogiques du texte.
    Retourne une liste de dicts {titre, texte, module_suggere}.
    """
    # Tronquer si trop long (garder les 12000 premiers caractères)
    texte_tronque = texte_brut[:12000]
    if len(texte_brut) > 12000:
        texte_tronque += "\n\n[... document tronqué pour l'extraction ...]"

    prompt = f"""Fichier source : {nom_fichier}

Texte à analyser :
{texte_tronque}

Extrais les concepts pédagogiques clés selon les instructions."""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4000,
        system=PROMPT_DECOUPAGE,
        messages=[{"role": "user", "content": prompt}],
    )

    raw = message.content[0].text.strip()
    raw = re.sub(r"^```(?:json)?\s*", "", raw)
    raw = re.sub(r"\s*```$", "", raw)
    return json.loads(raw)


# ── Gestion des concepts dynamiques ──────────────────────────────────────────

def charger_concepts_dynamiques() -> dict:
    """Charge et retourne le dict des concepts dynamiques (peut être vide)."""
    if not DYNAMIC_FILE.exists():
        return {}
    try:
        return json.loads(DYNAMIC_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}


def sauvegarder_concepts_dynamiques(concepts: dict) -> None:
    DYNAMIC_FILE.write_text(
        json.dumps(concepts, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )


def _slugifier(texte: str) -> str:
    """Transforme un titre en clé slug sans accents."""
    nfkd = unicodedata.normalize("NFKD", texte)
    ascii_str = nfkd.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^\w\s-]", "", ascii_str).strip().lower()
    slug = re.sub(r"[\s_-]+", "_", slug)
    return slug[:50]


def _prochain_ordre(concepts_existants: dict) -> int:
    """Retourne le prochain numéro d'ordre dans le module 5."""
    ordres = [
        v["ordre"] for v in concepts_existants.values()
        if v.get("module") == 5
    ]
    return max(ordres, default=0) + 1


# ── Point d'entrée principal ──────────────────────────────────────────────────

def lister_docs_disponibles() -> list[Path]:
    """Retourne les fichiers ingérables dans docs/."""
    extensions = {".pdf", ".md", ".txt"}
    return sorted([
        p for p in DOCS_DIR.iterdir()
        if p.suffix.lower() in extensions and p.name != "LISEZ_MOI.md"
    ])


def ingerer_fichier(filepath: Path, print_fn=print) -> list[str]:
    """
    Ingère un fichier dans le curriculum dynamique.
    Retourne la liste des clés de concepts créés.
    """
    print_fn(f"\n  Lecture de {filepath.name}...")
    texte = extraire_texte(filepath)

    if not texte.strip():
        raise ValueError("Le fichier est vide ou illisible.")

    print_fn(f"  {len(texte)} caractères extraits.")
    print_fn("  Analyse par Claude — extraction des concepts...")

    concepts_bruts = extraire_concepts(texte, filepath.name)

    if not concepts_bruts:
        raise ValueError("Claude n'a extrait aucun concept de ce document.")

    print_fn(f"  {len(concepts_bruts)} concept(s) identifié(s).")

    concepts_existants = charger_concepts_dynamiques()
    nouvelles_cles = []

    for cb in concepts_bruts:
        base_slug = f"doc_{_slugifier(cb['titre'])}"

        # Éviter les doublons de clé
        cle = base_slug
        i = 2
        while cle in concepts_existants:
            cle = f"{base_slug}_{i}"
            i += 1

        concepts_existants[cle] = {
            "module": 5,
            "ordre": _prochain_ordre(concepts_existants),
            "titre": cb["titre"],
            "prereqs": [],
            "texte": cb["texte"],
            "source": filepath.name,
            "module_suggere": cb.get("module_suggere", "Document"),
            "date_ingestion": datetime.now().strftime("%Y-%m-%d %H:%M"),
        }
        nouvelles_cles.append(cle)

    sauvegarder_concepts_dynamiques(concepts_existants)
    return nouvelles_cles


def supprimer_concept(cle: str) -> bool:
    """Supprime un concept dynamique. Retourne True si réussi."""
    concepts = charger_concepts_dynamiques()
    if cle not in concepts:
        return False
    del concepts[cle]
    sauvegarder_concepts_dynamiques(concepts)
    return True
