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
from i18n import t

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

if "ui_lang" not in st.session_state:
    st.session_state.ui_lang = "fr"  # default UI language
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
    # ── Language toggle FR / EN (top of sidebar) ──────────────────────────
    col_l1, col_l2 = st.columns(2)
    if col_l1.button(
            "FR",
            key="lang_fr",
            use_container_width=True,
            type="primary" if st.session_state.ui_lang == "fr" else "secondary"):
        st.session_state.ui_lang = "fr"
        st.rerun()
    if col_l2.button(
            "EN",
            key="lang_en",
            use_container_width=True,
            type="primary" if st.session_state.ui_lang == "en" else "secondary"):
        st.session_state.ui_lang = "en"
        st.rerun()

    st.markdown(sidebar_brand_html(), unsafe_allow_html=True)

    if st.button(t("sidebar.home"), use_container_width=True):
        aller_a("accueil")
        st.rerun()
    if st.button(t("sidebar.modules"), use_container_width=True):
        aller_a("modules")
        st.rerun()
    if st.button(t("sidebar.quick_review"), use_container_width=True):
        aller_a("revision_rapide")
        st.rerun()
    if st.button(t("sidebar.socratic"), use_container_width=True):
        aller_a("socratique")
        st.rerun()
    if st.button(t("sidebar.progress"), use_container_width=True):
        aller_a("progression")
        st.rerun()
    if st.button(t("sidebar.documents"), use_container_width=True):
        aller_a("documents")
        st.rerun()

    st.markdown("---")
    cartes_dues = nb_cartes_dues()
    streak = get_streak_jours()

    col_a, col_b = st.columns(2)
    if cartes_dues:
        col_a.metric(t("sidebar.due"), cartes_dues)
    else:
        col_a.success(t("sidebar.uptodate"))
    if streak > 0:
        col_b.metric(t("sidebar.streak"), f"{streak} j")

    st.caption(t("sidebar.concepts_total",
                 n=len(CURRICULUM), m=len(ORDRE_AFFICHAGE_MODULES)))


# ── Page : ACCUEIL ────────────────────────────────────────────────────────────

