#!/usr/bin/env python3
"""
SCIENTIA — Quiz de statistiques pour Charles Roy
Usage : python scientia.py
"""

import time
import sys
import os

# ── Vérification des dépendances ──────────────────────────────────────────────
try:
    import anthropic
except ImportError:
    print("\n⚠️  Package manquant. Lance cette commande d'abord :")
    print("    pip install anthropic\n")
    sys.exit(1)

from curriculum import CURRICULUM, lister_curriculum, get_concepts_par_module
from generator import generer_questions, evaluer_reponse
from db import initialiser_db, sauvegarder_cartes, sauvegarder_revision, \
               mettre_a_jour_progression, afficher_progression, get_cartes_concept

# ── Helpers d'affichage ────────────────────────────────────────────────────────

BLEU   = "\033[94m"
VERT   = "\033[92m"
ROUGE  = "\033[91m"
JAUNE  = "\033[93m"
GRIS   = "\033[90m"
RESET  = "\033[0m"
GRAS   = "\033[1m"

def ligne(car="─", n=60):
    print(GRIS + car * n + RESET)

def titre(texte):
    print()
    ligne("═")
    print(f"{GRAS}{BLEU}  {texte}{RESET}")
    ligne("═")

def sous_titre(texte):
    print(f"\n{GRAS}{JAUNE}  {texte}{RESET}")
    ligne()

def succes(texte):
    print(f"{VERT}  ✓ {texte}{RESET}")

def erreur(texte):
    print(f"{ROUGE}  ✗ {texte}{RESET}")

def info(texte):
    print(f"{GRIS}  {texte}{RESET}")

def pause():
    input(f"\n{GRIS}  [Appuie sur Entrée pour continuer...]{RESET}")

# ── Vérification de la clé API ─────────────────────────────────────────────────

def verifier_api():
    if not os.environ.get("ANTHROPIC_API_KEY"):
        titre("Configuration requise")
        print("""
  La clé API Anthropic n'est pas configurée.

  Pour la configurer, ouvre le Terminal et entre cette commande
  (remplace sk-ant-... par ta vraie clé) :

    export ANTHROPIC_API_KEY="sk-ant-..."

  Pour que ça persiste entre les sessions, ajoute cette ligne
  à ton fichier ~/.zshrc :

    echo 'export ANTHROPIC_API_KEY="sk-ant-..."' >> ~/.zshrc
        """)
        sys.exit(1)

# ── Session de quiz ────────────────────────────────────────────────────────────

def afficher_question(i: int, total: int, question: dict):
    print(f"\n{GRAS}  Question {i}/{total} — {question['type'].replace('_', ' ').upper()}{RESET}")
    ligne()
    print(f"\n  {question['question']}\n")

