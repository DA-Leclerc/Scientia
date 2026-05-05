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
    # Alpha School #1
    enregistrer_session,
    get_etat_maitrise,
    enregistrer_points_faibles,
    get_points_faibles,
    marquer_points_faibles_resolus,
    # Alpha School #4
    enregistrer_teach_back,
    get_meilleur_teach_back,
    est_pret_a_enseigner,
    # Alpha School #5
    sauvegarder_objectif,
    get_objectifs_actifs,
    calculer_velocite,
    get_revisions_par_jour,
    get_concepts_a_risque,
    # Round 2 — features supplémentaires
    sauvegarder_cheat_sheet,
    get_derniere_cheat_sheet,
    sauvegarder_mission,
    cloturer_mission,
    get_missions_recentes,
    calibration_stats,
    calibration_resume,
    previsions_oubli,
    cartes_en_risque_aujourd,
    sync_obsidian,
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
    generer_questions_ciblees,
    generer_diagnostic,
    evaluer_reponse,
    evaluer_teach_back,
    repondre_socratique,
    resumer_socratique,
    aide_socratique_question,
    # Round 2
    generer_cheat_sheet,
    generer_mission,
    evaluer_mission,
    transcrire_audio_whisper,
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
if "ratees_session" not in st.session_state:
    # Liste de dicts {critere, score} pour les questions ratées (Alpha #1)
    st.session_state.ratees_session = []
