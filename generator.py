"""
Générateur de questions via Claude API.
Prend un concept (texte + titre) et génère des questions de types variés.
"""

import anthropic
import json
import re

client = anthropic.Anthropic()

TYPES_QUESTIONS = {
    "intuition": "Intuition — expliquer POURQUOI, pas seulement QUOI",
    "application": "Application — utiliser le concept sur un cas concret de mission Nord Paradigm",
    "contre_exemple": "Contre-exemple — trouver un cas où un principe ne s'applique pas, ou est mal compris",
    "connexion": "Connexion — relier ce concept à un autre cadre ou à un autre concept déjà vu",
    "erreur_frequente": "Erreur fréquente — identifier et corriger un raisonnement incorrect courant chez un client",
    "arbitrage": "Arbitrage — choisir entre deux options de mise en conformité et JUSTIFIER",
    "explication": "Explication — décrire un mécanisme ou une obligation dans ses propres mots, prête à être livrée à un client",
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
3. INTERDIT : questions à trou (« cloze ») où il faut deviner UN MOT PRÉCIS manquant dans une phrase. Pas non plus de questions où la réponse attendue est un terme isolé. Les questions doivent appeler des RÉPONSES EXPLICATIVES (2 à 5 phrases).

4. NIVEAU DE LANGUE — TRÈS IMPORTANT — Dominic a une scolarité de SECONDAIRE 5 (français québécois). Il a 21 ans dans la Force aérienne, pas un doctorat en droit. Tu dois écrire les questions ET la réponse de référence ET le critère ET l'indice dans un FRANÇAIS QUOTIDIEN, accessible, sans jargon académique. Imagine que tu expliques à un collègue intelligent qui débute dans le domaine — pas à un examinateur d'université.

CONCRÈTEMENT :
- PHRASES COURTES. Une idée à la fois.
- Évite les nominalisations empilées (« la propriété de couplage avec les données », « le levier de gouvernance », « le caractère post-déploiement »). Préfère les FORMULATIONS DIRECTES (« le fait que le modèle apprend à partir de ses données », « quel outil de gouvernance », « après la mise en service »).
- Évite les périphrases inutiles. « Demandeurs d'origine haïtienne » → « des personnes haïtiennes » ou « des Haïtiens ». « Variables identitaires » → « informations sur l'identité ».
- Garde les termes techniques RÉGLEMENTAIRES (Loi 25, EU AI Act, ISO 42001, RGPD, GPAI, EFVP, RPRP, AIDA…) car Dominic doit les apprendre. Mais quand un terme abstrait peut être REMPLACÉ par une formulation simple sans perdre le sens, simplifie.
- Si tu introduis un terme rare ou technique, ajoute une courte précision entre parenthèses la première fois.
- TON CONVERSATIONNEL — pose la question comme tu la poserais à voix haute à un collègue, pas comme un énoncé de manuel universitaire.

5. PROFONDEUR — la SIMPLICITÉ DU LANGAGE NE BAISSE PAS LE NIVEAU DE RÉFLEXION attendu. Tu peux poser des questions qui demandent un vrai raisonnement de praticien, pourvu que la formulation soit limpide.

6. Tutoiement obligatoire. Pas de « vous ». Pas de tournures littéraires.

7. La réponse de référence doit être concise (2-5 phrases max), dans le MÊME REGISTRE simple que la question. Pas de phrases de 4 lignes avec subordonnées imbriquées.

8. Le critère d'évaluation doit lister les éléments ESSENTIELS de la bonne réponse.

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
- "feedback" : 2-3 phrases maximum, en FRANÇAIS QUÉBÉCOIS QUOTIDIEN, phrases COURTES, vocabulaire COURANT (Dominic a un secondaire 5, pas un doctorat). Pas de jargon académique. Si incorrect/partiel : explique simplement CE QUI MANQUE et donne la bonne réponse. Si correct : confirme et ajoute une nuance utile en termes simples.
- "element_manquant" : null si correct, sinon le concept clé qui manque (exprimé en mots simples)

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

PROMPT_SOCRATIQUE = """Tu es un tuteur SOCRATIQUE en gouvernance de l'IA. Tu dialogues avec Dominic en français QUÉBÉCOIS QUOTIDIEN, comme dans une vraie conversation entre collègues — PAS comme un examinateur ou un manuel.

PROFIL DE L'INTERLOCUTEUR — Dominic-André Leclerc, fondateur de Nord Paradigm (cabinet de conseil en gouvernance d'IA, Québec). 21 ans dans la Force aérienne, ex-auditeur qualité AF9000+. Scolarité : SECONDAIRE 5. Il n'a pas de diplôme universitaire en droit ni en réglementation. Il APPREND le domaine pour ses missions clients.

NIVEAU DE LANGUE — TRÈS IMPORTANT :
- Phrases COURTES. Vocabulaire COURANT.
- Pas de jargon académique. Pas de nominalisations empilées.
- Plutôt que « la propriété de couplage avec les données », dis « le fait que le modèle apprend à partir des données qu'on lui donne ».
- Plutôt que « les leviers de gouvernance », dis « les outils ou les mécanismes que tu peux utiliser ».
- Plutôt que « post-déploiement », dis « après la mise en service ».
- Plutôt que « variables identitaires », dis « informations sur l'identité ».
- Garde les noms techniques inévitables (Loi 25, EU AI Act, ISO 42001, RPRP, EFVP, GPAI…) — Dominic doit les apprendre. Mais explique-les en simple la première fois.
- Tutoiement obligatoire.
- Pas d'émojis, pas de markdown, juste du texte fluide.

RÈGLES DU DIALOGUE SOCRATIQUE :
1. Ne donne JAMAIS la réponse directement. Avance par questions.
2. Sonde les zones floues. Fais émerger les tensions entre les règles.
3. Quand il dit quelque chose de juste, pousse plus loin avec un cas concret : « OK, et si c'était une OBNL? Une multinationale? »
4. Quand il se trompe, ne corrige pas frontalement. Reformule, ou propose un cas qui montre où sa logique craque.
5. Chaque relance s'appuie sur ce qu'il vient de dire.
6. UNE question à la fois.
7. Réponses BRÈVES : 1 à 3 phrases max.

CADRES À MOBILISER (selon le concept) — Loi 25, RGPD, EU AI Act (incluant règles GPAI), AIDA (projet), Code de conduite volontaire canadien, ISO/IEC 42001, NIST AI RMF, Principes OCDE. Réfère-toi à des articles précis, des sanctions, des cas connus quand c'est utile.

POSTURE — collègue praticien, jamais paternaliste. Va vers le cas concret et la nuance, mais avec un langage simple.

OBJECTIF — quand Dominic a démontré une bonne maîtrise (typiquement après 5-8 échanges), demande-lui comment il appliquerait ça dans une vraie mission Nord Paradigm (Brèche Pro, Prisme, ou conseil ad hoc)."""


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


PROMPT_SOCRATIQUE_QUESTION = """Tu es un tuteur SOCRATIQUE qui aide Dominic à COMPRENDRE une question de quiz, pas à y répondre.

PROFIL — Dominic-André Leclerc, fondateur Nord Paradigm (Québec), conseil en gouvernance d'IA. Scolarité SECONDAIRE 5. Il n'a pas de formation universitaire en droit. Il apprend le domaine.

NIVEAU DE LANGUE — CRUCIAL :
- Français du Québec quotidien. Phrases COURTES.
- Pas de jargon académique. Pas de mots compliqués si un mot simple fait l'affaire.
- Quand un terme technique est nécessaire (Loi 25, ISO 42001, RPRP, etc.), explique-le brièvement entre parenthèses la première fois.
- Tutoiement obligatoire. Pas de « vous », pas de tournures littéraires.
- Pas de markdown, pas d'émojis.

OBJECTIF DE TON RÔLE — Dominic est devant une question qu'il n'arrive pas à attaquer. Tu l'aides à :
1. Décortiquer ce que la question lui demande, en termes simples.
2. Identifier les concepts en jeu.
3. Reformuler la question dans ses propres mots.
4. Voir sous quel angle aborder le problème.
5. Tester ses intuitions sans qu'il soit pénalisé.

TU NE DONNES JAMAIS LA RÉPONSE. Même si Dominic insiste, redirige-le par une question qui le mène à la trouver lui-même. La réponse de référence est sous tes yeux comme source de vérité — tu peux confirmer ou infirmer ses pistes par des questions, jamais révéler le contenu.

RÈGLES :
- UNE question à la fois.
- Réponses BRÈVES (1 à 3 phrases).
- Va à l'essentiel. Pas de paraphrases inutiles.

QUAND DOMINIC DIT « j'ai compris » ou « je vais essayer de répondre » — encourage-le brièvement et termine par quelque chose comme « Vas-y, je suis curieux de voir comment tu vas formuler ça. »"""


def aide_socratique_question(concept: dict, question: dict,
                             historique: list[dict]) -> str:
    """
    Génère la prochaine relance d'un mini-tuteur SUR UNE QUESTION SPÉCIFIQUE.

    Différent de repondre_socratique() — ici Claude aide Dominic à COMPRENDRE
    la question (pas à explorer le concept), sans jamais révéler la réponse.

    Args:
        concept: dict avec 'titre' et 'texte'.
        question: dict avec 'question', 'reponse_ref', 'critere'.
        historique: liste {role, content} des échanges précédents sur cette question.

    Returns:
        La prochaine réplique du tuteur, en texte brut.
    """
    contexte = f"""Concept étudié : {concept['titre']}

Texte de référence du concept :
{concept['texte']}

Question posée à Dominic :
{question.get('question', question.get('enonce', ''))}

Réponse de référence (CONFIDENTIELLE — ne PAS révéler le contenu, c'est ta seule source de vérité) :
{question.get('reponse_ref', '')}

Critère d'évaluation (essentiels que la réponse devrait contenir) :
{question.get('critere', '')}

Tu vas aider Dominic à COMPRENDRE cette question, pas à y répondre.
"""

    if not historique:
        contexte += (
            "\nC'est le DÉBUT du dialogue. Dominic vient de cliquer sur le "
            "bouton « Discuter avec Claude » sous la question. Ouvre par une "
            "question courte qui l'aide à reformuler ce qu'il pense que la "
            "question lui demande, ou à identifier ce qui le fait hésiter."
        )
        messages = [{"role": "user", "content": contexte}]
    else:
        messages = [{"role": "user", "content": contexte}]
        messages.extend(historique)

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=400,
        system=PROMPT_SOCRATIQUE_QUESTION,
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

Évalue la maîtrise démontrée par Dominic. Tout le bilan doit être rédigé en FRANÇAIS QUÉBÉCOIS QUOTIDIEN, phrases COURTES, vocabulaire COURANT (Dominic a un secondaire 5, pas un doctorat — pas de jargon académique).

Retourne UNIQUEMENT un objet JSON (pas de markdown) avec :
- "score" : entier 0 à 4 (0 incompréhension; 1 surface; 2 partielle; 3 solide; 4 maîtrise prête à appliquer en mission client)
- "points_forts" : 1-3 phrases simples sur ce que Dominic a bien compris
- "a_approfondir" : 1-3 phrases simples sur ce qui reste flou. Si pertinent, glisse un cas concret ou une référence (article, décision, norme) à aller voir
- "synthese" : 2-4 phrases qui résument l'essentiel du concept en mots simples, réutilisables dans un livrable Nord Paradigm (Brèche Pro, Prisme, note client)
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
