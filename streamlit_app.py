"""
SCIENTIA — Application web mobile-first.

Lance avec :
    streamlit run streamlit_app.py

Variable d'environnement requise :
    ANTHROPIC_API_KEY  (ou st.secrets["ANTHROPIC_API_KEY"] sur Streamlit Cloud)

Variables optionnelles :
    DATA_DIR           dossier persistant pour scientia.db (Railway/Render)
"""
from __future__ import annotations

import os
import time
from pathlib import Path

import streamlit as st

# ── Configuration globale (DOIT être le premier appel Streamlit) ──────────────

st.set_page_config(
    page_title="Scientia · Nord Paradigm",
    page_icon="📘",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        "About": "Scientia — Nord Paradigm | AI Governance Training. v0.4",
    },
)

# ── Branding global Nord Paradigm ─────────────────────────────────────────────

from brand import (
    global_css,
    hero_html,
    resume_card_html,
    reco_card_html,
    sidebar_brand_html,
    footer_html,
)
st.markdown(global_css(), unsafe_allow_html=True)

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
    LANGUE_MODULES,
    ORDRE_AFFICHAGE_MODULES,
    PARCOURS_CONSEILLES,
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
    # Sprint A
    set_derniere_activite,
    get_derniere_activite,
    effacer_derniere_activite,
    # Sprint B
    get_dialogue_socratique_actif,
    get_dialogue_socratique_par_id,
    sauvegarder_dialogue_socratique,
    terminer_dialogue_socratique,
    # Sprint D
    get_streak_jours,
    reset_progression_concept,
    export_progression_csv,
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

# ── Utilitaires UI ────────────────────────────────────────────────────────────

def langue_du_module(m: int) -> str:
    """Retourne l'étiquette de langue (FR / EN) du module."""
    code = LANGUE_MODULES.get(m, "fr")
    return "FR" if code == "fr" else ("EN" if code == "en" else "")


def nom_module_avec_drapeau(m: int) -> str:
    nom = NOMS_MODULES.get(m, "?")
    tag = langue_du_module(m)
    return f"[{tag}] M{m:02d} — {nom}".strip() if tag else f"M{m:02d} — {nom}"


def temps_relatif(iso_ts: str | None) -> str:
    """Convertit un timestamp ISO en 'il y a X minutes/heures/jours'."""
    if not iso_ts:
        return ""
    from datetime import datetime, timezone
    try:
        dt = datetime.fromisoformat(iso_ts[:19])
    except Exception:
        return iso_ts
    delta = datetime.now() - dt
    sec = int(delta.total_seconds())
    if sec < 60:
        return "à l'instant"
    if sec < 3600:
        return f"il y a {sec // 60} min"
    if sec < 86400:
        return f"il y a {sec // 3600} h"
    j = sec // 86400
    return f"il y a {j} jour" + ("s" if j > 1 else "")


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
if "soc_dialogue_id" not in st.session_state:
    st.session_state.soc_dialogue_id = None  # B : id en DB
if "soc_historique" not in st.session_state:
    st.session_state.soc_historique = []
if "soc_resume" not in st.session_state:
    st.session_state.soc_resume = None
if "soc_pending_user" not in st.session_state:
    st.session_state.soc_pending_user = ""
if "q_soc_dialogues" not in st.session_state:
    st.session_state.q_soc_dialogues = {}
if "q_soc_ouverts" not in st.session_state:
    st.session_state.q_soc_ouverts = set()
# Sprint C : filtre langue de modules (None = tous)
if "filtre_langue" not in st.session_state:
    st.session_state.filtre_langue = None
# Sprint D : taille du quiz par défaut
if "n_questions" not in st.session_state:
    st.session_state.n_questions = 5
# Drapeau pour bloquer la sauvegarde de dernière activité quand on consulte
# une page sans étudier (ex. Progression).
if "session_chargee_de_db" not in st.session_state:
    st.session_state.session_chargee_de_db = False


def aller_a(page: str, **kwargs):
    """Navigation avec mise à jour des états."""
    st.session_state.page = page
    for k, v in kwargs.items():
        st.session_state[k] = v


def reset_quiz():
    st.session_state.questions = []
    st.session_state.carte_ids = []
    st.session_state.index_question = 0
    st.session_state.scores_session = []
    st.session_state.evaluation_courante = None


# ── Reprise au démarrage : charger l'état de quiz si disponible ───────────────