def session_quiz(concept_id: str, concept: dict, regenerer: bool = False):
    """Lance une session de quiz pour un concept."""

    sous_titre(f"Concept : {concept['titre']}")

    # Vérifier si des cartes existent déjà
    cartes_existantes = get_cartes_concept(concept_id)

    if cartes_existantes and not regenerer:
        print(f"\n  {len(cartes_existantes)} questions déjà générées pour ce concept.")
        choix = input("  Utiliser les questions existantes ? [O/n] : ").strip().lower()
        if choix == "n":
            regenerer = True

    if not cartes_existantes or regenerer:
        print(f"\n{JAUNE}  ⏳ Génération des questions via Claude...{RESET}")
        try:
            questions = generer_questions(concept, n=5)
            carte_ids = sauvegarder_cartes(concept_id, questions)
            succes(f"{len(questions)} questions générées.")
        except Exception as e:
            erreur(f"Erreur de génération : {e}")
            return
    else:
        questions = cartes_existantes
        carte_ids = [q["id"] for q in questions]

    pause()

    # Afficher le texte source
    print(f"\n{GRIS}  ── Texte source ──{RESET}")
    for ligne_texte in concept["texte"].split("\n"):
        print(f"  {GRIS}{ligne_texte}{RESET}")
    print()
    pause()

    # Quiz
    scores = []
    total = len(questions)

    for i, (q, carte_id) in enumerate(zip(questions, carte_ids), 1):
        if isinstance(q, dict) and "carte_id" not in q:
            # Question fraîchement générée
            question_data = q
        else:
            # Question depuis la DB
            question_data = {
                "type": q["type"],
                "question": q["question"],
                "reponse_ref": q["reponse_ref"],
                "critere": q["critere"],
            }

        afficher_question(i, total, question_data)

        debut = time.time()
        try:
            reponse = input(f"  {GRAS}Ta réponse :{RESET} ").strip()
        except KeyboardInterrupt:
            print("\n\n  Session interrompue.")
            return

        if not reponse:
            reponse = "(sans réponse)"

        duree = int(time.time() - debut)

        print(f"\n{JAUNE}  ⏳ Évaluation...{RESET}", end="\r")
        try:
            eval_result = evaluer_reponse(question_data, reponse)
        except Exception as e:
            erreur(f"Erreur d'évaluation : {e}")
            continue

        score = eval_result.get("score", 0)
        scores.append(score)

        ligne()
        if eval_result.get("correct"):
            print(f"{VERT}  ✓ Correct  (score : {score}/4){RESET}")
        else:
            print(f"{ROUGE}  ✗ À revoir (score : {score}/4){RESET}")

        print(f"\n  {eval_result.get('feedback', '')}")

        if not eval_result.get("correct"):
            print(f"\n{GRIS}  Réponse de référence :{RESET}")
            print(f"  {question_data['reponse_ref']}")

        sauvegarder_revision(carte_id, score, duree, eval_result.get("feedback", ""))
        pause()

    # Résultats de session
    titre("Résultats de la session")
    score_moyen = sum(scores) / len(scores) if scores else 0
    barre = "█" * int(score_moyen) + "░" * (4 - int(score_moyen))

    print(f"\n  Score moyen : {GRAS}{barre} {score_moyen:.1f}/4{RESET}")
    print(f"  Questions   : {len(scores)}")

    if score_moyen >= 3.5:
        print(f"\n{VERT}  🎯 Excellent ! Concept bien maîtrisé.{RESET}")
    elif score_moyen >= 2.5:
        print(f"\n{JAUNE}  📚 Bien. Revois les points manquants.{RESET}")
    else:
        print(f"\n{ROUGE}  🔄 Concept à retravailler. Relis le texte source.{RESET}")

    mettre_a_jour_progression(concept_id, scores)
    succes("Progression sauvegardée.")

# ── Menu principal ─────────────────────────────────────────────────────────────

def menu_choisir_concept() -> tuple[str, dict] | None:
    """Affiche le curriculum et laisse l'utilisateur choisir un concept."""
    titre("Choisir un concept")
    lister_curriculum()

    print(f"\n{GRIS}  Entre la clé du concept (ex: m1_c1_population_echantillon){RESET}")
    print(f"{GRIS}  ou 'q' pour annuler.{RESET}\n")

    cles = list(CURRICULUM.keys())
    for i, k in enumerate(cles, 1):
        c = CURRICULUM[k]
        print(f"  {GRIS}[{i:02d}]{RESET} {c['titre']} {GRIS}(m{c['module']}){RESET}")

    print()
    choix = input("  Numéro ou clé : ").strip()

    if choix == "q":
        return None

    # Accepter un numéro
    if choix.isdigit():
        idx = int(choix) - 1
        if 0 <= idx < len(cles):
            cle = cles[idx]
            return cle, CURRICULUM[cle]
        else:
            erreur("Numéro invalide.")
            return None

    # Accepter une clé directe
    if choix in CURRICULUM:
        return choix, CURRICULUM[choix]

    erreur(f"Concept '{choix}' introuvable.")
    return None


