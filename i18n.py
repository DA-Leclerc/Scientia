"""
i18n — système de traduction FR/EN pour Scientia.

Toggle dans la sidebar (composant st.session_state.ui_lang).
Default : français.

Usage :
    from i18n import t
    st.title(t("home.hero.title_main"))

Clés organisées par hiérarchie :
    nav.*, home.*, modules.*, etudier.*, socratique.*, progression.*,
    documents.*, revision.*, sidebar.*, common.*
"""
from __future__ import annotations

TRANSLATIONS: dict[str, dict[str, str]] = {

    # ── Navigation sidebar ────────────────────────────────────────────────
    "sidebar.home":              {"fr": "🏠 Accueil",                "en": "🏠 Home"},
    "sidebar.modules":           {"fr": "📚 Modules",                "en": "📚 Modules"},
    "sidebar.quick_review":      {"fr": "🔁 Révision rapide",        "en": "🔁 Quick review"},
    "sidebar.socratic":          {"fr": "🗣️ Dialogue socratique",    "en": "🗣️ Socratic dialogue"},
    "sidebar.progress":          {"fr": "📈 Ma progression",         "en": "📈 My progress"},
    "sidebar.documents":         {"fr": "📥 Documents personnels",   "en": "📥 Personal documents"},
    "sidebar.due":               {"fr": "Dues",                      "en": "Due"},
    "sidebar.uptodate":          {"fr": "À jour",                    "en": "Up to date"},
    "sidebar.streak":            {"fr": "Streak",                    "en": "Streak"},
    "sidebar.concepts_total":    {"fr": "{n} concepts · {m} modules", "en": "{n} concepts · {m} modules"},
    "sidebar.lang_label":        {"fr": "Langue de l'interface",     "en": "Interface language"},

    # ── Hero accueil ──────────────────────────────────────────────────────
    "home.hero.title_main":      {"fr": "Une discipline militaire.", "en": "Military-grade discipline."},
    "home.hero.title_accent":    {"fr": "Une gouvernance d'IA qui marche.", "en": "AI governance that works."},
    "home.hero.subtitle":        {
        "fr": "Apprentissage espacé pour la pratique de gouvernance d'IA. "
              "Quiz adaptatifs, évaluation par Claude, planification FSRS-4.5. "
              "13 modules · 59 concepts · français et anglais.",
        "en": "Spaced-repetition training for AI governance practice. "
              "Adaptive quizzes, Claude-evaluated answers, FSRS-4.5 scheduling. "
              "13 modules · 59 concepts · French and English."},
    "home.hero.tag":             {"fr": "Scientia · Nord Paradigm",  "en": "Scientia · Nord Paradigm"},

    # ── Métriques accueil ─────────────────────────────────────────────────
    "home.metric.studied":       {"fr": "Étudiés",                   "en": "Studied"},
    "home.metric.mastered":      {"fr": "Maîtrisés",                 "en": "Mastered"},
    "home.metric.due":           {"fr": "À réviser",                 "en": "To review"},
    "home.metric.streak":        {"fr": "🔥 Streak",                 "en": "🔥 Streak"},

    # ── Bandeau reprise ───────────────────────────────────────────────────
    "home.resume.label":         {"fr": "▶ Reprendre où tu étais",  "en": "▶ Resume where you were"},
    "home.resume.button":        {"fr": "▶️ Reprendre",              "en": "▶️ Resume"},
    "home.resume.abandon":       {"fr": "✕ Abandonner",              "en": "✕ Abandon"},
    "home.resume.question_meta": {"fr": "Question {i}/{total}",      "en": "Question {i}/{total}"},
    "home.resume.socratic_meta": {"fr": "Dialogue socratique",        "en": "Socratic dialogue"},

    # ── Reco ──────────────────────────────────────────────────────────────
    "home.reco.label":           {"fr": "💡 Recommandé pour toi",   "en": "💡 Recommended for you"},
    "home.reco.button":          {"fr": "Étudier ce concept →",     "en": "Study this concept →"},
    "home.reco.reason_in_progress": {
        "fr": "Concept que tu as déjà commencé sans encore maîtriser.",
        "en": "Concept you've started but not yet mastered."},
    "home.reco.reason_first":    {
        "fr": "Premier concept non étudié du module M{m:02d}.",
        "en": "First unstudied concept of module M{m:02d}."},

    # ── Cartes dues + démarrage ───────────────────────────────────────────
    "home.due.title":            {"fr": "🔁 Révisions dues",         "en": "🔁 Reviews due"},
    "home.due.caption":          {"fr": "Cartes dont la prochaine révision est aujourd'hui ou passée.",
                                  "en": "Cards whose next review is today or overdue."},
    "home.due.start_review":     {"fr": "⚡ Lancer une session de révision rapide",
                                  "en": "⚡ Start a quick review session"},
    "home.due.review_one":       {"fr": "Réviser →",                 "en": "Review →"},
    "home.due.more":             {"fr": "+ {n} autres cartes dues",  "en": "+ {n} more cards due"},
    "home.start_quick":          {"fr": "Démarrer rapidement",       "en": "Quick start"},
    "home.start_choose":         {"fr": "📚 Choisir un concept à étudier",
                                  "en": "📚 Choose a concept to study"},
    "home.planning":             {"fr": "📆 Planning des 14 prochains jours",
                                  "en": "📆 Schedule for the next 14 days"},

    # ── Page Modules ──────────────────────────────────────────────────────
    "modules.hero.title_main":   {"fr": "Choisis un module,",         "en": "Pick a module,"},
    "modules.hero.title_accent": {"fr": "apprends à ton rythme.",     "en": "learn at your pace."},
    "modules.hero.subtitle":     {
        "fr": "13 modules de gouvernance d'IA · 59 concepts · français + anglais. "
              "Filtre par langue, étudie au fil des prérequis, "
              "ou laisse FSRS planifier tes révisions.",
        "en": "13 AI governance modules · 59 concepts · French + English. "
              "Filter by language, study following prerequisites, "
              "or let FSRS schedule your reviews."},
    "modules.hero.tag":          {"fr": "Curriculum · 13 modules",    "en": "Curriculum · 13 modules"},
    "modules.filter_all":        {"fr": "🌐 Tous",                    "en": "🌐 All"},
    "modules.filter_fr":         {"fr": "FR · Français",              "en": "FR · French"},
    "modules.filter_en":         {"fr": "EN · English",               "en": "EN · English"},
    "modules.no_match":          {"fr": "Aucun module ne correspond à ce filtre.",
                                  "en": "No module matches this filter."},
    "modules.label":             {"fr": "Module",                     "en": "Module"},
    "modules.concepts_count":    {"fr": "{n} concepts dans ce module", "en": "{n} concepts in this module"},
    "modules.study":             {"fr": "Étudier",                    "en": "Study"},

    # ── Page Étudier ──────────────────────────────────────────────────────
    "etudier.no_concept":        {"fr": "Aucun concept sélectionné.", "en": "No concept selected."},
    "etudier.back":              {"fr": "← Retour aux modules",       "en": "← Back to modules"},
    "etudier.source":            {"fr": "📖 Texte source",             "en": "📖 Source text"},
    "etudier.source_open":       {"fr": "📖 Texte source (livre ouvert)",
                                  "en": "📖 Source text (open book)"},
    "etudier.q_count":           {"fr": "Nombre de questions",        "en": "Number of questions"},
    "etudier.cards_saved":       {"fr": "Questions sauvegardées",     "en": "Saved questions"},
    "etudier.start_quiz":        {"fr": "▶️  Démarrer le quiz",       "en": "▶️  Start the quiz"},
    "etudier.regenerate":        {"fr": "🔄 Régénérer {n} questions", "en": "🔄 Regenerate {n} questions"},
    "etudier.generate":          {"fr": "✨ Générer {n} questions avec Claude",
                                  "en": "✨ Generate {n} questions with Claude"},
    "etudier.generating":        {"fr": "Génération en cours…",       "en": "Generating…"},
    "etudier.gen_error":         {"fr": "Erreur de génération : {e}", "en": "Generation error: {e}"},
    "etudier.reset.label":       {"fr": "⚠️ Réinitialiser la progression de ce concept",
                                  "en": "⚠️ Reset progress for this concept"},
    "etudier.reset.help":        {
        "fr": "Supprime les cartes sauvegardées, les révisions et la progression FSRS pour ce concept. Action irréversible.",
        "en": "Deletes saved cards, revisions, and FSRS progress for this concept. Cannot be undone."},
    "etudier.reset.button":      {"fr": "🗑 Reset complet",            "en": "🗑 Full reset"},
    "etudier.reset.done":        {"fr": "Progression réinitialisée.", "en": "Progress reset."},
    "etudier.notes":             {"fr": "📝 Mes notes sur ce concept", "en": "📝 My notes on this concept"},
    "etudier.notes_label":       {"fr": "Notes",                      "en": "Notes"},
    "etudier.notes_save":        {"fr": "💾 Sauvegarder la note",     "en": "💾 Save note"},
    "etudier.notes_saved":       {"fr": "Note sauvegardée.",          "en": "Note saved."},
    "etudier.session_done":      {"fr": "🎯 Session terminée",         "en": "🎯 Session complete"},
    "etudier.questions":         {"fr": "Questions",                  "en": "Questions"},
    "etudier.avg_score":         {"fr": "Score moyen",                "en": "Average score"},
    "etudier.mastery":           {"fr": "Maîtrise",                   "en": "Mastery"},
    "etudier.score_text":        {"fr": "Score : {s:.1f}/4",          "en": "Score: {s:.1f}/4"},
    "etudier.excellent":         {"fr": "🎉 Excellent — concept solidement maîtrisé.",
                                  "en": "🎉 Excellent — concept solidly mastered."},
    "etudier.good":              {"fr": "📚 Bon travail. Revois les points faibles.",
                                  "en": "📚 Good work. Review the weak points."},
    "etudier.redo":              {"fr": "🔁 Concept à retravailler. Relis le texte source.",
                                  "en": "🔁 Concept to revisit. Re-read the source text."},
    "etudier.retake":            {"fr": "🔁 Refaire un quiz",         "en": "🔁 Retake quiz"},
    "etudier.other":             {"fr": "📚 Autre concept",            "en": "📚 Other concept"},
    "etudier.progress":          {"fr": "Question {i} / {total}",     "en": "Question {i} / {total}"},
    "etudier.resume_at":         {"fr": "📖 Reprise — tu en étais à la question {n}.",
                                  "en": "📖 Resumed — you were on question {n}."},
    "etudier.q_type":            {"fr": "Type : {t}",                 "en": "Type: {t}"},
    "etudier.hint_show":         {"fr": "💡 Voir un indice",          "en": "💡 Show a hint"},
    "etudier.your_answer":       {"fr": "Ta réponse",                 "en": "Your answer"},
    "etudier.placeholder":       {"fr": "Réponds librement…",         "en": "Answer freely…"},
    "etudier.tutor_open":        {"fr": "🎓 Discuter avec Claude pour mieux comprendre la question",
                                  "en": "🎓 Chat with Claude to better understand the question"},
    "etudier.tutor_caption":     {
        "fr": "🎓 Mini-tuteur socratique — Claude ne donnera JAMAIS la réponse, il t'aide à comprendre la question.",
        "en": "🎓 Socratic mini-tutor — Claude will NEVER give you the answer, only help you understand the question."},
    "etudier.tutor_thinking":    {"fr": "Claude réfléchit…",          "en": "Claude is thinking…"},
    "etudier.tutor_opening":     {"fr": "Claude prépare une ouverture…", "en": "Claude is preparing an opening…"},
    "etudier.tutor_input":       {"fr": "Pose une question, partage ton intuition…",
                                  "en": "Ask a question, share your intuition…"},
    "etudier.tutor_close":       {"fr": "Fermer le tuteur",            "en": "Close tutor"},
    "etudier.tutor_error":       {"fr": "Erreur Socratique : {e}",    "en": "Socratic error: {e}"},
    "etudier.submit":            {"fr": "✓ Soumettre",                 "en": "✓ Submit"},
    "etudier.skip":              {"fr": "Passer",                     "en": "Skip"},
    "etudier.evaluating":        {"fr": "Évaluation par Claude…",     "en": "Claude is evaluating…"},
    "etudier.eval_error":        {"fr": "Erreur d'évaluation : {e}",  "en": "Evaluation error: {e}"},
    "etudier.correct":           {"fr": "✓ Correct ({s}/4)",          "en": "✓ Correct ({s}/4)"},
    "etudier.partial":           {"fr": "Partiel ({s}/4)",            "en": "Partial ({s}/4)"},
    "etudier.review":            {"fr": "À revoir ({s}/4)",            "en": "To review ({s}/4)"},
    "etudier.feedback":          {"fr": "**Feedback** — {f}",         "en": "**Feedback** — {f}"},
    "etudier.see_ref":           {"fr": "📖 Voir la réponse de référence",
                                  "en": "📖 See reference answer"},
    "etudier.next":              {"fr": "Question suivante →",         "en": "Next question →"},

    # ── Page Socratique ──────────────────────────────────────────────────
    "socratique.title":          {"fr": "🗣️ Dialogue socratique",     "en": "🗣️ Socratic dialogue"},
    "socratique.caption":        {
        "fr": "Mode tuteur : Claude te guide par questions plutôt que de te tester. "
              "Le dialogue n'est pas noté pendant l'échange — un bilan apparaît à la fin.",
        "en": "Tutor mode: Claude guides you with questions rather than testing you. "
              "The dialogue isn't graded during the exchange — a debrief appears at the end."},
    "socratique.choose":         {"fr": "Choisis un concept à explorer", "en": "Pick a concept to explore"},
    "socratique.lang":           {"fr": "Langue",                     "en": "Language"},
    "socratique.module":         {"fr": "Module",                     "en": "Module"},
    "socratique.concept":        {"fr": "Concept",                    "en": "Concept"},
    "socratique.has_active":     {"fr": "📖 Tu as un dialogue en cours sur ce concept ({n} échanges).",
                                  "en": "📖 You have a dialogue in progress on this concept ({n} exchanges)."},
    "socratique.resume":         {"fr": "▶️ Reprendre le dialogue",   "en": "▶️ Resume dialogue"},
    "socratique.new":            {"fr": "🆕 Nouveau dialogue",         "en": "🆕 New dialogue"},
    "socratique.start":          {"fr": "▶️ Démarrer le dialogue",    "en": "▶️ Start dialogue"},
    "socratique.preparing":      {"fr": "Claude prépare une question d'ouverture…",
                                  "en": "Claude is preparing an opening question…"},
    "socratique.error":          {"fr": "Erreur : {e}",               "en": "Error: {e}"},
    "socratique.concept_label":  {"fr": "**Concept : `[{tag}]` {titre}**",
                                  "en": "**Concept: `[{tag}]` {titre}**"},
    "socratique.new_concept":    {"fr": "🔄 Nouveau concept",          "en": "🔄 New concept"},
    "socratique.finish":         {"fr": "✓ Terminer et obtenir un bilan",
                                  "en": "✓ Finish and get a debrief"},
    "socratique.summary":        {"fr": "Claude rédige ton bilan…",   "en": "Claude is drafting your debrief…"},
    "socratique.bilan":          {"fr": "📋 Bilan du dialogue",        "en": "📋 Dialogue debrief"},
    "socratique.score_good":     {"fr": "Score : {s}/4 — bonne maîtrise",
                                  "en": "Score: {s}/4 — good mastery"},
    "socratique.score_partial":  {"fr": "Score : {s}/4 — partielle",   "en": "Score: {s}/4 — partial"},
    "socratique.score_redo":     {"fr": "Score : {s}/4 — à retravailler",
                                  "en": "Score: {s}/4 — to revisit"},
    "socratique.strengths":      {"fr": "**Points forts** — {x}",     "en": "**Strengths** — {x}"},
    "socratique.deepen":         {"fr": "**À approfondir** — {x}",    "en": "**To deepen** — {x}"},
    "socratique.synthesis":      {"fr": "📖 Synthèse du concept",     "en": "📖 Concept synthesis"},
    "socratique.relaunch":       {"fr": "🔁 Relancer un dialogue sur ce concept",
                                  "en": "🔁 Restart a dialogue on this concept"},
    "socratique.input":          {"fr": "Ta réponse à Claude…",       "en": "Your reply to Claude…"},

    # ── Page Progression ──────────────────────────────────────────────────
    "progress.hero.title_main":  {"fr": "Ta progression,",             "en": "Your progress,"},
    "progress.hero.title_accent": {"fr": "mois après mois.",            "en": "month after month."},
    "progress.hero.subtitle":    {
        "fr": "Tu as étudié {n} concepts, maîtrisé {m}, et tiens un streak de {s} jour{p}. "
              "Exporte ta progression en CSV pour archive personnelle.",
        "en": "You've studied {n} concepts, mastered {m}, and hold a streak of {s} day{p}. "
              "Export your progress to CSV for personal archive."},
    "progress.empty":            {"fr": "Aucune session enregistrée pour l'instant. Lance un quiz pour démarrer ta progression.",
                                  "en": "No sessions recorded yet. Launch a quiz to start your progress."},
    "progress.metric.curriculum": {"fr": "Concepts du curriculum",     "en": "Curriculum concepts"},
    "progress.global":           {"fr": "Maîtrise globale : {m}/{t}",  "en": "Overall mastery: {m}/{t}"},
    "progress.export":           {"fr": "📥 Exporter ma progression (CSV)",
                                  "en": "📥 Export my progress (CSV)"},
    "progress.detail":           {"fr": "Détail par concept",          "en": "Detail by concept"},
    "progress.session_count":    {"fr": "sur {n} session(s)",          "en": "across {n} session(s)"},

    # ── Page Documents ────────────────────────────────────────────────────
    "documents.title":           {"fr": "📥 Documents personnels",     "en": "📥 Personal documents"},
    "documents.caption":         {
        "fr": "Charge un PDF, MD ou TXT. Claude extrait 1 à 5 concepts qui rejoignent le bucket d'ingestion (M99).",
        "en": "Upload a PDF, MD or TXT. Claude extracts 1-5 concepts into the ingestion bucket (M99)."},
    "documents.choose":          {"fr": "Choisis un fichier",          "en": "Choose a file"},
    "documents.extract":         {"fr": "✨ Extraire les concepts",    "en": "✨ Extract concepts"},
    "documents.extracting":      {"fr": "Lecture et extraction par Claude…",
                                  "en": "Reading and extracting via Claude…"},
    "documents.added":           {"fr": "✓ {n} concept(s) ajouté(s) au module 99 (Documents ingérés). Va dans Modules pour les étudier.",
                                  "en": "✓ {n} concept(s) added to module 99 (Ingested documents). Go to Modules to study them."},
    "documents.ingested":        {"fr": "Concepts ingérés ({n})",      "en": "Ingested concepts ({n})"},
    "documents.source_meta":     {"fr": "Source : {s} · {d}",          "en": "Source: {s} · {d}"},
    "documents.study":           {"fr": "Étudier →",                   "en": "Study →"},
    "documents.empty":           {"fr": "Aucun document ingéré pour l'instant.",
                                  "en": "No documents ingested yet."},
    "documents.error":           {"fr": "Erreur : {e}",                "en": "Error: {e}"},

    # ── Page Révision rapide ──────────────────────────────────────────────
    "revision.title":            {"fr": "🔁 Révision rapide",           "en": "🔁 Quick review"},
    "revision.caption":          {"fr": "Cartes dues triées du plus en retard au plus récent, tous concepts confondus.",
                                  "en": "Due cards sorted from most overdue to most recent, all concepts."},
    "revision.back":             {"fr": "← Accueil",                   "en": "← Home"},
    "revision.empty":            {"fr": "✓ Aucune carte due. Tu es à jour.",
                                  "en": "✓ No cards due. You're up to date."},
    "revision.metric":           {"fr": "Cartes à réviser",            "en": "Cards to review"},
    "revision.concept_due":      {"fr": "{n} carte(s)",                "en": "{n} card(s)"},
    "revision.review_concept":   {"fr": "Réviser ce concept →",        "en": "Review this concept →"},

    # ── Footer ────────────────────────────────────────────────────────────
    "footer.tagline":            {"fr": "Une discipline militaire. Une gouvernance d'IA qui marche.",
                                  "en": "Military-grade discipline. AI governance that works."},

    # ══════════════════════════════════════════════════════════════════════
    # ALPHA SCHOOL features
    # ══════════════════════════════════════════════════════════════════════

    # ── #1 Paliers de maîtrise ────────────────────────────────────────────
    "mastery.progress.title":    {"fr": "🎯 Progrès vers la maîtrise",
                                  "en": "🎯 Progress toward mastery"},
    "mastery.progress.text":     {"fr": "Sessions consécutives à ≥3/4 : {p}/{r}",
                                  "en": "Consecutive sessions at ≥3/4: {p}/{r}"},
    "mastery.gap_hint":          {"fr": "Une 2e session ≥24h après la 1ère est requise pour confirmer la maîtrise.",
                                  "en": "A 2nd session ≥24h after the 1st is required to confirm mastery."},
    "mastery.failed":            {"fr": "📍 Tu as raté {n} question(s) — Claude peut générer des questions ciblées sur tes points faibles.",
                                  "en": "📍 You missed {n} question(s) — Claude can generate questions targeting your weak points."},
    "mastery.targeted_button":   {"fr": "🎯 Quiz ciblé sur mes points faibles",
                                  "en": "🎯 Targeted quiz on my weak points"},
    "mastery.targeted_label":    {"fr": "Mode ciblé · attaque tes points faibles",
                                  "en": "Targeted mode · attacks your weak points"},
    "mastery.unlocked":          {"fr": "🏆 Maîtrise confirmée. Le concept est solidement encodé.",
                                  "en": "🏆 Mastery confirmed. The concept is solidly encoded."},
    "mastery.almost":            {"fr": "Presque ! Refais une session après une nuit pour confirmer la maîtrise.",
                                  "en": "Almost there! Run another session after a night to confirm mastery."},

    # ── #2 Sprint de maîtrise ─────────────────────────────────────────────
    "sidebar.sprint":            {"fr": "⚡ Sprint de maîtrise",       "en": "⚡ Mastery sprint"},
    "sprint.hero.title_main":    {"fr": "Sprint de maîtrise.",         "en": "Mastery sprint."},
    "sprint.hero.title_accent":  {"fr": "L'entrelacement qui transfère.","en": "Interleaving that transfers."},
    "sprint.hero.subtitle":      {
        "fr": "Choisis 3-5 concepts. Le sprint tire 1 question de chacun, en ordre aléatoire, "
              "sans te dire de quel concept ça vient. C'est l'épreuve qui simule le mieux la pratique réelle.",
        "en": "Pick 3-5 concepts. The sprint pulls 1 question from each, in random order, "
              "without telling you which concept. It's the exercise that best mimics real practice."},
    "sprint.hero.tag":           {"fr": "⚡ Mode entrelacé",            "en": "⚡ Interleaved mode"},
    "sprint.choose":             {"fr": "Choisis 3-5 concepts pour le sprint",
                                  "en": "Pick 3-5 concepts for the sprint"},
    "sprint.need_more":          {"fr": "Sélectionne au moins 3 concepts.",
                                  "en": "Pick at least 3 concepts."},
    "sprint.need_cards":         {"fr": "Ces concepts n'ont pas de questions générées. Lance d'abord un quiz normal sur chacun.",
                                  "en": "These concepts have no generated questions. Run a normal quiz on each first."},
    "sprint.start":              {"fr": "⚡ Démarrer le sprint",        "en": "⚡ Start the sprint"},
    "sprint.q_of":               {"fr": "Question {i} / {total}",       "en": "Question {i} / {total}"},
    "sprint.concept_hidden":     {"fr": "Concept masqué — identifie-le par le contexte.",
                                  "en": "Concept hidden — identify it from context."},
    "sprint.results":            {"fr": "📊 Résultats du sprint",       "en": "📊 Sprint results"},
    "sprint.score_per_concept":  {"fr": "Score par concept",             "en": "Score by concept"},
    "sprint.transfer_tip":       {"fr": "Astuce : si tu as bien réussi, tu transfères. Si tu as buté, le concept est isolé — fais un quiz normal pour consolider.",
                                  "en": "Hint: if you scored well, you're transferring. If you stumbled, the concept is isolated — run a normal quiz to consolidate."},
    "sprint.restart":            {"fr": "🔁 Nouveau sprint",            "en": "🔁 New sprint"},

    # ── #3 Diagnostic pré-module ──────────────────────────────────────────
    "diag.button":               {"fr": "🎯 Diagnostic rapide ({n} concepts)",
                                  "en": "🎯 Quick diagnostic ({n} concepts)"},
    "diag.intro":                {"fr": "1 question par concept. Les concepts que tu réussis seront marqués comme déjà acquis. Les autres garderont la trace de ce que tu as raté.",
                                  "en": "1 question per concept. Successful ones are marked as already learned. Failed ones keep track of what you missed."},
    "diag.generating":           {"fr": "Génération du diagnostic…",   "en": "Generating diagnostic…"},
    "diag.q_progress":           {"fr": "Diagnostic · {i} / {total}",   "en": "Diagnostic · {i} / {total}"},
    "diag.skip_button":          {"fr": "❓ Je ne sais pas",            "en": "❓ I don't know"},
    "diag.results":              {"fr": "📊 Résultats du diagnostic",   "en": "📊 Diagnostic results"},
    "diag.already_mastered":     {"fr": "✓ Déjà acquis ({n})",          "en": "✓ Already learned ({n})"},
    "diag.to_study":             {"fr": "📚 À étudier ({n})",            "en": "📚 To study ({n})"},
    "diag.continue":             {"fr": "Continuer vers le module →",   "en": "Continue to module →"},

    # ── #4 Teach-back ─────────────────────────────────────────────────────
    "teach.button":              {"fr": "🎤 Mode Teach-back",            "en": "🎤 Teach-back mode"},
    "teach.locked":              {"fr": "Disponible une fois le concept maîtrisé.",
                                  "en": "Available once the concept is mastered."},
    "teach.hero.title_main":     {"fr": "Si tu peux l'enseigner,",      "en": "If you can teach it,"},
    "teach.hero.title_accent":   {"fr": "tu le maîtrises vraiment.",     "en": "you truly own it."},
    "teach.hero.subtitle":       {
        "fr": "Le client te demande d'expliquer ce concept. Réponds comme tu le ferais dans une rencontre de cadrage. "
              "Claude évalue selon 3 critères : clarté pour un non-initié, précision technique, exemple concret.",
        "en": "The client asks you to explain this concept. Reply as you would in a scoping meeting. "
              "Claude scores on 3 criteria: clarity for a non-expert, technical precision, concrete example."},
    "teach.hero.tag":             {"fr": "🎤 Apprendre en enseignant",   "en": "🎤 Learn by teaching"},
    "teach.scenario":            {"fr": "Scénario : un client moyen ne connaît rien à la gouvernance d'IA. Explique-lui.",
                                  "en": "Scenario: a typical client knows nothing about AI governance. Explain it to them."},
    "teach.input_label":         {"fr": "Ton explication",              "en": "Your explanation"},
    "teach.input_placeholder":   {"fr": "Comme si tu lui parlais en personne…",
                                  "en": "As if speaking to them in person…"},
    "teach.submit":              {"fr": "✓ Soumettre mon explication",  "en": "✓ Submit my explanation"},
    "teach.evaluating":          {"fr": "Claude évalue ton enseignement…",
                                  "en": "Claude is evaluating your teaching…"},
    "teach.error":               {"fr": "Erreur d'évaluation : {e}",    "en": "Evaluation error: {e}"},
    "teach.results":             {"fr": "📋 Évaluation",                 "en": "📋 Assessment"},
    "teach.score_clarity":       {"fr": "Clarté",                        "en": "Clarity"},
    "teach.score_precision":     {"fr": "Précision",                     "en": "Precision"},
    "teach.score_example":       {"fr": "Exemple",                       "en": "Example"},
    "teach.score_total":         {"fr": "Score total : {t}/12",          "en": "Total score: {t}/12"},
    "teach.ready":               {"fr": "✓ Prêt à enseigner — score ≥ 9/12. Tu peux livrer ce concept en mission.",
                                  "en": "✓ Ready to teach — score ≥ 9/12. You can deliver this concept in a mission."},
    "teach.not_ready":           {"fr": "Pas encore. Vise une note ≥ 9/12 pour être prêt à livrer en mission.",
                                  "en": "Not yet. Aim for ≥ 9/12 to be ready to deliver in a mission."},
    "teach.feedback":            {"fr": "**Feedback de Claude** — {f}", "en": "**Claude's feedback** — {f}"},
    "teach.retry":               {"fr": "🔁 Refaire un teach-back",     "en": "🔁 Retry teach-back"},
    "teach.best":                {"fr": "🏆 Meilleur score : {t}/12",   "en": "🏆 Best score: {t}/12"},

    # ── #5 Tableau de bord + objectifs ────────────────────────────────────
    "sidebar.dashboard":         {"fr": "🎯 Mes objectifs",              "en": "🎯 My goals"},
    "dash.hero.title_main":      {"fr": "Pilote ta progression.",         "en": "Pilot your progress."},
    "dash.hero.title_accent":    {"fr": "Avec tes propres données.",      "en": "With your own data."},
    "dash.hero.subtitle":        {
        "fr": "Fixe une cible, suis ta vélocité, identifie les concepts à risque. "
              "Comme à Alpha School, c'est toi qui pilotes — les données t'aident à voir clair.",
        "en": "Set a target, track your velocity, spot at-risk concepts. "
              "Like at Alpha School, you steer — the data helps you see."},
    "dash.hero.tag":             {"fr": "🎯 Tableau de bord personnel",   "en": "🎯 Personal dashboard"},
    "dash.goal_section":         {"fr": "Objectif courant",                "en": "Current goal"},
    "dash.no_goal":              {"fr": "Aucun objectif fixé pour l'instant.",
                                  "en": "No goal set yet."},
    "dash.goal_create":          {"fr": "Définir un objectif",             "en": "Set a goal"},
    "dash.goal_target_module":   {"fr": "Module à maîtriser",              "en": "Module to master"},
    "dash.goal_deadline":        {"fr": "Échéance",                        "en": "Deadline"},
    "dash.goal_save":             {"fr": "💾 Enregistrer l'objectif",     "en": "💾 Save goal"},
    "dash.goal_saved":            {"fr": "Objectif enregistré.",           "en": "Goal saved."},
    "dash.goal_active":           {"fr": "Objectif : maîtriser **{nom}** d'ici **{deadline}**.",
                                  "en": "Goal: master **{nom}** by **{deadline}**."},
    "dash.goal_progress":         {"fr": "Progrès : {m}/{n} concepts maîtrisés du module.",
                                  "en": "Progress: {m}/{n} concepts of the module mastered."},
    "dash.goal_projection":       {"fr": "Au rythme actuel ({c:.1f} concepts/sem), atteinte estimée le **{date}**.",
                                  "en": "At current pace ({c:.1f} concepts/wk), expected completion **{date}**."},
    "dash.goal_on_track":         {"fr": "✓ En avance sur l'échéance.",    "en": "✓ Ahead of schedule."},
    "dash.goal_late":              {"fr": "⚠ {d} jour(s) de retard sur le plan.",
                                  "en": "⚠ {d} day(s) behind schedule."},
    "dash.goal_no_velocity":       {"fr": "Pas assez de données pour projeter — fais quelques sessions.",
                                  "en": "Not enough data to project yet — run a few sessions."},
    "dash.goal_clear":            {"fr": "🗑 Effacer l'objectif",          "en": "🗑 Clear goal"},
    "dash.velocity":               {"fr": "Vélocité (7 derniers jours)",    "en": "Velocity (last 7 days)"},
    "dash.metric.sessions":       {"fr": "Sessions",                       "en": "Sessions"},
    "dash.metric.minutes":         {"fr": "Minutes",                       "en": "Minutes"},
    "dash.metric.mastered":       {"fr": "Concepts maîtrisés",             "en": "Concepts mastered"},
    "dash.metric.per_week":       {"fr": "Concepts/semaine",                "en": "Concepts/week"},
    "dash.heatmap":                {"fr": "Carte de chaleur — 90 derniers jours",
                                  "en": "Heatmap — last 90 days"},
    "dash.at_risk":                {"fr": "Concepts à risque (oubli imminent)",
                                  "en": "At-risk concepts (forgetting soon)"},
    "dash.no_risk":                {"fr": "Aucun concept en zone d'oubli pour l'instant.",
                                  "en": "No concepts in the forgetting zone yet."},

    # ══════════════════════════════════════════════════════════════════════
    # Round 2 — features supplémentaires
    # ══════════════════════════════════════════════════════════════════════

    # ── #2 Cheat sheet ────────────────────────────────────────────────────
    "cheat.button":              {"fr": "📝 Générer une cheat sheet client",
                                  "en": "📝 Generate a client cheat sheet"},
    "cheat.regenerate":          {"fr": "🔁 Regénérer",                 "en": "🔁 Regenerate"},
    "cheat.generating":          {"fr": "Claude rédige le livrable…",   "en": "Claude is drafting the deliverable…"},
    "cheat.title":               {"fr": "Cheat sheet pour usage client", "en": "Client-facing cheat sheet"},
    "cheat.download":            {"fr": "📥 Télécharger en .md",         "en": "📥 Download as .md"},
    "cheat.copy_hint":           {"fr": "Sélectionne le bloc et copie. Tu peux le coller tel quel dans un livrable Brèche Pro.",
                                  "en": "Select the block and copy. You can paste it as-is into a Brèche Pro deliverable."},

    # ── #4 Calibration ───────────────────────────────────────────────────
    "calib.label":               {"fr": "Confiance avant de répondre",   "en": "Confidence before answering"},
    "calib.help":                {"fr": "1 = je devine · 5 = je suis certain. Aide-toi à voir tes biais.",
                                  "en": "1 = I'm guessing · 5 = I'm certain. Helps you see your biases."},
    "calib.summary_title":       {"fr": "🎯 Calibration",                "en": "🎯 Calibration"},
    "calib.no_data":             {"fr": "Pas encore assez de prédictions pour calibrer. Continue.",
                                  "en": "Not enough predictions yet to calibrate. Keep going."},
    "calib.summary":             {"fr": "Sur {n} questions, écart moyen confiance−score : **{e:+.2f}**. Surconfiance : {s:.0f}%.",
                                  "en": "Across {n} questions, average gap confidence−score: **{e:+.2f}**. Over-confidence: {s:.0f}%."},
    "calib.tip_over":            {"fr": "💡 Tu es plus souvent sur-confiant qu'autre chose. En consulting, ça mène aux promesses qui blessent. Vérifie deux fois avant de répondre.",
                                  "en": "💡 You skew over-confident. In consulting, that leads to over-promising. Double-check before answering."},
    "calib.tip_under":            {"fr": "💡 Tu es plus prudent que ton vrai niveau. Tu sais plus que tu ne crois — fais-toi confiance.",
                                  "en": "💡 You're more cautious than your actual level. You know more than you think — trust yourself."},
    "calib.tip_balanced":         {"fr": "💡 Calibration excellente. Ton intuition de niveau est fiable.",
                                  "en": "💡 Excellent calibration. Your level intuition is reliable."},

    # ── #1 Mission Mode ───────────────────────────────────────────────────
    "sidebar.mission":           {"fr": "🎯 Mission Mode",                "en": "🎯 Mission Mode"},
    "mission.hero.title_main":   {"fr": "Un client. Un mandat.",          "en": "A client. A mission."},
    "mission.hero.title_accent": {"fr": "Tu mobilises tout.",              "en": "You mobilize it all."},
    "mission.hero.subtitle":     {
        "fr": "Scénario fictif — TechCorp QC, GroupeSanté Boréal, Logifin Inc. — basé sur les concepts que tu as déjà étudiés. "
              "Tu identifies les obligations, tu priorises, tu proposes Brèche / Brèche Pro / Prisme. C'est ton examen de synthèse.",
        "en": "Fictional scenario — TechCorp QC, GroupeSanté Boréal, Logifin Inc. — based on the concepts you've already studied. "
              "You identify obligations, prioritize, and pitch Brèche / Brèche Pro / Prisme. This is your synthesis exam."},
    "mission.hero.tag":          {"fr": "🎯 Examen de synthèse",          "en": "🎯 Synthesis exam"},
    "mission.choose_concepts":   {"fr": "Choisis 3-7 concepts (déjà étudiés) pour la mission",
                                  "en": "Pick 3-7 (already studied) concepts for the mission"},
    "mission.need_more":          {"fr": "Sélectionne 3-7 concepts.",     "en": "Pick 3-7 concepts."},
    "mission.generate":          {"fr": "🎲 Générer le scénario",         "en": "🎲 Generate scenario"},
    "mission.generating":        {"fr": "Claude écrit le mandat…",        "en": "Claude is drafting the mission…"},
    "mission.scenario_label":    {"fr": "📋 Scénario",                    "en": "📋 Scenario"},
    "mission.your_response":     {"fr": "Ta réponse stratégique",         "en": "Your strategic response"},
    "mission.placeholder":       {"fr": "Identifie les obligations applicables, priorise, et propose un engagement Nord Paradigm. Réponds comme tu le ferais à un client.",
                                  "en": "Identify applicable obligations, prioritize, and propose a Nord Paradigm engagement. Reply as you would to a client."},
    "mission.submit":            {"fr": "✓ Soumettre la réponse",         "en": "✓ Submit response"},
    "mission.evaluating":        {"fr": "Claude évalue ta réponse stratégique…",
                                  "en": "Claude is evaluating your strategic response…"},
    "mission.results":           {"fr": "📊 Évaluation de la mission",    "en": "📊 Mission assessment"},
    "mission.score_exhaustivity": {"fr": "Exhaustivité",                   "en": "Exhaustiveness"},
    "mission.score_prioritization": {"fr": "Priorisation",                 "en": "Prioritization"},
    "mission.score_deliverability": {"fr": "Livrabilité",                  "en": "Deliverability"},
    "mission.score_total":       {"fr": "Score total : {t}/12",            "en": "Total score: {t}/12"},
    "mission.feedback":          {"fr": "**Feedback** — {f}",              "en": "**Feedback** — {f}"},
    "mission.new":               {"fr": "🔁 Nouvelle mission",             "en": "🔁 New mission"},
    "mission.history":           {"fr": "Missions passées",                "en": "Past missions"},

    # ── #7 Constellation ──────────────────────────────────────────────────
    "sidebar.constellation":     {"fr": "✨ Constellation",                 "en": "✨ Constellation"},
    "const.hero.title_main":     {"fr": "Ta carte du savoir,",              "en": "Your map of knowledge,"},
    "const.hero.title_accent":   {"fr": "elle s'illumine.",                  "en": "lighting up over time."},
    "const.hero.subtitle":       {
        "fr": "Chaque étoile = un concept. Les liens = les prérequis. Les étoiles dorées sont maîtrisées. "
              "Au fil des semaines, ta constellation Nord Paradigm prend forme.",
        "en": "Each star = a concept. Links = prerequisites. Golden stars are mastered. "
              "Over the weeks, your Nord Paradigm constellation takes shape."},
    "const.hero.tag":            {"fr": "✨ Vue d'ensemble",                 "en": "✨ Big picture"},
    "const.legend":              {"fr": "🟢 Maîtrisé · 🟡 En cours · ⚪ Pas encore étudié",
                                  "en": "🟢 Mastered · 🟡 In progress · ⚪ Not yet studied"},

    # ── #8 Forgetting forecast ────────────────────────────────────────────
    "sidebar.forecast":          {"fr": "🔮 Prévision d'oubli",            "en": "🔮 Forgetting forecast"},
    "forecast.hero.title_main":  {"fr": "Ce que tu oublieras,",             "en": "What you'll forget,"},
    "forecast.hero.title_accent": {"fr": "avant que ça ne devienne un trou.","en": "before it becomes a gap."},
    "forecast.hero.subtitle":    {
        "fr": "Le modèle FSRS-4.5 projette la probabilité de rappel pour chaque carte sur 60 jours. "
              "Anticipe — bloque du temps maintenant pour les cartes qui rentreront en zone à risque.",
        "en": "The FSRS-4.5 model projects recall probability for each card over 60 days. "
              "Plan ahead — block time now for cards that will enter the risk zone."},
    "forecast.hero.tag":         {"fr": "🔮 Anticipation FSRS",             "en": "🔮 FSRS anticipation"},
    "forecast.chart_title":      {"fr": "Cartes à risque par jour (60 jours)",
                                  "en": "Cards at risk per day (60 days)"},
    "forecast.now_at_risk":      {"fr": "🚨 Cartes déjà en zone à risque",  "en": "🚨 Cards already at risk"},
    "forecast.no_risk_now":       {"fr": "Aucune carte n'est en zone à risque aujourd'hui.",
                                  "en": "No cards are in the risk zone today."},
    "forecast.review_card":      {"fr": "Réviser →",                        "en": "Review →"},

    # ── #10 Obsidian sync ─────────────────────────────────────────────────
    "obs.button":                {"fr": "🔗 Sync vers Obsidian",            "en": "🔗 Sync to Obsidian"},
    "obs.no_vault":              {"fr": "OBSIDIAN_VAULT_PATH non configurée. Ajoute-la dans tes secrets ou .env.",
                                  "en": "OBSIDIAN_VAULT_PATH not configured. Add it to your secrets or .env."},
    "obs.synced":                {"fr": "✓ Synchronisé : {p}",              "en": "✓ Synced: {p}"},
    "obs.error":                 {"fr": "Erreur de sync : {e}",             "en": "Sync error: {e}"},

    # ── #3 Vocal teach-back ───────────────────────────────────────────────
    "teach.audio_label":         {"fr": "Enregistre ton explication (max 2 min).",
                                  "en": "Record your explanation (max 2 min)."},
    "teach.transcribing":        {"fr": "Transcription en cours…",           "en": "Transcribing…"},
    "teach.transcription_label": {"fr": "Transcription :",                   "en": "Transcription:"},
    "teach.no_openai":           {"fr": "Mode vocal indisponible : OPENAI_API_KEY non configurée. Tape ta réponse à la place.",
                                  "en": "Voice mode unavailable: OPENAI_API_KEY not set. Type your answer instead."},
    "teach.use_voice":           {"fr": "🎤 Mode vocal",                    "en": "🎤 Voice mode"},
    "teach.use_text":            {"fr": "⌨️ Mode texte",                    "en": "⌨️ Text mode"},
}


def t(key: str, lang: str | None = None, **kwargs) -> str:
    """
    Retourne la traduction de `key` dans la langue `lang` (par défaut depuis
    st.session_state.ui_lang ou 'fr'). Format avec `kwargs` si fournis.
    """
    if lang is None:
        try:
            import streamlit as st
            lang = st.session_state.get("ui_lang", "fr")
        except Exception:
            lang = "fr"
    entry = TRANSLATIONS.get(key)
    if not entry:
        return key  # fallback : afficher la clé pour repérage
    txt = entry.get(lang) or entry.get("fr") or key
    if kwargs:
        try:
            return txt.format(**kwargs)
        except (KeyError, IndexError):
            return txt
    return txt
