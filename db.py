from __future__ import annotations

"""
Base de données SQLite — contenu, cartes, révisions, progression.
SRS : algorithme FSRS-4.5 (Free Spaced Repetition Scheduler).

FSRS-4.5 gère deux états par carte :
  - stability (S) : nombre de jours pour que R descende à 90%
  - difficulty (D) : coefficient de difficulté intrinsèque [1, 10]
  - retrievability (R) : probabilité de rappel au moment de la révision

Paramètres FSRS par défaut (entraînés sur des millions de révisions Anki/SuperMemo).
"""

import sqlite3
import json
import math
import os
from datetime import datetime, timedelta
from pathlib import Path

# DATA_DIR : dossier persistant configuré via variable d'environnement
# Sur Railway → monter un volume sur /data et définir DATA_DIR=/data
# En local    → utilise le dossier courant (comportement inchangé)
_data_dir = Path(os.getenv("DATA_DIR", Path(__file__).parent))
_data_dir.mkdir(parents=True, exist_ok=True)
DB_PATH = _data_dir / "scientia.db"


# ── FSRS-4.5 : paramètres et formules ────────────────────────────────────────
#
# Paramètres w[0..16] tirés du papier FSRS-4.5 (Ye, 2023).
# Voir : https://github.com/open-spaced-repetition/fsrs4anki/wiki/The-Algorithm

W = [
    0.4072, 1.1829, 3.1262, 15.4722,   # w0-w3 : initialisation S selon note initiale
    7.2102, 0.5316, 1.0651, 0.0589,    # w4-w7
    1.5330, 0.1544, 1.0071, 1.9395,    # w8-w11
    0.1100, 0.2900, 2.2700, 0.2400,    # w12-w15
    2.9898,                             # w16
]

DECAY    = -0.5
FACTOR   = 0.9 ** (1 / DECAY) - 1   # ≈ 0.1111...
R_TARGET = 0.9                        # Retrievability cible au moment de la révision
AGAIN, HARD, GOOD, EASY = 1, 2, 3, 4  # Mapping score 0→0, 1→1, 2→2, 3→3, 4→4


def _fsrs_retrievability(stability: float, elapsed_days: float) -> float:
    """R(t) = (1 + FACTOR * t / S) ^ DECAY"""
    if stability <= 0:
        return 0.0
    return (1 + FACTOR * elapsed_days / stability) ** DECAY


def _fsrs_next_interval(stability: float) -> int:
    """I = S / FACTOR * (R_TARGET^(1/DECAY) - 1)"""
    interval = stability / FACTOR * (R_TARGET ** (1 / DECAY) - 1)
    return max(1, round(interval))


def _fsrs_init_stability(grade: int) -> float:
    """Stabilité initiale selon la note (première révision d'une carte)."""
    # grade 1=Faible, 2=Partiel, 3=Correct, 4=Excellent
    idx = max(0, min(3, grade - 1))
    return W[idx]


def _fsrs_init_difficulty(grade: int) -> float:
    """Difficulté initiale."""
    d = W[4] - (grade - 3) * W[5]
    return max(1.0, min(10.0, d))


def _fsrs_next_difficulty(d: float, grade: int) -> float:
    """Mise à jour de la difficulté après révision."""
    delta = -W[6] * (grade - 3)
    d_new = d + delta * ((10 - d) / 9)
    # Mean-reversion
    d_new = W[7] * W[4] + (1 - W[7]) * d_new
    return max(1.0, min(10.0, d_new))