def page_accueil():
    # Hero brandé Nord Paradigm
    st.markdown(
        hero_html(
            title_main=t("home.hero.title_main"),
            title_accent=t("home.hero.title_accent"),
            subtitle=t("home.hero.subtitle"),
            tag_text=t("home.hero.tag"),
        ),
        unsafe_allow_html=True,
    )

    progression = get_toute_progression()
    nb_concepts_etudies = len(progression)
    nb_maitrises = sum(1 for p in progression.values() if p.get("statut") == "maitrise")
    streak = get_streak_jours()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric(t("home.metric.studied"), nb_concepts_etudies)
    col2.metric(t("home.metric.mastered"), nb_maitrises)
    col3.metric(t("home.metric.due"), nb_cartes_dues())
    col4.metric(t("home.metric.streak"), f"{streak} j" if streak > 0 else "—")

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
                    f"{t('home.resume.question_meta', i=min(idx+1, total), total=total)} · "
                    f"{nom_module_avec_drapeau(concept['module'])} · {quand}"
                )
            elif action == "socratique":
                meta = (
                    f"{t('home.resume.socratic_meta')} · "
                    f"{nom_module_avec_drapeau(concept['module'])} · {quand}"
                )
            else:
                meta = f"{nom_module_avec_drapeau(concept['module'])} · {quand}"

            st.markdown(
                resume_card_html(
                    label=t("home.resume.label"),
                    title=concept["titre"],
                    meta=meta,
                ),
                unsafe_allow_html=True,
            )
            col_a, col_b = st.columns([3, 1])
            if col_a.button(t("home.resume.button"),
                            type="primary",
                            use_container_width=True):
                if action == "socratique":
                    aller_a("socratique", soc_concept=cle)
                else:
                    aller_a("etudier", concept_actuel=cle)
                    st.session_state.session_chargee_de_db = False
                st.rerun()
            if col_b.button(t("home.resume.abandon"),
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
                label=t("home.reco.label"),
                title=c["titre"],
                meta=f"{nom_module_avec_drapeau(c['module'])} · {raison}",
            ),
            unsafe_allow_html=True,
        )
        if st.button(t("home.reco.button"),
                     key="reco_btn",
                     type="primary", use_container_width=True):
            aller_a("etudier", concept_actuel=cle)
            reset_quiz()
            st.session_state.session_chargee_de_db = False
            st.rerun()

    # ── Cartes dues ──────────────────────────────────────────────────────────
    cartes_dues = get_cartes_dues()
    if cartes_dues:
        st.markdown(f"### {t('home.due.title')}")
        st.caption(t("home.due.caption"))
        if len(cartes_dues) >= 3:
            if st.button(t("home.due.start_review"),
                         use_container_width=True):
                aller_a("revision_rapide")
                st.rerun()
        for c in cartes_dues[:5]:
            cle_cpt = c["concept_id"]
            titre_cpt = CURRICULUM.get(cle_cpt, {}).get("titre", cle_cpt)
            with st.container(border=True):
                st.markdown(f"**{titre_cpt}**")
                st.caption(c["enonce"][:150])
                if st.button(t("home.due.review_one"), key=f"rev_{c['id']}",
                             use_container_width=True):
                    aller_a("etudier", concept_actuel=cle_cpt)
                    reset_quiz()
                    st.session_state.session_chargee_de_db = False
                    st.rerun()
        if len(cartes_dues) > 5:
            st.caption(t("home.due.more", n=len(cartes_dues) - 5))
    else:
        # Pas de révisions dues → bouton démarrer
        st.markdown(f"### {t('home.start_quick')}")
        if st.button(t("home.start_choose"),
                     type="primary", use_container_width=True):
            aller_a("modules")
            st.rerun()

    planning = get_planning_14j()
    if planning:
        with st.expander(t("home.planning")):
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
        return en_cours[0], t("home.reco.reason_in_progress")

    # 2. Concept jamais étudié, en respectant l'ordre des modules
    deja_vus = set(progression.keys())
    for m in ORDRE_AFFICHAGE_MODULES:
        if m == 99:
            continue
        for cle in get_concepts_par_module(m):
            if cle in deja_vus:
                continue
            return cle, t("home.reco.reason_first", m=m)
    return None


# ── Page : MODULES (vue compacte, filtre langue) ──────────────────────────────

