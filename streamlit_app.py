"""
SCIENTIA — Application web mobile-first.

Lance avec :
    streamlit run streamlit_app.py

Variable d'environnement requise :
    ANTHROPIC_API_KEY  (ou st.secrets["ANTHROPIC_API_KEY"] sur Streamlit Cloud)

Variables optionnelles :
    DATA_DIR           dossier persistant pour scientia.db (Railway/Render)
    CURRICULUM_USER    "conjointe" pour charger curriculum_conjointe.py
"""
from __future__ import annotations

import os
import time
from pathlib import Path

import streamlit as st

# ── Configuration globale (DOIT être le premier appel Streamlit) ──────────────

st.set_page_config(
    page_title="Scientia",
    page_icon="📘",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        "About": "Scientia — apprentissage espacé pour la science.",
    },
)

# ── Récupération de la clé API : .env → st.secrets → env ─────────────────────

if not os.environ.get("ANTHROPIC_API_KEY"):
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass

if not os.environ.get("ANTHROPIC_API_KEY"):
    try:
        cle = st.secrets.get("ANTHROPIC_API_KEY", "")
        if cle:
            os.environ["ANTHROPIC_API_KEY"] = cle
    except Exception:
        pass

# Imports tardifs : ANTHROPIC_API_KEY doit être défini AVANT d'importer generator
from curriculum import (
    CURRICULUM,
    NOMS_MODULES,
    ORDRE_AFFICHAGE_MODULES,
    get_concepts_par_module,
)
from db import (
    init,
    get_cartes_concept,
    sauvegarder_cartes,
    sauvegarder_revision,
    maj_progression,
    get_progression,
    get_toute_progression,
    get_note,
    save_note,
    nb_cartes_dues,
    get_cartes_dues,
    get_planning_14j,
)

# ── Initialisation DB ─────────────────────────────────────────────────────────

init()

# ── Vérification clé API ──────────────────────────────────────────────────────

API_PRESENTE = bool(os.environ.get("ANTHROPIC_API_KEY"))

if not API_PRESENTE:
    st.title("📘 Scientia")
    st.error(
        "Clé API Anthropic manquante.\n\n"
        "**Local** : ajoute `ANTHROPIC_API_KEY=sk-ant-...` à un fichier `.env` "
        "ou exporte la variable.\n\n"
        "**Streamlit Cloud** : ajoute la dans *Settings → Secrets* :\n"
        "```\nANTHROPIC_API_KEY = \"sk-ant-...\"\n```\n\n"
        "Récupère ta clé sur https://console.anthropic.com/keys"
    )
    st.stop()

# Le générateur instancie un client Anthropic au moment de l'import,
# donc on ne l'importe que si la clé est définie.
from generator import (
    generer_questions,
    evaluer_reponse,
    repondre_socratique,
    resumer_socratique,
    aide_socratique_question,
)

# ── État de session ───────────────────────────────────────────────────────────

if "page" not in st.session_state:
    st.session_state.page = "accueil"
if "concept_actuel" not in st.session_state:
    st.session_state.concept_actuel = None
if "questions" not in st.session_state:
    st.session_state.questions = []
if "carte_ids" not in st.session_state:
    st.session_state.carte_ids = []
if "index_question" not in st.session_state:
    st.session_state.index_question = 0
if "scores_session" not in st.session_state:
    st.session_state.scores_session = []
if "evaluation_courante" not in st.session_state:
    st.session_state.evaluation_courante = None
if "debut_question" not in st.session_state:
    st.session_state.debut_question = 0.0
if "indice_visible" not in st.session_state:
    st.session_state.indice_visible = {}
if "soc_concept" not in st.session_state:
    st.session_state.soc_concept = None
if "soc_historique" not in st.session_state:
    st.session_state.soc_historique = []
if "soc_resume" not in st.session_state:
    st.session_state.soc_resume = None
if "soc_pending_user" not in st.session_state:
    st.session_state.soc_pending_user = ""
# Mini-tuteur socratique attaché à une question de quiz spécifique.
# Clé = (concept_id, question_index). Valeur = liste de messages {role, content}.
if "q_soc_dialogues" not in st.session_state:
    st.session_state.q_soc_dialogues = {}