def tenter_reprise_si_demande():
    """
    Si on est sur la page 'etudier' avec un concept choisi mais pas de
    questions chargées en mémoire, et qu'il y a une session en cours en DB
    pour ce même concept, on restaure les questions et l'index.
    """
    if (st.session_state.page == "etudier"
            and st.session_state.concept_actuel
            and not st.session_state.questions
            and not st.session_state.session_chargee_de_db):
        derniere = get_derniere_activite()
        if (derniere
                and derniere.get("derniere_action") == "quiz"
                and derniere.get("concept_id") == st.session_state.concept_actuel):
            cle = derniere["concept_id"]
            cartes = get_cartes_concept(cle)
            if cartes:
                st.session_state.questions = [
                    {
                        "type": q["type"],
                        "question": q["enonce"],
                        "reponse_ref": q["reponse_ref"],
                        "critere": q["critere"],
                        "indice": q.get("indice", "") or "",
                        "difficulte": q["niveau"],
                        "langue": q.get("langue") or
                                  CURRICULUM.get(cle, {}).get("langue", "fr"),
                    }
                    for q in cartes
                ]
                st.session_state.carte_ids = [q["id"] for q in cartes]
                st.session_state.index_question = derniere.get(
                    "index_question", 0
                ) or 0
                st.session_state.scores_session = list(
                    derniere.get("quiz_scores") or []
                )
                st.session_state.debut_question = time.time()
                st.session_state.session_chargee_de_db = True


tenter_reprise_si_demande()


# ── Sidebar : navigation + statistiques rapides ───────────────────────────────

with st.sidebar:
    st.markdown(sidebar_brand_html(), unsafe_allow_html=True)

    if st.button("🏠 Accueil", use_container_width=True):
        aller_a("accueil")
        st.rerun()
    if st.button("📚 Modules", use_container_width=True):
        aller_a("modules")
        st.rerun()
    if st.button("🔁 Révision rapide", use_container_width=True):
        aller_a("revision_rapide")
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
    streak = get_streak_jours()

    col_a, col_b = st.columns(2)
    if cartes_dues:
        col_a.metric("📅 Dues", cartes_dues)
    else:
        col_a.success("✓ À jour")
    if streak > 0:
        col_b.metric("🔥 Streak", f"{streak} j")

    st.caption(f"{len(CURRICULUM)} concepts · {len(ORDRE_AFFICHAGE_MODULES)} modules")


# ── Page : ACCUEIL ────────────────────────────────────────────────────────────

