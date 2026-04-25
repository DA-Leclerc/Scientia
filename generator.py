"""
Générateur de questions via Claude API.
Prend un concept (texte + titre) et génère des questions de types variés.
"""

import anthropic
import json
import re

client = anthropic.Anthropic()

TYPES_QUESTIONS = {
    "definition": "Définition atomique — tester la compréhension d'un terme précis",
    "cloze": "Cloze — compléter une formule ou phrase clé avec le terme manquant",
    "intuition": "Intuition — expliquer POURQUOI, pas seulement QUOI",
    "contre_exemple": "Contre-exemple — trouver un cas où un principe ne s'applique pas ou est mal compris",
    "application": "Application — utiliser le concept sur un exemple concret",
    "connexion": "Connexion — relier ce concept à un autre déjà vu",
    "erreur_frequente": "Erreur fréquente — identifier et corriger un raisonnement incorrect",
}

PROMPT_SYSTEME = """Tu es un expert en gouvernance de l'IA, en cadres réglementaires (Loi 25, AIDA/LIAD, EU AI Act, ISO/IEC 42001, NIST AI RMF, OCDE) et en conception de questions pédagogiques de niveau professionnel.

PROFIL DE L'APPRENANT — Dominic-André Leclerc, fondateur de Nord Paradigm (Québec), conseil en gouvernance d'IA. 21+ ans dans la Force aérienne royale canadienne (RCAF), ex-officier de conformité qualité certifié AF9000+ sur systèmes aéronautiques complexes. Il approfondit ses connaissances pour livrer ses services à des clients de moyenne et grande taille au Canada : Brèche (analyse de risque IA gratuite), Brèche Pro (évaluation de gouvernance RADAR), Prisme (audit interne ISO 42001).

POSTURE PÉDAGOGIQUE — Dominic est un PRATICIEN AVANCÉ, pas un débutant. Pose des questions de niveau professionnel : arbitrages de mise en conformité, jurisprudence CAI / EDPB, articulation entre cadres, scénarios de cabinet de conseil, points où l'application réelle diverge de la lettre du texte. Évite la simple récitation.

EXEMPLES — privilégie systématiquement :
- Cas concrets d'organisations canadiennes (publiques, OBNL, PME, grandes entreprises) confrontées à des décisions de conformité.
- Décisions documentées de la CAI (Québec), de l'AI Office (UE), et autres enforcement actions.
- Arbitrages d'audit ISO 42001 (Annexe A, Statement of Applicability, audits Stage 1/2, gestion des non-conformités).
- Articulation Loi 25 ↔ RGPD ↔ EU AI Act ↔ NIST RMF dans des cas de chaîne de valeur internationale.
- Parallèles avec les systèmes qualité aérospatiaux (AF9000, AS9100, audits qualité de complexité critique) où c'est pédagogiquement éclairant.

À ÉVITER ABSOLUMENT — exemples tirés du jiu-jitsu brésilien, du sport, de l'apprentissage moteur, de la psychométrie ou de la finance personnelle. Ces thèmes appartiennent à un autre apprenant et ne sont pas pertinents pour Nord Paradigm. Si un concept de stats est nécessaire, prends un exemple lié à l'audit ou à l'IA (ex : taux de faux positifs d'un système de détection de fraude, p-value d'un test A/B sur un modèle de scoring).

RÈGLES ABSOLUES :
1. Une seule idée par question. Jamais deux concepts dans une seule question.
2. Les questions testent la COMPRÉHENSION et la CAPACITÉ D'APPLICATION, pas la mémorisation brute.
3. Français du Québec; tutoiement. Termes techniques anglais établis acceptés (GPAI, AIA, FRIA, EFVP, AIMS, AISA, etc.).
4. La réponse de référence doit être concise (2-5 phrases max).
5. Le critère d'évaluation doit indiquer les éléments ESSENTIELS de la bonne réponse.

IMPORTANT sur le JSON : retourne UNIQUEMENT du JSON valide, sans markdown, sans backticks.
"""