def menu_ingerer_document():
    """Affiche les fichiers disponibles dans docs/ et lance l'ingestion."""
    from ingestion import lister_docs_disponibles, ingerer_fichier, charger_concepts_dynamiques

    titre("Ingérer un document")
    docs = lister_docs_disponibles()

    if not docs:
        info("Aucun fichier trouvé dans le dossier docs/")
        info("Glisse un PDF, Markdown ou TXT dans scientia/docs/ et relance.")
        pause()
        return

    print(f"\n{GRAS}  Fichiers disponibles :{RESET}")
    for i, p in enumerate(docs, 1):
        taille = p.stat().st_size // 1024
        print(f"  {BLEU}[{i}]{RESET} {p.name}  {GRIS}({taille} Ko){RESET}")
    print(f"  {GRIS}[0]{RESET} Annuler\n")

    choix = input("  Numéro du fichier : ").strip()
    if choix == "0" or not choix:
        return

    try:
        idx = int(choix) - 1
        if not (0 <= idx < len(docs)):
            erreur("Numéro invalide.")
            return
    except ValueError:
        erreur("Entre un numéro.")
        return

    fichier = docs[idx]

    try:
        nouvelles_cles = ingerer_fichier(fichier, print_fn=lambda m: print(m))
    except Exception as e:
        erreur(f"Erreur d'ingestion : {e}")
        pause()
        return

    # Recharger le curriculum pour inclure les nouveaux concepts
    from curriculum import _charger_concepts_dynamiques
    _charger_concepts_dynamiques()

    succes(f"{len(nouvelles_cles)} concept(s) ajouté(s) au curriculum :")
    for cle in nouvelles_cles:
        from curriculum import CURRICULUM
        print(f"    • {CURRICULUM.get(cle, {}).get('titre', cle)}")

    print(f"\n{GRIS}  Ces concepts sont maintenant disponibles dans 'Étudier un concept'.{RESET}")
    pause()


def menu_gerer_documents():
    """Affiche et permet de supprimer les concepts ingérés."""
    from ingestion import charger_concepts_dynamiques, supprimer_concept

    titre("Gérer les documents ingérés")
    concepts = charger_concepts_dynamiques()

    if not concepts:
        info("Aucun concept ingéré pour l'instant.")
        pause()
        return

    cles = list(concepts.keys())
    print(f"\n{GRAS}  Concepts ingérés ({len(cles)}) :{RESET}")
    for i, cle in enumerate(cles, 1):
        c = concepts[cle]
        print(f"  {BLEU}[{i}]{RESET} {c['titre']}  {GRIS}← {c.get('source', '?')} ({c.get('date_ingestion', '?')}){RESET}")

    print(f"\n  {GRIS}[s<N>]{RESET} Supprimer le concept N  (ex: s2)")
    print(f"  {GRIS}[0]{RESET} Retour\n")

    choix = input("  Choix : ").strip()
    if choix == "0" or not choix:
        return

    if choix.startswith("s"):
        try:
            idx = int(choix[1:]) - 1
            cle = cles[idx]
            if supprimer_concept(cle):
                succes(f"Concept '{concepts[cle]['titre']}' supprimé.")
            else:
                erreur("Concept introuvable.")
        except (ValueError, IndexError):
            erreur("Commande invalide. Exemple : s2 pour supprimer le concept 2.")
        pause()


def main():
    verifier_api()
    initialiser_db()

    titre("SCIENTIA — Statistiques pour lire la recherche")
    info("Quiz actif · Répétition espacée · Curriculum structuré")

    from curriculum import CURRICULUM
    info(f"{len(CURRICULUM)} concepts · Apprentissage moteur & Psychométrie")

    while True:
        from ingestion import charger_concepts_dynamiques
        nb_doc = len(charger_concepts_dynamiques())
        tag_doc = f" {GRIS}({nb_doc} ingérés){RESET}" if nb_doc else ""

        print(f"""
{GRAS}  Menu principal{RESET}
  {BLEU}[1]{RESET} Étudier un concept
  {BLEU}[2]{RESET} Voir ma progression
  {BLEU}[3]{RESET} Ingérer un document{tag_doc}
  {BLEU}[4]{RESET} Gérer les documents ingérés
  {BLEU}[5]{RESET} Quitter
        """)

        choix = input("  Choix : ").strip()

        if choix == "1":
            resultat = menu_choisir_concept()
            if resultat:
                concept_id, concept = resultat
                session_quiz(concept_id, concept)

        elif choix == "2":
            titre("Ma progression")
            afficher_progression()
            pause()

        elif choix == "3":
            menu_ingerer_document()

        elif choix == "4":
            menu_gerer_documents()

        elif choix == "5" or choix.lower() == "q":
            print(f"\n{GRIS}  À bientôt, Charles.{RESET}\n")
            break

        else:
            erreur("Choix invalide. Entre 1 à 5.")


if __name__ == "__main__":
    main()