def page_accueil():
    # Hero brandé Nord Paradigm
    st.markdown(
        hero_html(
            title_main="Military-grade discipline.",
            title_accent="AI governance that works.",
            subtitle=(
                "Apprentissage espacé pour la pratique de gouvernance d'IA. "
                "Quiz adaptatifs, évaluation par Claude, planification FSRS-4.5. "
                "13 modules · 59 concepts · français et anglais."
            ),
            tag_text="Scientia · Nord Paradigm",
        ),
        unsafe_allow_html=True,
    )

    progression = get_toute_progression()
    nb_concepts_etudies = len(progression)
    nb_maitrises = sum(1 for p in progression.values() if p.get("statut") == "maitrise")
    streak = get_streak_jours()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Étudiés", nb_concepts_etudies)
    col2.metric("Maîtrisés", nb_maitrises)
    col3.metric("À réviser", nb_cartes_dues())
    col4.metric("🔥 Streak", f"{streak} j" if streak > 0 else "—")

    st.markdown("")

    # ── Bandeau de reprise ────────────────────────────────────────────────────
    derniere = get_derniere_activite()
    if derniere and derniere.get("derniere_action"):
        cle = derniere.get("concept_id")
        concept = CURRICULUM.get(cle) if cle else None
        if concept:
            action = derniere.get("derniere_action")
            idx = derniere.get("index_question", 0) or 0
            cartes = get_cartes_concept(cle)
            total = len(cartes)
            quand = temps_relatif(derniere.get("derniere_activite"))
            if action == "quiz" and total:
                meta = (
                    f"Question {min(idx + 1, total)}/{total} · "
                    f"{nom_module_avec_drapeau(concept['module'])} · {quand}"
                )
            elif action == "socratique":
                meta = (
                    f"Dialogue socratique · "
                    f"{nom_module_avec_drapeau(concept['module'])} · {quand}"
                )
            else:
                meta = f"{nom_module_avec_drapeau(concept['module'])} · {quand}"

            st.markdown(
                resume_card_html(
                    label="▶ Reprendre où tu étais",
                    title=concept["titre"],
                    meta=meta,
                ),
                unsafe_allow_html=True,
            )
            col_a, col_b = st.columns([3, 1])
            if col_a.button("▶️ Reprendre",
                            type="primary",
                            use_container_width=True):
                if action == "socratique":
                    aller_a("socratique", soc_concept=cle)
                else:
                    aller_a("etudier", concept_actuel=cle)
                    st.session_state.session_chargee_de_db = False
                st.rerun()
            if col_b.button("✕ Abandonner",
                            use_container_width=True):
                effacer_derniere_activite()
                st.rerun()

    # ── Recommandé pour toi ──────────────────────────────────────────────────
    reco = recommander_concept(progression)
    if reco:
        cle, raison = reco
        c = CURRICULUM[cle]
        st.markdown(
            reco_card_html(
                label="💡 Recommandé pour toi",
                title=c["titre"],
                meta=f"{nom_module_avec_drapeau(c['module'])} · {raison}",
            ),
            unsafe_allow_html=True,
        )
        if st.button("Étudier ce concept →",
                     key="reco_btn",
                     type="primary", use_container_width=True):
            aller_a("etudier", concept_actuel=cle)
            reset_quiz()
            st.session_state.session_chargee_de_db = False
            st.rerun()

    # ── Cartes dues ──────────────────────────────────────────────────────────
    cartes_dues = get_cartes_dues()
    if cartes_dues:
        st.markdown("### 🔁 Révisions dues")
        st.caption("Cartes dont la prochaine révision est aujourd'hui ou passée.")
        if len(cartes_dues) >= 3:
            if st.button("⚡ Lancer une session de révision rapide",
                         use_container_width=True):
                aller_a("revision_rapide")
                st.rerun()
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
                    st.session_state.session_chargee_de_db = False
                    st.rerun()
        if len(cartes_dues) > 5:
            st.caption(f"+ {len(cartes_dues) - 5} autres cartes dues")
    else:
        # Pas de révisions dues → bouton démarrer
        st.markdown("### Démarrer rapidement")
        if st.button("📚 Choisir un concept à étudier",
                     type="primary", use_container_width=True):
            aller_a("modules")
            st.rerun()

    planning = get_planning_14j()
    if planning:
        with st.expander("📆 Planning des 14 prochains jours"):
            for r in planning[:30]:
                st.write(f"`{r['prochaine_rev']}` · {r['enonce'][:80]}")


def recommander_concept(progression: dict) -> tuple[str, str] | None:
    """
    Logique de recommandation :
      1. Concept en_cours (statut='en_cours' avec score < 3) → continuer.
      2. Premier concept jamais étudié dans le module en cours.
      3. Premier concept du curriculum jamais étudié.
    Retourne (concept_id, raison) ou None.
    """
    # 1. Concept en cours non maîtrisé
    en_cours = [
        cid for cid, p in progression.items()
        if p.get("statut") == "en_cours"
        and (p.get("score_moyen") or 0) < 3.0
        and cid in CURRICULUM
    ]
    if en_cours:
        return en_cours[0], "Concept que tu as déjà commencé sans encore maîtriser."

    # 2. Concept jamais étudié, en respectant l'ordre des modules
    deja_vus = set(progression.keys())
    for m in ORDRE_AFFICHAGE_MODULES:
        if m == 99:
            continue
        for cle in get_concepts_par_module(m):
            if cle in deja_vus:
                continue
            return cle, f"Premier concept non étudié du module M{m:02d}."
    return None


# ── Page : MODULES (vue compacte, filtre langue) ──────────────────────────────