def generer_questions(concept: dict, n: int = 5) -> list[dict]:
    """
    Génère n questions pour un concept donné.
    Retourne une liste de dicts avec : type, question, reponse_ref, critere, difficulte.
    """
    types_choisis = list(TYPES_QUESTIONS.keys())[:n]

    prompt = f"""Concept à enseigner : {concept['titre']}

Texte source :
{concept['texte']}

Génère exactement {n} questions de types variés pour ce concept.
Utilise ces types dans cet ordre : {', '.join(types_choisis[:n])}

Pour chaque question, fournis un objet JSON avec ces champs :
- "type" : le type de question
- "question" : la question posée à Dominic (tu/toi)
- "reponse_ref" : la réponse de référence complète
- "critere" : CHAÎNE DE CARACTÈRES unique listant les 2-3 éléments ESSENTIELS que la réponse doit contenir, séparés par "; ". Pas de tableau JSON, juste une chaîne.
- "indice" : CHAÎNE de 1 phrase max qui pointe vers la réponse sans la donner. Active le rappel actif (ex: « Pense à ce qui distingue X de Y… » ou « Quel article du règlement traite ce cas? »). PAS la réponse, PAS un mot-clé seul.
- "difficulte" : 1 (facile), 2 (moyen), 3 (difficile)

Retourne un tableau JSON de {n} objets. Rien d'autre. Pas de markdown. Juste le JSON."""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=6000,
        system=PROMPT_SYSTEME,
        messages=[{"role": "user", "content": prompt}],
    )

    contenu = message.content[0].text.strip()

    # Nettoyer si markdown accidentel
    contenu = re.sub(r"^```(?:json)?\n?", "", contenu)
    contenu = re.sub(r"\n?```$", "", contenu)

    # Sécurité : si le JSON est tronqué, tenter de couper proprement
    # à la dernière question complète.
    try:
        questions = json.loads(contenu)
    except json.JSONDecodeError:
        # Cherche le dernier "}" suivi d'une virgule ou d'un crochet
        # fermant pour récupérer un tableau partiel valide.
        match = re.search(r"^(\[.*?\}),?\s*[^}]*$", contenu, re.DOTALL)
        if match:
            partial = match.group(1) + "]"
            questions = json.loads(partial)
        else:
            raise
    return questions


def evaluer_reponse(question: dict, reponse_utilisateur: str) -> dict:
    """
    Évalue la réponse de l'utilisateur.
    Retourne : score (0-4), feedback, correct (bool).
    Score : 0=blanc, 1=faux, 2=partiel, 3=bon, 4=excellent
    """
    prompt = f"""Type de question : {question['type']}
Question posée : {question['question']}
Réponse de référence : {question['reponse_ref']}
Critères essentiels : {question['critere']}

Réponse de Dominic : {reponse_utilisateur}

Évalue cette réponse et retourne un objet JSON avec :
- "score" : entier de 0 à 4
  0 = aucune réponse ou complètement faux
  1 = faux avec une légère compréhension
  2 = partiellement correct, manque des éléments essentiels
  3 = correct, tous les éléments essentiels présents
  4 = excellent, complet et précis
- "correct" : true si score >= 3, false sinon
- "feedback" : 2-3 phrases maximum. Si incorrect/partiel : explique CE QUI MANQUE
  et donne la réponse correcte. Si correct : confirme et ajoute une nuance utile.
- "element_manquant" : null si correct, sinon le concept clé qui manque

Retourne UNIQUEMENT le JSON. Pas de markdown."""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}],
    )

    contenu = message.content[0].text.strip()
    contenu = re.sub(r"^```(?:json)?\n?", "", contenu)
    contenu = re.sub(r"\n?```$", "", contenu)

    return json.loads(contenu)


# ── Dialogue socratique ───────────────────────────────────────────────────────

PROMPT_SOCRATIQUE = """Tu es un tuteur SOCRATIQUE de niveau senior en gouvernance de l'IA, qui dialogue avec un PAIR PROFESSIONNEL — pas un étudiant.

PROFIL DE L'INTERLOCUTEUR — Dominic-André Leclerc, fondateur de Nord Paradigm (cabinet de conseil en gouvernance d'IA, Québec). 21+ ans RCAF, auditeur AF9000+ sur systèmes aéronautiques. Il maîtrise déjà les bases ; il vient pour AFFINER son raisonnement, tester ses arbitrages, identifier ses angles morts. Posture : entretien collégial entre praticiens, pas leçon magistrale.

RÈGLES DU DIALOGUE SOCRATIQUE :
1. Ne donne JAMAIS la réponse directement. Avance par questions et reformulations.
2. Sonde les zones floues, fais émerger les tensions entre cadres réglementaires.
3. Quand il dit quelque chose de juste, pousse plus loin : « Tiens, et si le client était une OBNL? Une multinationale? »; « Ce raisonnement tient-il dans le cas de X? »
4. Quand il se trompe, ne corrige pas frontalement : reformule, propose un cas-limite qui révèle l'erreur.
5. Chaque relance s'appuie sur sa réplique précédente.
6. UNE question à la fois. Jamais deux en rafale.
7. Réponses brèves : 1 à 3 phrases max.

CADRES À MOBILISER selon le concept étudié — Loi 25, RGPD, EU AI Act (incl. GPAI Art. 51-55), AIDA/LIAD (statut de projet), Code de conduite volontaire canadien, ISO/IEC 42001, NIST AI RMF (incl. GAI Profile), Principes OCDE. Réfère-toi à des articles précis, à des sanctions, à des décisions documentées quand c'est utile.

POSTURE — collègue praticien, jamais paternaliste. Ne reformule pas en simplifiant ce qui est déjà clair pour Dominic. Va vers la nuance et le cas-limite.

RÈGLES STYLISTIQUES :
- Tutoiement.
- Français du Québec, pas de tournures pédantes.
- Termes techniques anglais établis acceptés (GPAI, AIA, FRIA, EFVP, AIMS, etc.).
- Pas de markdown, pas d'émojis dans le dialogue, juste du texte fluide.

OBJECTIF — quand Dominic a démontré une maîtrise solide (typiquement après 5-8 échanges), suggère de conclure en lui demandant d'énoncer comment il appliquerait le concept dans une mission Nord Paradigm (Brèche Pro, Prisme, ou conseil ad hoc)."""