def _fsrs_next_stability(s: float, d: float, r: float, grade: int) -> float:
    """
    Calcule la nouvelle stabilité après une révision.
    grade : 1=Again, 2=Hard, 3=Good, 4=Easy

    Note : quand r ≈ 1 (révision très anticipée), le gain de stabilité est minimal
    par conception de l'algorithme FSRS. La stabilité ne diminue jamais suite à une
    révision réussie.
    """
    if grade == AGAIN:
        # Après oubli : reset partiel de la stabilité
        s_new = (
            W[11]
            * (d ** (-W[12]))
            * ((s + 1) ** W[13] - 1)
            * math.exp((1 - r) * W[14])
        )
        return max(0.1, s_new)
    else:
        # Révision réussie (Hard / Good / Easy)
        hard_penalty = W[15] if grade == HARD else 1.0
        easy_bonus   = W[16] if grade == EASY else 1.0
        # Clamp r pour éviter s_new = 0 quand r = 1.0 (révision très anticipée)
        r_eff = min(r, 0.999)
        s_new = (
            s
            * math.exp(W[8])
            * (11 - d)
            * (s ** (-W[9]))
            * (math.exp((1 - r_eff) * W[10]) - 1)
            * hard_penalty
            * easy_bonus
        )
        # La stabilité ne peut qu'augmenter sur une révision réussie
        return max(s, s_new)


def _score_to_grade(score: int) -> int:
    """Convertit le score 0-4 de l'évaluation Claude en grade FSRS 1-4."""
    mapping = {0: 1, 1: 1, 2: 2, 3: 3, 4: 4}
    return mapping.get(score, 1)


# ── Connexion SQLite ──────────────────────────────────────────────────────────

def conn() -> sqlite3.Connection:
    c = sqlite3.connect(DB_PATH)
    c.row_factory = sqlite3.Row
    return c


def init() -> None:
    """Initialise (ou migre) le schéma de la base de données."""
    with conn() as c:
        c.executescript("""
        CREATE TABLE IF NOT EXISTS concepts_contenu (
            concept_id   TEXT PRIMARY KEY,
            contenu_json TEXT NOT NULL,
            version      INTEGER DEFAULT 1,
            genere_le    TEXT DEFAULT (datetime('now'))
        );

        CREATE TABLE IF NOT EXISTS cartes (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            concept_id   TEXT NOT NULL,
            section_num  INTEGER NOT NULL,
            type         TEXT NOT NULL,
            niveau       INTEGER DEFAULT 1,
            enonce       TEXT NOT NULL,
            reponse_ref  TEXT NOT NULL,
            critere      TEXT NOT NULL,
            indice       TEXT,
            langue       TEXT    DEFAULT 'fr',
            -- FSRS state
            stabilite    REAL    DEFAULT 0.0,
            difficulte   REAL    DEFAULT 5.0,
            nb_revisions INTEGER DEFAULT 0,
            cree_le      TEXT DEFAULT (datetime('now'))
        );

        CREATE TABLE IF NOT EXISTS revisions (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            carte_id      INTEGER NOT NULL REFERENCES cartes(id),
            score         INTEGER NOT NULL,
            grade         INTEGER NOT NULL,
            retrievability REAL,
            feedback      TEXT,
            duree_sec     INTEGER,
            revise_le     TEXT DEFAULT (datetime('now')),
            prochaine_rev TEXT
        );

        CREATE TABLE IF NOT EXISTS progression (
            concept_id    TEXT PRIMARY KEY,
            nb_sessions   INTEGER DEFAULT 0,
            score_moyen   REAL    DEFAULT 0.0,
            derniere_rev  TEXT,
            statut        TEXT    DEFAULT 'nouveau'
        );

        CREATE TABLE IF NOT EXISTS notes (
            concept_id   TEXT PRIMARY KEY,
            texte        TEXT NOT NULL DEFAULT '',
            modifie_le   TEXT DEFAULT (datetime('now'))
        );

        -- Sprint A : reprise. Singleton qui mémorise la dernière activité.
        CREATE TABLE IF NOT EXISTS session_state (
            id                 INTEGER PRIMARY KEY CHECK (id = 1),
            derniere_activite  TEXT NOT NULL DEFAULT (datetime('now')),
            derniere_action    TEXT,           -- 'quiz' | 'socratique' | 'lecture'
            concept_id         TEXT,
            index_question     INTEGER DEFAULT 0,
            quiz_scores_json   TEXT DEFAULT '[]',
            quiz_carte_ids_json TEXT DEFAULT '[]',
            quiz_termine       INTEGER DEFAULT 0
        );

        -- Sprint B : persistance des dialogues socratiques.
        CREATE TABLE IF NOT EXISTS dialogues_socratique (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            concept_id    TEXT NOT NULL,
            historique_json TEXT NOT NULL DEFAULT '[]',
            statut        TEXT NOT NULL DEFAULT 'en_cours',  -- 'en_cours' | 'termine'
            resume_json   TEXT,
            cree_le       TEXT DEFAULT (datetime('now')),
            modifie_le    TEXT DEFAULT (datetime('now'))
        );

        CREATE INDEX IF NOT EXISTS idx_dialogues_concept
          ON dialogues_socratique(concept_id, statut);
        """)

        # Migration : ajouter les colonnes FSRS si elles n'existent pas encore
        colonnes_cartes = {
            row[1] for row in c.execute("PRAGMA table_info(cartes)").fetchall()
        }
        for col, defn in [
            ("niveau",       "INTEGER DEFAULT 1"),
            ("stabilite",    "REAL DEFAULT 0.0"),
            ("difficulte",   "REAL DEFAULT 5.0"),
            ("nb_revisions", "INTEGER DEFAULT 0"),
            ("langue",       "TEXT DEFAULT 'fr'"),
        ]:
            if col not in colonnes_cartes:
                c.execute(f"ALTER TABLE cartes ADD COLUMN {col} {defn}")

        colonnes_rev = {
            row[1] for row in c.execute("PRAGMA table_info(revisions)").fetchall()
        }
        for col, defn in [
            ("grade",          "INTEGER DEFAULT 3"),
            ("retrievability", "REAL"),
        ]:
            if col not in colonnes_rev:
                c.execute(f"ALTER TABLE revisions ADD COLUMN {col} {defn}")

        colonnes_contenu = {
            row[1] for row in c.execute("PRAGMA table_info(concepts_contenu)").fetchall()
        }
        if "version" not in colonnes_contenu:
            c.execute("ALTER TABLE concepts_contenu ADD COLUMN version INTEGER DEFAULT 1")