def page_modules():
    st.markdown(
        hero_html(
            title_main=t("modules.hero.title_main"),
            title_accent=t("modules.hero.title_accent"),
            subtitle=t("modules.hero.subtitle"),
            tag_text=t("modules.hero.tag"),
        ),
        unsafe_allow_html=True,
    )

    # Filtre langue
    col_f1, col_f2, col_f3 = st.columns(3)
    if col_f1.button(
            t("modules.filter_all"), use_container_width=True,
            type="primary" if st.session_state.filtre_langue is None else "secondary"):
        st.session_state.filtre_langue = None
        st.rerun()
    if col_f2.button(
            t("modules.filter_fr"), use_container_width=True,
            type="primary" if st.session_state.filtre_langue == "fr" else "secondary"):
        st.session_state.filtre_langue = "fr"
        st.rerun()
    if col_f3.button(
            t("modules.filter_en"), use_container_width=True,
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
        st.info(t("modules.no_match"))
        return

    nom_choisi = st.selectbox(
        t("modules.label"),
        options=[m for m, _ in modules_avec_concepts],
        format_func=nom_module_avec_drapeau,
        key="select_module",
    )

    concepts = get_concepts_par_module(nom_choisi)
    progression = get_toute_progression()

    st.markdown(f"### {nom_module_avec_drapeau(nom_choisi)}")
    st.caption(t("modules.concepts_count", n=len(concepts)))

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
        if col_b.button(t("modules.study"),
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
        st.warning(t("etudier.no_concept"))
        if st.button(t("etudier.back"), use_container_width=True):
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

    if st.button(t("etudier.back"), use_container_width=False):
        aller_a("modules")
        reset_quiz()
        st.rerun()

    # ── Étape 1 : pas de questions chargées → générer ou recharger ───────────

    if not st.session_state.questions:
        with st.expander(t("etudier.source"), expanded=False):
            st.markdown(concept["texte"])

        cartes_existantes = get_cartes_concept(cle)

        n_q = st.slider(
            t("etudier.q_count"),
            min_value=3, max_value=10,
            value=st.session_state.n_questions,
            key=f"n_q_{cle}",
        )
        st.session_state.n_questions = n_q

        col1, col2 = st.columns(2)
        if cartes_existantes:
            col1.metric(t("etudier.cards_saved"), len(cartes_existantes))
            if col1.button(t("etudier.start_quiz"),
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
            t("etudier.regenerate", n=n_q) if cartes_existantes
            else t("etudier.generate", n=n_q)
        )
        if col2.button(bouton_label, use_container_width=True):
            with st.spinner(t("etudier.generating")):
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
                    st.error(t("etudier.gen_error", e=e))

        # Bouton reset progression (Sprint D)
        st.markdown("---")
        with st.expander(t("etudier.reset.label")):
            st.caption(t("etudier.reset.help"))
            if st.button(t("etudier.reset.button"),
                         key=f"reset_{cle}",
                         use_container_width=True):
                reset_progression_concept(cle)
                st.success(t("etudier.reset.done"))
                st.rerun()

        # Notes personnelles persistantes
        st.markdown("---")
        with st.expander(t("etudier.notes")):
            note = st.text_area(
                t("etudier.notes_label"),
                value=get_note(cle),
                height=150,
                label_visibility="collapsed",
            )
            if st.button(t("etudier.notes_save"), use_container_width=True):
                save_note(cle, note)
                st.success(t("etudier.notes_saved"))
        return

    # ── Étape 2 : quiz en cours ──────────────────────────────────────────────

    i = st.session_state.index_question
    total = len(st.session_state.questions)

    if i >= total:
        # Fin de session
        st.success(t("etudier.session_done"))
        scores = st.session_state.scores_session
        moyenne = sum(scores) / len(scores) if scores else 0
        col1, col2, col3 = st.columns(3)
        col1.metric(t("etudier.questions"), total)
        col2.metric(t("etudier.avg_score"), f"{moyenne:.2f}/4")
        col3.metric(t("etudier.mastery"), "✓" if moyenne >= 3 else "↻")

        st.progress(min(1.0, moyenne / 4),
                    text=t("etudier.score_text", s=moyenne))

        if moyenne >= 3.5:
            st.balloons()
            st.markdown(f"### {t('etudier.excellent')}")
        elif moyenne >= 2.5:
            st.markdown(f"### {t('etudier.good')}")
        else:
            st.markdown(f"### {t('etudier.redo')}")

        maj_progression(cle, scores)
        effacer_derniere_activite()

        col_a, col_b = st.columns(2)
        if col_a.button(t("etudier.retake"), use_container_width=True):
            reset_quiz()
            st.rerun()
        if col_b.button(t("etudier.other"),
                        type="primary", use_container_width=True):
            aller_a("modules")
            reset_quiz()
            st.rerun()
        return

    # Question courante
    question = st.session_state.questions[i]
    progress = (i) / total
    st.progress(progress, text=t("etudier.progress", i=i+1, total=total))

    if st.session_state.session_chargee_de_db and i > 0:
        st.info(t("etudier.resume_at", n=i+1))
        st.session_state.session_chargee_de_db = False

    # Texte source disponible pendant tout le quiz (livre ouvert)
    with st.expander(t("etudier.source_open"), expanded=False):
        st.markdown(concept["texte"])

    type_q = question.get("type", "?").replace("_", " ").title()
    st.caption(t("etudier.q_type", t=type_q))
    st.markdown(f"### {question['question']}")

    # Bouton indice (n'apparaît que si la question en a un)
    indice_txt = question.get("indice", "") or ""
    if indice_txt:
        cle_indice = f"indice_{cle}_{i}"
        deja_visible = st.session_state.indice_visible.get(cle_indice, False)
        if not deja_visible:
            if st.button(t("etudier.hint_show"), key=f"btn_{cle_indice}",
                         use_container_width=False):
                st.session_state.indice_visible[cle_indice] = True
                st.rerun()
        else:
            st.info(f"💡 {indice_txt}")

    cle_zone = f"reponse_{cle}_{i}"
    cle_soc = (cle, i)
    if st.session_state.evaluation_courante is None:
        reponse = st.text_area(
            t("etudier.your_answer"),
            key=cle_zone,
            height=150,
            placeholder=t("etudier.placeholder"),
        )

        # ── Tuteur socratique sur la question (sous le champ de réponse) ──
        soc_ouvert = cle_soc in st.session_state.q_soc_ouverts
        if not soc_ouvert:
            if st.button(t("etudier.tutor_open"),
                         key=f"open_soc_{cle}_{i}",
                         use_container_width=True):
                st.session_state.q_soc_ouverts.add(cle_soc)
                if cle_soc not in st.session_state.q_soc_dialogues:
                    with st.spinner(t("etudier.tutor_opening")):
                        try:
                            ouverture = aide_socratique_question(
                                concept, question, []
                            )
                            st.session_state.q_soc_dialogues[cle_soc] = [
                                {"role": "assistant", "content": ouverture}
                            ]
                        except Exception as e:
                            st.error(t("etudier.tutor_error", e=e))
                            st.session_state.q_soc_dialogues[cle_soc] = []
                st.rerun()
        else:
            with st.container(border=True):
                st.caption(t("etudier.tutor_caption"))

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
                    t("etudier.tutor_input"),
                    key=f"soc_input_{cle}_{i}",
                )
                if user_msg:
                    dialogue.append({"role": "user", "content": user_msg})
                    with st.spinner(t("etudier.tutor_thinking")):
                        try:
                            relance = aide_socratique_question(
                                concept, question, dialogue
                            )
                            dialogue.append(
                                {"role": "assistant", "content": relance}
                            )
                        except Exception as e:
                            st.error(t("socratique.error", e=e))
                    st.session_state.q_soc_dialogues[cle_soc] = dialogue
                    st.rerun()

                if st.button(t("etudier.tutor_close"),
                             key=f"close_soc_{cle}_{i}",
                             use_container_width=False):
                    st.session_state.q_soc_ouverts.discard(cle_soc)
                    st.rerun()

        col_a, col_b = st.columns([1, 1])
        if col_a.button(t("etudier.submit"),
                        type="primary",
                        use_container_width=True,
                        disabled=not reponse.strip()):
            duree = int(time.time() - st.session_state.debut_question)
            question_for_eval = dict(question)
            if "langue" not in question_for_eval:
                question_for_eval["langue"] = concept.get("langue", "fr")
            with st.spinner(t("etudier.evaluating")):
                try:
                    evaluation = evaluer_reponse(question_for_eval, reponse)
                except Exception as e:
                    st.error(t("etudier.eval_error", e=e))
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

        if col_b.button(t("etudier.skip"), use_container_width=True):
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
        st.success(t("etudier.correct", s=score))
    elif score >= 2:
        st.warning(t("etudier.partial", s=score))
    else:
        st.error(t("etudier.review", s=score))

    st.markdown(t("etudier.feedback", f=evaluation.get('feedback', '')))

    if not correct:
        with st.expander(t("etudier.see_ref")):
            st.markdown(question.get("reponse_ref", ""))

    if st.button(t("etudier.next"),
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
    st.title(t("revision.title"))
    st.caption(t("revision.caption"))
    if st.button(t("revision.back"), use_container_width=False):
        aller_a("accueil")
        st.rerun()

    cartes = get_cartes_dues()
    if not cartes:
        st.success(t("revision.empty"))
        return

    st.metric(t("revision.metric"), len(cartes))

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
            st.markdown(f"`[{tag}]` **{c['titre']}** — "
                         + t("revision.concept_due", n=len(lot)))
            st.caption(
                f"Module {c['module']} — {NOMS_MODULES.get(c['module'], '?')}"
            )
            if st.button(t("revision.review_concept"),
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
            title_main=t("progress.hero.title_main"),
            title_accent=t("progress.hero.title_accent"),
            subtitle=t(
                "progress.hero.subtitle",
                n=len(progression),
                m=nb_maitrises,
                s=streak,
                p="s" if streak != 1 else "",
            ),
            tag_text=f"📈 Streak {streak} j" if streak else "📈 Progress",
        ),
        unsafe_allow_html=True,
    )

    if not progression:
        st.info(t("progress.empty"))
        return

    nb_total = len(CURRICULUM)
    nb_etudies = len(progression)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric(t("progress.metric.curriculum"), nb_total)
    col2.metric(t("home.metric.studied"), nb_etudies)
    col3.metric(t("home.metric.mastered"), nb_maitrises)
    col4.metric(t("home.metric.streak"), f"{streak} j" if streak > 0 else "—")

    st.progress(
        nb_maitrises / nb_total if nb_total else 0,
        text=t("progress.global", m=nb_maitrises, t=nb_total),
    )

    st.markdown("---")

    # Export CSV
    csv_data = export_progression_csv()
    st.download_button(
        t("progress.export"),
        data=csv_data,
        file_name="scientia_progression.csv",
        mime="text/csv",
        use_container_width=True,
    )

    st.markdown("---")
    st.subheader(t("progress.detail"))

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
                    f"`{moyenne:.2f}/4` " + t("progress.session_count", n=nb)
                )