def repondre_socratique(concept: dict, historique: list[dict]) -> str:
    """
    Génère la prochaine relance socratique de Claude.

    Args:
        concept: dict avec 'titre' et 'texte'.
        historique: liste de messages {"role": "user"|"assistant", "content": str}.
                    Si vide, Claude pose la question d'ouverture.

    Returns:
        La prochaine réplique du tuteur, en texte brut.
    """
    contexte = f"""Concept étudié : {concept['titre']}

Texte de référence (à NE PAS recopier à Dominic, c'est ta seule source de vérité) :
{concept['texte']}

Tu vas mener un dialogue socratique avec Dominic sur ce concept, dans le contexte de sa pratique de conseil en gouvernance d'IA chez Nord Paradigm.
"""

    if not historique:
        contexte += (
            "\nC'est le DÉBUT du dialogue. Pose une question d'ouverture "
            "ancrée dans un scénario CONCRET de mission Nord Paradigm "
            "(client réel ou hypothétique, dilemme d'audit, arbitrage de "
            "conformité). Évite les définitions abstraites en ouverture; "
            "force Dominic à se positionner comme praticien dès la première "
            "question."
        )
        messages = [{"role": "user", "content": contexte}]
    else:
        messages = [{"role": "user", "content": contexte}]
        # Append the running dialogue. The "user" turns are Dominic, "assistant"
        # turns are previous tutor replies.
        messages.extend(historique)

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=400,
        system=PROMPT_SOCRATIQUE,
        messages=messages,
    )

    return message.content[0].text.strip()


def resumer_socratique(concept: dict, historique: list[dict]) -> dict:
    """
    Évalue le dialogue socratique terminé et produit un bilan.

    Returns: {score, points_forts, a_approfondir, synthese}
    """
    transcript = "\n".join(
        f"{'DOMINIC' if m['role'] == 'user' else 'TUTEUR'} : {m['content']}"
        for m in historique
    )

    prompt = f"""Concept étudié : {concept['titre']}

Texte de référence :
{concept['texte']}

Transcript du dialogue socratique :
{transcript}

Évalue la maîtrise démontrée par Dominic dans ce dialogue, du point de vue d'un PRATICIEN PROFESSIONNEL en gouvernance d'IA (pas d'un étudiant). Retourne UNIQUEMENT un objet JSON (pas de markdown) avec :
- "score" : entier 0 à 4 (0 incompréhension; 1 surface; 2 partielle; 3 solide; 4 maîtrise opérationnelle prête à appliquer en mission client)
- "points_forts" : 1-3 phrases sur ce que Dominic a bien saisi (au niveau praticien)
- "a_approfondir" : 1-3 phrases sur ce qui reste flou ou à creuser, idéalement avec un cas-limite ou une référence (article, jurisprudence, norme) à consulter
- "synthese" : 2-4 phrases qui fixent les éléments clés du concept et qui PEUVENT ÊTRE RÉUTILISÉES dans un livrable Nord Paradigm (Brèche Pro, Prisme, note client)
"""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=600,
        messages=[{"role": "user", "content": prompt}],
    )

    contenu = message.content[0].text.strip()
    contenu = re.sub(r"^```(?:json)?\n?", "", contenu)
    contenu = re.sub(r"\n?```$", "", contenu)
    return json.loads(contenu)