if "session_type" not in st.session_state:
    # 'quiz' (normal) | 'targeted' (Alpha #1) | 'sprint' (Alpha #2) | 'diagnostic' (Alpha #3)
    st.session_state.session_type = "quiz"
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
    st.session_state.ratees_session = []
    st.session_state.session_type = "quiz"
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
    if st.button(t("sidebar.sprint"), use_container_width=True):
        aller_a("sprint")
        st.rerun()
    if st.button(t("sidebar.mission"), use_container_width=True):
        aller_a("mission")
        st.rerun()
    if st.button(t("sidebar.socratic"), use_container_width=True):
        aller_a("socratique")
        st.rerun()
    if st.button(t("teach.button"), use_container_width=True):
        aller_a("teach_back")
        st.rerun()
    if st.button(t("sidebar.constellation"), use_container_width=True):
        aller_a("constellation")
        st.rerun()
    if st.button(t("sidebar.forecast"), use_container_width=True):
        aller_a("forecast")
        st.rerun()
    if st.button(t("sidebar.dashboard"), use_container_width=True):
        aller_a("dashboard")
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

    # Alpha #3 : bouton diagnostic si aucun concept du module n'a été étudié
    deja_etudies = [k for k in concepts if k in progression]
    if not deja_etudies and len(concepts) >= 3:
        if st.button(t("diag.button", n=len(concepts)),
                     use_container_width=True):
            st.session_state.diag_module = nom_choisi
            aller_a("diagnostic")
            st.rerun()

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
                st.session_state.ratees_session = []
                st.session_state.session_type = "quiz"
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
                    st.session_state.ratees_session = []
                    st.session_state.session_type = "quiz"
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

        # ── Idea #2 + #10 : cheat sheet + sync Obsidian ─────────────────
        # Visible si le concept est au moins étudié (a déjà des cartes)
        if cartes_existantes:
            st.markdown("---")
            with st.expander(t("cheat.button")):
                st.caption(t("cheat.copy_hint"))
                cs = get_derniere_cheat_sheet(cle)
                col_cs1, col_cs2 = st.columns([3, 1])
                bouton_label_cs = (
                    t("cheat.regenerate") if cs else t("cheat.button")
                )
                if col_cs1.button(bouton_label_cs,
                                   key=f"cs_btn_{cle}",
                                   use_container_width=True):
                    with st.spinner(t("cheat.generating")):
                        try:
                            md = generer_cheat_sheet(concept)
                            sauvegarder_cheat_sheet(cle, md)
                            cs = {"contenu_md": md}
                        except Exception as e:
                            st.error(f"Error: {e}")
                if cs:
                    st.markdown("---")
                    st.markdown(cs["contenu_md"])
                    st.download_button(
                        t("cheat.download"),
                        data=cs["contenu_md"],
                        file_name=f"{cle}.md",
                        mime="text/markdown",
                        use_container_width=True,
                        key=f"cs_dl_{cle}",
                    )

            # Sync Obsidian
            with st.expander(t("obs.button")):
                if not os.environ.get("OBSIDIAN_VAULT_PATH"):
                    st.info(t("obs.no_vault"))
                else:
                    if st.button(t("obs.button"),
                                 key=f"obs_btn_{cle}",
                                 use_container_width=True):
                        from db import (get_meilleur_teach_back as _g_tb,
                                          get_derniere_cheat_sheet as _g_cs)
                        tb = _g_tb(cle)
                        cs_db = _g_cs(cle)
                        try:
                            path = sync_obsidian(
                                cle, concept,
                                teach_back=tb,
                                cheat_sheet=(cs_db.get("contenu_md")
                                             if cs_db else None),
                            )
                            if path:
                                st.success(t("obs.synced", p=path))
                            else:
                                st.info(t("obs.no_vault"))
                        except Exception as e:
                            st.error(t("obs.error", e=e))

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

        # Alpha #1 — enregistrement de session + paliers de maîtrise
        enregistrer_session(cle, st.session_state.session_type or "quiz", scores)
        if st.session_state.ratees_session:
            enregistrer_points_faibles(cle, st.session_state.ratees_session)

        # Affichage du progrès vers la maîtrise
        etat = get_etat_maitrise(cle)
        st.markdown("---")
        st.markdown(f"### {t('mastery.progress.title')}")
        st.progress(
            min(1.0, etat["sessions_passees"] / max(1, etat["sessions_requises"])),
            text=t("mastery.progress.text",
                   p=etat["sessions_passees"], r=etat["sessions_requises"]),
        )
        if etat["statut"] == "maitrise":
            st.success(t("mastery.unlocked"))
            marquer_points_faibles_resolus(cle)
        elif etat["sessions_passees"] >= 1 and moyenne >= 3.0:
            st.info(t("mastery.almost"))
            st.caption(t("mastery.gap_hint"))

        # Re-test ciblé si on a raté au moins 2 questions
        nb_ratees = len(st.session_state.ratees_session)
        if nb_ratees >= 2:
            st.warning(t("mastery.failed", n=nb_ratees))
            if st.button(t("mastery.targeted_button"),
                         use_container_width=True):
                pf = get_points_faibles(cle, limit=5)
                with st.spinner(t("etudier.generating")):
                    try:
                        qs = generer_questions_ciblees(concept, pf,
                                                        n=min(5, max(3, nb_ratees)))
                        ids = sauvegarder_cartes(cle, qs,
                                                  langue=concept.get("langue", "fr"))
                        st.session_state.questions = qs
                        st.session_state.carte_ids = ids
                        st.session_state.index_question = 0
                        st.session_state.scores_session = []
                        st.session_state.ratees_session = []
                        st.session_state.session_type = "targeted"
                        st.session_state.debut_question = time.time()
                        st.session_state.evaluation_courante = None
                        set_derniere_activite(
                            "quiz", cle, 0,
                            quiz_scores=[],
                            quiz_carte_ids=ids,
                            termine=False,
                        )
                        st.rerun()
                    except Exception as e:
                        st.error(t("etudier.gen_error", e=e))

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

    if st.session_state.session_type == "targeted":
        st.caption(f"🎯 {t('mastery.targeted_label')}")

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
    cle_conf = f"conf_{cle}_{i}"
    cle_soc = (cle, i)
    if st.session_state.evaluation_courante is None:
        reponse = st.text_area(
            t("etudier.your_answer"),
            key=cle_zone,
            height=150,
            placeholder=t("etudier.placeholder"),
        )

        # Idea #4 — slider de calibration de confiance
        confiance = st.slider(
            t("calib.label"),
            min_value=1, max_value=5, value=3,
            key=cle_conf,
            help=t("calib.help"),
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
            # Alpha #1 : capture du critère raté pour re-test ciblé
            if score < 3:
                st.session_state.ratees_session.append({
                    "critere": question.get("critere", "") or "",
                    "score": score,
                })

            carte_id = st.session_state.carte_ids[i]
            sauvegarder_revision(
                carte_id=carte_id,
                score=score,
                feedback=evaluation.get("feedback", ""),
                duree_sec=duree,
                confiance_predite=int(st.session_state.get(cle_conf, 3) or 3),
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


# ══════════════════════════════════════════════════════════════════════════════
# ALPHA SCHOOL #2 — Sprint de maîtrise (entrelacement)
# ══════════════════════════════════════════════════════════════════════════════

def page_sprint():
    st.markdown(
        hero_html(
            title_main=t("sprint.hero.title_main"),
            title_accent=t("sprint.hero.title_accent"),
            subtitle=t("sprint.hero.subtitle"),
            tag_text=t("sprint.hero.tag"),
        ),
        unsafe_allow_html=True,
    )

    if "sprint_concepts" not in st.session_state:
        st.session_state.sprint_concepts = []
    if "sprint_questions" not in st.session_state:
        st.session_state.sprint_questions = []
    if "sprint_carte_ids" not in st.session_state:
        st.session_state.sprint_carte_ids = []
    if "sprint_index" not in st.session_state:
        st.session_state.sprint_index = 0
    if "sprint_resultats" not in st.session_state:
        # liste de {concept_id, concept_titre, score, langue}
        st.session_state.sprint_resultats = []
    if "sprint_eval_courante" not in st.session_state:
        st.session_state.sprint_eval_courante = None

    # ── Étape 1 : pas encore démarré → sélection des concepts ────────────────
    if not st.session_state.sprint_questions:
        st.subheader(t("sprint.choose"))

        # Liste des concepts ayant au moins 1 carte sauvegardée
        from db import conn as _conn
        with _conn() as c:
            rows = c.execute(
                "SELECT DISTINCT concept_id FROM cartes"
            ).fetchall()
        eligibles_set = {r["concept_id"] for r in rows}
        eligibles = [(k, CURRICULUM[k]) for k in eligibles_set
                      if k in CURRICULUM]
        if not eligibles:
            st.info(t("sprint.need_cards"))
            return

        # Tri par module puis ordre
        eligibles.sort(key=lambda kv: (kv[1].get("module", 99),
                                        kv[1].get("ordre", 0)))

        choix = st.multiselect(
            t("sprint.choose"),
            options=[k for k, _ in eligibles],
            format_func=lambda k: (
                f"[{ 'FR' if CURRICULUM[k].get('langue','fr') == 'fr' else 'EN' }] "
                f"M{CURRICULUM[k]['module']:02d} — {CURRICULUM[k]['titre']}"
            ),
            key="sprint_select",
        )

        if len(choix) < 3:
            st.warning(t("sprint.need_more"))
            return

        if st.button(t("sprint.start"),
                     type="primary", use_container_width=True):
            # Tirer 1 question aléatoire de chaque concept choisi
            import random
            qs = []
            ids = []
            ordres = []
            for cle in choix:
                cartes = get_cartes_concept(cle)
                if not cartes:
                    continue
                c_choisie = random.choice(cartes)
                qs.append({
                    "type": c_choisie["type"],
                    "question": c_choisie["enonce"],
                    "reponse_ref": c_choisie["reponse_ref"],
                    "critere": c_choisie["critere"],
                    "indice": c_choisie.get("indice", "") or "",
                    "difficulte": c_choisie["niveau"],
                    "langue": c_choisie.get("langue") or
                              CURRICULUM[cle].get("langue", "fr"),
                    "concept_id": cle,
                    "concept_titre": CURRICULUM[cle]["titre"],
                })
                ids.append(c_choisie["id"])
            # Mélanger
            indices = list(range(len(qs)))
            random.shuffle(indices)
            st.session_state.sprint_concepts = choix
            st.session_state.sprint_questions = [qs[i] for i in indices]
            st.session_state.sprint_carte_ids = [ids[i] for i in indices]
            st.session_state.sprint_index = 0
            st.session_state.sprint_resultats = []
            st.session_state.sprint_eval_courante = None
            st.rerun()
        return

    i = st.session_state.sprint_index
    total = len(st.session_state.sprint_questions)

    # ── Étape 3 : résultats ──────────────────────────────────────────────────
    if i >= total:
        st.subheader(t("sprint.results"))
        moyenne = (
            sum(r["score"] for r in st.session_state.sprint_resultats) /
            max(1, len(st.session_state.sprint_resultats))
        )
        col1, col2 = st.columns(2)
        col1.metric(t("etudier.questions"), total)
        col2.metric(t("etudier.avg_score"), f"{moyenne:.2f}/4")

        st.markdown(f"### {t('sprint.score_per_concept')}")
        # Regrouper par concept (1 question par concept dans ce sprint)
        for r in st.session_state.sprint_resultats:
            score = r["score"]
            emoji = "🟢" if score >= 3 else ("🟡" if score >= 2 else "🔴")
            st.markdown(f"{emoji} **{r['concept_titre']}** — {score}/4")

        st.info(t("sprint.transfer_tip"))

        # Enregistrer une session 'sprint' par concept (avec 1 score chacun)
        for r in st.session_state.sprint_resultats:
            enregistrer_session(r["concept_id"], "sprint", [r["score"]])
            if r["score"] < 3:
                enregistrer_points_faibles(r["concept_id"], [{
                    "critere": r.get("critere", ""),
                    "score": r["score"],
                }])

        if st.button(t("sprint.restart"),
                     type="primary", use_container_width=True):
            st.session_state.sprint_concepts = []
            st.session_state.sprint_questions = []
            st.session_state.sprint_carte_ids = []
            st.session_state.sprint_index = 0
            st.session_state.sprint_resultats = []
            st.session_state.sprint_eval_courante = None
            st.rerun()
        return

    # ── Étape 2 : question courante ──────────────────────────────────────────
    question = st.session_state.sprint_questions[i]
    st.progress(i / total,
                text=t("sprint.q_of", i=i+1, total=total))
    st.caption(t("sprint.concept_hidden"))

    type_q = question.get("type", "?").replace("_", " ").title()
    st.caption(t("etudier.q_type", t=type_q))
    st.markdown(f"### {question['question']}")

    cle_zone = f"sprint_reponse_{i}"
    if st.session_state.sprint_eval_courante is None:
        reponse = st.text_area(
            t("etudier.your_answer"),
            key=cle_zone, height=150,
            placeholder=t("etudier.placeholder"),
        )
        col_a, col_b = st.columns([1, 1])
        if col_a.button(t("etudier.submit"),
                        key=f"sprint_submit_{i}",
                        type="primary", use_container_width=True,
                        disabled=not reponse.strip()):
            with st.spinner(t("etudier.evaluating")):
                try:
                    evaluation = evaluer_reponse(question, reponse)
                except Exception as e:
                    st.error(t("etudier.eval_error", e=e))
                    return
            score = int(evaluation.get("score", 0))
            sauvegarder_revision(
                carte_id=st.session_state.sprint_carte_ids[i],
                score=score,
                feedback=evaluation.get("feedback", ""),
                duree_sec=0,
            )
            st.session_state.sprint_resultats.append({
                "concept_id": question["concept_id"],
                "concept_titre": question["concept_titre"],
                "score": score,
                "critere": question.get("critere", ""),
                "langue": question.get("langue", "fr"),
            })
            st.session_state.sprint_eval_courante = evaluation
            st.rerun()

        if col_b.button(t("etudier.skip"),
                        key=f"sprint_skip_{i}",
                        use_container_width=True):
            st.session_state.sprint_resultats.append({
                "concept_id": question["concept_id"],
                "concept_titre": question["concept_titre"],
                "score": 0,
                "critere": question.get("critere", ""),
                "langue": question.get("langue", "fr"),
            })
            st.session_state.sprint_index += 1
            st.rerun()
        return

    # Affichage évaluation courante
    evaluation = st.session_state.sprint_eval_courante
    score = int(evaluation.get("score", 0))
    correct = bool(evaluation.get("correct", False))

    if correct:
        st.success(t("etudier.correct", s=score))
    elif score >= 2:
        st.warning(t("etudier.partial", s=score))
    else:
        st.error(t("etudier.review", s=score))

    st.markdown(f"**{question['concept_titre']}**")
    st.markdown(t("etudier.feedback", f=evaluation.get('feedback', '')))

    if not correct:
        with st.expander(t("etudier.see_ref")):
            st.markdown(question.get("reponse_ref", ""))

    if st.button(t("etudier.next"),
                 key=f"sprint_next_{i}",
                 type="primary", use_container_width=True):
        st.session_state.sprint_index += 1
        st.session_state.sprint_eval_courante = None
        st.rerun()


# ══════════════════════════════════════════════════════════════════════════════
# ALPHA SCHOOL #3 — Diagnostic pré-module
# ══════════════════════════════════════════════════════════════════════════════

def page_diagnostic():
    if not st.session_state.get("diag_module"):
        st.warning("Aucun module sélectionné pour le diagnostic.")
        if st.button(t("etudier.back"), use_container_width=True):
            aller_a("modules")
            st.rerun()
        return

    m = st.session_state.diag_module
    nom = NOMS_MODULES.get(m, "?")
    st.markdown(
        hero_html(
            title_main=f"M{m:02d}",
            title_accent=nom,
            subtitle=t("diag.intro"),
            tag_text=t("diag.button", n=len(get_concepts_par_module(m))).split('(')[0],
        ),
        unsafe_allow_html=True,
    )

    if "diag_questions" not in st.session_state:
        st.session_state.diag_questions = []
    if "diag_carte_ids" not in st.session_state:
        st.session_state.diag_carte_ids = []
    if "diag_index" not in st.session_state:
        st.session_state.diag_index = 0
    if "diag_resultats" not in st.session_state:
        st.session_state.diag_resultats = []
    if "diag_eval_courante" not in st.session_state:
        st.session_state.diag_eval_courante = None

    # Étape 1 : générer le diagnostic
    if not st.session_state.diag_questions:
        with st.spinner(t("diag.generating")):
            concepts_cles = get_concepts_par_module(m)
            concepts_dicts = []
            for cle in concepts_cles:
                c = dict(CURRICULUM[cle])
                c["id"] = cle
                c["cle"] = cle
                concepts_dicts.append(c)
            try:
                qs = generer_diagnostic(concepts_dicts)
                # Sauvegarder en cartes pour persister, puis mémoriser ids
                ids = []
                for cle, q in zip([c["cle"] for c in concepts_dicts], qs):
                    saved = sauvegarder_cartes(cle, [q],
                                                langue=q.get("langue", "fr"))
                    if saved:
                        ids.append(saved[0])
                    else:
                        ids.append(None)
                st.session_state.diag_questions = qs
                st.session_state.diag_carte_ids = ids
                st.session_state.diag_index = 0
                st.session_state.diag_resultats = []
                st.session_state.diag_eval_courante = None
                st.rerun()
            except Exception as e:
                st.error(t("etudier.gen_error", e=e))
                return
        return

    i = st.session_state.diag_index
    total = len(st.session_state.diag_questions)

    # Étape 3 : résultats
    if i >= total:
        st.subheader(t("diag.results"))
        already = [r for r in st.session_state.diag_resultats if r["score"] >= 3]
        to_study = [r for r in st.session_state.diag_resultats if r["score"] < 3]

        col1, col2 = st.columns(2)
        col1.metric(t("diag.already_mastered", n=len(already)).split('(')[0].strip(),
                    len(already))
        col2.metric(t("diag.to_study", n=len(to_study)).split('(')[0].strip(),
                    len(to_study))

        if already:
            st.markdown(f"### {t('diag.already_mastered', n=len(already))}")
            for r in already:
                st.markdown(f"🟢 **{r['concept_titre']}** — {r['score']}/4")
                # Crée 1 session « diagnostic » comptant comme 1 vers la maîtrise
                enregistrer_session(r["concept_id"], "diagnostic",
                                     [r["score"]])

        if to_study:
            st.markdown(f"### {t('diag.to_study', n=len(to_study))}")
            for r in to_study:
                st.markdown(f"🔴 **{r['concept_titre']}** — {r['score']}/4")
                # Capture le critère raté pour quiz futur
                enregistrer_points_faibles(r["concept_id"], [{
                    "critere": r.get("critere", ""),
                    "score": r["score"],
                }])

        if st.button(t("diag.continue"),
                     type="primary", use_container_width=True):
            st.session_state.diag_questions = []
            st.session_state.diag_carte_ids = []
            st.session_state.diag_index = 0
            st.session_state.diag_resultats = []
            st.session_state.diag_eval_courante = None
            st.session_state.diag_module = None
            aller_a("modules")
            st.session_state.select_module = m
            st.rerun()
        return

    question = st.session_state.diag_questions[i]
    st.progress(i / total,
                text=t("diag.q_progress", i=i+1, total=total))
    st.markdown(f"**{question.get('concept_titre', '')}**")
    st.caption(t("etudier.q_type",
                 t=question.get("type", "?").replace("_", " ").title()))
    st.markdown(f"### {question['question']}")

    cle_zone = f"diag_rep_{i}"
    if st.session_state.diag_eval_courante is None:
        reponse = st.text_area(
            t("etudier.your_answer"),
            key=cle_zone, height=150,
            placeholder=t("etudier.placeholder"),
        )
        col_a, col_b = st.columns([1, 1])
        if col_a.button(t("etudier.submit"),
                        key=f"diag_submit_{i}",
                        type="primary", use_container_width=True,
                        disabled=not reponse.strip()):
            with st.spinner(t("etudier.evaluating")):
                try:
                    evaluation = evaluer_reponse(question, reponse)
                except Exception as e:
                    st.error(t("etudier.eval_error", e=e))
                    return
            score = int(evaluation.get("score", 0))
            cid = st.session_state.diag_carte_ids[i]
            if cid:
                sauvegarder_revision(
                    carte_id=cid, score=score,
                    feedback=evaluation.get("feedback", ""),
                    duree_sec=0,
                )
            st.session_state.diag_resultats.append({
                "concept_id": question.get("concept_id", ""),
                "concept_titre": question.get("concept_titre", ""),
                "score": score,
                "critere": question.get("critere", ""),
            })
            st.session_state.diag_eval_courante = evaluation
            st.rerun()

        if col_b.button(t("diag.skip_button"),
                        key=f"diag_skip_{i}",
                        use_container_width=True):
            st.session_state.diag_resultats.append({
                "concept_id": question.get("concept_id", ""),
                "concept_titre": question.get("concept_titre", ""),
                "score": 0,
                "critere": question.get("critere", ""),
            })
            st.session_state.diag_index += 1
            st.rerun()
        return

    evaluation = st.session_state.diag_eval_courante
    score = int(evaluation.get("score", 0))
    correct = bool(evaluation.get("correct", False))
    if correct:
        st.success(t("etudier.correct", s=score))
    elif score >= 2:
        st.warning(t("etudier.partial", s=score))
    else:
        st.error(t("etudier.review", s=score))

    if st.button(t("etudier.next"),
                 key=f"diag_next_{i}",
                 type="primary", use_container_width=True):
        st.session_state.diag_index += 1
        st.session_state.diag_eval_courante = None
        st.rerun()


# ══════════════════════════════════════════════════════════════════════════════
# ALPHA SCHOOL #4 — Teach-back
# ══════════════════════════════════════════════════════════════════════════════

def page_teach_back():
    st.markdown(
        hero_html(
            title_main=t("teach.hero.title_main"),
            title_accent=t("teach.hero.title_accent"),
            subtitle=t("teach.hero.subtitle"),
            tag_text=t("teach.hero.tag"),
        ),
        unsafe_allow_html=True,
    )

    # Sélection : seulement les concepts maîtrisés
    progression = get_toute_progression()
    maitrises = sorted(
        [cid for cid, p in progression.items()
         if p.get("statut") == "maitrise" and cid in CURRICULUM],
        key=lambda k: (CURRICULUM[k]["module"], CURRICULUM[k]["ordre"])
    )

    if not maitrises:
        st.info(t("teach.locked"))
        return

    if "teach_concept" not in st.session_state:
        st.session_state.teach_concept = None
    if "teach_resultat" not in st.session_state:
        st.session_state.teach_resultat = None

    cle = st.selectbox(
        t("socratique.concept"),
        options=maitrises,
        format_func=lambda k: (
            f"[{'FR' if CURRICULUM[k].get('langue','fr') == 'fr' else 'EN'}] "
            f"M{CURRICULUM[k]['module']:02d} — {CURRICULUM[k]['titre']}"
        ),
        key="teach_concept_select",
    )
    concept = CURRICULUM[cle]

    st.session_state.teach_concept = cle

    # Meilleur score actuel
    best = get_meilleur_teach_back(cle)
    if best:
        st.caption(t("teach.best", t=best["score_total"]))

    st.markdown(f"### {concept['titre']}")
    st.caption(t("teach.scenario"))

    if st.session_state.teach_resultat is None:
        explication = st.text_area(
            t("teach.input_label"),
            key=f"teach_input_{cle}", height=240,
            placeholder=t("teach.input_placeholder"),
        )
        if st.button(t("teach.submit"),
                     type="primary", use_container_width=True,
                     disabled=not explication.strip()):
            with st.spinner(t("teach.evaluating")):
                try:
                    res = evaluer_teach_back(concept, explication)
                except Exception as e:
                    st.error(t("teach.error", e=e))
                    return
            scores = {
                "clarte": int(res.get("score_clarte", 0)),
                "precision": int(res.get("score_precision", 0)),
                "exemple": int(res.get("score_exemple", 0)),
            }
            feedback = res.get("feedback", "")
            tb_id = enregistrer_teach_back(cle, explication, scores, feedback)
            st.session_state.teach_resultat = {
                **scores,
                "feedback": feedback,
                "tb_id": tb_id,
            }
            st.rerun()
        return

    # Affichage du résultat
    res = st.session_state.teach_resultat
    total = res["clarte"] + res["precision"] + res["exemple"]
    st.markdown(f"### {t('teach.results')}")

    col1, col2, col3 = st.columns(3)
    col1.metric(t("teach.score_clarity"), f"{res['clarte']}/4")
    col2.metric(t("teach.score_precision"), f"{res['precision']}/4")
    col3.metric(t("teach.score_example"), f"{res['exemple']}/4")

    st.progress(total / 12, text=t("teach.score_total", t=total))

    if total >= 9:
        st.success(t("teach.ready"))
    else:
        st.warning(t("teach.not_ready"))

    st.markdown(t("teach.feedback", f=res["feedback"]))

    col_a, col_b = st.columns(2)
    if col_a.button(t("teach.retry"), use_container_width=True):
        st.session_state.teach_resultat = None
        st.rerun()
    if col_b.button(t("etudier.other"),
                    type="primary", use_container_width=True):
        st.session_state.teach_concept = None
        st.session_state.teach_resultat = None
        st.rerun()


# ══════════════════════════════════════════════════════════════════════════════
# ALPHA SCHOOL #5 — Tableau de bord + Objectifs
# ══════════════════════════════════════════════════════════════════════════════

def page_dashboard():
    st.markdown(
        hero_html(
            title_main=t("dash.hero.title_main"),
            title_accent=t("dash.hero.title_accent"),
            subtitle=t("dash.hero.subtitle"),
            tag_text=t("dash.hero.tag"),
        ),
        unsafe_allow_html=True,
    )

    # ── Section objectif ────────────────────────────────────────────────────
    st.markdown(f"### {t('dash.goal_section')}")
    objectifs = get_objectifs_actifs()
    obj = objectifs[0] if objectifs else None

    if obj and obj.get("type") == "module_target":
        m_cible = obj["cible_module"]
        deadline = obj["deadline"]
        nom_m = NOMS_MODULES.get(m_cible, f"M{m_cible:02d}")
        st.markdown(t("dash.goal_active", nom=nom_m, deadline=deadline))

        # Progrès
        progression = get_toute_progression()
        concepts_module = get_concepts_par_module(m_cible)
        nb_total = len(concepts_module)
        nb_mait = sum(
            1 for k in concepts_module
            if progression.get(k, {}).get("statut") == "maitrise"
        )
        st.progress(nb_mait / max(1, nb_total),
                    text=t("dash.goal_progress", m=nb_mait, n=nb_total))

        # Projection
        velo = calculer_velocite(jours=7)
        cps = velo["concepts_par_semaine"]
        if cps > 0:
            from datetime import datetime as _dt, timedelta as _td
            restants = nb_total - nb_mait
            if restants > 0:
                semaines = restants / cps
                expected = _dt.now() + _td(weeks=semaines)
                expected_iso = expected.strftime("%Y-%m-%d")
                st.caption(t("dash.goal_projection",
                              c=cps, date=expected_iso))
                # Comparaison à la deadline
                try:
                    dl = _dt.strptime(deadline, "%Y-%m-%d")
                    delta_j = (expected - dl).days
                    if delta_j <= 0:
                        st.success(t("dash.goal_on_track"))
                    else:
                        st.warning(t("dash.goal_late", d=delta_j))
                except Exception:
                    pass
        else:
            st.caption(t("dash.goal_no_velocity"))

        if st.button(t("dash.goal_clear"),
                     use_container_width=False):
            from db import conn as _conn
            with _conn() as c:
                c.execute(
                    "UPDATE objectifs SET statut = 'abandonne' "
                    "WHERE id = ?", (obj["id"],)
                )
            st.rerun()

    else:
        st.info(t("dash.no_goal"))
        with st.expander(t("dash.goal_create"), expanded=True):
            modules_choix = [m for m in ORDRE_AFFICHAGE_MODULES if m != 99]
            m_cible = st.selectbox(
                t("dash.goal_target_module"),
                options=modules_choix,
                format_func=nom_module_avec_drapeau,
                key="goal_module_select",
            )
            from datetime import date as _date, timedelta as _td2
            deadline = st.date_input(
                t("dash.goal_deadline"),
                value=_date.today() + _td2(days=30),
                min_value=_date.today(),
                key="goal_deadline_input",
            )
            if st.button(t("dash.goal_save"),
                         type="primary", use_container_width=True):
                sauvegarder_objectif(
                    "module_target",
                    cible_module=m_cible,
                    deadline=deadline.isoformat(),
                )
                st.success(t("dash.goal_saved"))
                st.rerun()

    # ── Vélocité 7 jours ────────────────────────────────────────────────────
    st.markdown("---")
    st.markdown(f"### {t('dash.velocity')}")
    velo = calculer_velocite(jours=7)
    cv1, cv2, cv3, cv4 = st.columns(4)
    cv1.metric(t("dash.metric.sessions"), velo["sessions_periode"])
    cv2.metric(t("dash.metric.minutes"), velo["minutes_periode"])
    cv3.metric(t("dash.metric.mastered"), velo["concepts_maitrises_periode"])
    cv4.metric(t("dash.metric.per_week"),
                f"{velo['concepts_par_semaine']:.1f}")

    # ── Heatmap 90 jours ───────────────────────────────────────────────────
    st.markdown("---")
    st.markdown(f"### {t('dash.heatmap')}")
    revs_par_jour = get_revisions_par_jour(jours=90)
    if revs_par_jour:
        from datetime import date as _d, timedelta as _td3
        # Construit un dict complet pour les 90 jours
        today = _d.today()
        debut = today - _td3(days=89)
        rows_chart = []
        cur = debut
        while cur <= today:
            iso = cur.isoformat()
            rows_chart.append({
                "date": cur.isoformat(),
                "weekday": cur.weekday(),
                "week": (cur - debut).days // 7,
                "n": revs_par_jour.get(iso, 0),
            })
            cur = cur + _td3(days=1)
        try:
            import altair as alt
            import pandas as pd
            df = pd.DataFrame(rows_chart)
            chart = alt.Chart(df).mark_rect().encode(
                x=alt.X("week:O", title=None,
                        axis=alt.Axis(labels=False, ticks=False)),
                y=alt.Y("weekday:O", title=None,
                        sort=[0, 1, 2, 3, 4, 5, 6]),
                color=alt.Color("n:Q",
                                 scale=alt.Scale(scheme="goldgreen"),
                                 legend=None),
                tooltip=["date", "n"],
            ).properties(height=180)
            st.altair_chart(chart, use_container_width=True)
        except Exception:
            # Fallback sans altair : grille texte simple
            for r in rows_chart[-21:]:
                st.write(f"`{r['date']}` · {r['n']} révisions")

    # ── Calibration de confiance (Idea #4) ─────────────────────────────────
    st.markdown("---")
    st.markdown(f"### {t('calib.summary_title')}")
    calib = calibration_resume()
    if calib["n"] < 5:
        st.info(t("calib.no_data"))
    else:
        st.markdown(t("calib.summary",
                      n=calib["n"],
                      e=calib["ecart_moyen"],
                      s=calib["surconfiance_pct"]))
        if calib["ecart_moyen"] > 0.5:
            st.warning(t("calib.tip_over"))
        elif calib["ecart_moyen"] < -0.5:
            st.info(t("calib.tip_under"))
        else:
            st.success(t("calib.tip_balanced"))

    # ── Concepts à risque ──────────────────────────────────────────────────
    st.markdown("---")
    st.markdown(f"### {t('dash.at_risk')}")
    risques = get_concepts_a_risque(seuil_stab=1.0, limit=10)
    if risques:
        for r in risques:
            cle = r["concept_id"]
            c = CURRICULUM.get(cle)
            if not c:
                continue
            with st.container(border=True):
                tag = "FR" if c.get("langue", "fr") == "fr" else "EN"
                st.markdown(f"`[{tag}]` **{c['titre']}** — "
                              f"stabilité {r['s_moy']:.2f} j")
                if st.button(t("home.due.review_one"),
                             key=f"risk_{cle}",
                             use_container_width=True):
                    aller_a("etudier", concept_actuel=cle)
                    reset_quiz()
                    st.session_state.session_chargee_de_db = False
                    st.rerun()
    else:
        st.info(t("dash.no_risk"))


# ══════════════════════════════════════════════════════════════════════════════
# IDEA #1 — Mission Mode (scénarios clients multi-concepts)
# ══════════════════════════════════════════════════════════════════════════════

def page_mission():
    st.markdown(
        hero_html(
            title_main=t("mission.hero.title_main"),
            title_accent=t("mission.hero.title_accent"),
            subtitle=t("mission.hero.subtitle"),
            tag_text=t("mission.hero.tag"),
        ),
        unsafe_allow_html=True,
    )

    if "mission_id" not in st.session_state:
        st.session_state.mission_id = None
    if "mission_scenario" not in st.session_state:
        st.session_state.mission_scenario = None
    if "mission_concept_ids" not in st.session_state:
        st.session_state.mission_concept_ids = []
    if "mission_resultat" not in st.session_state:
        st.session_state.mission_resultat = None

    progression = get_toute_progression()
    eligibles = sorted(
        [cid for cid, p in progression.items()
         if p.get("statut") in ("en_cours", "maitrise")
         and cid in CURRICULUM],
        key=lambda k: (CURRICULUM[k]["module"], CURRICULUM[k]["ordre"])
    )

    if not eligibles:
        st.info(t("modules.no_match"))
        return

    # Étape 1 : pas encore de scénario
    if not st.session_state.mission_scenario:
        choix = st.multiselect(
            t("mission.choose_concepts"),
            options=eligibles,
            format_func=lambda k: (
                f"[{ 'FR' if CURRICULUM[k].get('langue', 'fr') == 'fr' else 'EN' }] "
                f"M{CURRICULUM[k]['module']:02d} — {CURRICULUM[k]['titre']}"
            ),
            max_selections=7,
            key="mission_select",
        )
        if len(choix) < 3 or len(choix) > 7:
            st.warning(t("mission.need_more"))
            return
        if st.button(t("mission.generate"),
                     type="primary", use_container_width=True):
            concepts_dicts = [CURRICULUM[k] for k in choix]
            with st.spinner(t("mission.generating")):
                try:
                    scenario = generer_mission(concepts_dicts)
                    mid = sauvegarder_mission(scenario, choix)
                    st.session_state.mission_id = mid
                    st.session_state.mission_scenario = scenario
                    st.session_state.mission_concept_ids = choix
                    st.session_state.mission_resultat = None
                    st.rerun()
                except Exception as e:
                    st.error(t("etudier.gen_error", e=e))
        return

    # Étape 2 : scénario affiché, réponse à fournir
    st.markdown(f"### {t('mission.scenario_label')}")
    with st.container(border=True):
        st.markdown(st.session_state.mission_scenario)

    if st.session_state.mission_resultat is None:
        reponse = st.text_area(
            t("mission.your_response"),
            key="mission_input",
            height=320,
            placeholder=t("mission.placeholder"),
        )
        if st.button(t("mission.submit"),
                     type="primary", use_container_width=True,
                     disabled=not reponse.strip()):
            with st.spinner(t("mission.evaluating")):
                try:
                    concepts_dicts = [
                        CURRICULUM[k] for k in
                        st.session_state.mission_concept_ids
                        if k in CURRICULUM
                    ]
                    eval_result = evaluer_mission(
                        st.session_state.mission_scenario,
                        reponse,
                        concepts_dicts,
                    )
                except Exception as e:
                    st.error(t("etudier.eval_error", e=e))
                    return
            scores = {
                "exhaustivite": int(eval_result.get("exhaustivite", 0)),
                "priorisation": int(eval_result.get("priorisation", 0)),
                "livrabilite": int(eval_result.get("livrabilite", 0)),
            }
            total = sum(scores.values())
            feedback = eval_result.get("feedback", "")
            cloturer_mission(
                st.session_state.mission_id,
                reponse, total, feedback, scores
            )
            st.session_state.mission_resultat = {
                **scores,
                "total": total,
                "feedback": feedback,
                "reponse": reponse,
            }
            st.rerun()
        return

    # Étape 3 : résultats
    res = st.session_state.mission_resultat
    st.markdown("---")
    st.markdown(f"### {t('mission.results')}")

    col1, col2, col3 = st.columns(3)
    col1.metric(t("mission.score_exhaustivity"), f"{res['exhaustivite']}/4")
    col2.metric(t("mission.score_prioritization"), f"{res['priorisation']}/4")
    col3.metric(t("mission.score_deliverability"), f"{res['livrabilite']}/4")

    st.progress(res["total"] / 12,
                text=t("mission.score_total", t=res["total"]))
    st.markdown(t("mission.feedback", f=res["feedback"]))

    if st.button(t("mission.new"),
                 type="primary", use_container_width=True):
        st.session_state.mission_id = None
        st.session_state.mission_scenario = None
        st.session_state.mission_concept_ids = []
        st.session_state.mission_resultat = None
        st.rerun()

    # Historique
    historique = get_missions_recentes(limit=5)
    if historique:
        st.markdown("---")
        st.markdown(f"### {t('mission.history')}")
        for m in historique:
            with st.expander(f"#{m['id']} · {m['cree_le'][:10]} · {m.get('score_total', '?')}/12"):
                st.markdown("**Scénario**")
                st.markdown(m["scenario"][:600] + ("…" if len(m["scenario"]) > 600 else ""))
                if m.get("feedback"):
                    st.markdown(f"**Feedback** — {m['feedback']}")


# ══════════════════════════════════════════════════════════════════════════════
# IDEA #7 — Constellation des concepts
# ══════════════════════════════════════════════════════════════════════════════

def page_constellation():
    st.markdown(
        hero_html(
            title_main=t("const.hero.title_main"),
            title_accent=t("const.hero.title_accent"),
            subtitle=t("const.hero.subtitle"),
            tag_text=t("const.hero.tag"),
        ),
        unsafe_allow_html=True,
    )

    progression = get_toute_progression()

    # Construction d'un graphe Graphviz par module (lisibilité)
    try:
        import graphviz
    except ImportError:
        st.error("Le paquet `graphviz` n'est pas installé. Lance : pip install graphviz")
        return

    # Filtre par module pour ne pas afficher 60 nœuds d'un coup
    modules_choix = [m for m in ORDRE_AFFICHAGE_MODULES if m != 99]
    m_sel = st.selectbox(
        t("modules.label"),
        options=[None] + modules_choix,
        format_func=lambda x: (t("modules.filter_all") if x is None
                                else nom_module_avec_drapeau(x)),
        key="const_module",
    )

    st.caption(t("const.legend"))

    g = graphviz.Digraph(graph_attr={
        "rankdir": "LR",
        "bgcolor": "#0a0f1e",
        "color": "#2a4a6b",
        "fontcolor": "#eaf2f8",
        "splines": "spline",
        "pad": "0.3",
        "nodesep": "0.4",
        "ranksep": "0.6",
    })

    concepts_a_afficher = []
    if m_sel is not None:
        concepts_a_afficher = get_concepts_par_module(m_sel)
    else:
        for m in modules_choix:
            concepts_a_afficher.extend(get_concepts_par_module(m))

    for cle in concepts_a_afficher:
        c = CURRICULUM.get(cle)
        if not c:
            continue
        statut = progression.get(cle, {}).get("statut", "nouveau")
        if statut == "maitrise":
            fill, font = "#d4a853", "#0a0f1e"
        elif statut == "en_cours":
            fill, font = "#f0c060", "#0a0f1e"
        else:
            fill, font = "#1a3050", "#c4d5e8"
        # Label : titre court
        label = c["titre"][:35] + ("…" if len(c["titre"]) > 35 else "")
        g.node(cle, label=label,
                shape="box",
                style="rounded,filled",
                fillcolor=fill,
                fontcolor=font,
                fontname="Helvetica",
                fontsize="11")

    # Arêtes : prereqs (seulement pour les concepts visibles)
    set_visibles = set(concepts_a_afficher)
    for cle in concepts_a_afficher:
        c = CURRICULUM.get(cle)
        if not c:
            continue
        for pr in c.get("prereqs", []):
            if pr in set_visibles:
                g.edge(pr, cle, color="#2a4a6b", arrowsize="0.6")

    st.graphviz_chart(g, use_container_width=True)


# ══════════════════════════════════════════════════════════════════════════════
# IDEA #8 — Prévision d'oubli
# ══════════════════════════════════════════════════════════════════════════════

def page_forecast():
    st.markdown(
        hero_html(
            title_main=t("forecast.hero.title_main"),
            title_accent=t("forecast.hero.title_accent"),
            subtitle=t("forecast.hero.subtitle"),
            tag_text=t("forecast.hero.tag"),
        ),
        unsafe_allow_html=True,
    )

    # Cartes en risque AUJOURD'HUI
    en_risque = cartes_en_risque_aujourd(seuil_R=0.7)
    st.markdown(f"### {t('forecast.now_at_risk')}")
    if not en_risque:
        st.success(t("forecast.no_risk_now"))
    else:
        for r in en_risque[:10]:
            cle_cpt = r["concept_id"]
            titre = CURRICULUM.get(cle_cpt, {}).get("titre", cle_cpt)
            with st.container(border=True):
                st.markdown(f"**{titre}** — R = {r['retrievability']:.0%} "
                              f"· stab. {r['stabilite']:.1f} j")
                st.caption(r["enonce"][:120])
                if st.button(t("forecast.review_card"),
                             key=f"forecast_rev_{r['carte_id']}",
                             use_container_width=True):
                    aller_a("etudier", concept_actuel=cle_cpt)
                    reset_quiz()
                    st.session_state.session_chargee_de_db = False
                    st.rerun()

    # Chart 60 jours
    st.markdown("---")
    st.markdown(f"### {t('forecast.chart_title')}")
    forecast = previsions_oubli(jours=60, seuil_R=0.7)
    if forecast and any(v > 0 for v in forecast.values()):
        try:
            import altair as alt
            import pandas as pd
            rows = [{"date": d, "n": n} for d, n in forecast.items()]
            df = pd.DataFrame(rows)
            chart = alt.Chart(df).mark_area(
                color="#d4a853",
                opacity=0.7,
                line={"color": "#f0c060"},
            ).encode(
                x=alt.X("date:T", title=None),
                y=alt.Y("n:Q", title="Cartes à risque"),
                tooltip=["date", "n"],
            ).properties(height=200)
            st.altair_chart(chart, use_container_width=True)
        except Exception:
            for d, n in list(forecast.items())[:30]:
                if n > 0:
                    st.write(f"`{d}` · {n} cartes")
    else:
        st.info(t("forecast.no_risk_now"))


# ══════════════════════════════════════════════════════════════════════════════
# IDEA #3 — Vocal teach-back (mise à jour de la page existante)
# ══════════════════════════════════════════════════════════════════════════════

# Note : je remplace la fonction page_teach_back existante par une version
# qui supporte un toggle texte / vocal.

def page_teach_back():
    st.markdown(
        hero_html(
            title_main=t("teach.hero.title_main"),
            title_accent=t("teach.hero.title_accent"),
            subtitle=t("teach.hero.subtitle"),
            tag_text=t("teach.hero.tag"),
        ),
        unsafe_allow_html=True,
    )

    progression = get_toute_progression()
    maitrises = sorted(
        [cid for cid, p in progression.items()
         if p.get("statut") == "maitrise" and cid in CURRICULUM],
        key=lambda k: (CURRICULUM[k]["module"], CURRICULUM[k]["ordre"])
    )

    if not maitrises:
        st.info(t("teach.locked"))
        return

    if "teach_concept" not in st.session_state:
        st.session_state.teach_concept = None
    if "teach_resultat" not in st.session_state:
        st.session_state.teach_resultat = None
    if "teach_mode" not in st.session_state:
        st.session_state.teach_mode = "text"
    if "teach_transcription" not in st.session_state:
        st.session_state.teach_transcription = ""

    cle = st.selectbox(
        t("socratique.concept"),
        options=maitrises,
        format_func=lambda k: (
            f"[{'FR' if CURRICULUM[k].get('langue','fr') == 'fr' else 'EN'}] "
            f"M{CURRICULUM[k]['module']:02d} — {CURRICULUM[k]['titre']}"
        ),
        key="teach_concept_select",
    )
    concept = CURRICULUM[cle]
    st.session_state.teach_concept = cle

    best = get_meilleur_teach_back(cle)
    if best:
        st.caption(t("teach.best", t=best["score_total"]))

    st.markdown(f"### {concept['titre']}")
    st.caption(t("teach.scenario"))

    if st.session_state.teach_resultat is None:
        # Toggle mode texte / vocal
        col_m1, col_m2 = st.columns(2)
        if col_m1.button(t("teach.use_text"), use_container_width=True,
                          type="primary" if st.session_state.teach_mode == "text" else "secondary"):
            st.session_state.teach_mode = "text"
            st.rerun()
        if col_m2.button(t("teach.use_voice"), use_container_width=True,
                          type="primary" if st.session_state.teach_mode == "voice" else "secondary"):
            st.session_state.teach_mode = "voice"
            st.rerun()

        explication = ""
        if st.session_state.teach_mode == "voice":
            if not os.environ.get("OPENAI_API_KEY"):
                st.warning(t("teach.no_openai"))
            else:
                st.caption(t("teach.audio_label"))
                try:
                    audio_bytes = st.audio_input(t("teach.audio_label"),
                                                   key=f"teach_audio_{cle}")
                except AttributeError:
                    st.error("st.audio_input requires Streamlit ≥ 1.41.")
                    audio_bytes = None
                if audio_bytes is not None:
                    if st.button(t("teach.transcribing").rstrip("…"),
                                 key=f"teach_transcribe_{cle}",
                                 use_container_width=True):
                        with st.spinner(t("teach.transcribing")):
                            try:
                                txt = transcrire_audio_whisper(
                                    audio_bytes.read(),
                                    langue=concept.get("langue", "fr"),
                                )
                                st.session_state.teach_transcription = txt
                            except Exception as e:
                                st.error(f"Whisper: {e}")

                if st.session_state.teach_transcription:
                    st.markdown(f"**{t('teach.transcription_label')}**")
                    explication = st.text_area(
                        t("teach.transcription_label"),
                        value=st.session_state.teach_transcription,
                        key=f"teach_transcribed_text_{cle}",
                        height=200,
                        label_visibility="collapsed",
                    )
        else:
            explication = st.text_area(
                t("teach.input_label"),
                key=f"teach_input_{cle}",
                height=240,
                placeholder=t("teach.input_placeholder"),
            )

        if st.button(t("teach.submit"),
                     type="primary", use_container_width=True,
                     disabled=not (explication or "").strip()):
            with st.spinner(t("teach.evaluating")):
                try:
                    res = evaluer_teach_back(concept, explication)
                except Exception as e:
                    st.error(t("teach.error", e=e))
                    return
            scores = {
                "clarte": int(res.get("score_clarte", 0)),
                "precision": int(res.get("score_precision", 0)),
                "exemple": int(res.get("score_exemple", 0)),
            }
            feedback = res.get("feedback", "")
            tb_id = enregistrer_teach_back(cle, explication, scores, feedback)
            st.session_state.teach_resultat = {
                **scores,
                "feedback": feedback,
                "tb_id": tb_id,
            }
            st.session_state.teach_transcription = ""
            st.rerun()
        return

    # Affichage du résultat
    res = st.session_state.teach_resultat
    total = res["clarte"] + res["precision"] + res["exemple"]
    st.markdown(f"### {t('teach.results')}")

    col1, col2, col3 = st.columns(3)
    col1.metric(t("teach.score_clarity"), f"{res['clarte']}/4")
    col2.metric(t("teach.score_precision"), f"{res['precision']}/4")
    col3.metric(t("teach.score_example"), f"{res['exemple']}/4")

    st.progress(total / 12, text=t("teach.score_total", t=total))

    if total >= 9:
        st.success(t("teach.ready"))
    else:
        st.warning(t("teach.not_ready"))

    st.markdown(t("teach.feedback", f=res["feedback"]))

    col_a, col_b = st.columns(2)
    if col_a.button(t("teach.retry"), use_container_width=True):
        st.session_state.teach_resultat = None
        st.rerun()
    if col_b.button(t("etudier.other"),
                    type="primary", use_container_width=True):
        st.session_state.teach_concept = None
        st.session_state.teach_resultat = None
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
    "sprint": page_sprint,
    "diagnostic": page_diagnostic,
    "teach_back": page_teach_back,
    "dashboard": page_dashboard,
    "mission": page_mission,
    "constellation": page_constellation,
    "forecast": page_forecast,
}

PAGES.get(st.session_state.page, page_accueil)()

st.markdown(footer_html(), unsafe_allow_html=True)