# ── Page : DOCUMENTS ─────────────────────────────────────────────────────────

def page_documents():
    st.title(t("documents.title"))
    st.caption(t("documents.caption"))

    DOCS_DIR = Path(__file__).parent / "docs"
    DOCS_DIR.mkdir(exist_ok=True)

    fichier = st.file_uploader(
        t("documents.choose"),
        type=["pdf", "md", "txt"],
        accept_multiple_files=False,
    )

    if fichier:
        st.write(f"**{fichier.name}** — {fichier.size // 1024} Ko")
        if st.button(t("documents.extract"),
                     type="primary", use_container_width=True):
            from ingestion import ingerer_fichier
            chemin = DOCS_DIR / fichier.name
            chemin.write_bytes(fichier.getvalue())
            with st.spinner(t("documents.extracting")):
                try:
                    nouvelles_cles = ingerer_fichier(chemin)
                    from curriculum import _charger_concepts_dynamiques
                    _charger_concepts_dynamiques()
                    st.success(t("documents.added", n=len(nouvelles_cles)))
                except Exception as e:
                    st.error(t("documents.error", e=e))

    st.markdown("---")
    from ingestion import charger_concepts_dynamiques, supprimer_concept
    concepts_dyn = charger_concepts_dynamiques()
    if concepts_dyn:
        st.subheader(t("documents.ingested", n=len(concepts_dyn)))
        for cle, c in concepts_dyn.items():
            with st.container(border=True):
                st.markdown(f"**{c['titre']}**")
                st.caption(t("documents.source_meta",
                              s=c.get('source', '?'),
                              d=c.get('date_ingestion', '?')))
                col1, col2 = st.columns([3, 1])
                if col1.button(t("documents.study"), key=f"etu_dyn_{cle}",
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
        st.info(t("documents.empty"))


# ── Page : DIALOGUE SOCRATIQUE ───────────────────────────────────────────────

def page_socratique():
    st.title(t("socratique.title"))
    st.caption(t("socratique.caption"))

    # Étape 1 : sélection du concept
    if not st.session_state.soc_concept:
        st.subheader(t("socratique.choose"))

        # Filtre langue
        opt_all = "Toutes" if st.session_state.ui_lang == "fr" else "All"
        opt_fr = t("modules.filter_fr")
        opt_en = t("modules.filter_en")
        langue = st.radio(
            t("socratique.lang"),
            options=[opt_all, opt_fr, opt_en],
            horizontal=True,
            key="soc_filtre_langue",
        )
        filtre = "fr" if langue == opt_fr else (
            "en" if langue == opt_en else None
        )

        modules_avec_concepts = []
        for m in ORDRE_AFFICHAGE_MODULES:
            if filtre and LANGUE_MODULES.get(m) != filtre:
                continue
            cs = get_concepts_par_module(m)
            if cs:
                modules_avec_concepts.append((m, cs))

        if not modules_avec_concepts:
            st.info(t("modules.no_match"))
            return

        m_choisi = st.selectbox(
            t("socratique.module"),
            options=[m for m, _ in modules_avec_concepts],
            format_func=nom_module_avec_drapeau,
            key="soc_module_select",
        )
        concepts = get_concepts_par_module(m_choisi)

        cle_choisie = st.selectbox(
            t("socratique.concept"),
            options=concepts,
            format_func=lambda k: CURRICULUM[k]["titre"],
            key="soc_concept_select",
        )

        dialogue_actif = get_dialogue_socratique_actif(cle_choisie)
        if dialogue_actif and dialogue_actif.get("historique"):
            st.info(t("socratique.has_active",
                      n=len(dialogue_actif['historique'])))
            col_r1, col_r2 = st.columns(2)
            if col_r1.button(t("socratique.resume"),
                              type="primary", use_container_width=True):
                st.session_state.soc_concept = cle_choisie
                st.session_state.soc_dialogue_id = dialogue_actif["id"]
                st.session_state.soc_historique = dialogue_actif["historique"]
                st.session_state.soc_resume = None
                set_derniere_activite("socratique", cle_choisie)
                st.rerun()
            if col_r2.button(t("socratique.new"),
                              use_container_width=True):
                terminer_dialogue_socratique(
                    dialogue_actif["id"],
                    {"score": 0, "synthese": "(dialogue abandonné)"}
                )
                _demarrer_dialogue(cle_choisie)
            return

        if st.button(t("socratique.start"),
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
    st.markdown(t("socratique.concept_label", tag=tag, titre=concept['titre']))
    st.caption(
        f"Module {concept['module']} — "
        f"{NOMS_MODULES.get(concept['module'], '?')}"
    )

    set_derniere_activite("socratique", cle)

    col_a, col_b = st.columns([1, 1])
    if col_a.button(t("socratique.new_concept"), use_container_width=True):
        st.session_state.soc_concept = None
        st.session_state.soc_dialogue_id = None
        st.session_state.soc_historique = []
        st.session_state.soc_resume = None
        st.rerun()
    termine = col_b.button(
        t("socratique.finish"),
        type="primary",
        use_container_width=True,
        disabled=len(st.session_state.soc_historique) < 3,
    )

    if termine and not st.session_state.soc_resume:
        with st.spinner(t("socratique.summary")):
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
                st.error(t("socratique.error", e=e))

    # Affichage du bilan si présent
    if st.session_state.soc_resume:
        r = st.session_state.soc_resume
        score = int(r.get("score", 0))
        st.markdown("---")
        st.subheader(t("socratique.bilan"))

        if score >= 3:
            st.success(t("socratique.score_good", s=score))
        elif score >= 2:
            st.warning(t("socratique.score_partial", s=score))
        else:
            st.error(t("socratique.score_redo", s=score))

        st.markdown(t("socratique.strengths", x=r.get('points_forts', '')))
        st.markdown(t("socratique.deepen", x=r.get('a_approfondir', '')))

        with st.expander(t("socratique.synthesis")):
            st.markdown(r.get("synthese", ""))

        col_c, col_d = st.columns(2)
        if col_c.button(t("socratique.relaunch"),
                        use_container_width=True):
            _demarrer_dialogue(cle, force_nouveau=True)
        if col_d.button(t("etudier.other"),
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

    reponse = st.chat_input(t("socratique.input"), key="soc_chat_input")
    if reponse:
        st.session_state.soc_historique.append(
            {"role": "user", "content": reponse}
        )
        with st.spinner(t("etudier.tutor_thinking")):
            try:
                relance = repondre_socratique(
                    concept, st.session_state.soc_historique
                )
                st.session_state.soc_historique.append(
                    {"role": "assistant", "content": relance}
                )
            except Exception as e:
                st.error(t("socratique.error", e=e))
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
    with st.spinner(t("socratique.preparing")):
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
            st.error(t("socratique.error", e=e))
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