# Quelles questions ont leur expander socratique ouvert
if "q_soc_ouverts" not in st.session_state:
    st.session_state.q_soc_ouverts = set()


def aller_a(page: str, **kwargs):
    """Navigation avec reset des états de quiz."""
    st.session_state.page = page
    for k, v in kwargs.items():
        st.session_state[k] = v


def reset_quiz():
    st.session_state.questions = []
    st.session_state.carte_ids = []
    st.session_state.index_question = 0
    st.session_state.scores_session = []
    st.session_state.evaluation_courante = None


# ── Sidebar : navigation + statistiques rapides ───────────────────────────────

with st.sidebar:
    st.markdown("# 📘 Scientia")
    st.caption("Apprentissage espacé · Quiz IA")

    st.markdown("---")
    if st.button("🏠 Accueil", use_container_width=True):
        aller_a("accueil")
        st.rerun()
    if st.button("📚 Parcourir les modules", use_container_width=True):
        aller_a("modules")
        st.rerun()
    if st.button("🗣️ Dialogue socratique", use_container_width=True):
        aller_a("socratique")
        st.rerun()
    if st.button("📈 Ma progression", use_container_width=True):
        aller_a("progression")
        st.rerun()
    if st.button("📥 Documents personnels", use_container_width=True):
        aller_a("documents")
        st.rerun()

    st.markdown("---")
    cartes_dues = nb_cartes_dues()
    if cartes_dues:
        st.metric("📅 À réviser aujourd'hui", cartes_dues)
    else:
        st.success("✓ Aucune révision due")

    st.caption(f"{len(CURRICULUM)} concepts au total")


# ── Page : ACCUEIL ────────────────────────────────────────────────────────────

def page_accueil():
    st.title("📘 Scientia")
    st.markdown(
        "**Apprentissage espacé pour lire la recherche.** "
        "Quiz adaptatifs, évaluation par Claude, planification FSRS."
    )

    progression = get_toute_progression()
    nb_concepts_etudies = len(progression)
    nb_maitrises = sum(1 for p in progression.values() if p.get("statut") == "maitrise")

    col1, col2, col3 = st.columns(3)
    col1.metric("Concepts étudiés", nb_concepts_etudies)
    col2.metric("Maîtrisés", nb_maitrises)
    col3.metric("À réviser", nb_cartes_dues())

    st.markdown("---")
    st.subheader("Démarrer rapidement")

    if st.button("📚 Choisir un concept à étudier",
                 type="primary", use_container_width=True):
        aller_a("modules")
        st.rerun()

    cartes_dues = get_cartes_dues()
    if cartes_dues:
        st.markdown("### 🔁 Révisions dues")
        st.caption("Cartes dont la prochaine révision est aujourd'hui ou passée.")
        for c in cartes_dues[:5]:
            cle_cpt = c["concept_id"]
            titre_cpt = CURRICULUM.get(cle_cpt, {}).get("titre", cle_cpt)
            with st.container(border=True):
                st.markdown(f"**{titre_cpt}**")
                st.caption(c["enonce"][:150])
                if st.button("Réviser →", key=f"rev_{c['id']}",
                             use_container_width=True):
                    aller_a("etudier", concept_actuel=cle_cpt)
                    reset_quiz()
                    st.rerun()
        if len(cartes_dues) > 5:
            st.caption(f"+ {len(cartes_dues) - 5} autres cartes dues")

    planning = get_planning_14j()
    if planning:
        with st.expander("📆 Planning des 14 prochains jours"):
            for r in planning[:30]:
                st.write(f"`{r['prochaine_rev']}` · {r['enonce'][:80]}")


# ── Page : MODULES ────────────────────────────────────────────────────────────