# ── Contenu généré ────────────────────────────────────────────────────────────

CURRENT_CONTENT_VERSION = 2  # Doit correspondre à CONTENT_VERSION dans content_generator.py


def get_contenu(concept_id: str) -> dict | None:
    """Retourne le contenu si présent ET à jour (bonne version)."""
    with conn() as c:
        row = c.execute(
            "SELECT contenu_json, version FROM concepts_contenu WHERE concept_id = ?",
            (concept_id,)
        ).fetchone()
    if not row:
        return None
    if (row["version"] or 1) < CURRENT_CONTENT_VERSION:
        return None  # Forcer la régénération
    return json.loads(row["contenu_json"])


def sauvegarder_contenu(concept_id: str, contenu: dict) -> None:
    version = contenu.get("version", 1)
    with conn() as c:
        c.execute(
            """INSERT INTO concepts_contenu (concept_id, contenu_json, version)
               VALUES (?, ?, ?)
               ON CONFLICT(concept_id) DO UPDATE SET
               contenu_json = excluded.contenu_json,
               version      = excluded.version,
               genere_le    = datetime('now')""",
            (concept_id, json.dumps(contenu, ensure_ascii=False), version)
        )
        # Recréer les cartes (les anciennes révisions sont conservées par FK)
        c.execute("DELETE FROM cartes WHERE concept_id = ?", (concept_id,))
        for section in contenu.get("sections", []):
            q = section.get("question", {})
            if q:
                c.execute(
                    """INSERT INTO cartes
                       (concept_id, section_num, type, niveau,
                        enonce, reponse_ref, critere, indice)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                    (concept_id, section["numero"],
                     q.get("type", ""),
                     q.get("niveau", section["numero"]),
                     q.get("enonce", ""),
                     q.get("reponse_ref", ""),
                     q.get("critere", ""),
                     q.get("indice", ""))
                )


# ── Révisions avec FSRS ───────────────────────────────────────────────────────

def sauvegarder_revision(carte_id: int, score: int,
                         feedback: str, duree_sec: int = 0) -> None:
    """
    Enregistre une révision et met à jour l'état FSRS de la carte.
    """
    grade = _score_to_grade(score)

    with conn() as c:
        # Lire l'état courant de la carte
        row = c.execute(
            "SELECT stabilite, difficulte, nb_revisions, cree_le FROM cartes WHERE id = ?",
            (carte_id,)
        ).fetchone()
        if not row:
            return

        s_old = row["stabilite"]
        d_old = row["difficulte"]
        n     = row["nb_revisions"]

        # Calculer l'elapsed depuis la création ou dernière révision
        last_rev = c.execute(
            "SELECT MAX(revise_le) as lr FROM revisions WHERE carte_id = ?",
            (carte_id,)
        ).fetchone()["lr"]
        ref_date = last_rev or row["cree_le"]
        try:
            ref_dt = datetime.fromisoformat(ref_date[:19])
        except Exception:
            ref_dt = datetime.now()
        elapsed_days = max(0.0, (datetime.now() - ref_dt).total_seconds() / 86400)

        # ── Calculer nouveaux paramètres FSRS ────────────────────────────────
        if n == 0:
            # Première révision : initialisation
            s_new = _fsrs_init_stability(grade)
            d_new = _fsrs_init_difficulty(grade)
            r_cur = 1.0
        else:
            r_cur = _fsrs_retrievability(s_old, elapsed_days)
            s_new = _fsrs_next_stability(s_old, d_old, r_cur, grade)
            d_new = _fsrs_next_difficulty(d_old, grade)

        interval = _fsrs_next_interval(s_new)
        prochaine = (datetime.now() + timedelta(days=interval)).strftime("%Y-%m-%d")

        # Enregistrer la révision
        c.execute(
            """INSERT INTO revisions
               (carte_id, score, grade, retrievability, feedback, duree_sec, prochaine_rev)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (carte_id, score, grade, r_cur, feedback, duree_sec, prochaine)
        )

        # Mettre à jour l'état FSRS de la carte
        c.execute(
            """UPDATE cartes
               SET stabilite    = ?,
                   difficulte   = ?,
                   nb_revisions = nb_revisions + 1
               WHERE id = ?""",
            (s_new, d_new, carte_id)
        )


