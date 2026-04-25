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
- "critere" : les 2-3 éléments ESSENTIELS que la réponse doit contenir
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