def page_modules():
    st.title("📚 Modules")
    st.caption("Choisis un module, puis un concept à étudier.")

    modules_avec_concepts = []
    for m in ORDRE_AFFICHAGE_MODULES:
        concepts = get_concepts_par_module(m)
        if concepts:
            modules_avec_concepts.append((m, concepts))

    nom_choisi = st.selectbox(
        "Module",
        options=[m for m, _ in modules_avec_concepts],
        format_func=lambda m: f"M{m:02d} — {NOMS_MODULES.get(m, '?')}",
    )

    concepts = get_concepts_par_module(nom_choisi)
    progression = get_toute_progression()

    st.markdown(f"### {NOMS_MODULES.get(nom_choisi, '?')}")
    st.caption(f"{len(concepts)} concepts dans ce module")

    for cle in concepts:
        c = CURRICULUM[cle]
        prog = progression.get(cle, {})
        statut = prog.get("statut", "nouveau")
        moyenne = prog.get("score_moyen", 0)

        emoji = {"nouveau": "○", "en_cours": "🟡", "maitrise": "🟢"}.get(statut, "○")
        score_txt = f"  ·  {moyenne:.1f}/4" if moyenne else ""

        with st.container(border=True):
            st.markdown(f"**{emoji} {c['titre']}**{score_txt}")
            with st.expander("Voir le texte source"):
                st.markdown(c["texte"])
            if st.button("Étudier ce concept →",
                         key=f"etu_{cle}",
                         use_container_width=True,
                         type="primary"):
                aller_a("etudier", concept_actuel=cle)
                reset_quiz()
                st.rerun()


# ── Page : ÉTUDIER UN CONCEPT ────────────────────────────────────────────────