def page_modules():
    st.markdown(
        hero_html(
            title_main="Choisis un module",
            title_accent="apprends à ton rythme.",
            subtitle=(
                "13 modules de gouvernance d'IA · 59 concepts · français + anglais. "
                "Filtre par langue, étudie au fil des prérequis, "
                "ou laisse FSRS planifier tes révisions."
            ),
            tag_text="Curriculum · 13 modules",
        ),
        unsafe_allow_html=True,
    )

    # Filtre langue
    col_f1, col_f2, col_f3 = st.columns(3)
    if col_f1.button(
            "🌐 Tous", use_container_width=True,
            type="primary" if st.session_state.filtre_langue is None else "secondary"):
        st.session_state.filtre_langue = None
        st.rerun()
    if col_f2.button(
            "FR · Français", use_container_width=True,
            type="primary" if st.session_state.filtre_langue == "fr" else "secondary"):
        st.session_state.filtre_langue = "fr"
        st.rerun()
    if col_f3.button(
            "EN · English", use_container_width=True,
            type="primary" if st.session_state.filtre_langue == "en" else "secondary"):
        st.session_state.filtre_langue = "en"
        st.rerun()

    # Construire la liste filtrée
    modules_avec_concepts = []
    for m in ORDRE_AFFICHAGE_MODULES:
        if (st.session_state.filtre_langue
                and LANGUE_MODULES.get(m) != st.session_state.filtre_langue):
            continue
        concepts = get_concepts_par_module(m)
        if concepts:
            modules_avec_concepts.append((m, concepts))

    if not modules_avec_concepts:
        st.info("Aucun module ne correspond à ce filtre.")
        return

    nom_choisi = st.selectbox(
        "Module",
        options=[m for m, _ in modules_avec_concepts],
        format_func=nom_module_avec_drapeau,
        key="select_module",
    )

    concepts = get_concepts_par_module(nom_choisi)
    progression = get_toute_progression()

    st.markdown(f"### {nom_module_avec_drapeau(nom_choisi)}")
    st.caption(f"{len(concepts)} concepts dans ce module")

    # Vue compacte : un bloc par concept, sans expander de texte par défaut.
    for cle in concepts:
        c = CURRICULUM[cle]
        prog = progression.get(cle, {})
        statut = prog.get("statut", "nouveau")
        moyenne = prog.get("score_moyen", 0)

        emoji = {"nouveau": "○", "en_cours": "🟡", "maitrise": "🟢"}.get(statut, "○")
        score_txt = f"  ·  {moyenne:.1f}/4" if moyenne else ""
        col_a, col_b = st.columns([4, 1])
        col_a.markdown(f"{emoji} **{c['titre']}**{score_txt}")
        if col_b.button("Étudier",
                        key=f"etu_{cle}",
                        use_container_width=True,
                        type="primary"):
            aller_a("etudier", concept_actuel=cle)
            reset_quiz()
            st.session_state.session_chargee_de_db = False
            st.rerun()

    # Lien vers le module suivant si pertinent
    parcours = PARCOURS_CONSEILLES.get(nom_choisi)
    if parcours:
        st.markdown("")
        if st.button(parcours["label"], use_container_width=True):
            st.session_state.select_module = parcours["module"]
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
    tag = "FR" if concept.get("langue", "fr") == "fr" else "EN"
    st.title(f"[{tag}] {concept['titre']}")
    st.caption(
        f"Module {concept['module']} — "
        f"{NOMS_MODULES.get(concept['module'], '?')}"
    )

    # Mémoriser l'activité 'lecture' pour la reprise
    set_derniere_activite("lecture", cle, 0,
                          quiz_scores=[], quiz_carte_ids=[],
                          termine=False)

    if st.button("← Retour aux modules", use_container_width=False):
        aller_a("modules")
        reset_quiz()
        st.rerun()

    # ── Étape 1 : pas de questions chargées → générer ou recharger ───────────

    if not st.session_state.questions:
        with st.expander("📖 Texte source", expanded=False):
            st.markdown(concept["texte"])

        cartes_existantes = get_cartes_concept(cle)

        n_q = st.slider(
            "Nombre de questions",
            min_value=3, max_value=10,
            value=st.session_state.n_questions,
            key=f"n_q_{cle}",
        )
        st.session_state.n_questions = n_q

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
                        "langue": q.get("langue") or
                                  concept.get("langue", "fr"),
                    }
                    for q in cartes_existantes
                ]
                st.session_state.carte_ids = [q["id"] for q in cartes_existantes]
                st.session_state.index_question = 0
                st.session_state.scores_session = []
                st.session_state.debut_question = time.time()
                set_derniere_activite(
                    "quiz", cle, 0,
                    quiz_scores=[],
                    quiz_carte_ids=st.session_state.carte_ids,
                    termine=False,
                )
                st.rerun()

        bouton_label = (
            f"🔄 Régénérer {n_q} questions" if cartes_existantes
            else f"✨ Générer {n_q} questions avec Claude"
        )
        if col2.button(bouton_label, use_container_width=True):
            with st.spinner("Génération en cours…"):
                try:
                    qs = generer_questions(concept, n=n_q)
                    ids = sauvegarder_cartes(cle, qs,
                                              langue=concept.get("langue", "fr"))
                    st.session_state.questions = qs
                    st.session_state.carte_ids = ids
                    st.session_state.index_question = 0
                    st.session_state.scores_session = []
                    st.session_state.debut_question = time.time()
                    set_derniere_activite(
                        "quiz", cle, 0,
                        quiz_scores=[],
                        quiz_carte_ids=ids,
                        termine=False,
                    )
                    st.rerun()
                except Exception as e:
                    st.error(f"Erreur de génération : {e}")

        # Bouton reset progression (Sprint D)
        st.markdown("---")
        with st.expander("⚠️ Réinitialiser la progression de ce concept"):
            st.caption(
                "Supprime les cartes sauvegardées, les révisions et la "
                "progression FSRS pour ce concept. Action irréversible."
            )
            if st.button("🗑 Reset complet",
                         key=f"reset_{cle}",
                         use_container_width=True):
                reset_progression_concept(cle)
                st.success("Progression réinitialisée.")
                st.rerun()

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
        # On marque la session comme terminée (rien à reprendre)
        effacer_derniere_activite()

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

    if st.session_state.session_chargee_de_db and i > 0:
        st.info(f"📖 Reprise — tu en étais à la question {i + 1}.")
        # Réinitialiser le drapeau pour ne plus afficher le badge.
        st.session_state.session_chargee_de_db = False

    # Texte source disponible pendant tout le quiz (livre ouvert)
    with st.expander("📖 Texte source (livre ouvert)", expanded=False):
        st.markdown(concept["texte"])

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
            placeholder="Réponds librement…",
        )

        # ── Tuteur socratique sur la question (sous le champ de réponse) ──
        soc_ouvert = cle_soc in st.session_state.q_soc_ouverts
        if not soc_ouvert:
            if st.button("🎓 Discuter avec Claude pour mieux comprendre la question",
                         key=f"open_soc_{cle}_{i}",
                         use_container_width=True):
                st.session_state.q_soc_ouverts.add(cle_soc)
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

                with st.container(height=400):
                    for m in dialogue:
                        if m["role"] == "assistant":
                            with st.chat_message("assistant", avatar="🎓"):
                                st.markdown(m["content"])
                        else:
                            with st.chat_message("user", avatar="🧑"):
                                st.markdown(m["content"])

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
            question_for_eval = dict(question)
            if "langue" not in question_for_eval:
                question_for_eval["langue"] = concept.get("langue", "fr")
            with st.spinner("Évaluation par Claude…"):
                try:
                    evaluation = evaluer_reponse(question_for_eval, reponse)
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
            # Mémoriser l'activité au passage
            set_derniere_activite(
                "quiz", cle, i,
                quiz_scores=st.session_state.scores_session,
                quiz_carte_ids=st.session_state.carte_ids,
                termine=False,
            )
            st.rerun()

        if col_b.button("Passer", use_container_width=True):
            st.session_state.scores_session.append(0)
            carte_id = st.session_state.carte_ids[i]
            sauvegarder_revision(
                carte_id=carte_id, score=0, feedback="(passée)", duree_sec=0,
            )
            st.session_state.index_question += 1
            st.session_state.debut_question = time.time()
            set_derniere_activite(
                "quiz", cle,
                st.session_state.index_question,
                quiz_scores=st.session_state.scores_session,
                quiz_carte_ids=st.session_state.carte_ids,
                termine=False,
            )
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
        set_derniere_activite(
            "quiz", cle,
            st.session_state.index_question,
            quiz_scores=st.session_state.scores_session,
            quiz_carte_ids=st.session_state.carte_ids,
            termine=False,
        )
        st.rerun()