def get_carte(carte_id: int) -> dict | None:
    with conn() as c:
        row = c.execute(
            "SELECT * FROM cartes WHERE id = ?", (carte_id,)
        ).fetchone()
    return dict(row) if row else None


def get_cartes_dues() -> list[dict]:
    """Retourne les cartes dont la prochaine révision est aujourd'hui ou passée."""
    today = datetime.now().strftime("%Y-%m-%d")
    with conn() as c:
        rows = c.execute(
            """SELECT c.*, r.prochaine_rev, r.score as dernier_score,
                      r.grade as dernier_grade
               FROM cartes c
               JOIN (
                   SELECT carte_id, MAX(revise_le) as max_rev
                   FROM revisions GROUP BY carte_id
               ) latest ON c.id = latest.carte_id
               JOIN revisions r ON r.carte_id = c.id
                                AND r.revise_le = latest.max_rev
               WHERE r.prochaine_rev <= ?
               ORDER BY r.prochaine_rev ASC, c.niveau ASC""",
            (today,)
        ).fetchall()
    return [dict(r) for r in rows]


def nb_cartes_dues() -> int:
    return len(get_cartes_dues())


# ── Progression ───────────────────────────────────────────────────────────────

def maj_progression(concept_id: str, scores: list[int]) -> None:
    if not scores:
        return
    score_moyen = sum(scores) / len(scores)
    statut = "maitrise" if score_moyen >= 3.0 else "en_cours"
    with conn() as c:
        c.execute(
            """INSERT INTO progression (concept_id, nb_sessions, score_moyen,
               derniere_rev, statut)
               VALUES (?, 1, ?, datetime('now'), ?)
               ON CONFLICT(concept_id) DO UPDATE SET
               nb_sessions  = nb_sessions + 1,
               score_moyen  = (score_moyen * nb_sessions + ?) / (nb_sessions + 1),
               derniere_rev = datetime('now'),
               statut       = ?""",
            (concept_id, score_moyen, statut, score_moyen, statut)
        )