def page_etudier():
    cle = st.session_state.concept_actuel
    if not cle or cle not in CURRICULUM:
        st.warning("Aucun concept sélectionné.")
        if st.button("← Retour aux modules", use_container_width=True):
            aller_a("modules")
            st.rerun()
        return

    concept = CURRICULUM[cle]
    st.title(concept["titre"])
    st.caption(
        f"Module {concept['module']} — "
        f"{NOMS_MODULES.get(concept['module'], '?')}"
    )

    if st.button("← Retour aux modules", use_container_width=False):
        aller_a("modules")
        reset_quiz()
        st.rerun()

    # ── Étape 1 : pas de questions chargées → générer ou recharger ───────────

    if not st.session_state.questions:
        with st.expander("📖 Texte source", expanded=False):
            st.markdown(concept["texte"])

        cartes_existantes = get_cartes_concept(cle)

        col1, col2 = st.columns(2)
        if cartes_existantes:
            col1.metric("Questions sauvegardées", len(cartes_existantes))
            if col1.button("▶️  Démarrer le quiz",
                           type="primary", use_container_width=True):
                st.session_state.questions = [
                    {
                        "type": q["type"],
                        "question": q["enonce"],
                        "reponse_ref": q["reponse_ref"],
                        "critere": q["critere"],
                        "indice": q.get("indice", "") or "",
                        "difficulte": q["niveau"],
                    }
                    for q in cartes_existantes
                ]
                st.session_state.carte_ids = [q["id"] for q in cartes_existantes]
                st.session_state.index_question = 0
                st.session_state.scores_session = []
                st.session_state.debut_question = time.time()
                st.rerun()

        bouton_label = (
            "🔄 Régénérer les questions" if cartes_existantes
            else "✨ Générer 5 questions avec Claude"
        )
        if col2.button(bouton_label, use_container_width=True):
            with st.spinner("Génération en cours…"):
                try:
                    qs = generer_questions(concept, n=5)
                    ids = sauvegarder_cartes(cle, qs)
                    st.session_state.questions = qs
                    st.session_state.carte_ids = ids
                    st.session_state.index_question = 0
                    st.session_state.scores_session = []
                    st.session_state.debut_question = time.time()
                    st.rerun()
                except Exception as e:
                    st.error(f"Erreur de génération : {e}")

        # Notes personnelles persistantes
        st.markdown("---")
        with st.expander("📝 Mes notes sur ce concept"):
            note = st.text_area(
                "Notes",
                value=get_note(cle),
                height=150,
                label_visibility="collapsed",
            )
            if st.button("💾 Sauvegarder la note", use_container_width=True):
                save_note(cle, note)
                st.success("Note sauvegardée.")
        return

    # ── Étape 2 : quiz en cours ──────────────────────────────────────────────

    i = st.session_state.index_question
    total = len(st.session_state.questions)

    if i >= total:
        # Fin de session
        st.success("🎯 Session terminée")
        scores = st.session_state.scores_session
        moyenne = sum(scores) / len(scores) if scores else 0
        col1, col2, col3 = st.columns(3)
        col1.metric("Questions", total)
        col2.metric("Score moyen", f"{moyenne:.2f}/4")
        col3.metric("Maîtrise", "✓" if moyenne >= 3 else "↻")

        st.progress(min(1.0, moyenne / 4), text=f"Score : {moyenne:.1f}/4")

        if moyenne >= 3.5:
            st.balloons()
            st.markdown("### 🎉 Excellent — concept solidement maîtrisé.")
        elif moyenne >= 2.5:
            st.markdown("### 📚 Bon travail. Revois les points faibles.")
        else:
            st.markdown("### 🔁 Concept à retravailler. Relis le texte source.")

        maj_progression(cle, scores)

        col_a, col_b = st.columns(2)
        if col_a.button("🔁 Refaire un quiz", use_container_width=True):
            reset_quiz()
            st.rerun()
        if col_b.button("📚 Autre concept",
                        type="primary", use_container_width=True):
            aller_a("modules")
            reset_quiz()
            st.rerun()
        return

    # Question courante
    question = st.session_state.questions[i]
    progress = (i) / total
    st.progress(progress, text=f"Question {i + 1} / {total}")

    type_q = question.get("type", "?").replace("_", " ").title()
    st.caption(f"Type : {type_q}")
    st.markdown(f"### {question['question']}")

    # Bouton indice (n'apparaît que si la question en a un)
    indice_txt = question.get("indice", "") or ""
    if indice_txt:
        cle_indice = f"indice_{cle}_{i}"
        deja_visible = st.session_state.indice_visible.get(cle_indice, False)
        if not deja_visible:
            if st.button("💡 Voir un indice", key=f"btn_{cle_indice}",
                         use_container_width=False):
                st.session_state.indice_visible[cle_indice] = True
                st.rerun()
        else:
            st.info(f"💡 {indice_txt}")

    cle_zone = f"reponse_{cle}_{i}"
    cle_soc = (cle, i)
    if st.session_state.evaluation_courante is None:
        reponse = st.text_area(
            "Ta réponse",
            key=cle_zone,
            height=150,
            placeholder="Réponds librement, en français…",
        )

        # ── Tuteur socratique sur la question (sous le champ de réponse) ──
        soc_ouvert = cle_soc in st.session_state.q_soc_ouverts
        if not soc_ouvert:
            if st.button("🎓 Discuter avec Claude pour mieux comprendre la question",
                         key=f"open_soc_{cle}_{i}",
                         use_container_width=True):
                st.session_state.q_soc_ouverts.add(cle_soc)
                # Ouverture du dialogue : Claude pose la première question
                if cle_soc not in st.session_state.q_soc_dialogues:
                    with st.spinner("Claude prépare une ouverture…"):
                        try:
                            ouverture = aide_socratique_question(
                                concept, question, []
                            )
                            st.session_state.q_soc_dialogues[cle_soc] = [
                                {"role": "assistant", "content": ouverture}
                            ]
                        except Exception as e:
                            st.error(f"Erreur Socratique : {e}")
                            st.session_state.q_soc_dialogues[cle_soc] = []
                st.rerun()
        else:
            with st.container(border=True):
                st.caption("🎓 Mini-tuteur socratique — Claude ne donnera "
                           "JAMAIS la réponse, il t'aide à comprendre la question.")

                dialogue = st.session_state.q_soc_dialogues.get(cle_soc, [])

                # Zone à hauteur fixe (scroll interne, auto-scroll vers le bas
                # sur nouveau message — pas besoin de scroller la page).
                with st.container(height=400):
                    for m in dialogue:
                        if m["role"] == "assistant":
                            with st.chat_message("assistant", avatar="🎓"):
                                st.markdown(m["content"])
                        else:
                            with st.chat_message("user", avatar="🧑"):
                                st.markdown(m["content"])

                # Le chat_input reste hors de la zone scrollable :
                # il s'affiche toujours juste en dessous, visible.
                user_msg = st.chat_input(
                    "Pose une question, partage ton intuition…",
                    key=f"soc_input_{cle}_{i}",
                )
                if user_msg:
                    dialogue.append({"role": "user", "content": user_msg})
                    with st.spinner("Claude réfléchit…"):
                        try:
                            relance = aide_socratique_question(
                                concept, question, dialogue
                            )
                            dialogue.append(
                                {"role": "assistant", "content": relance}
                            )
                        except Exception as e:
                            st.error(f"Erreur : {e}")
                    st.session_state.q_soc_dialogues[cle_soc] = dialogue
                    st.rerun()

                if st.button("Fermer le tuteur",
                             key=f"close_soc_{cle}_{i}",
                             use_container_width=False):
                    st.session_state.q_soc_ouverts.discard(cle_soc)
                    st.rerun()

        col_a, col_b = st.columns([1, 1])
        if col_a.button("✓ Soumettre",
                        type="primary",
                        use_container_width=True,
                        disabled=not reponse.strip()):
            duree = int(time.time() - st.session_state.debut_question)
            with st.spinner("Évaluation par Claude…"):
                try:
                    evaluation = evaluer_reponse(question, reponse)
                except Exception as e:
                    st.error(f"Erreur d'évaluation : {e}")
                    return

            score = int(evaluation.get("score", 0))
            st.session_state.scores_session.append(score)

            carte_id = st.session_state.carte_ids[i]
            sauvegarder_revision(
                carte_id=carte_id,
                score=score,
                feedback=evaluation.get("feedback", ""),
                duree_sec=duree,
            )
            st.session_state.evaluation_courante = evaluation
            st.rerun()

        if col_b.button("Passer", use_container_width=True):
            st.session_state.scores_session.append(0)
            carte_id = st.session_state.carte_ids[i]
            sauvegarder_revision(
                carte_id=carte_id, score=0, feedback="(passée)", duree_sec=0,
            )
            st.session_state.index_question += 1
            st.session_state.debut_question = time.time()
            st.rerun()
        return

    # ── Affichage de l'évaluation ─────────────────────────────────────────────
    evaluation = st.session_state.evaluation_courante
    score = int(evaluation.get("score", 0))
    correct = bool(evaluation.get("correct", False))

    if correct:
        st.success(f"✓ Correct ({score}/4)")
    elif score >= 2:
        st.warning(f"Partiel ({score}/4)")
    else:
        st.error(f"À revoir ({score}/4)")

    st.markdown(f"**Feedback** — {evaluation.get('feedback', '')}")

    if not correct:
        with st.expander("📖 Voir la réponse de référence"):
            st.markdown(question.get("reponse_ref", ""))

    if st.button("Question suivante →",
                 type="primary", use_container_width=True):
        st.session_state.index_question += 1
        st.session_state.evaluation_courante = None
        st.session_state.debut_question = time.time()
        st.rerun()


