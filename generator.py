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

PROMPT_SYSTEME = """Tu es un expert en statistiques et en conception de questions pédagogiques.
Tu génères des questions pour un adulte autodidacte (Charles) qui apprend les statistiques
pour pouvoir lire des études en apprentissage moteur, biologie, et psychométrie
(The Bell Curve, études sur les sports, etc.).

RÈGLES ABSOLUES :
1. Une seule idée par question. Jamais deux concepts dans une seule question.
2. Les questions doivent tester la COMPRÉHENSION, pas la mémorisation brute.
3. Utilise des exemples tirés du domaine de Charles quand possible :
   JJB, études sportives, apprentissage moteur, QI/intelligence.
4. Formule en français, sauf les termes techniques anglais établis (p-value, t-test, etc.).
5. La réponse de référence doit être concise (2-5 phrases max).
6. Le critère d'évaluation doit indiquer les éléments ESSENTIELS de la bonne réponse.

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
- "question" : la question posée à Charles (tu/toi)
- "reponse_ref" : la réponse de référence complète
- "critere" : CHAÎNE DE CARACTÈRES unique listant les 2-3 éléments ESSENTIELS que la réponse doit contenir, séparés par "; ". Pas de tableau JSON, juste une chaîne.
- "indice" : CHAÎNE de 1 phrase max qui pointe vers la réponse sans la donner. Active le rappel actif (ex: « Pense à ce qui distingue X de Y… » ou « Quel article du règlement traite ce cas? »). PAS la réponse, PAS un mot-clé seul.
- "difficulte" : 1 (facile), 2 (moyen), 3 (difficile)

Retourne un tableau JSON de {n} objets. Rien d'autre. Pas de markdown. Juste le JSON."""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2000,
        system=PROMPT_SYSTEME,
        messages=[{"role": "user", "content": prompt}],
    )

    contenu = message.content[0].text.strip()

    # Nettoyer si markdown accidentel
    contenu = re.sub(r"^```(?:json)?\n?", "", contenu)
    contenu = re.sub(r"\n?```$", "", contenu)

    questions = json.loads(contenu)
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

Réponse de Charles : {reponse_utilisateur}

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

PROMPT_SOCRATIQUE = """Tu es un tuteur SOCRATIQUE pour Charles, un adulte autodidacte.

RÈGLES DU DIALOGUE SOCRATIQUE :
1. Ne donne JAMAIS la réponse directement. Guide Charles par des questions.
2. Reformule, sonde, fais émerger les contradictions et les zones floues.
3. Quand il dit quelque chose de juste, demande-lui de l'expliquer plus profondément ou de l'appliquer.
4. Quand il se trompe, ne corrige pas — pose une question qui le mène à voir son erreur.
5. Construis sur ses réponses précédentes : chaque relance doit refléter ce qu'il vient de dire.
6. Une question à la fois. Jamais deux ou trois en rafale.
7. Réponses brèves : 1 à 3 phrases max.

RÈGLES STYLISTIQUES :
- Tutoiement.
- Français du Québec, pas de tournures pédantes.
- Termes techniques anglais établis acceptés (p-value, EFVP, GPAI, etc.).
- Pas de markdown, pas d'émojis dans le dialogue, juste du texte fluide.

OBJECTIF — quand Charles a démontré une compréhension solide (typiquement après 5-8 échanges), tu peux suggérer de conclure en lui demandant d'énoncer le point clé qu'il retire."""


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

Texte de référence (à NE PAS recopier à Charles, c'est ta seule source de vérité) :
{concept['texte']}

Tu vas mener un dialogue socratique avec Charles sur ce concept.
"""

    if not historique:
        contexte += (
            "\nC'est le DÉBUT du dialogue. Pose une question d'ouverture qui "
            "ancre Charles dans le concept par une situation concrète ou un "
            "questionnement intuitif. Évite les définitions abstraites en ouverture."
        )
        messages = [{"role": "user", "content": contexte}]
    else:
        messages = [{"role": "user", "content": contexte}]
        # Append the running dialogue. The "user" turns are Charles, "assistant"
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
        f"{'CHARLES' if m['role'] == 'user' else 'TUTEUR'} : {m['content']}"
        for m in historique
    )

    prompt = f"""Concept étudié : {concept['titre']}

Texte de référence :
{concept['texte']}

Transcript du dialogue socratique :
{transcript}

Évalue la compréhension démontrée par Charles dans ce dialogue. Retourne
UNIQUEMENT un objet JSON (pas de markdown) avec :
- "score" : entier 0 à 4 (0 incompréhension; 4 maîtrise solide)
- "points_forts" : 1-3 phrases sur ce que Charles a bien saisi
- "a_approfondir" : 1-3 phrases sur ce qui reste flou ou à creuser
- "synthese" : 2-4 phrases résumant le concept en fixant correctement les éléments clés (pour servir de récap utile à Charles)
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