def get_progression(concept_id: str) -> dict | None:
    with conn() as c:
        row = c.execute(
            "SELECT * FROM progression WHERE concept_id = ?", (concept_id,)
        ).fetchone()
    return dict(row) if row else None


def get_toute_progression() -> dict[str, dict]:
    with conn() as c:
        rows = c.execute("SELECT * FROM progression").fetchall()
    return {r["concept_id"]: dict(r) for r in rows}


# ── Notes persistantes ────────────────────────────────────────────────────────

def get_note(concept_id: str) -> str:
    with conn() as c:
        row = c.execute(
            "SELECT texte FROM notes WHERE concept_id = ?", (concept_id,)
        ).fetchone()
    return row["texte"] if row else ""


def save_note(concept_id: str, texte: str) -> None:
    with conn() as c:
        c.execute(
            """INSERT INTO notes (concept_id, texte, modifie_le)
               VALUES (?, ?, datetime('now'))
               ON CONFLICT(concept_id) DO UPDATE SET
               texte      = excluded.texte,
               modifie_le = datetime('now')""",
            (concept_id, texte)
        )


def get_toutes_notes() -> dict[str, str]:
    """Retourne toutes les notes non-vides {concept_id: texte}."""
    with conn() as c:
        rows = c.execute(
            "SELECT concept_id, texte FROM notes WHERE texte != ''"
        ).fetchall()
    return {r["concept_id"]: r["texte"] for r in rows}


# ── Planning — prochaines révisions par concept ───────────────────────────────

def get_prochaine_rev_par_concept() -> dict[str, str]:
    """
    Retourne un dict concept_id → date (YYYY-MM-DD) de la prochaine révision.
    Seule la carte dont la révision est la plus proche est retenue par concept.
    """
    with conn() as c:
        rows = c.execute(
            """SELECT c.concept_id, MIN(r.prochaine_rev) as prochaine
               FROM cartes c
               JOIN (
                   SELECT carte_id, MAX(revise_le) as max_rev
                   FROM revisions GROUP BY carte_id
               ) latest ON c.id = latest.carte_id
               JOIN revisions r ON r.carte_id = c.id
                                AND r.revise_le = latest.max_rev
               WHERE r.prochaine_rev IS NOT NULL
               GROUP BY c.concept_id"""
        ).fetchall()
    return {r["concept_id"]: r["prochaine"] for r in rows}


def get_toutes_dates_revision() -> list[str]:
    """Retourne toutes les dates de révision (pour calcul du streak)."""
    with conn() as c:
        rows = c.execute(
            "SELECT DISTINCT date(revise_le) as jour FROM revisions ORDER BY jour DESC"
        ).fetchall()
    return [r["jour"] for r in rows]


def get_planning_14j() -> list[dict]:
    """
    Retourne la liste des révisions prévues dans les 14 prochains jours,
    regroupées par date.
    """
    today = datetime.now().date()
    fin   = today + timedelta(days=14)
    with conn() as c:
        rows = c.execute(
            """SELECT c.concept_id, c.enonce, r.prochaine_rev
               FROM cartes c
               JOIN (
                   SELECT carte_id, MAX(revise_le) as max_rev
                   FROM revisions GROUP BY carte_id
               ) latest ON c.id = latest.carte_id
               JOIN revisions r ON r.carte_id = c.id
                                AND r.revise_le = latest.max_rev
               WHERE r.prochaine_rev BETWEEN ? AND ?
               ORDER BY r.prochaine_rev ASC""",
            (today.isoformat(), fin.isoformat())
        ).fetchall()
    return [dict(r) for r in rows]