# ── Page : PROGRESSION ───────────────────────────────────────────────────────

def page_progression():
    st.title("📈 Ma progression")
    progression = get_toute_progression()

    if not progression:
        st.info("Aucune session enregistrée pour l'instant. "
                "Lance un quiz pour démarrer ta progression.")
        return

    nb_total = len(CURRICULUM)
    nb_etudies = len(progression)
    nb_maitrises = sum(1 for p in progression.values()
                       if p.get("statut") == "maitrise")

    col1, col2, col3 = st.columns(3)
    col1.metric("Concepts du curriculum", nb_total)
    col2.metric("Étudiés", nb_etudies, f"+{nb_etudies}")
    col3.metric("Maîtrisés", nb_maitrises)

    st.progress(
        nb_maitrises / nb_total if nb_total else 0,
        text=f"Maîtrise globale : {nb_maitrises}/{nb_total}",
    )

    st.markdown("---")
    st.subheader("Détail par concept")

    par_module: dict[int, list[tuple[str, dict]]] = {}
    for cid, p in progression.items():
        c = CURRICULUM.get(cid)
        if not c:
            continue
        par_module.setdefault(c["module"], []).append((cid, p))

    for m in sorted(par_module.keys()):
        with st.expander(f"M{m:02d} — {NOMS_MODULES.get(m, '?')}"):
            for cid, p in par_module[m]:
                titre = CURRICULUM.get(cid, {}).get("titre", cid)
                statut = p.get("statut", "?")
                moyenne = p.get("score_moyen", 0) or 0
                nb = p.get("nb_sessions", 0)
                emoji = {"en_cours": "🟡", "maitrise": "🟢",
                         "nouveau": "○"}.get(statut, "○")
                st.markdown(
                    f"{emoji} **{titre}** — "
                    f"`{moyenne:.2f}/4` sur {nb} session(s)"
                )