# ── Page : RÉVISION RAPIDE (toutes cartes dues, multi-concepts) ──────────────

def page_revision_rapide():
    st.title("🔁 Révision rapide")
    st.caption(
        "Cartes dues triées du plus en retard au plus récent, "
        "tous concepts confondus."
    )
    if st.button("← Accueil", use_container_width=False):
        aller_a("accueil")
        st.rerun()

    cartes = get_cartes_dues()
    if not cartes:
        st.success("✓ Aucune carte due. Tu es à jour.")
        return

    st.metric("Cartes à réviser", len(cartes))

    # Regrouper par concept pour offrir un click direct.
    par_concept: dict = {}
    for c in cartes:
        par_concept.setdefault(c["concept_id"], []).append(c)

    for cle, lot in par_concept.items():
        c = CURRICULUM.get(cle)
        if not c:
            continue
        with st.container(border=True):
            tag = "FR" if c.get("langue", "fr") == "fr" else "EN"
            st.markdown(f"`[{tag}]` **{c['titre']}** — {len(lot)} carte(s)")
            st.caption(
                f"Module {c['module']} — {NOMS_MODULES.get(c['module'], '?')}"
            )
            if st.button("Réviser ce concept →",
                         key=f"rapid_{cle}",
                         type="primary",
                         use_container_width=True):
                aller_a("etudier", concept_actuel=cle)
                reset_quiz()
                st.session_state.session_chargee_de_db = False
                st.rerun()