# ── Helpers haut niveau pour cartes (utilisés par streamlit_app.py) ───────────

def get_cartes_concept(concept_id: str) -> list[dict]:
    """Retourne toutes les cartes liées à un concept."""
    with conn() as c:
        rows = c.execute(
            "SELECT * FROM cartes WHERE concept_id = ? ORDER BY id ASC",
            (concept_id,)
        ).fetchall()
    return [dict(r) for r in rows]


def _coerce_str(v) -> str:
    """
    Sécurise une valeur pour insertion SQLite TEXT.
    Claude peut parfois renvoyer une liste ou un dict pour un champ
    où on attend une chaîne — on aplatit proprement.
    """
    if v is None:
        return ""
    if isinstance(v, str):
        return v
    if isinstance(v, (list, tuple)):
        return "; ".join(_coerce_str(x) for x in v)
    if isinstance(v, dict):
        return "; ".join(f"{k}: {_coerce_str(val)}" for k, val in v.items())
    return str(v)


def sauvegarder_cartes(concept_id: str, questions: list[dict],
                        langue: str = "fr") -> list[int]:
    """
    Persiste une liste de questions générées par generator.py
    et retourne la liste des id des cartes créées.

    Convertit le format generator (question, difficulte) → format DB
    (enonce, niveau). Coerce les champs texte au cas où Claude renvoie
    une liste plutôt qu'une chaîne.

    `langue` est mémorisée par carte pour ne plus dépendre du dict CURRICULUM
    au moment de l'évaluation.
    """
    ids: list[int] = []
    with conn() as c:
        c.execute("DELETE FROM cartes WHERE concept_id = ?", (concept_id,))
        for i, q in enumerate(questions, start=1):
            q_langue = q.get("langue") or langue
            cur = c.execute(
                """INSERT INTO cartes
                   (concept_id, section_num, type, niveau,
                    enonce, reponse_ref, critere, indice, langue)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (concept_id, i,
                 _coerce_str(q.get("type", "")),
                 int(q.get("difficulte", q.get("niveau", 1)) or 1),
                 _coerce_str(q.get("question", q.get("enonce", ""))),
                 _coerce_str(q.get("reponse_ref", "")),
                 _coerce_str(q.get("critere", "")),
                 _coerce_str(q.get("indice", "")),
                 _coerce_str(q_langue) or "fr")
            )
            ids.append(cur.lastrowid)
    return ids


# ══════════════════════════════════════════════════════════════════════════════
# SPRINT A — Reprise de session (table session_state, singleton)
# ══════════════════════════════════════════════════════════════════════════════

def set_derniere_activite(action: str | None,
                           concept_id: str | None = None,
                           index_question: int = 0,
                           quiz_scores: list[int] | None = None,
                           quiz_carte_ids: list[int] | None = None,
                           termine: bool = False) -> None:
    """
    Mémorise la dernière activité de l'utilisateur.

    action ∈ {'quiz', 'socratique', 'lecture', None}.
    None efface l'activité (reprise impossible).
    """
    with conn() as c:
        c.execute(
            """INSERT INTO session_state
               (id, derniere_activite, derniere_action, concept_id,
                index_question, quiz_scores_json, quiz_carte_ids_json,
                quiz_termine)
               VALUES (1, datetime('now'), ?, ?, ?, ?, ?, ?)
               ON CONFLICT(id) DO UPDATE SET
                  derniere_activite    = datetime('now'),
                  derniere_action      = excluded.derniere_action,
                  concept_id           = excluded.concept_id,
                  index_question       = excluded.index_question,
                  quiz_scores_json     = excluded.quiz_scores_json,
                  quiz_carte_ids_json  = excluded.quiz_carte_ids_json,
                  quiz_termine         = excluded.quiz_termine""",
            (action,
             concept_id,
             int(index_question or 0),
             json.dumps(list(quiz_scores or [])),
             json.dumps(list(quiz_carte_ids or [])),
             1 if termine else 0)
        )


def get_derniere_activite() -> dict | None:
    """
    Retourne la dernière activité non terminée, ou None.

    Si quiz_termine=1, on considère qu'il n'y a rien à reprendre.
    """
    with conn() as c:
        row = c.execute(
            "SELECT * FROM session_state WHERE id = 1"
        ).fetchone()
    if not row:
        return None
    d = dict(row)
    if d.get("quiz_termine"):
        return None
    if not d.get("derniere_action"):
        return None
    try:
        d["quiz_scores"] = json.loads(d.get("quiz_scores_json") or "[]")
    except Exception:
        d["quiz_scores"] = []
    try:
        d["quiz_carte_ids"] = json.loads(d.get("quiz_carte_ids_json") or "[]")
    except Exception:
        d["quiz_carte_ids"] = []
    return d


def effacer_derniere_activite() -> None:
    """Marque la session comme terminée (rien à reprendre)."""
    with conn() as c:
        c.execute(
            "UPDATE session_state SET quiz_termine = 1, derniere_action = NULL "
            "WHERE id = 1"
        )


# ══════════════════════════════════════════════════════════════════════════════
# SPRINT B — Persistance des dialogues socratiques
# ══════════════════════════════════════════════════════════════════════════════

def get_dialogue_socratique_actif(concept_id: str) -> dict | None:
    """Retourne le dialogue 'en_cours' le plus récent pour ce concept, ou None."""
    with conn() as c:
        row = c.execute(
            """SELECT * FROM dialogues_socratique
               WHERE concept_id = ? AND statut = 'en_cours'
               ORDER BY modifie_le DESC LIMIT 1""",
            (concept_id,)
        ).fetchone()
    if not row:
        return None
    d = dict(row)
    try:
        d["historique"] = json.loads(d.get("historique_json") or "[]")
    except Exception:
        d["historique"] = []
    return d


def get_dialogue_socratique_par_id(dialogue_id: int) -> dict | None:
    with conn() as c:
        row = c.execute(
            "SELECT * FROM dialogues_socratique WHERE id = ?", (dialogue_id,)
        ).fetchone()
    if not row:
        return None
    d = dict(row)
    try:
        d["historique"] = json.loads(d.get("historique_json") or "[]")
    except Exception:
        d["historique"] = []
    if d.get("resume_json"):
        try:
            d["resume"] = json.loads(d["resume_json"])
        except Exception:
            d["resume"] = None
    return d


def sauvegarder_dialogue_socratique(concept_id: str,
                                      historique: list[dict],
                                      dialogue_id: int | None = None) -> int:
    """
    Sauvegarde un dialogue socratique en cours.
    Si dialogue_id est fourni, met à jour. Sinon insère.
    Retourne l'id du dialogue.
    """
    payload = json.dumps(historique, ensure_ascii=False)
    with conn() as c:
        if dialogue_id is None:
            cur = c.execute(
                """INSERT INTO dialogues_socratique
                   (concept_id, historique_json, statut)
                   VALUES (?, ?, 'en_cours')""",
                (concept_id, payload)
            )
            return cur.lastrowid
        else:
            c.execute(
                """UPDATE dialogues_socratique
                   SET historique_json = ?, modifie_le = datetime('now')
                   WHERE id = ?""",
                (payload, dialogue_id)
            )
            return dialogue_id


def terminer_dialogue_socratique(dialogue_id: int, resume: dict) -> None:
    """Marque un dialogue comme terminé et y attache le résumé."""
    with conn() as c:
        c.execute(
            """UPDATE dialogues_socratique
               SET statut = 'termine',
                   resume_json = ?,
                   modifie_le = datetime('now')
               WHERE id = ?""",
            (json.dumps(resume, ensure_ascii=False), dialogue_id)
        )


# ══════════════════════════════════════════════════════════════════════════════
# SPRINT D — Streak, recommandation, reset, export
# ══════════════════════════════════════════════════════════════════════════════

def get_streak_jours() -> int:
    """
    Calcule le streak (jours consécutifs avec au moins une révision)
    en remontant à partir d'aujourd'hui.
    """
    jours = get_toutes_dates_revision()
    if not jours:
        return 0
    aujourd = datetime.now().date()
    # Convertir en set pour lookup O(1)
    set_jours = set()
    for j in jours:
        try:
            set_jours.add(datetime.strptime(j, "%Y-%m-%d").date())
        except Exception:
            continue
    streak = 0
    cursor = aujourd
    # Tolère qu'aujourd'hui n'ait pas encore de révision : on compte à partir
    # d'hier dans ce cas.
    if aujourd not in set_jours:
        cursor = aujourd - timedelta(days=1)
    while cursor in set_jours:
        streak += 1
        cursor = cursor - timedelta(days=1)
    return streak


def reset_progression_concept(concept_id: str) -> None:
    """Supprime cartes, révisions et progression pour un concept donné."""
    with conn() as c:
        # Récupérer les cartes pour effacer leurs révisions
        carte_rows = c.execute(
            "SELECT id FROM cartes WHERE concept_id = ?", (concept_id,)
        ).fetchall()
        carte_ids = [r["id"] for r in carte_rows]
        if carte_ids:
            placeholders = ",".join("?" * len(carte_ids))
            c.execute(
                f"DELETE FROM revisions WHERE carte_id IN ({placeholders})",
                tuple(carte_ids)
            )
        c.execute("DELETE FROM cartes WHERE concept_id = ?", (concept_id,))
        c.execute("DELETE FROM progression WHERE concept_id = ?", (concept_id,))
        # Si la session courante portait sur ce concept, on la termine
        c.execute(
            "UPDATE session_state SET quiz_termine = 1, derniere_action = NULL "
            "WHERE id = 1 AND concept_id = ?", (concept_id,)
        )


def export_progression_csv() -> str:
    """
    Retourne un CSV (avec en-tête) de la progression de tous les concepts
    avec révisions. Format : concept_id, nb_sessions, score_moyen,
    statut, derniere_rev, nb_cartes, nb_revisions.
    """
    import csv
    from io import StringIO
    buf = StringIO()
    writer = csv.writer(buf)
    writer.writerow([
        "concept_id", "nb_sessions", "score_moyen", "statut",
        "derniere_rev", "nb_cartes", "nb_revisions",
    ])
    with conn() as c:
        rows = c.execute("""
            SELECT p.concept_id, p.nb_sessions, p.score_moyen, p.statut,
                   p.derniere_rev,
                   (SELECT COUNT(*) FROM cartes WHERE concept_id = p.concept_id)
                     AS nb_cartes,
                   (SELECT COUNT(*) FROM revisions r
                     JOIN cartes c2 ON c2.id = r.carte_id
                     WHERE c2.concept_id = p.concept_id) AS nb_revisions
            FROM progression p
            ORDER BY p.concept_id
        """).fetchall()
    for r in rows:
        writer.writerow([
            r["concept_id"], r["nb_sessions"],
            f"{(r['score_moyen'] or 0):.2f}",
            r["statut"], r["derniere_rev"] or "",
            r["nb_cartes"], r["nb_revisions"],
        ])
    return buf.getvalue()


# ── Alias pour compatibilité avec l'ancien scientia.py ────────────────────────

initialiser_db = init
mettre_a_jour_progression = maj_progression


def afficher_progression() -> None:
    """Imprime un résumé de progression sur stdout (utilisé par scientia.py)."""
    progression = get_toute_progression()
    if not progression:
        print("  Aucune progression enregistrée pour l'instant.")
        return
    for cid, p in sorted(progression.items()):
        statut = p.get("statut", "?")
        moyenne = p.get("score_moyen", 0.0) or 0.0
        nb = p.get("nb_sessions", 0)
        print(f"  • {cid:40s}  {statut:10s}  {moyenne:.2f}/4  ({nb} sess.)")