# ── Page : DOCUMENTS ─────────────────────────────────────────────────────────

def page_documents():
    st.title("📥 Documents personnels")
    st.caption(
        "Charge un PDF, MD ou TXT. Claude extrait 1 à 5 concepts pédagogiques "
        "qui rejoignent ton curriculum (Module 5)."
    )

    DOCS_DIR = Path(__file__).parent / "docs"
    DOCS_DIR.mkdir(exist_ok=True)

    fichier = st.file_uploader(
        "Choisis un fichier",
        type=["pdf", "md", "txt"],
        accept_multiple_files=False,
    )

    if fichier:
        st.write(f"**{fichier.name}** — {fichier.size // 1024} Ko")
        if st.button("✨ Extraire les concepts",
                     type="primary", use_container_width=True):
            from ingestion import ingerer_fichier
            chemin = DOCS_DIR / fichier.name
            chemin.write_bytes(fichier.getvalue())
            with st.spinner("Lecture et extraction par Claude…"):
                try:
                    nouvelles_cles = ingerer_fichier(chemin)
                    from curriculum import _charger_concepts_dynamiques
                    _charger_concepts_dynamiques()
                    st.success(
                        f"✓ {len(nouvelles_cles)} concept(s) ajouté(s) "
                        "au Module 5. Va dans Modules pour les étudier."
                    )
                except Exception as e:
                    st.error(f"Erreur : {e}")

    st.markdown("---")
    from ingestion import charger_concepts_dynamiques, supprimer_concept
    concepts_dyn = charger_concepts_dynamiques()
    if concepts_dyn:
        st.subheader(f"Concepts ingérés ({len(concepts_dyn)})")
        for cle, c in concepts_dyn.items():
            with st.container(border=True):
                st.markdown(f"**{c['titre']}**")
                st.caption(
                    f"Source : {c.get('source', '?')} · "
                    f"{c.get('date_ingestion', '?')}"
                )
                col1, col2 = st.columns([3, 1])
                if col1.button("Étudier →", key=f"etu_dyn_{cle}",
                               use_container_width=True):
                    aller_a("etudier", concept_actuel=cle)
                    reset_quiz()
                    st.rerun()
                if col2.button("🗑", key=f"sup_{cle}",
                               use_container_width=True):
                    supprimer_concept(cle)
                    st.rerun()
    else:
        st.info("Aucun document ingéré pour l'instant.")


# ── Page : DIALOGUE SOCRATIQUE ───────────────────────────────────────────────