# ── Page : PROGRESSION ───────────────────────────────────────────────────────

def page_progression():
    streak = get_streak_jours()
    progression = get_toute_progression()
    nb_maitrises = sum(1 for p in progression.values()
                        if p.get("statut") == "maitrise") if progression else 0
    st.markdown(
        hero_html(
            title_main="Ta progression,",
            title_accent="mois après mois.",
            subtitle=(
                f"Tu as étudié {len(progression)} concepts, "
                f"maîtrisé {nb_maitrises}, et tiens un streak de {streak} jour"
                f"{'s' if streak != 1 else ''}. "
                "Exporte ta progression en CSV pour archive personnelle."
            ),
            tag_text=f"📈 Streak {streak} j" if streak else "📈 Progression",
        ),
        unsafe_allow_html=True,
    )

    if not progression:
        st.info("Aucune session enregistrée pour l'instant. "
                "Lance un quiz pour démarrer ta progression.")
        return

    nb_total = len(CURRICULUM)
    nb_etudies = len(progression)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Concepts du curriculum", nb_total)
    col2.metric("Étudiés", nb_etudies)
    col3.metric("Maîtrisés", nb_maitrises)
    col4.metric("🔥 Streak", f"{streak} j" if streak > 0 else "—")

    st.progress(
        nb_maitrises / nb_total if nb_total else 0,
        text=f"Maîtrise globale : {nb_maitrises}/{nb_total}",
    )

    st.markdown("---")

    # Export CSV (Sprint D)
    csv_data = export_progression_csv()
    st.download_button(
        "📥 Exporter ma progression (CSV)",
        data=csv_data,
        file_name="scientia_progression.csv",
        mime="text/csv",
        use_container_width=True,
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
        with st.expander(nom_module_avec_drapeau(m)):
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
        "Charge un PDF, MD ou TXT. Claude extrait 1 à 5 concepts "
        "qui rejoignent le bucket d'ingestion (M99)."
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
                        "au module 99 (Documents ingérés). Va dans Modules pour "
                        "les étudier."
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
                    st.session_state.session_chargee_de_db = False
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

        # Filtre langue
        langue = st.radio(
            "Langue",
            options=["Toutes", "FR · Français", "EN · English"],
            horizontal=True,
            key="soc_filtre_langue",
        )
        filtre = "fr" if langue == "FR · Français" else (
            "en" if langue == "EN · English" else None
        )

        modules_avec_concepts = []
        for m in ORDRE_AFFICHAGE_MODULES:
            if filtre and LANGUE_MODULES.get(m) != filtre:
                continue
            cs = get_concepts_par_module(m)
            if cs:
                modules_avec_concepts.append((m, cs))

        if not modules_avec_concepts:
            st.info("Aucun module ne correspond à ce filtre.")
            return

        m_choisi = st.selectbox(
            "Module",
            options=[m for m, _ in modules_avec_concepts],
            format_func=nom_module_avec_drapeau,
            key="soc_module_select",
        )
        concepts = get_concepts_par_module(m_choisi)

        cle_choisie = st.selectbox(
            "Concept",
            options=concepts,
            format_func=lambda k: CURRICULUM[k]["titre"],
            key="soc_concept_select",
        )

        # Vérifier s'il existe un dialogue actif pour ce concept (Sprint B)
        dialogue_actif = get_dialogue_socratique_actif(cle_choisie)
        if dialogue_actif and dialogue_actif.get("historique"):
            st.info(
                f"📖 Tu as un dialogue en cours sur ce concept "
                f"({len(dialogue_actif['historique'])} échanges)."
            )
            col_r1, col_r2 = st.columns(2)
            if col_r1.button("▶️ Reprendre le dialogue",
                              type="primary", use_container_width=True):
                st.session_state.soc_concept = cle_choisie
                st.session_state.soc_dialogue_id = dialogue_actif["id"]
                st.session_state.soc_historique = dialogue_actif["historique"]
                st.session_state.soc_resume = None
                set_derniere_activite("socratique", cle_choisie)
                st.rerun()
            if col_r2.button("🆕 Nouveau dialogue",
                              use_container_width=True):
                # Marquer l'ancien comme terminé pour ne plus le proposer
                terminer_dialogue_socratique(
                    dialogue_actif["id"],
                    {"score": 0, "synthese": "(dialogue abandonné)"}
                )
                _demarrer_dialogue(cle_choisie)
            return

        if st.button("▶️ Démarrer le dialogue",
                     type="primary", use_container_width=True):
            _demarrer_dialogue(cle_choisie)
        return

    # Étape 2 : dialogue en cours
    cle = st.session_state.soc_concept
    concept = CURRICULUM.get(cle)
    if not concept:
        st.warning("Concept introuvable.")
        st.session_state.soc_concept = None
        return

    tag = "FR" if concept.get("langue", "fr") == "fr" else "EN"
    st.markdown(f"**Concept : `[{tag}]` {concept['titre']}**")
    st.caption(
        f"Module {concept['module']} — "
        f"{NOMS_MODULES.get(concept['module'], '?')}"
    )

    set_derniere_activite("socratique", cle)

    col_a, col_b = st.columns([1, 1])
    if col_a.button("🔄 Nouveau concept", use_container_width=True):
        # Sauvegarder l'état actuel comme dialogue 'en_cours' (déjà fait au fil
        # de l'eau), puis basculer vers la sélection.
        st.session_state.soc_concept = None
        st.session_state.soc_dialogue_id = None
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
                maj_progression(cle, [int(resume.get("score", 0))])
                if st.session_state.soc_dialogue_id:
                    terminer_dialogue_socratique(
                        st.session_state.soc_dialogue_id, resume
                    )
                effacer_derniere_activite()
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
            _demarrer_dialogue(cle, force_nouveau=True)
        if col_d.button("📚 Autre concept",
                        type="primary", use_container_width=True):
            st.session_state.soc_concept = None
            st.session_state.soc_dialogue_id = None
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
        # Persister en DB (Sprint B)
        st.session_state.soc_dialogue_id = sauvegarder_dialogue_socratique(
            cle, st.session_state.soc_historique,
            dialogue_id=st.session_state.soc_dialogue_id,
        )
        set_derniere_activite("socratique", cle)
        st.rerun()


def _demarrer_dialogue(cle: str, force_nouveau: bool = False) -> None:
    """Lance un nouveau dialogue socratique sur le concept donné."""
    concept = CURRICULUM.get(cle)
    if not concept:
        return
    st.session_state.soc_concept = cle
    st.session_state.soc_historique = []
    st.session_state.soc_resume = None
    st.session_state.soc_pending_user = ""
    with st.spinner("Claude prépare une question d'ouverture…"):
        try:
            ouverture = repondre_socratique(concept, [])
            st.session_state.soc_historique.append(
                {"role": "assistant", "content": ouverture}
            )
            st.session_state.soc_dialogue_id = sauvegarder_dialogue_socratique(
                cle, st.session_state.soc_historique
            )
            set_derniere_activite("socratique", cle)
        except Exception as e:
            st.error(f"Erreur : {e}")
            st.session_state.soc_concept = None
            return
    st.rerun()


# ── Routeur principal ─────────────────────────────────────────────────────────

PAGES = {
    "accueil": page_accueil,
    "modules": page_modules,
    "etudier": page_etudier,
    "socratique": page_socratique,
    "progression": page_progression,
    "documents": page_documents,
    "revision_rapide": page_revision_rapide,
}

PAGES.get(st.session_state.page, page_accueil)()

st.markdown(footer_html(), unsafe_allow_html=True)