def page_socratique():
    st.title("🗣️ Dialogue socratique")
    st.caption(
        "Mode tuteur : Claude te guide par questions plutôt que de te tester. "
        "Le dialogue n'est pas noté pendant l'échange — un bilan apparaît à la fin."
    )

    # Étape 1 : sélection du concept
    if not st.session_state.soc_concept:
        st.subheader("Choisis un concept à explorer")

        modules_avec_concepts = []
        for m in ORDRE_AFFICHAGE_MODULES:
            cs = get_concepts_par_module(m)
            if cs:
                modules_avec_concepts.append((m, cs))

        m_choisi = st.selectbox(
            "Module",
            options=[m for m, _ in modules_avec_concepts],
            format_func=lambda m: f"M{m:02d} — {NOMS_MODULES.get(m, '?')}",
            key="soc_module_select",
        )
        concepts = get_concepts_par_module(m_choisi)

        cle_choisie = st.selectbox(
            "Concept",
            options=concepts,
            format_func=lambda k: CURRICULUM[k]["titre"],
            key="soc_concept_select",
        )

        if st.button("▶️ Démarrer le dialogue",
                     type="primary", use_container_width=True):
            st.session_state.soc_concept = cle_choisie
            st.session_state.soc_historique = []
            st.session_state.soc_resume = None
            st.session_state.soc_pending_user = ""
            # Génère la question d'ouverture
            with st.spinner("Claude prépare une question d'ouverture…"):
                try:
                    ouverture = repondre_socratique(
                        CURRICULUM[cle_choisie], []
                    )
                    st.session_state.soc_historique.append(
                        {"role": "assistant", "content": ouverture}
                    )
                except Exception as e:
                    st.error(f"Erreur : {e}")
                    st.session_state.soc_concept = None
                    return
            st.rerun()
        return

    # Étape 2 : dialogue en cours
    cle = st.session_state.soc_concept
    concept = CURRICULUM.get(cle)
    if not concept:
        st.warning("Concept introuvable.")
        st.session_state.soc_concept = None
        return

    st.markdown(f"**Concept : {concept['titre']}**")
    st.caption(
        f"Module {concept['module']} — "
        f"{NOMS_MODULES.get(concept['module'], '?')}"
    )

    col_a, col_b = st.columns([1, 1])
    if col_a.button("🔄 Nouveau concept", use_container_width=True):
        st.session_state.soc_concept = None
        st.session_state.soc_historique = []
        st.session_state.soc_resume = None
        st.rerun()
    termine = col_b.button(
        "✓ Terminer et obtenir un bilan",
        type="primary",
        use_container_width=True,
        disabled=len(st.session_state.soc_historique) < 3,
    )

    # Si bilan demandé : génère et affiche
    if termine and not st.session_state.soc_resume:
        with st.spinner("Claude rédige ton bilan…"):
            try:
                resume = resumer_socratique(
                    concept, st.session_state.soc_historique
                )
                st.session_state.soc_resume = resume
                # Met à jour la progression avec le score du dialogue
                maj_progression(cle, [int(resume.get("score", 0))])
            except Exception as e:
                st.error(f"Erreur : {e}")

    # Affichage du bilan si présent
    if st.session_state.soc_resume:
        r = st.session_state.soc_resume
        score = int(r.get("score", 0))
        st.markdown("---")
        st.subheader("📋 Bilan du dialogue")

        if score >= 3:
            st.success(f"Score : {score}/4 — bonne maîtrise")
        elif score >= 2:
            st.warning(f"Score : {score}/4 — partielle")
        else:
            st.error(f"Score : {score}/4 — à retravailler")

        st.markdown(f"**Points forts** — {r.get('points_forts', '')}")
        st.markdown(f"**À approfondir** — {r.get('a_approfondir', '')}")

        with st.expander("📖 Synthèse du concept"):
            st.markdown(r.get("synthese", ""))

        col_c, col_d = st.columns(2)
        if col_c.button("🔁 Relancer un dialogue sur ce concept",
                        use_container_width=True):
            st.session_state.soc_historique = []
            st.session_state.soc_resume = None
            with st.spinner("Nouvelle ouverture…"):
                ouverture = repondre_socratique(concept, [])
                st.session_state.soc_historique.append(
                    {"role": "assistant", "content": ouverture}
                )
            st.rerun()
        if col_d.button("📚 Autre concept",
                        type="primary", use_container_width=True):
            st.session_state.soc_concept = None
            st.session_state.soc_historique = []
            st.session_state.soc_resume = None
            st.rerun()
        return

    # Affichage du dialogue dans une zone à hauteur fixe avec scroll interne.
    st.markdown("---")
    with st.container(height=500):
        for m in st.session_state.soc_historique:
            if m["role"] == "assistant":
                with st.chat_message("assistant", avatar="🎓"):
                    st.markdown(m["content"])
            else:
                with st.chat_message("user", avatar="🧑"):
                    st.markdown(m["content"])

    # Zone de saisie en dehors de la zone scrollable, donc toujours visible.
    reponse = st.chat_input("Ta réponse à Claude…", key="soc_chat_input")
    if reponse:
        st.session_state.soc_historique.append(
            {"role": "user", "content": reponse}
        )
        with st.spinner("Claude réfléchit…"):
            try:
                relance = repondre_socratique(
                    concept, st.session_state.soc_historique
                )
                st.session_state.soc_historique.append(
                    {"role": "assistant", "content": relance}
                )
            except Exception as e:
                st.error(f"Erreur : {e}")
        st.rerun()


# ── Routeur principal ─────────────────────────────────────────────────────────

PAGES = {
    "accueil": page_accueil,
    "modules": page_modules,
    "etudier": page_etudier,
    "socratique": page_socratique,
    "progression": page_progression,
    "documents": page_documents,
}

PAGES.get(st.session_state.page, page_accueil)()

st.markdown("---")
st.caption(
    "Scientia · Apprentissage espacé FSRS-4.5 · "
    "Évaluation Claude · v0.2"
)
