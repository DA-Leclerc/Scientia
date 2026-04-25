from __future__ import annotations

"""
Curriculum de statistiques — 4 mois, 39 concepts statiques
+ concepts dynamiques ingérés depuis docs/ (module 5).

Chaque concept contient le texte de référence et les métadonnées.
Le texte éducatif complet est généré par Claude à la première visite.
"""

CURRICULUM = {

    # ══════════════════════════════════════════════════════════════════════
    # MOIS 1 — FONDATIONS  (14 concepts)
    # ══════════════════════════════════════════════════════════════════════

    "m1_c1_population_echantillon": {
        "module": 1, "ordre": 1,
        "titre": "Population et Échantillon",
        "prereqs": [],
        "texte": """
Une POPULATION est l'ensemble complet de toutes les observations qui nous intéressent.
Un ÉCHANTILLON est le sous-ensemble étudié réellement. La TAILLE (n) conditionne la fiabilité.
Les PARAMÈTRES (μ, σ) décrivent la population; les STATISTIQUES (x̄, s) décrivent l'échantillon.
L'inférence statistique consiste à estimer les paramètres depuis les statistiques.
Un bon échantillon est représentatif — ses caractéristiques reflètent celles de la population.
        """.strip(),
    },

    "m1_c2_types_variables": {
        "module": 1, "ordre": 2,
        "titre": "Types de Variables",
        "prereqs": ["m1_c1_population_echantillon"],
        "texte": """
Variables QUANTITATIVES continues (temps de réaction, angle articulaire) ou discrètes (nb de soumissions).
Variables QUALITATIVES nominales (groupe CLA/DL/traditionnel) ou ordinales (niveau 1-5).
Le type de variable détermine l'analyse applicable — t-test impossible sur une variable nominale.
        """.strip(),
    },

    "m1_c3_moyenne_mediane_mode": {
        "module": 1, "ordre": 3,
        "titre": "Tendance Centrale",
        "prereqs": ["m1_c2_types_variables"],
        "texte": """
Moyenne (x̄) : somme / n. Sensible aux outliers.
Médiane : valeur centrale sur données ordonnées. Robuste aux outliers.
Mode : valeur la plus fréquente.
La moyenne de groupe peut masquer la réalité individuelle (Zheng et al. 2008 : 18 pros PGA,
mêmes moyennes, patterns individuels tous différents — mythe de la technique correcte).
        """.strip(),
    },

    "m1_c4_ecart_type_variance": {
        "module": 1, "ordre": 4,
        "titre": "Variance et Écart-Type",
        "prereqs": ["m1_c3_moyenne_mediane_mode"],
        "texte": """
Variance : s² = Σ(xi − x̄)² / (n−1). Le (n−1) est la correction de Bessel.
Écart-type : s = √s², dans les mêmes unités que les données.
En apprentissage moteur, l'écart-type MESURE la variabilité du mouvement —
le concept central de Gray. Deux groupes à même moyenne peuvent avoir des dispersions
radicalement différentes, ce que seul l'écart-type révèle.
        """.strip(),
    },

    "m1_c5_distribution_normale": {
        "module": 1, "ordre": 5,
        "titre": "La Distribution Normale",
        "prereqs": ["m1_c4_ecart_type_variance"],
        "texte": """
La distribution normale (courbe en cloche) est décrite par μ et σ uniquement.
Règle 68-95-99.7 : 68% des valeurs à ±1σ, 95% à ±2σ, 99.7% à ±3σ.
Centrale pour The Bell Curve : QI ~ N(100, 15²). Le titre fait directement
référence à cette courbe. Le Théorème Central Limite explique son omniprésence :
la somme de nombreuses variables indépendantes tend vers une distribution normale.
        """.strip(),
    },

    "m1_c6_z_scores": {
        "module": 1, "ordre": 6,
        "titre": "Z-scores et Percentiles",
        "prereqs": ["m1_c5_distribution_normale"],
        "texte": """
Z-score : z = (x − μ) / σ. Exprime la position en écarts-types.
Permet de comparer des mesures sur des échelles différentes.
QI 130 → z = (130−100)/15 = +2 → 97.7e percentile.
Le d de Cohen (différence entre groupes en écarts-types) est un z-score appliqué
à la comparaison de moyennes — fondamental pour lire The Bell Curve.
        """.strip(),
    },

    "m1_c7_types_etudes": {
        "module": 1, "ordre": 7,
        "titre": "Types d'Études",
        "prereqs": ["m1_c1_population_echantillon"],
        "texte": """
Étude EXPÉRIMENTALE (RCT) : assignation aléatoire des participants aux conditions.
Peut établir la causalité. Gold standard. Ex : Orangi et al. — 69 novices assignés
aléatoirement à CLA, DL ou traditionnel sur 12 semaines.

Étude OBSERVATIONNELLE : on observe sans manipuler. Peut identifier des associations,
pas des causes. Sous-types : transversale, longitudinale, cohorte, cas-témoins.

Étude QUASI-EXPÉRIMENTALE : ressemble à l'expérimental mais sans randomisation complète.
Ex : comparer des équipes qui ont choisi elles-mêmes leur méthode d'entraînement.

Hiérarchie des preuves : méta-analyse > RCT > cohorte > cas-témoins > expert opinion.
        """.strip(),
    },

    "m1_c8_biais_recherche": {
        "module": 1, "ordre": 8,
        "titre": "Biais en Recherche",
        "prereqs": ["m1_c7_types_etudes"],
        "texte": """
Biais de SÉLECTION : l'échantillon ne représente pas la population cible.
Ex : étudier la créativité motrice uniquement chez des athlètes universitaires.

Biais de CONFIRMATION : le chercheur interprète les données pour confirmer ses hypothèses.
Contre-mesure : préenregistrement des hypothèses avant la collecte.

Biais de MESURE : l'instrument de mesure est imparfait ou non calibré.
Ex : questionnaire de douleur subjectif vs capteurs de force objectifs.

Biais de PUBLICATION : les études avec résultats positifs sont publiées plus facilement.
Conduit à surestimer la taille des effets dans la littérature — lié à la crise de reproductibilité.

Biais de CONFUSION (confounding) : une troisième variable explique la corrélation observée.
        """.strip(),
    },

    "m1_c9_loi_grands_nombres": {
        "module": 1, "ordre": 9,
        "titre": "Loi des Grands Nombres",
        "prereqs": ["m1_c5_distribution_normale"],
        "texte": """
La loi des grands nombres affirme que la moyenne d'un échantillon converge vers
la vraie moyenne de la population quand n → ∞.

Implication directe : un petit n (n=12, n=42) donne une moyenne qui peut s'écarter
beaucoup de la vraie moyenne. C'est pourquoi les études avec petit échantillon
(fréquentes en sciences du sport) doivent être interprétées avec prudence.

L'erreur standard de la moyenne (SEM = s / √n) quantifie cette incertitude :
plus n est grand, plus la SEM est petite, plus l'estimation est précise.
        """.strip(),
    },

    "m1_c10_intervalle_confiance": {
        "module": 1, "ordre": 10,
        "titre": "Intervalles de Confiance",
        "prereqs": ["m1_c9_loi_grands_nombres", "m1_c6_z_scores"],
        "texte": """
Un intervalle de confiance à 95% est une plage de valeurs construite de telle façon
que, si on répétait l'étude un grand nombre de fois, 95% de ces intervalles
contiendraient le vrai paramètre de la population.

IC 95% pour la moyenne : x̄ ± 1.96 × (s / √n)

Interprétation critique : l'IC n'est PAS "la probabilité que le vrai paramètre
soit dans cet intervalle est 95%". Le vrai paramètre est fixe — c'est l'intervalle
qui est aléatoire. Erreur de raisonnement très fréquente dans les articles.

Un IC qui ne chevauche pas zéro (ou la valeur nulle) correspond à un résultat
statistiquement significatif au seuil α = 0.05.
        """.strip(),
    },

    "m1_c11_distribution_t": {
        "module": 1, "ordre": 11,
        "titre": "Distribution t de Student",
        "prereqs": ["m1_c10_intervalle_confiance"],
        "texte": """
Quand n est petit (<30) et σ inconnu (quasi-toujours en pratique), la distribution
normale ne s'applique plus exactement. La distribution t de Student la remplace.

La distribution t a des queues plus lourdes que la normale — elle attribue plus
de probabilité aux valeurs extrêmes, reflétant l'incertitude supplémentaire due au
petit échantillon.

Quand n → ∞, la distribution t converge vers la distribution normale. Avec n=120,
la différence est négligeable; avec n=10, elle est importante.

Le t-test compare deux moyennes en tenant compte de cette distribution. C'est le
test le plus fréquent dans les études d'apprentissage moteur.
        """.strip(),
    },

    "m1_c12_chi_carre": {
        "module": 1, "ordre": 12,
        "titre": "Test du Chi-carré (χ²)",
        "prereqs": ["m1_c2_types_variables", "m1_c10_intervalle_confiance"],
        "texte": """
Le test du chi-carré (χ²) compare des fréquences observées à des fréquences attendues.
Il s'applique aux variables catégorielles (nominales ou ordinales) — là où le t-test
ne s'applique pas.

Test d'INDÉPENDANCE : est-ce que deux variables catégorielles sont associées?
Ex : est-ce que le type de blessure (genou / épaule / autre) est indépendant
de la méthode d'entraînement (CLA / DL / traditionnel)?

Test de CONFORMITÉ : les données s'ajustent-elles à une distribution théorique?
Ex : la distribution des types de prises en JJB suit-elle une loi uniforme?

χ² = Σ (Observé − Attendu)² / Attendu. Plus χ² est grand, plus la différence
entre observé et attendu est importante.
        """.strip(),
    },

    "m1_c13_taille_echantillon": {
        "module": 1, "ordre": 13,
        "titre": "Taille d'Échantillon et Puissance",
        "prereqs": ["m1_c6_z_scores", "m1_c9_loi_grands_nombres"],
        "texte": """
La PUISSANCE statistique (1 − β) est la probabilité de détecter un effet réel
s'il existe. Elle dépend de trois paramètres : α (seuil), d (taille d'effet), n.

Puissance insuffisante → trop de faux négatifs. Majorité des études en sciences
du sport ont une puissance <0.80 avec des n autour de 10-30.

Pour une puissance de 0.80, avec α=0.05 et un effet moyen (d=0.5) :
n ≈ 64 participants par groupe. Beaucoup d'études publiées ont 15-20 par groupe.

Analyse de puissance A PRIORI : calculer n nécessaire avant l'étude.
Analyse de puissance A POSTERIORI : calculer la puissance réelle après — souvent
utilisée abusivement pour justifier un résultat négatif.
        """.strip(),
    },

    "m1_c14_visualisation_donnees": {
        "module": 1, "ordre": 14,
        "titre": "Visualisation des Données",
        "prereqs": ["m1_c4_ecart_type_variance", "m1_c5_distribution_normale"],
        "texte": """
HISTOGRAMME : distribue les données en classes. Révèle la forme de la distribution
(normale, asymétrique, bimodale). Toujours visualiser avant d'analyser.

BOXPLOT (boîte à moustaches) : montre la médiane, les quartiles (Q1, Q3),
l'IQR (Q3−Q1) et les outliers. Parfait pour comparer plusieurs groupes.

SCATTER PLOT : chaque point = un individu (x, y). Révèle la forme d'une relation
avant de calculer la corrélation. Une corrélation de 0.7 peut cacher des relations
très différentes — l'Anscombe's Quartet le démontre.

QQ-PLOT : vérifie si les données suivent une distribution normale. Points alignés
sur la diagonale = normalité. Présupposé de nombreux tests paramétriques.
        """.strip(),
    },

    # ══════════════════════════════════════════════════════════════════════
    # MOIS 2 — INFÉRENCE STATISTIQUE  (9 concepts)
    # ══════════════════════════════════════════════════════════════════════

    "m2_c1_hypotheses": {
        "module": 2, "ordre": 1,
        "titre": "Tests d'Hypothèses : H₀ et H₁",
        "prereqs": ["m1_c10_intervalle_confiance"],
        "texte": """
H₀ (hypothèse nulle) : pas d'effet, pas de différence — position par défaut.
H₁ (hypothèse alternative) : il y a un effet — ce que le chercheur cherche.
On suppose H₀ vraie, on calcule la probabilité des données observées sous H₀.
Si cette probabilité est très faible (p < α), on rejette H₀.
Erreur type I (α) : rejeter H₀ quand elle est vraie. Erreur type II (β) : ne pas la rejeter quand elle est fausse.
        """.strip(),
    },

    "m2_c2_p_value": {
        "module": 2, "ordre": 2,
        "titre": "La p-value",
        "prereqs": ["m2_c1_hypotheses"],
        "texte": """
p-value = probabilité d'observer des données aussi extrêmes si H₀ est vraie.
Seuil α = 0.05 par convention. p < 0.05 → "statistiquement significatif".
Ce que la p-value ne dit PAS : ni la probabilité que H₀ est vraie, ni l'importance pratique.
Avec n=10 000, un effet négligeable peut être p < 0.001.
Dans les études d'apprentissage moteur, toujours chercher la taille d'effet à côté de la p-value.
        """.strip(),
    },

    "m2_c3_taille_effet": {
        "module": 2, "ordre": 3,
        "titre": "Taille d'Effet : d de Cohen",
        "prereqs": ["m2_c2_p_value"],
        "texte": """
d de Cohen = (μ₁ − μ₂) / σ_poolé. Mesure l'importance pratique, indépendamment de n.
0.2 = petit, 0.5 = moyen, 0.8 = grand (conventions de Cohen, 1988).
Dans The Bell Curve, les différences inter-groupes sont exprimées en d.
Toujours rapporter d (ou η², ω²) à côté de la p-value dans les études.
        """.strip(),
    },

    "m2_c4_anova": {
        "module": 2, "ordre": 4,
        "titre": "ANOVA à Un Facteur",
        "prereqs": ["m2_c3_taille_effet", "m1_c11_distribution_t"],
        "texte": """
L'ANOVA (Analysis of Variance) compare les moyennes de 3 groupes ou plus simultanément.
Faire plusieurs t-tests augmenterait le risque de faux positifs (problème des comparaisons multiples).

L'ANOVA décompose la variance totale en variance INTER-groupes (signal) et
variance INTRA-groupes (bruit). Le ratio F = variance inter / variance intra.
Grand F → les groupes sont plus différents entre eux qu'au sein de chacun.

Dans Orangi et al. : ANOVA compare CLA, DL et traditionnel sur les facteurs de risque LCA.
η² (eta-carré) = variance expliquée par le groupe. Équivalent du R² pour l'ANOVA.
Présupposés : normalité dans chaque groupe, homogénéité des variances (test de Levene).
        """.strip(),
    },

    "m2_c5_anova_mesures_repetees": {
        "module": 2, "ordre": 5,
        "titre": "ANOVA à Mesures Répétées",
        "prereqs": ["m2_c4_anova"],
        "texte": """
Utilisée quand les mêmes participants sont mesurés plusieurs fois (pré-test, post-test,
suivi à 3 mois). Chaque participant sert de son propre contrôle — élimine la variabilité
inter-individuelle de l'erreur, augmentant la puissance.

Structure des données : chaque ligne = un participant, chaque colonne = un temps de mesure.
Présupposé critique : SPHÉRICITÉ — les variances des différences entre paires de
temps de mesure sont égales. Test de Mauchly. Si violé, correction d'Epsilon
(Greenhouse-Geisser ou Huynh-Feldt).

Très fréquente dans les études longitudinales en apprentissage moteur
(mesures à T1, T2, T3... pendant une intervention d'entraînement).
        """.strip(),
    },

    "m2_c6_tests_non_parametriques": {
        "module": 2, "ordre": 6,
        "titre": "Tests Non Paramétriques",
        "prereqs": ["m2_c4_anova"],
        "texte": """
Les tests paramétriques (t-test, ANOVA) présupposent la normalité.
Quand ce présupposé est violé — petit n, distribution asymétrique, données ordinales —
on utilise les équivalents non paramétriques.

Mann-Whitney U : alternative au t-test indépendant. Compare les rangs, pas les moyennes.
Wilcoxon signé : alternative au t-test apparié (mesures répétées sur 2 temps).
Kruskal-Wallis : alternative à l'ANOVA à un facteur.

Plus robustes aux outliers et aux distributions asymétriques.
Moins puissants que les tests paramétriques quand leurs présupposés sont respectés.
Fréquents dans les études avec petits échantillons (n < 20) en sciences du sport.
        """.strip(),
    },

    "m2_c7_comparaisons_multiples": {
        "module": 2, "ordre": 7,
        "titre": "Comparaisons Multiples",
        "prereqs": ["m2_c4_anova", "m2_c2_p_value"],
        "texte": """
Problème : si on fait 20 tests avec α = 0.05, on s'attend à un faux positif par chance.
L'ANOVA globale protège contre ça, mais les comparaisons POST-HOC entre paires de groupes
nécessitent une correction.

Correction de BONFERRONI : divise α par le nombre de tests. Simple mais conservative
(augmente les faux négatifs). α_corrigé = 0.05 / k tests.

FDR (False Discovery Rate, Benjamini-Hochberg) : contrôle la proportion attendue de
faux positifs parmi les résultats significatifs. Moins conservative que Bonferroni.

Tests POST-HOC courants : Tukey HSD, Scheffé, Dunnett (comparaison à un contrôle).
En lisant un article : vérifier si des comparaisons multiples ont été effectuées
et si une correction a été appliquée.
        """.strip(),
    },

    "m2_c8_tests_unilateraux_bilateraux": {
        "module": 2, "ordre": 8,
        "titre": "Tests Unilatéraux vs Bilatéraux",
        "prereqs": ["m2_c2_p_value"],
        "texte": """
Test BILATÉRAL (two-tailed) : teste si μ₁ ≠ μ₂, sans présumer de la direction.
H₁ : μ₁ − μ₂ ≠ 0. L'aire de rejet est répartie des deux côtés.

Test UNILATÉRAL (one-tailed) : teste si μ₁ > μ₂ OU μ₁ < μ₂ — directionnel.
H₁ : μ₁ − μ₂ > 0. Plus puissant (aire de rejet d'un seul côté), mais justification
théorique préalable requise.

Problème en pratique : les chercheurs qui obtiennent p = 0.07 bilatéral peuvent être
tentés de justifier après coup un test unilatéral pour obtenir p = 0.035. C'est du
"p-hacking". Un test unilatéral doit être justifié AVANT de voir les données.

Standard dans les articles : test bilatéral sauf mention explicite et justification.
        """.strip(),
    },

    "m2_c9_crise_reproductibilite": {
        "module": 2, "ordre": 9,
        "titre": "Crise de la Reproductibilité",
        "prereqs": ["m2_c7_comparaisons_multiples", "m1_c8_biais_recherche"],
        "texte": """
En 2015, le Reproducibility Project tente de reproduire 100 études de psychologie :
seulement 36 obtiennent des résultats statistiquement significatifs (vs 97 originales).

Causes principales : p-hacking (chercher jusqu'à p < 0.05), HARKing (formuler
l'hypothèse après les résultats), biais de publication (uniquement les positifs publiés),
petits n, faibles tailles d'effet, flexibilité non déclarée dans l'analyse.

Solutions adoptées : préenregistrement des hypothèses (OSF), open data, open materials,
registered reports (revue avant collecte), méta-analyses à effets aléatoires.

Impact sur la lecture d'articles : un résultat unique p < 0.05 n'est pas convaincant.
Chercher : réplication, effet large, préenregistrement, données disponibles.
        """.strip(),
    },

    # ══════════════════════════════════════════════════════════════════════
    # MOIS 3 — RELATIONS ENTRE VARIABLES  (8 concepts)
    # ══════════════════════════════════════════════════════════════════════

    "m3_c1_correlation": {
        "module": 3, "ordre": 1,
        "titre": "Corrélation de Pearson",
        "prereqs": ["m2_c3_taille_effet"],
        "texte": """
r de Pearson varie de −1 à +1. Mesure la relation linéaire entre deux variables continues.
|r| : 0.1-0.3 faible, 0.3-0.5 modéré, 0.5-0.7 fort, >0.7 très fort.
Corrélation ≠ causalité. Toujours tracer le scatter plot avant de calculer r.
Han et al. (2015) : acuité proprioceptive "prédit 30% de la variance du niveau de compétition" → r² = 0.30 → r ≈ 0.55.
        """.strip(),
    },

    "m3_c2_regression_lineaire": {
        "module": 3, "ordre": 2,
        "titre": "Régression Linéaire et R²",
        "prereqs": ["m3_c1_correlation"],
        "texte": """
Y = a + bX + erreur. b = pente (changement de Y par unité de X). a = ordonnée à l'origine.
R² = proportion de variance de Y expliquée par X = r².
Régression multiple : Y = a + b₁X₁ + b₂X₂ + ... — contrôle des confondants.
The Bell Curve utilise massivement la régression multiple pour isoler l'effet du QI
sur les outcomes sociaux en contrôlant le statut socio-économique parental.
        """.strip(),
    },

    "m3_c3_regression_logistique": {
        "module": 3, "ordre": 3,
        "titre": "Régression Logistique et Odds Ratio",
        "prereqs": ["m3_c2_regression_lineaire"],
        "texte": """
Quand Y est binaire (blessé/non blessé, succès/échec), la régression linéaire produit
des prédictions absurdes (probabilités < 0 ou > 1). La régression logistique modélise
log(p/(1-p)) = a + bX — la transformation logit maintient les prédictions entre 0 et 1.

ODDS RATIO (OR) : rapport de cotes. OR = (p/(1-p))₁ / (p/(1-p))₂.
OR > 1 : facteur augmente les chances. OR = 2 : deux fois plus probable.
OR ≠ Risque Relatif (RR). Pour les événements rares, OR ≈ RR. Pour les événements
fréquents, OR exagère le risque relatif.

Très fréquent en épidémiologie et études de blessures sportives.
        """.strip(),
    },

    "m3_c4_variables_confondantes": {
        "module": 3, "ordre": 4,
        "titre": "Variables Confondantes",
        "prereqs": ["m3_c2_regression_lineaire"],
        "texte": """
Un CONFONDANT est une variable liée à la fois à X et à Y, qui crée une fausse
association entre eux. Ex : les pays avec plus de chocolat per capita ont plus de
lauréats Nobel — mais la richesse nationale (confondant) explique les deux.

En sciences du sport : niveau initial des participants peut confondre l'effet
d'une méthode d'entraînement. Un groupe CLA avec des participants initialement
plus forts semblera plus efficace même si ce n'est pas la méthode qui explique.

Contrôle des confondants : randomisation (RCT) élimine les confondants connus ET
inconnus. En étude observationnelle, on les inclut dans la régression multiple.

Biais de COLLIDER : contrôler une variable qui est causée à la fois par X et Y
peut créer une fausse association plutôt que l'éliminer.
        """.strip(),
    },

    "m3_c5_correlation_spearman": {
        "module": 3, "ordre": 5,
        "titre": "Corrélation de Spearman",
        "prereqs": ["m3_c1_correlation", "m2_c6_tests_non_parametriques"],
        "texte": """
Le ρ (rho) de Spearman est la corrélation de Pearson calculée sur les RANGS des données
plutôt que sur les valeurs brutes. Équivalent non paramétrique.

Utiliser Spearman quand : la relation n'est pas linéaire mais monotone, les données
sont ordinales, il y a des outliers influents, ou la normalité est violée.

Interprétation identique à Pearson : varie de −1 à +1. Un ρ = 0.8 signifie
que quand X augmente, Y tend aussi à augmenter (relation monotone forte).

En psychométrie : les échelles ordinales (Likert 1-5) sont souvent corrélées
avec Spearman plutôt que Pearson, bien que le débat sur la bonne approche persiste.
        """.strip(),
    },

    "m3_c6_regression_multiple_avancee": {
        "module": 3, "ordre": 6,
        "titre": "Régression Multiple Avancée",
        "prereqs": ["m3_c2_regression_lineaire", "m3_c4_variables_confondantes"],
        "texte": """
Coefficients STANDARDISÉS (bêta) : permettent de comparer l'importance relative
des prédicteurs sur une échelle commune (en écarts-types).

MULTICOLINÉARITÉ : quand deux prédicteurs sont très corrélés entre eux, leurs
coefficients deviennent instables et difficiles à interpréter. VIF (Variance Inflation
Factor) > 10 indique une multicolinéarité problématique.

INTERACTIONS : l'effet de X₁ sur Y dépend de la valeur de X₂.
Ex : l'effet de la méthode d'entraînement (CLA vs traditionnel) sur la performance
diffère selon le niveau d'expertise du participant.

VALEURS ABERRANTES ET INFLUENCE : un point levier peut fortement distordre la droite
de régression. Distance de Cook mesure l'influence de chaque observation.
        """.strip(),
    },

    "m3_c7_modeles_mixtes": {
        "module": 3, "ordre": 7,
        "titre": "Modèles Mixtes (Effets Aléatoires)",
        "prereqs": ["m2_c5_anova_mesures_repetees", "m3_c6_regression_multiple_avancee"],
        "texte": """
Les modèles mixtes (Linear Mixed Models, LMM) combinent effets FIXES (prédicteurs
qu'on veut estimer : méthode d'entraînement, temps) et effets ALÉATOIRES (variation
entre participants, entre équipes, entre études).

Pourquoi c'est important : dans les données longitudinales, les mesures répétées du
même participant ne sont pas indépendantes — elles se ressemblent. Ignorer cette
structure donne des erreurs standard incorrectes (souvent trop petites).

Remplace avantageusement l'ANOVA à mesures répétées : gère les données manquantes,
les mesures irrégulières dans le temps, les effets aléatoires multiples.

Standard dans les études longitudinales récentes en apprentissage moteur et en
psychologie cognitive. Expression courante dans les articles : "we used a LMM
with random intercepts for participants."
        """.strip(),
    },

    "m3_c8_meta_analyse": {
        "module": 3, "ordre": 8,
        "titre": "Méta-Analyse",
        "prereqs": ["m2_c3_taille_effet", "m2_c9_crise_reproductibilite"],
        "texte": """
La méta-analyse combine quantitativement les résultats de plusieurs études pour
estimer un effet moyen plus précis. Chaque étude est pondérée par sa précision (n).

FOREST PLOT : graphique standard de la méta-analyse. Chaque ligne = une étude,
avec son effet estimé (carré) et son IC 95% (barre horizontale). Le diamant
en bas = effet poolé de toutes les études.

Hétérogénéité (I²) : proportion de la variabilité totale due aux différences réelles
entre études (vs variation d'échantillonnage). I² > 75% = hétérogénéité élevée →
un effet poolé unique est difficile à interpréter.

Effets FIXES vs ALÉATOIRES : effets fixes supposent que toutes les études estiment
le même vrai effet. Effets aléatoires (recommandés) supposent que les vrais effets
varient entre études. Buszard (2016) : méta-analyse sur 25 études d'équipement scalé.
        """.strip(),
    },

    # ══════════════════════════════════════════════════════════════════════
    # MOIS 4 — PSYCHOMÉTRIE ET GÉNÉTIQUE  (8 concepts)
    # ══════════════════════════════════════════════════════════════════════

    "m4_c1_analyse_factorielle": {
        "module": 4, "ordre": 1,
        "titre": "Analyse Factorielle et Facteur g",
        "prereqs": ["m3_c1_correlation"],
        "texte": """
L'analyse factorielle identifie des variables latentes qui expliquent les corrélations
entre variables observées. Le facteur g (Spearman, 1904) est le facteur commun
extrait des scores à de multiples tests cognitifs — tous corrélés positivement.
Saturation factorielle (loading) : degré auquel un test mesure g.
Le débat : g existe statistiquement. Sa signification biologique est contestée.
        """.strip(),
    },

    "m4_c2_heritabilite": {
        "module": 4, "ordre": 2,
        "titre": "Héritabilité (h²)",
        "prereqs": ["m4_c1_analyse_factorielle"],
        "texte": """
h² = variance génétique / variance totale. Spécifique à UNE population dans UN environnement.
h² = 0.8 pour le QI ne signifie pas que le QI est immuable ni que les différences
inter-groupes sont génétiques. Erreur de Lewontin : h² élevée dans chaque groupe
n'implique rien sur la cause de la différence ENTRE groupes.
Études de jumeaux : MZ vs DZ permettent de décomposer la variance en A, C, E.
        """.strip(),
    },

    "m4_c3_fidelite_validite": {
        "module": 4, "ordre": 3,
        "titre": "Fiabilité et Validité",
        "prereqs": ["m3_c1_correlation"],
        "texte": """
FIABILITÉ (reliability) : consistance de la mesure. Un test fiable donne les mêmes
résultats dans les mêmes conditions. Mesurée par : alpha de Cronbach (cohérence
interne), fidélité test-retest (corrélation entre deux passations), accord inter-juge.

Alpha de Cronbach (α) : mesure si les items d'une échelle mesurent le même construit.
α > 0.70 acceptable, > 0.80 bon, > 0.90 excellent. N'implique pas la validité.

VALIDITÉ : le test mesure-t-il ce qu'il prétend mesurer?
Validité de CONTENU : les items couvrent-ils le construit entier?
Validité de CONSTRUIT : le test se comporte-t-il comme la théorie le prédit?
Validité PRÉDICTIVE : le score prédit-il un critère externe pertinent?

Un test peut être fiable sans être valide (mesurer systématiquement la mauvaise chose).
        """.strip(),
    },

    "m4_c4_structure_factorielle": {
        "module": 4, "ordre": 4,
        "titre": "Structure Factorielle",
        "prereqs": ["m4_c1_analyse_factorielle", "m4_c3_fidelite_validite"],
        "texte": """
Analyse Factorielle EXPLORATOIRE (AFE) : cherche la structure sous-jacente sans
hypothèse préalable. Combien de facteurs? Scree plot, règle de Kaiser (valeurs propres > 1),
analyse parallèle. Rotation VARIMAX (orthogonale) ou OBLIMIN (oblique si facteurs corrélés).

Analyse Factorielle CONFIRMATOIRE (AFC) : teste une structure théorique prédéfinie.
Indices d'ajustement : CFI > 0.95, RMSEA < 0.06, SRMR < 0.08 (critères de Hu & Bentler).

Valeur propre (eigenvalue) : variance expliquée par un facteur. La somme des valeurs
propres = nombre de variables. Le premier facteur en extrait toujours le plus.

En psychologie de l'intelligence : le débat g vs modèles hiérarchiques (CHC, CATTELL)
porte précisément sur la structure factorielle optimale des tests cognitifs.
        """.strip(),
    },

    "m4_c5_mesure_invariance": {
        "module": 4, "ordre": 5,
        "titre": "Invariance de Mesure",
        "prereqs": ["m4_c4_structure_factorielle"],
        "texte": """
L'invariance de mesure répond à : est-ce que le même construit est mesuré de la
même façon dans différents groupes (sexes, cultures, niveaux d'expertise)?

Si un test de QI n'est pas invariant entre groupes, comparer les moyennes de ces
groupes est trompeur — on compare des choses différentes.

Niveaux d'invariance (du plus faible au plus fort) :
1. Configural : même structure factorielle dans chaque groupe
2. Métrique : mêmes saturations (loadings) — permet de comparer les corrélations
3. Scalaire : mêmes interceptes — permet de comparer les moyennes
4. Stricte : mêmes variances résiduelles

La plupart des comparaisons inter-groupes publiées supposent l'invariance scalaire
sans la tester — biais fréquent dans la littérature sur l'intelligence.
        """.strip(),
    },

    "m4_c6_genetique_comportementale": {
        "module": 4, "ordre": 6,
        "titre": "Génétique Comportementale",
        "prereqs": ["m4_c2_heritabilite"],
        "texte": """
Méthodes pour décomposer la variance phénotypique (A + C + E = 1) :

Études de JUMEAUX : MZ (identiques, 100% gènes partagés) vs DZ (fraternels, 50%).
Si MZ plus similaires que DZ → composante génétique (A). Si MZ élevés et DZ bas → peu d'environnement partagé (C faible).

Études d'ADOPTION : enfants biologiques vs adoptés. Compare l'effet des gènes (biologiques) vs l'environnement (adoptifs).

GWAS (Genome-Wide Association Studies) : cherche les variants génétiques (SNPs) associés
à un trait. Pour le QI : milliers de SNPs chacun avec effet minuscule — architecture
polygénique. Les scores polygéniques expliquent ~12% de la variance du QI.

Lien avec The Bell Curve : Herrnstein & Murray invoquent l'héritabilité mais
le livre (1994) précède l'ère GWAS. Les preuves ont évolué depuis.
        """.strip(),
    },

    "m4_c7_biais_publication": {
        "module": 4, "ordre": 7,
        "titre": "Biais de Publication et Forest Plots",
        "prereqs": ["m3_c8_meta_analyse", "m2_c9_crise_reproductibilite"],
        "texte": """
Le biais de publication : les études avec résultats positifs sont publiées 3-4x
plus facilement que les négatives. Résultat : la littérature surestime les effets.

FUNNEL PLOT : scatter plot de la taille d'effet vs la précision (1/SE).
Sans biais : forme d'entonnoir symétrique. Asymétrie → biais de publication probable.
Test d'Egger : test statistique de l'asymétrie du funnel plot.

TRIM-AND-FILL : méthode pour estimer l'effet "corrigé" en imputant les études manquantes.

P-CURVE : distribution des p-values significatives. Si les effets sont réels,
la p-curve devrait être décroissante (beaucoup de p très petits). Si plate ou
croissante → les études positives sont probablement des faux positifs.

En psychométrie : les études sur les différences de groupes en QI sont particulièrement
affectées par les biais de publication dans les deux directions.
        """.strip(),
    },

    "m4_c8_lecture_critique": {
        "module": 4, "ordre": 8,
        "titre": "Lecture Critique d'un Article",
        "prereqs": [
            "m2_c9_crise_reproductibilite",
            "m4_c7_biais_publication",
            "m3_c8_meta_analyse"
        ],
        "texte": """
Grille de lecture systématique d'un article empirique :

1. QUESTION : est-elle clairement formulée? Préenregistrée?
2. DESIGN : quel type d'étude? Randomisé? Groupe contrôle adéquat?
3. ÉCHANTILLON : n suffisant? Représentatif? Critères d'inclusion/exclusion?
4. MESURES : fiabilité et validité rapportées? Outcome primaire défini a priori?
5. ANALYSE : test adapté au type de données? Présupposés vérifiés?
6. RÉSULTATS : taille d'effet rapportée? IC 95%? P-value seule insuffisante.
7. DISCUSSION : les auteurs surestiment-ils la portée des conclusions?
   Correlation présentée comme causalité? Généralisation abusive?
8. CONFLIT D'INTÉRÊTS : financement? Affiliation des auteurs?
9. RÉPLICATION : résultat confirmé ailleurs? Dans un pré-enregistrement?
        """.strip(),
    },
}


# ── Helpers ───────────────────────────────────────────────────────────────────

def get_concepts_par_module(module: int) -> list[str]:
    return sorted(
        [k for k, v in CURRICULUM.items() if v["module"] == module],
        key=lambda k: CURRICULUM[k]["ordre"]
    )


def get_concept(key: str) -> dict | None:
    return CURRICULUM.get(key)


def prereqs_satisfaits(concept_id: str, progression) -> bool:
    """
    Vérifie si tous les prérequis d'un concept sont satisfaits.

    progression peut être :
      - un set / frozenset d'IDs de concepts maîtrisés (usage app.py)
      - un dict {concept_id: {"statut": ...}} (usage héritage)
    """
    prereqs = CURRICULUM.get(concept_id, {}).get("prereqs", [])
    if not prereqs:
        return True
    if isinstance(progression, (set, frozenset)):
        return all(p in progression for p in prereqs)
    # dict avec clé "statut"
    for p in prereqs:
        if p not in progression:
            return False
        if progression[p].get("statut") not in ("en_cours", "maitrise"):
            return False
    return True


def lister_curriculum() -> None:
    modules = NOMS_MODULES if "NOMS_MODULES" in globals() else {
        1: "Fondations", 2: "Inférence", 3: "Relations",
        4: "Psychométrie", 5: "Documents personnels"
    }
    for m, nom in modules.items():
        concepts = get_concepts_par_module(m)
        if not concepts:
            continue
        print(f"\n  Mois {m} — {nom}")
        for k in concepts:
            source = CURRICULUM[k].get("source", "")
            tag = f"  [{source}]" if source else ""
            print(f"    • {CURRICULUM[k]['titre']}{tag}")


NOMS_MODULES = {
    1: "Fondations",
    2: "Inférence statistique",
    3: "Relations entre variables",
    4: "Psychométrie et génétique",
    5: "Documents personnels",
    6: "Biologie",
    7: "Sciences politiques",
    8: "Informatique",
    9: "Finances",
    10: "Histoire — Historionomie",
    11: "Antiquité — Grèce & Rome",
    12: "Apprentissage moteur",
    13: "Mécanique et leviers",
    14: "Historiographie de la Shoah",
    15: "Architecture Railway",
    16: "Bitcoin & Cryptomonnaies",
    17: "JSON pour non-programmeurs",
    18: "Lire une erreur d'agent",
    19: "Anatomie d'un workflow Claude",
    20: "Concevoir un workflow multi-agents",
    21: "Bash et terminal — l'essentiel",
    22: "Gouvernance de l'IA",
}

DOMAINES_MODULES = {
    1: "statistiques", 2: "statistiques", 3: "statistiques",
    4: "statistiques", 5: "statistiques",
    6: "biologie", 7: "sciences_politiques",
    8: "informatique", 9: "finances",
    10: "histoire", 11: "histoire",
    12: "apprentissage_moteur",
    13: "mecanique",
    14: "histoire",
    15: "informatique",
    16: "finances",
    17: "informatique",
    18: "informatique",
    19: "informatique",
    20: "informatique",
    21: "informatique",
    22: "gouvernance_ia",
}

# ── Sous-groupes : segmente les modules longs en sections nommées ─────────────
# Clé = numéro de module, valeur = liste ordonnée de sections.
# "min"/"max" correspondent à l'attribut "ordre" des concepts.

SOUS_GROUPES: dict[int, list[dict]] = {
    7: [
        {"titre": "Théorie générale & Relations internationales", "min": 1, "max": 9},
        {"titre": "Canada",        "min": 10, "max": 10},
        {"titre": "France",        "min": 11, "max": 12},
        {"titre": "États-Unis",    "min": 13, "max": 14},
    ],
    11: [
        {"titre": "T1 — Grèce archaïque et classique",        "min": 1,  "max": 9},
        {"titre": "T2 — Rome républicaine (origines à Auguste)", "min": 10, "max": 18},
        {"titre": "T3 — Haut-Empire",                          "min": 19, "max": 27},
        {"titre": "T4 — Déclin, chute et héritage",            "min": 28, "max": 36},
    ],
    12: [
        {"titre": "Baccalauréat — Fondements",        "min": 1,  "max": 10},
        {"titre": "Maîtrise — Approfondissement",     "min": 11, "max": 19},
        {"titre": "Doctorat — Frontières de la recherche", "min": 20, "max": 28},
    ],
}

# ── Parcours conseillés : enchaînements recommandés entre modules ─────────────
# Clé = module source, valeur = {"module": int, "label": str}

PARCOURS_CONSEILLES: dict[int, dict] = {
    10: {"module": 11, "label": "Approfondir avec l'Antiquité — Grèce & Rome →"},
    11: {"module": 10, "label": "Retourner à l'Historionomie (relire Fabry) →"},
}


# ══════════════════════════════════════════════════════════════════════
# MODULE 6 — BIOLOGIE  (10 concepts)
# ══════════════════════════════════════════════════════════════════════

CURRICULUM.update({

    "m6_c1_cellule": {
        "module": 6, "ordre": 1,
        "titre": "La Cellule : Unité du Vivant",
        "prereqs": [],
        "texte": """
La cellule est l'unité fonctionnelle et structurale de tout être vivant.
Cellules PROCARYOTES (bactéries) : pas de noyau, ADN libre dans le cytoplasme.
Cellules EUCARYOTES (animaux, végétaux) : noyau membranaire, organites compartimentés.
Organites clés : noyau (ADN), mitochondries (ATP), réticulum endoplasmique (protéines),
appareil de Golgi (tri/export), ribosomes (synthèse protéique), lysosomes (dégradation).
La membrane plasmique : bicouche lipidique + protéines. Sélectivement perméable.
        """.strip(),
    },

    "m6_c2_adn": {
        "module": 6, "ordre": 2,
        "titre": "L'ADN et l'Information Génétique",
        "prereqs": ["m6_c1_cellule"],
        "texte": """
L'ADN (acide désoxyribonucléique) est une double hélice de nucléotides (A-T, C-G).
Le GÉNOME humain : ~3 milliards de paires de bases, ~20 000 gènes, 46 chromosomes.
GÈNE : séquence d'ADN codant pour une protéine ou un ARN fonctionnel.
Dogme central : ADN → ARNm (transcription) → protéine (traduction).
La majorité du génome (~98%) est non-codante. Certaines séquences régulent l'expression des gènes.
SNP (Single Nucleotide Polymorphism) : variation d'une seule base. Clé pour les études GWAS.
        """.strip(),
    },

    "m6_c3_division_cellulaire": {
        "module": 6, "ordre": 3,
        "titre": "Mitose et Méiose",
        "prereqs": ["m6_c2_adn"],
        "texte": """
MITOSE : division cellulaire qui produit 2 cellules filles génétiquement identiques.
Phases : prophase, métaphase, anaphase, télophase. Utilisée pour la croissance et la réparation.
MÉIOSE : division qui produit 4 gamètes (spermatozoïdes/ovules) avec la moitié du génome (n=23).
Inclut la recombinaison génétique (crossing-over) — source majeure de variation génétique.
La méiose est la raison pour laquelle les enfants ne sont pas des clones de leurs parents.
Erreurs de méiose : trisomie 21 (chromosome 21 en 3 exemplaires).
        """.strip(),
    },

    "m6_c4_genetique_mendelienne": {
        "module": 6, "ordre": 4,
        "titre": "Génétique Mendélienne",
        "prereqs": ["m6_c3_division_cellulaire"],
        "texte": """
Mendel (1866) : lois de la transmission héréditaire via des «facteurs» discrets (gènes).
ALLÈLES : variantes d'un même gène. Dominant (A) masque le récessif (a).
Génotype AA ou Aa → phénotype dominant. aa → phénotype récessif.
Loi de ségrégation : chaque individu transmet un allèle par gamète.
Loi d'assortiment indépendant : gènes sur chromosomes différents se transmettent indépendamment.
Limites du mendélisme : la plupart des traits humains (taille, QI, sportivité) sont POLYGÉNIQUES
— influencés par des milliers de gènes, chacun avec un petit effet.
        """.strip(),
    },

    "m6_c5_evolution": {
        "module": 6, "ordre": 5,
        "titre": "Évolution et Sélection Naturelle",
        "prereqs": ["m6_c4_genetique_mendelienne"],
        "texte": """
Darwin (1859) : la sélection naturelle favorise les individus les mieux adaptés à leur environnement.
Mécanismes évolutifs : sélection naturelle, dérive génétique, flux génique, mutations.
Fitness darwinienne : succès reproducteur, pas force physique ou santé.
DÉRIVE GÉNÉTIQUE : changement aléatoire des fréquences alléliques, surtout dans les petites populations.
Goulot d'étranglement : réduction sévère de la population → perte de diversité génétique.
Sélection DIRECTIONNELLE (vers un extrême), STABILISANTE (vers la moyenne), DISRUPTIVE (vers les extrêmes).
La sélection n'est pas prévoyante — elle optimise pour l'environnement actuel.
        """.strip(),
    },

    "m6_c6_expression_genique": {
        "module": 6, "ordre": 6,
        "titre": "Expression Génique et Épigénétique",
        "prereqs": ["m6_c2_adn"],
        "texte": """
Tous les cellules d'un organisme ont le même ADN, mais n'expriment pas les mêmes gènes.
L'EXPRESSION GÉNIQUE est régulée par des facteurs de transcription, des enhancers, des silencers.
ÉPIGÉNÉTIQUE : modifications héréditaires de l'expression génique sans changer la séquence ADN.
Mécanismes : méthylation de l'ADN (silence les gènes), modification des histones (activation/répression).
L'environnement (stress, nutrition, exercice) influence l'épigénome.
Les marques épigénétiques peuvent être partiellement transmises aux générations suivantes.
Lien avec la performance sportive : l'entraînement modifie l'expression des gènes musculaires.
        """.strip(),
    },

    "m6_c7_systeme_nerveux": {
        "module": 6, "ordre": 7,
        "titre": "Système Nerveux et Neurotransmission",
        "prereqs": ["m6_c1_cellule"],
        "texte": """
Le NEURONE : cellule spécialisée dans la transmission d'information électrique et chimique.
Potentiel d'action : signal électrique qui se propage le long de l'axone (dépolarisation).
SYNAPSE : jonction entre deux neurones. Neurotransmetteurs traversent la fente synaptique.
Principaux neurotransmetteurs : dopamine (récompense/motivation), sérotonine (humeur),
acétylcholine (mémoire/mouvements), GABA (inhibition), glutamate (excitation).
Plasticité synaptique : les synapses se renforcent avec l'usage (LTP) — base neurologique de l'apprentissage.
Myélinisation : gaine de myéline accélère la conduction. Se développe jusqu'au milieu de la vingtaine.
        """.strip(),
    },

    "m6_c8_systeme_immunitaire": {
        "module": 6, "ordre": 8,
        "titre": "Système Immunitaire",
        "prereqs": ["m6_c1_cellule"],
        "texte": """
Immunité INNÉE : première ligne de défense, rapide, non spécifique.
Cellules : macrophages, cellules NK, neutrophiles. Reconnaît des motifs généraux (PAMP).
Immunité ADAPTATIVE : spécifique, plus lente, développe une mémoire.
Lymphocytes B : produisent des anticorps (immunoglobulines). Immunité humorale.
Lymphocytes T : tuent les cellules infectées (T cytotoxiques) ou coordonnent (T auxiliaires).
VACCINS : exposent le système immunitaire à un antigène inoffensif pour créer une mémoire.
Inflammation : réponse innée au dommage tissulaire. Chronique si persistante → maladies auto-immunes.
        """.strip(),
    },

    "m6_c9_biologie_moleculaire": {
        "module": 6, "ordre": 9,
        "titre": "Biotechnologies et CRISPR",
        "prereqs": ["m6_c2_adn", "m6_c4_genetique_mendelienne"],
        "texte": """
PCR (Polymerase Chain Reaction) : amplification d'un fragment d'ADN. Utilisé en diagnostics et GWAS.
Séquençage ADN : lecture de la séquence de bases. Coût passé de ~3 milliards (2003) à ~500$ (2023).
CRISPR-Cas9 : ciseau moléculaire qui coupe l'ADN à un site précis pour éditer le génome.
Applications : thérapies géniques (maladies héréditaires), cultures OGM résistantes, recherche.
Débats éthiques : édition germinale (modification transmissible), designer babies.
Séquençage de nouvelle génération (NGS) : permet les GWAS à grande échelle — base des études
sur la génétique de l'intelligence et des traits comportementaux (lien avec module stats/psychométrie).
        """.strip(),
    },

    "m6_c10_ecologie": {
        "module": 6, "ordre": 10,
        "titre": "Écologie et Flux d'Énergie",
        "prereqs": ["m6_c5_evolution"],
        "texte": """
ÉCOSYSTÈME : communauté d'organismes + leur environnement abiotique.
Chaînes alimentaires : producteurs (végétaux) → consommateurs primaires → secondaires → décomposeurs.
Seulement ~10% de l'énergie est transférée à chaque niveau trophique (règle des 10%).
BIODIVERSITÉ : variété des espèces dans un écosystème. Corrélée à la résilience et la stabilité.
Biomes : forêt tropicale, savane, toundra, désert — définis par le climat et la végétation.
Changement climatique : perturbation des cycles biogéochimiques (carbone, azote, eau).
CO₂ atmosphérique : de 280 ppm (préindustriel) à 420 ppm (2023) → effet de serre amplifié.
        """.strip(),
    },
})


# ══════════════════════════════════════════════════════════════════════
# MODULE 7 — SCIENCES POLITIQUES  (10 concepts)
# ══════════════════════════════════════════════════════════════════════

CURRICULUM.update({

    "m7_c1_etat_souverainete": {
        "module": 7, "ordre": 1,
        "titre": "L'État et la Souveraineté",
        "prereqs": [],
        "texte": """
L'ÉTAT : entité politique avec un territoire délimité, une population, un gouvernement souverain.
Weber : l'État détient le monopole de la violence légitime sur son territoire.
SOUVERAINETÉ : pouvoir suprême d'un État sur son territoire, interne et externe.
Souveraineté WESTPHALIENNE (1648) : principe de non-ingérence dans les affaires intérieures.
Remise en question par : droit d'ingérence humanitaire, mondialisation, institutions supranationales.
État FAILLI (failed state) : incapable d'exercer ses fonctions de base (sécurité, ordre, services).
La légitimité de l'État repose sur le consentement des gouvernés (Locke) ou la légalité-rationalité (Weber).
        """.strip(),
    },

    "m7_c2_regimes_politiques": {
        "module": 7, "ordre": 2,
        "titre": "Régimes Politiques",
        "prereqs": ["m7_c1_etat_souverainete"],
        "texte": """
DÉMOCRATIE LIBÉRALE : élections libres, séparation des pouvoirs, État de droit, droits fondamentaux.
Sous-types : parlementaire (Canada, UK), présidentiel (USA), semi-présidentiel (France).
AUTOCRATIE : pouvoir concentré, absence de contraintes institutionnelles effectives.
Sous-types : dictature militaire, parti unique (Chine), monarchie absolue.
RÉGIMES HYBRIDES (illiberal democracies) : élections tenues mais biaisées, institutions affaiblies.
Indice de démocratie (EIU, V-Dem) : recul démocratique global depuis 2016.
THÉORIE DE LA MODERNISATION : développement économique favorise la démocratisation (Lipset 1959).
Critique : Chine, Singapour — richesse sans démocratie libérale.
        """.strip(),
    },

    "m7_c3_systemes_electoraux": {
        "module": 7, "ordre": 3,
        "titre": "Systèmes Électoraux",
        "prereqs": ["m7_c2_regimes_politiques"],
        "texte": """
SCRUTIN MAJORITAIRE UNINOMINAL à un tour (SMUT) : Canada, UK. Le candidat avec le plus de voix gagne.
Produit des gouvernements majoritaires stables, mais mal représentatifs (vote stratégique, partis forts).
REPRÉSENTATION PROPORTIONNELLE (RP) : sièges proportionnels aux votes. Pays-Bas, Scandinavie.
Plus représentative, mais coalitions instables fréquentes.
SCRUTIN À DEUX TOURS : France. Si aucun candidat n'obtient la majorité au 1er tour, second tour.
VOTE ALTERNATIF (AV) : Australie. Classement préférentiel des candidats.
Loi de Duverger : le SMUT tend vers un bipartisme. La RP favorise le multipartisme.
Au Canada : débat sur la réforme électorale (référendums en CB et Ontario ont rejeté la RP).
        """.strip(),
    },

    "m7_c4_ideologies": {
        "module": 7, "ordre": 4,
        "titre": "Idéologies Politiques",
        "prereqs": ["m7_c2_regimes_politiques"],
        "texte": """
LIBÉRALISME : liberté individuelle, marchés libres, État de droit, droits civils (Locke, Mill).
Libéralisme CLASSIQUE (droite libérale) vs libéralisme SOCIAL (gauche libérale — intervention de l'État).
CONSERVATISME : prudence envers le changement, traditions, ordre social, institutions établies (Burke).
SOCIALISME : propriété collective des moyens de production, réduction des inégalités.
Sous-types : social-démocratie (réforme graduelle) vs socialisme révolutionnaire (Marx).
NATIONALISME : primauté de la nation. Civique (citoyenneté) vs ethnique (ascendance).
POPULISME : le «peuple pur» contre l'«élite corrompue». Peut être de gauche ou de droite.
La distinction gauche-droite est multidimensionnelle : économique + culturelle (GAL-TAN).
        """.strip(),
    },

    "m7_c5_relations_internationales": {
        "module": 7, "ordre": 5,
        "titre": "Relations Internationales",
        "prereqs": ["m7_c1_etat_souverainete"],
        "texte": """
RÉALISME : les États sont acteurs rationnels dans un système anarchique. Priorité à la survie et la puissance.
Dilemme de sécurité : les renforcements défensifs d'un État menacent ses voisins → course aux armements.
LIBÉRALISME : coopération possible via institutions (ONU, OMC), interdépendance économique réduit les guerres.
Paix démocratique : les démocraties ne se font pas la guerre entre elles (Kant, Doyle).
CONSTRUCTIVISME : les identités et les normes sociales façonnent les intérêts des États (Wendt).
PUISSANCE DOUCE (Nye) : influence par l'attraction culturelle, les valeurs, la diplomatie (vs puissance dure).
Ordre international LIBÉRAL : institutions multilatérales post-1945. En crise depuis 2016.
        """.strip(),
    },

    "m7_c6_geopolitique": {
        "module": 7, "ordre": 6,
        "titre": "Géopolitique et Grandes Puissances",
        "prereqs": ["m7_c5_relations_internationales"],
        "texte": """
GÉOPOLITIQUE : influence de la géographie sur la politique étrangère et la stratégie.
Heartland (Mackinder 1904) : qui contrôle l'Eurasie centrale contrôle le monde.
Rimland (Spykman) : les côtes et les mers périphériques sont la clé stratégique.
GUERRE FROIDE (1947-1991) : bipolarité USA-URSS. Dissuasion nucléaire (MAD). Proxy wars.
Moment UNIPOLAIRE (1991-2008) : hégémonie américaine. Expansion OTAN. Mondialisation.
MULTIPOLARITÉ émergente : montée de la Chine, affirmation de la Russie, Inde, etc.
Compétition sino-américaine : économique (tarifs, technologie), militaire (mer de Chine), normative.
        """.strip(),
    },

    "m7_c7_economie_politique": {
        "module": 7, "ordre": 7,
        "titre": "Économie Politique Internationale",
        "prereqs": ["m7_c5_relations_internationales", "m7_c4_ideologies"],
        "texte": """
MERCANTILISME : l'État doit maximiser les exportations et accumuler des réserves. Commerce = somme nulle.
LIBRE-ÉCHANGE : avantage comparatif (Ricardo). Commerce est à somme positive. Fondement de l'OMC.
CONSENSUS DE WASHINGTON (années 1980-90) : privatisation, déréglementation, austérité, FMI/Banque mondiale.
Critiquez comme facteur d'inégalités dans les pays en développement.
MONDIALISATION : intégration des marchés de biens, capitaux, travail. Réduit la pauvreté globale,
augmente les inégalités internes dans les pays riches.
Chaînes d'approvisionnement mondiales : efficaces mais fragiles (COVID-19, guerre en Ukraine).
DÉDOLLARISATION : tentatives de réduire la dépendance au dollar américain (BRICS, yuan digital).
        """.strip(),
    },

    "m7_c8_institutions_internationales": {
        "module": 7, "ordre": 8,
        "titre": "Institutions Internationales",
        "prereqs": ["m7_c5_relations_internationales"],
        "texte": """
ONU (1945) : maintien de la paix, droits humains, développement. Conseil de sécurité : 5 membres permanents avec droit de veto.
Limite : le veto paralyse souvent l'action face aux conflits impliquant les grandes puissances.
OMC : libéralisation du commerce, règlement des différends. 164 membres.
FMI : stabilité du système monétaire international, prêts conditionnels aux États en difficulté.
OTAN : alliance militaire défensive. Article 5 : attaque contre un = attaque contre tous.
UE : intégration économique et politique la plus avancée. Marché unique, euro, Parlement élu.
Institutions régionales : ASEAN, UA, Mercosur, OEA.
Critique réaliste : les institutions ne contraignent les grandes puissances que quand c'est dans leur intérêt.
        """.strip(),
    },

    "m7_c9_democratie_defis": {
        "module": 7, "ordre": 9,
        "titre": "Défis de la Démocratie Contemporaine",
        "prereqs": ["m7_c2_regimes_politiques", "m7_c4_ideologies"],
        "texte": """
POLARISATION POLITIQUE : creusement du fossé entre partis et électeurs. USA, Europe.
Causes : tri géographique, médias sociaux, inégalités économiques.
DÉSINFORMATION : diffusion massive de fausses nouvelles. Impact sur les élections (2016).
Contre-mesures : vérification des faits, réglementation des plateformes, littératie médiatique.
CRISE DE REPRÉSENTATION : sentiment que les élites politiques ne représentent pas le peuple.
Montée des partis populistes : Trumpisme, partis d'extrême droite en Europe, Bolsonaro.
TECHNOCRATIE vs DÉMOCRATIE : décisions complexes (politique monétaire, IA) confiées à des experts.
DÉMOCRATIE ILLIBÉRALE : Orbán (Hongrie), Erdoğan (Turquie) — élu mais affaiblit les contre-pouvoirs.
        """.strip(),
    },

    "m7_c10_politique_canadienne": {
        "module": 7, "ordre": 10,
        "titre": "Système Politique Canadien",
        "prereqs": ["m7_c3_systemes_electoraux", "m7_c2_regimes_politiques"],
        "texte": """
MONARCHIE CONSTITUTIONNELLE PARLEMENTAIRE : souverain symbolique, Premier ministre détient le pouvoir.
Gouverneur général : représente la Couronne. Rôle largement cérémonial.
FÉDÉRALISME : compétences partagées entre fédéral et provinces. Santé, éducation = provinces.
Accord de Charlottetown (1992) rejeté. Loi de clarté (2000) après le référendum québécois de 1995 (50,58%).
SYSTÈME DE WESTMINSTER : gouvernement responsable devant la Chambre des communes.
Partis principaux : Libéral, Conservateur, NPD, Bloc québécois, Vert.
Sénat : non élu, théoriquement chambre de «sober second thought». Réformes partielles depuis 2016.
Charte canadienne des droits et libertés (1982) : protège les droits fondamentaux,
soumis à la clause dérogatoire (notwithstanding clause, art. 33).
        """.strip(),
    },
})


# ══════════════════════════════════════════════════════════════════════
# MODULE 8 — INFORMATIQUE  (10 concepts)
# ══════════════════════════════════════════════════════════════════════

CURRICULUM.update({

    "m8_c1_binaire_representation": {
        "module": 8, "ordre": 1,
        "titre": "Représentation Binaire et Systèmes de Numération",
        "prereqs": [],
        "texte": """
Le binaire (base 2) est le langage fondamental des ordinateurs : 0 et 1 (bits).
Bit → Octet (byte) = 8 bits → Ko → Mo → Go → To.
Conversions : binaire → décimal (10110₂ = 22₁₀), décimal → binaire (division successive par 2).
HEXADÉCIMAL (base 16) : 0-9 puis A-F. Compact pour représenter des adresses mémoire.
Représentation des nombres négatifs : complément à deux.
Représentation des flottants : IEEE 754. Erreurs d'arrondi (0.1 + 0.2 ≠ 0.3 en binaire).
ASCII puis UNICODE (UTF-8) pour les caractères. Emoji : jusqu'à 4 octets en UTF-8.
        """.strip(),
    },

    "m8_c2_algorithmes_complexite": {
        "module": 8, "ordre": 2,
        "titre": "Algorithmes et Complexité (Big-O)",
        "prereqs": ["m8_c1_binaire_representation"],
        "texte": """
ALGORITHME : suite finie d'instructions pour résoudre un problème.
COMPLEXITÉ TEMPORELLE : comment le temps d'exécution croit avec la taille de l'entrée n.
Notation Big-O : O(1) constant, O(log n) logarithmique, O(n) linéaire,
O(n log n) quasi-linéaire, O(n²) quadratique, O(2ⁿ) exponentiel.
Exemple : chercher un élément dans une liste non triée = O(n). Dans une liste triée (recherche binaire) = O(log n).
COMPLEXITÉ SPATIALE : mémoire utilisée. Souvent un compromis espace/temps.
Problèmes P vs NP : P = résolubles efficacement. NP = vérifiables efficacement.
Le problème du voyageur de commerce est NP-dur — pas d'algorithme polynomial connu.
        """.strip(),
    },

    "m8_c3_structures_donnees": {
        "module": 8, "ordre": 3,
        "titre": "Structures de Données Fondamentales",
        "prereqs": ["m8_c2_algorithmes_complexite"],
        "texte": """
TABLEAU (array) : accès O(1) par index, insertion/suppression O(n).
LISTE CHAÎNÉE : insertion O(1) en tête, accès O(n).
PILE (stack) : LIFO. Opérations : push, pop. Usage : appels de fonctions, undo.
FILE (queue) : FIFO. Usage : file d'attente, BFS.
ARBRE BINAIRE : chaque nœud a 0-2 enfants. BST : nœud gauche < nœud < nœud droit.
ARBRE ÉQUILIBRÉ (AVL, Rouge-Noir) : recherche/insertion/suppression O(log n).
TABLE DE HACHAGE (hash map) : paires clé-valeur. Accès O(1) en moyenne. Collisions gérées.
GRAPHE : nœuds + arêtes. Orienté ou non, pondéré ou non. Base de Google Maps, réseaux sociaux.
        """.strip(),
    },

    "m8_c4_programmation_objet": {
        "module": 8, "ordre": 4,
        "titre": "Programmation Orientée Objet",
        "prereqs": ["m8_c2_algorithmes_complexite"],
        "texte": """
POO : organise le code autour d'OBJETS qui combinent données (attributs) et comportements (méthodes).
CLASSE : modèle/gabarit. OBJET : instance d'une classe.
Quatre piliers : ENCAPSULATION (cacher l'état interne), HÉRITAGE (partager le code entre classes),
POLYMORPHISME (même interface, comportements différents), ABSTRACTION (exposer l'essentiel).
Python, Java, C++, C# sont des langages orientés objet.
PRINCIPES SOLID : Single responsibility, Open/closed, Liskov substitution,
Interface segregation, Dependency inversion.
Alternatives : programmation fonctionnelle (Haskell, Erlang), procédurale (C).
        """.strip(),
    },

    "m8_c5_bases_donnees": {
        "module": 8, "ordre": 5,
        "titre": "Bases de Données Relationnelles et SQL",
        "prereqs": ["m8_c3_structures_donnees"],
        "texte": """
Base de données RELATIONNELLE : données organisées en tables (lignes = enregistrements, colonnes = attributs).
NORMALISATION : éliminer la redondance. 1NF, 2NF, 3NF. Clés primaires et étrangères.
SQL (Structured Query Language) : SELECT, INSERT, UPDATE, DELETE, JOIN.
JOIN : INNER (intersection), LEFT (tout de gauche + correspondances), FULL OUTER.
Transactions ACID : Atomicité, Cohérence, Isolation, Durabilité.
Bases NoSQL : MongoDB (documents JSON), Redis (clé-valeur), Neo4j (graphes).
Utile quand le schéma est flexible, les données sont massives, ou la structure est hiérarchique.
SQLite : base de données légère dans un fichier — utilisée par Scientia.
        """.strip(),
    },

    "m8_c6_reseaux_protocoles": {
        "module": 8, "ordre": 6,
        "titre": "Réseaux et Protocoles Internet",
        "prereqs": ["m8_c1_binaire_representation"],
        "texte": """
Modèle OSI : 7 couches (physique, liaison, réseau, transport, session, présentation, application).
TCP/IP : protocole fondamental d'Internet. TCP (fiable, ordonné) vs UDP (rapide, sans garantie).
ADRESSE IP : IPv4 (32 bits, ex : 192.168.1.1), IPv6 (128 bits).
DNS : traduit les noms de domaine en adresses IP.
HTTP/HTTPS : protocole du web. HTTPS = HTTP + chiffrement TLS.
REST API : architecture web basée sur HTTP. Verbes : GET, POST, PUT, DELETE.
WebSocket : connexion bidirectionnelle persistante. Utile pour le streaming (ex : réponses IA).
Latence vs bande passante : la latence (délai aller-retour) est souvent le facteur limitant.
        """.strip(),
    },

    "m8_c7_systemes_exploitation": {
        "module": 8, "ordre": 7,
        "titre": "Systèmes d'Exploitation",
        "prereqs": ["m8_c3_structures_donnees"],
        "texte": """
Le système d'exploitation (OS) gère les ressources matérielles et fournit des services aux applications.
PROCESSUS : programme en cours d'exécution. Chaque processus a son espace mémoire.
THREAD : unité légère d'exécution dans un processus. Partage la mémoire du processus parent.
CONCURRENCE vs PARALLÉLISME : concurrence = gérer plusieurs tâches (alternance), parallélisme = simultanéité réelle (multi-cœurs).
MÉMOIRE VIRTUELLE : chaque processus voit un espace d'adressage complet. Pagination.
SYSTÈME DE FICHIERS : NTFS (Windows), ext4 (Linux), APFS (macOS).
Ordonnancement (scheduling) : comment l'OS alloue le CPU aux processus. Round-robin, priorités.
Unix/Linux : tout est fichier. Shell, pipes, permissions (chmod).
        """.strip(),
    },

    "m8_c8_apprentissage_machine": {
        "module": 8, "ordre": 8,
        "titre": "Intelligence Artificielle et Apprentissage Machine",
        "prereqs": ["m8_c5_bases_donnees", "m8_c2_algorithmes_complexite"],
        "texte": """
IA TRADITIONNELLE : règles codées explicitement. Expert systems.
APPRENTISSAGE MACHINE (ML) : le modèle apprend des patterns à partir de données.
Supervisé : données étiquetées. Classification (spam/non-spam), régression (prédire un prix).
Non supervisé : pas d'étiquettes. Clustering (k-means), réduction de dimensionnalité (PCA).
Par renforcement : l'agent apprend par essais-erreurs avec récompenses.
RÉSEAU DE NEURONES : inspiré du cerveau. Couches d'entrée, cachées, sortie.
Apprentissage PROFOND (deep learning) : nombreuses couches cachées. GPT, diffusion models.
OVERFITTING : modèle qui mémorise les données d'entraînement mais généralise mal.
Régularisation, validation croisée, early stopping pour éviter l'overfitting.
        """.strip(),
    },

    "m8_c9_securite_informatique": {
        "module": 8, "ordre": 9,
        "titre": "Sécurité Informatique",
        "prereqs": ["m8_c6_reseaux_protocoles"],
        "texte": """
CIA Triad : Confidentialité, Intégrité, Disponibilité.
CHIFFREMENT SYMÉTRIQUE : même clé pour chiffrer et déchiffrer (AES). Rapide. Pb : distribution des clés.
CHIFFREMENT ASYMÉTRIQUE : clé publique (chiffre) + clé privée (déchiffre). RSA, ECC.
TLS : utilise les deux. Asymétrique pour l'échange de clé, symétrique pour les données.
HACHAGE : fonction unidirectionnelle (SHA-256). Stockage des mots de passe (+ sel).
ATTAQUES COURANTES : phishing, injection SQL, XSS, CSRF, man-in-the-middle, ransomware.
Authentification : MFA (multi-facteur) fortement recommandée. Mots de passe uniques + gestionnaire.
ZERO TRUST : ne faire confiance à aucun réseau, même interne. Vérifier tout, tout le temps.
        """.strip(),
    },

    "m8_c10_dev_web_api": {
        "module": 8, "ordre": 10,
        "titre": "Développement Web et APIs",
        "prereqs": ["m8_c6_reseaux_protocoles", "m8_c4_programmation_objet"],
        "texte": """
FRONTEND : ce que l'utilisateur voit. HTML (structure), CSS (style), JavaScript (interactivité).
Frameworks frontend : React, Vue, Angular. Composants réutilisables, état géré.
BACKEND : serveur + logique métier + base de données.
Frameworks backend : FastAPI (Python), Express (Node.js), Django, Rails.
API REST : interface standard pour communiquer entre frontend/backend/services.
JSON : format d'échange de données léger. Clés-valeurs, tableaux.
DÉPLOIEMENT : containerisation (Docker), orchestration (Kubernetes), PaaS (Railway, Heroku, Vercel).
CI/CD : intégration continue (tests automatiques) + déploiement continu. GitHub Actions.
Architecture microservices vs monolithique : compromis entre complexité et scalabilité.
        """.strip(),
    },
})


# ══════════════════════════════════════════════════════════════════════
# MODULE 9 — FINANCES  (10 concepts)
# ══════════════════════════════════════════════════════════════════════

CURRICULUM.update({

    "m9_c1_valeur_temps": {
        "module": 9, "ordre": 1,
        "titre": "Valeur Temps de l'Argent",
        "prereqs": [],
        "texte": """
1$ aujourd'hui vaut plus que 1$ demain : il peut être investi et générer des rendements.
VALEUR FUTURE : FV = PV × (1 + r)ⁿ. Ex : 10 000$ à 8%/an pendant 10 ans = 21 589$.
VALEUR ACTUELLE : PV = FV / (1 + r)ⁿ. Actualisation des flux futurs.
TAUX D'ACTUALISATION : reflète le coût d'opportunité et le risque.
ANNUITÉ : série de paiements égaux à intervalles réguliers. Hypothèque, cotisations REER.
Règle de 72 : 72 / taux = nombre d'années pour doubler. À 8% → ~9 ans.
L'inflation érode la valeur réelle de l'argent : rendement RÉEL = rendement nominal - inflation.
        """.strip(),
    },

    "m9_c2_marches_financiers": {
        "module": 9, "ordre": 2,
        "titre": "Marchés Financiers et Instruments",
        "prereqs": ["m9_c1_valeur_temps"],
        "texte": """
MARCHÉS PRIMAIRES : émission de nouveaux titres (IPO). MARCHÉS SECONDAIRES : échange entre investisseurs.
ACTIONS : part de propriété d'une entreprise. Rendement = dividendes + plus-value.
OBLIGATIONS : prêt à l'émetteur. Taux fixe, duration, sensibilité aux taux d'intérêt.
Prix obligation ↑ quand taux d'intérêt ↓ (relation inverse). Duration = sensibilité.
FONDS NÉGOCIÉS EN BOURSE (ETF) : panier d'actifs, frais bas, liquidité intraday.
MATIÈRES PREMIÈRES : or, pétrole, blé. Hedge contre l'inflation, volatilité élevée.
DEVISES (FOREX) : paire EUR/USD. Volume quotidien : 7 000 milliards USD.
MARCHÉS DÉRIVÉS : options, contrats à terme — permettent la couverture et la spéculation.
        """.strip(),
    },

    "m9_c3_options": {
        "module": 9, "ordre": 3,
        "titre": "Options et Stratégies (Covered Calls)",
        "prereqs": ["m9_c2_marches_financiers"],
        "texte": """
OPTION CALL : droit d'ACHETER 100 actions à un prix fixe (strike) avant une date (expiration).
OPTION PUT : droit de VENDRE 100 actions au strike avant l'expiration.
PRIME : prix payé par l'acheteur. Déterminée par : intrinsèque + valeur temps.
Greeks : Delta (sensibilité au prix), Theta (décroissance temporelle), Vega (volatilité), Gamma.
Theta est positif pour le vendeur : la prime perd de la valeur chaque jour qui passe.
COVERED CALL : posséder l'action + vendre un call. Génère un revenu (prime) au prix d'un plafond de gain.
Stratégie de Charles : vente de covered calls sur MSTR pour générer des revenus réguliers.
ROLL : racheter l'option avant expiration et en vendre une nouvelle plus lointaine.
Risque principal : l'action monte fortement au-dessus du strike → profit plafonné.
        """.strip(),
    },

    "m9_c4_theorie_portefeuille": {
        "module": 9, "ordre": 4,
        "titre": "Théorie Moderne du Portefeuille",
        "prereqs": ["m9_c2_marches_financiers"],
        "texte": """
Markowitz (1952) : la diversification réduit le risque sans sacrifier le rendement espéré.
RISQUE SYSTÉMATIQUE (β) : non diversifiable. Lié aux mouvements du marché global.
RISQUE SPÉCIFIQUE : propre à l'entreprise. Diversifiable.
FRONTIÈRE EFFICIENTE : ensemble des portefeuilles offrant le meilleur rendement pour un risque donné.
CAPM (Capital Asset Pricing Model) : E(r) = rf + β × (E(rm) − rf). Relation risque-rendement.
Sharpe Ratio : (rendement − taux sans risque) / volatilité. Mesure le rendement ajusté au risque.
CORRÉLATION des actifs : clé de la diversification. Actifs corrélés à -1 = diversification parfaite.
Critique : hypothèse de distributions normales. Les marchés ont des queues épaisses (kurtosis élevé).
        """.strip(),
    },

    "m9_c5_analyse_fondamentale": {
        "module": 9, "ordre": 5,
        "titre": "Analyse Fondamentale",
        "prereqs": ["m9_c2_marches_financiers"],
        "texte": """
L'analyse fondamentale vise à estimer la valeur intrinsèque d'une action.
Ratios clés : P/E (prix/bénéfice), P/B (prix/valeur comptable), EV/EBITDA, rendement dividende.
DCF (Discounted Cash Flow) : actualiser les flux de trésorerie futurs au coût du capital.
Valeur intrinsèque > prix → sous-évalué (opportunité). Valeur < prix → surévalué.
ANALYSE DU SECTEUR : PEST (politique, économique, social, technologique), forces de Porter.
Éléments qualitatifs : avantage concurrentiel (moat), management, qualité des bénéfices.
Warren Buffett/Graham : investissement dans la valeur. Marge de sécurité.
Limite : les prévisions de flux futurs sont très incertaines. Petit changement du taux → grand impact.
        """.strip(),
    },

    "m9_c6_analyse_technique": {
        "module": 9, "ordre": 6,
        "titre": "Analyse Technique",
        "prereqs": ["m9_c2_marches_financiers"],
        "texte": """
L'analyse technique prédit les prix futurs à partir des prix et volumes passés.
SUPPORT : niveau de prix où la demande est forte (plancher). RÉSISTANCE : niveau de plafond.
Moyennes mobiles : MM20 (court terme), MM200 (long terme). Croisement → signal.
RSI (Relative Strength Index) : mesure la vitesse des variations de prix. >70 suracheté, <30 survendu.
MACD : croisement de deux moyennes mobiles exponentielles. Signal d'achat/vente.
Bandes de Bollinger : MM ± 2 écarts-types. Identifie la volatilité et les extrêmes.
CHANDELIERS JAPONAIS : open, high, low, close. Doji, marteau, étoile du matin.
Efficience des marchés (EMH) : les prix reflètent déjà toute l'information. Si vrai, AT est inutile.
Débat empirique : momentum (force) et mean-reversion sont documentés mais difficiles à exploiter.
        """.strip(),
    },

    "m9_c7_fiscalite_canadienne": {
        "module": 9, "ordre": 7,
        "titre": "Fiscalité des Investissements au Canada",
        "prereqs": ["m9_c2_marches_financiers"],
        "texte": """
CELI (Compte d'Épargne Libre d'Impôt) : cotisations après impôt, croissance et retraits NON imposables.
Droits de cotisation 2024 : 95 000$ cumulatifs (depuis 2009). Réinitialisation chaque 1er janvier.
REER : cotisations déductibles du revenu imposable, imposition au retrait.
REEE : épargne-études. Subvention fédérale 20% jusqu'à 500$/an (SCEE).
COMPTE CORPORATIF : les gains en capital sont imposés à 50% (inclusion). Dividendes inter-corporatifs souvent exonérés.
GAIN EN CAPITAL : réalisé seulement lors de la vente. Inclusion = 50% imposable. Stratégie de report.
Règle des 30 jours (superficial loss) : ne pas racheter un titre vendu à perte dans les 30 jours.
Options dans le CELI : permises mais risquées — l'ARC surveille les activités de trading actif.
        """.strip(),
    },

    "m9_c8_crypto": {
        "module": 9, "ordre": 8,
        "titre": "Cryptomonnaies et Actifs Numériques",
        "prereqs": ["m9_c2_marches_financiers", "m8_c9_securite_informatique"],
        "texte": """
BITCOIN (2009, Satoshi Nakamoto) : argent numérique pair-à-pair sans tiers de confiance.
BLOCKCHAIN : registre distribué et immuable. Chaque bloc contient des transactions + hash du bloc précédent.
PROOF OF WORK : les mineurs résolvent des problèmes cryptographiques pour valider les blocs. Énergivore.
PROOF OF STAKE (Ethereum, Cardano) : validateurs qui mettent des actifs en garantie. Plus efficace.
DeFi (Finance Décentralisée) : protocoles financiers sur blockchain (prêts, échanges) sans intermédiaires.
NFT (Non-Fungible Token) : actif numérique unique sur blockchain. Droits de propriété contestés.
Risques : volatilité extrême, hacks d'exchanges, fraudes, réglementation incertaine.
ETF Bitcoin (IBIT) : accès indirect via un compte de courtage traditionnel (ex : CELI).
MSTR (MicroStrategy/Strategy) : société qui détient Bitcoin comme actif principal. Proxy Bitcoin.
        """.strip(),
    },

    "m9_c9_psychologie_investissement": {
        "module": 9, "ordre": 9,
        "titre": "Psychologie et Biais Cognitifs en Investissement",
        "prereqs": ["m9_c4_theorie_portefeuille"],
        "texte": """
AVERSION À LA PERTE (Kahneman & Tversky) : une perte de 100$ fait plus mal qu'un gain de 100$ fait plaisir.
Ratio douleur/plaisir ≈ 2:1. Conduit à vendre trop tôt les gains et garder trop longtemps les pertes.
BIAIS DE CONFIRMATION : chercher les informations qui confirment notre thèse. Filtrer les contradictions.
EFFET DE DISPOSITION : vendre les gagnants trop tôt, garder les perdants trop longtemps.
EXCÈS DE CONFIANCE : surestimer sa capacité à prédire les marchés. Très fréquent chez les traders actifs.
BIAIS DE RÉCENCE : surpondérer les événements récents. Acheter au sommet, vendre au creux.
ANCRAGE : s'accrocher à un prix de référence (prix d'achat, sommet historique).
Solutions : règles systématiques (rebalancement), journal de trading, investissement passif.
        """.strip(),
    },

    "m9_c10_gestion_risque": {
        "module": 9, "ordre": 10,
        "titre": "Gestion du Risque et Dimensionnement de Position",
        "prereqs": ["m9_c3_options", "m9_c4_theorie_portefeuille", "m9_c9_psychologie_investissement"],
        "texte": """
RISQUE DE MARCHÉ : perte due aux mouvements des prix. VOLATILITÉ (σ annualisée) comme mesure proxy.
VaR (Value at Risk) : perte maximale estimée sur une période donnée avec un niveau de confiance.
Ex : VaR 95% sur 1 jour = 10 000$ signifie 5% de chances de perdre plus de 10 000$ en un jour.
KELLY CRITERION : f* = (bp - q) / b. Taille optimale de la mise en fonction du edge et de la cote.
b = odds net, p = probabilité de gain, q = 1 - p. Souvent utilisé à 1/2 ou 1/4 Kelly pour réduire la volatilité.
STOP-LOSS : niveau de prix où on coupe automatiquement la perte. Discipline vs flexibilité.
DIVERSIFICATION temporelle : DCA (Dollar Cost Averaging) — investir régulièrement lisse les points d'entrée.
Risque de CONCENTRATION : Charles a une forte exposition à MSTR/Bitcoin. Covered calls = gestion partielle.
Risque de LIQUIDITÉ : ne pas pouvoir vendre rapidement sans impacter le prix. Options sur actifs peu liquides.
        """.strip(),
    },
})


# ══════════════════════════════════════════════════════════════════════
# MODULE 7 — SCIENCES POLITIQUES : France et États-Unis  (4 concepts supplémentaires)
# ══════════════════════════════════════════════════════════════════════

CURRICULUM.update({

    "m7_c11_ve_republique": {
        "module": 7, "ordre": 11,
        "titre": "La Ve République Française",
        "prereqs": ["m7_c2_regimes_politiques"],
        "texte": """
La Ve République (1958) a été conçue par de Gaulle pour mettre fin à l'instabilité de la IVe.
RÉGIME SEMI-PRÉSIDENTIEL : un président élu directement (depuis 1962, au suffrage universel direct)
avec des pouvoirs forts, ET un Premier ministre responsable devant l'Assemblée nationale.
Cohabitation : quand le président et le Premier ministre sont de partis opposés (1986-88, 1993-95, 1997-2002).
Le FAIT MAJORITAIRE : la discipline partisane à l'Assemblée concentre le pouvoir dans l'exécutif.
La COEXISTENCE ARTICLE 49-3 : le gouvernement peut engager sa responsabilité sur un texte de loi
pour le faire passer sans vote (usage controversé par Borne/Macron en 2023 sur la réforme des retraites).
CONSEIL CONSTITUTIONNEL : 9 membres, vérifie la constitutionnalité des lois. N'est pas une cour suprême au sens américain.
Spécificité française : la LAÏCITÉ — séparation État/religion ancrée depuis la loi de 1905.
        """.strip(),
    },

    "m7_c12_partis_france": {
        "module": 7, "ordre": 12,
        "titre": "Le Paysage Politique Français",
        "prereqs": ["m7_c11_ve_republique", "m7_c4_ideologies"],
        "texte": """
La France a connu une recomposition majeure depuis 2017.
GAUCHE : Parti Socialiste (PS, social-démocrate, affaibli), La France Insoumise (LFI, populisme de gauche, Mélenchon),
PCF (communiste, marginal), EELV (écologistes).
CENTRE : Renaissance (anciennement La République En Marche — Macron). MoDem (Bayrou). Tiers entre gauche et droite.
DROITE : Les Républicains (LR, gaullisme/droite classique, affaibli), Rassemblement National (RN, Le Pen —
montée en puissance constante depuis 2012, 1er parti en voix aux législatives 2022).
Clivage central actuel : Macronisme (centre libéral) vs RN (populisme nationaliste) vs gauche unie (NUPES/NFP).
La DÉDIABOLISATION du RN sous Marine Le Pen : abandon de la sortie de l'euro, discours normalisé.
Tension entre le modèle républicain universaliste et l'identitarisme.
        """.strip(),
    },

    "m7_c13_systeme_americain": {
        "module": 7, "ordre": 13,
        "titre": "Le Système Politique Américain",
        "prereqs": ["m7_c2_regimes_politiques", "m7_c3_systemes_electoraux"],
        "texte": """
PRÉSIDENTIALISME pur : séparation stricte des pouvoirs. Le président n'est pas responsable devant le Congrès.
Checks and balances : le Congrès vote les lois et le budget, le président peut y opposer son veto,
la Cour Suprême peut les annuler. Chaque branche contrôle les deux autres.
CONGRÈS bicaméral : Sénat (100 sénateurs, 2 par État, 6 ans) + Chambre des représentants (435 membres, 2 ans).
Le filibuster au Sénat : possibilité de bloquer un vote en parlant indéfiniment. Nécessite 60 voix pour y mettre fin.
COLLÈGE ÉLECTORAL : le président n'est pas élu au vote populaire direct. 538 grands électeurs.
Un candidat peut gagner la présidence en perdant le vote populaire (Bush 2000, Trump 2016).
COUR SUPRÊME : 9 juges nommés à vie. Décisions fondamentales : Roe v. Wade (annulé 2022), Citizens United (2010).
Bipartisme structurel (loi de Duverger + scrutin majoritaire) : Républicains vs Démocrates.
        """.strip(),
    },

    "m7_c14_polarisation_americaine": {
        "module": 7, "ordre": 14,
        "titre": "La Polarisation Politique Américaine",
        "prereqs": ["m7_c13_systeme_americain", "m7_c9_democratie_defis"],
        "texte": """
Depuis les années 1990, le fossé entre Républicains et Démocrates s'est creusé sur deux axes :
ÉCONOMIQUE : Républicains (baisses d'impôts, dérégulation) vs Démocrates (État-providence, droits sociaux).
CULTUREL : Républicains (tradionalisme, religion, nationalisme) vs Démocrates (progressisme, diversité, droit à l'avortement).
LE TRUMPISME : Donald Trump (2016, 2024) — populisme nationaliste, protectionnisme, scepticisme envers les institutions.
Sa base électorale : classes moyennes-blanches en déclin économique, évangéliques, rural vs urbain.
GERRYMANDERING : redécoupage des circonscriptions par le parti au pouvoir pour s'avantager. Validé partiellement par la Cour Suprême.
Primaires ouvertes : le système de primaires favorise les candidats extrêmes car les électeurs les plus partisans y participent.
LES SWING STATES : la présidentielle se joue dans ~7 États pivots (Wisconsin, Pennsylvanie, Michigan, Arizona, Nevada, Géorgie, Caroline du Nord).
Citizens United (2010) : décision de la Cour Suprême autorisant les dépenses illimitées en politique. Argent = expression politique.
        """.strip(),
    },
})


# ══════════════════════════════════════════════════════════════════════
# MODULE 10 — HISTOIRE : HISTORIONOMIE (Philippe Fabry)  (10 concepts)
# ══════════════════════════════════════════════════════════════════════

CURRICULUM.update({

    "m10_c1_definition_historionomie": {
        "module": 10, "ordre": 1,
        "titre": "L'Historionomie : Définition et Méthode",
        "prereqs": [],
        "texte": """
L'HISTORIONOMIE, terme forgé par Philippe Fabry (juriste et essayiste, né 1984), désigne
l'étude scientifique des lois régissant l'évolution historique des civilisations.

Elle se distingue de l'historiographie classique (récit des faits) en cherchant des LOIS RÉCURRENTES,
comparables à celles des sciences naturelles. La méthode : comparer rigoureusement les trajectoires
de plusieurs civilisations sur le long terme pour identifier des patterns répétables.

SOURCES INTELLECTUELLES : Polybe (anacyclosis — cycle des régimes politiques dans l'Antiquité),
Toynbee (cycles de civilisations), Braudel (longue durée), Kondratiev (cycles économiques longs).

POSTULAT CENTRAL : l'Histoire n'est pas un flux aléatoire d'événements mais obéit à des structures
profondes prévisibles. Les civilisations passent par des phases comparables de naissance, expansion,
apogée et déclin — indépendamment de leur culture spécifique.

LIMITES ET CRITIQUES : la méthode est contestée comme non-falsifiable (elle peut toujours trouver
une analogie qui convient), et accusée de déterminisme réducteur. Les historiens académiques
restent largement sceptiques.
        """.strip(),
    },

    "m10_c2_anacyclosis_polybe": {
        "module": 10, "ordre": 2,
        "titre": "L'Anacyclosis de Polybe",
        "prereqs": ["m10_c1_definition_historionomie"],
        "texte": """
POLYBE (200-118 av. J.-C.), historien grec, formule la théorie de l'ANACYCLOSIS dans ses
Histoires : les régimes politiques se succèdent selon un cycle inévitable.

Cycle de Polybe : Monarchie → Tyrannie → Aristocratie → Oligarchie → Démocratie → Ochlocratie (foule) → retour à la Monarchie.

Chaque régime contient en lui-même les germes de sa dégénérescence :
- La monarchie juste dégénère en tyrannie (pouvoir personnel arbitraire)
- L'aristocratie des meilleurs dégénère en oligarchie des riches
- La démocratie du peuple dégénère en ochlocratie (démagogie, populisme)

Pour Polybe, Rome a réussi à éviter ce cycle grâce à sa CONSTITUTION MIXTE (consul = monarchique,
Sénat = aristocratique, Assemblées = démocratique). C'est cette constitution qui fonde
l'Historionomie de Fabry : Rome a finalement succombé au cycle.

PERTINENCE CONTEMPORAINE : Fabry voit dans le populisme occidental actuel les signes d'une
transition vers la phase d'ochlocratie précédant la concentration du pouvoir.
        """.strip(),
    },

    "m10_c3_loi_republique_liberale": {
        "module": 10, "ordre": 3,
        "titre": "La Loi de la République Libérale",
        "prereqs": ["m10_c2_anacyclosis_polybe"],
        "texte": """
Fabry formule sa thèse centrale dans "Rome, du libéralisme au socialisme" (2014) :

TOUTE RÉPUBLIQUE LIBÉRALE suit une trajectoire prévisible en quatre phases :

1. PHASE LIBÉRALE (naissance) : fondation sur l'État de droit, liberté économique, égalité juridique.
   Les inégalités de résultats sont acceptées. Croissance forte, expansion de la puissance.
   Rome : de la fondation (-509) au IIe siècle av. J.-C.

2. PHASE DE CRISE SOCIALE : l'expansion crée des INÉGALITÉS CROISSANTES. Classe populaire appauvrie,
   classe dirigeante enrichie. Tensions politiques, demandes de redistribution.
   Rome : période des Gracques (-133 à -121), guerres civiles.

3. PHASE SOCIALISTE (interventionnisme) : l'État répond aux demandes redistributives.
   Distributions gratuites (panem et circenses), contrôle des prix, fiscalité lourde.
   Ce faisant, il concentre progressivement le pouvoir économique et politique.

4. PHASE IMPÉRIALE (concentration) : un HOMME PROVIDENTIEL incarne la volonté populaire
   contre les élites traditionnelles. La liberté formelle est préservée mais la substance est perdue.
   Rome : Jules César, puis Auguste — la République formelle persiste, l'Empire réel commence.
        """.strip(),
    },

    "m10_c4_rome_republique": {
        "module": 10, "ordre": 4,
        "titre": "Rome Républicaine : Archétype Libéral",
        "prereqs": ["m10_c3_loi_republique_liberale"],
        "texte": """
La Rome républicaine (-509 à -27) est pour Fabry l'archétype de la phase libérale.

FONDEMENTS JURIDIQUES : la Loi des XII Tables (-450) codifie les droits des citoyens contre
l'arbitraire des patriciens. La LIBERTAS romaine n'est pas la liberté abstraite des modernes
mais la protection contre le pouvoir arbitraire et la garantie du droit de propriété.

CONSTITUTION MIXTE (Polybe) : les deux consuls (monarchique), le Sénat (aristocratique),
les assemblées comices (démocratique). Les institutions limitent la concentration du pouvoir.

EXPANSION : cette fondation libérale génère une croissance économique et une puissance militaire
permettant la conquête de la Méditerranée. Les guerres puniques (-264 à -146) culminent
avec la destruction de Carthage.

INÉGALITÉS MONTANTES : la conquête enrichit les aristocrates et déplace les paysans. Le latifundium
(grande propriété) se développe. Tiberius et Caïus Gracchus (-133 et -121) tentent une réforme
agraire — ils sont assassinés. Pour Fabry, c'est le début de la crise de la République.
        """.strip(),
    },

    "m10_c5_chute_republique_rome": {
        "module": 10, "ordre": 5,
        "titre": "La Chute de la République et l'Empire",
        "prereqs": ["m10_c4_rome_republique"],
        "texte": """
La CRISE DE LA RÉPUBLIQUE (-133 à -27) illustre la loi de Fabry en action.

MARIUS ET SYLLA (-107 à -78) : réforme militaire (armée professionnelle — soldats liés au général,
pas à Rome), puis guerres civiles. Sylla impose sa dictature (-82 à -79) et restaure le Sénat,
mais le précédent est posé : l'armée peut faire l'histoire.

TRIUMVIRATS : César, Pompée, Crassus (60 av. J.-C.) — puis César, Octave, Antoine.
L'accumultion de pouvoirs informels contourne les institutions formelles.

JULES CÉSAR (-100 à -44) : figure de l'homme providentiel. Réformes sociales populaires
(distributions de grain, colonies de vétérans), pouvoir personnel absolu malgré le titre
de "dictateur temporaire". Son assassinat aux Ides de Mars (-44) ne restaure pas la République.

OCTAVE AUGUSTE (-27 à 14 ap. J.-C.) : PRINCIPAT — formellement, les institutions républicaines
subsistent (Sénat, consuls). En substance, Octave est le maître absolu. C'est le modèle
de la démocratie illibérale : les formes sans la substance.

Parallèle Fabry : la démocratie occidentale actuelle évolue vers ce modèle.
        """.strip(),
    },

    "m10_c6_declin_empire": {
        "module": 10, "ordre": 6,
        "titre": "Déclin et Chute de l'Empire Romain",
        "prereqs": ["m10_c5_chute_republique_rome"],
        "texte": """
La PHASE SOCIALISTE de l'Empire romain (selon Fabry) se manifeste par :

PANEM ET CIRCENSES : distributions gratuites de grain, jeux, spectacles. Clientélisme de masse.
FISCALITÉ CROISSANTE : pour financer l'armée et les distributions, les impôts augmentent.
Les provinces sont saignées. Les producteurs fuient le système (peasant flight).
DÉVALUATION MONÉTAIRE : réduction du titre en argent des pièces (de 90% à <5% entre le Ier et IIIe s.).
Équivalent antique de la planche à billets.
CONTRÔLE ÉCONOMIQUE : édit de Dioclétien (301) — contrôle des prix, corporatisme forcé, héréditarité
des métiers. Chaque artisan est lié à sa profession à vie.

CRISES DU IIIe SIÈCLE : 50 ans de guerres civiles, ~50 empereurs, invasions barbares.
L'État ne peut plus se financer ni défendre ses frontières.

CHUTE DE ROME (476 ap. J.-C.) : Odoacre dépose le dernier empereur d'Occident.
Pour Fabry, la chute est la conséquence directe du "socialisme impérial" qui a détruit
les bases économiques et institutionnelles de la puissance romaine.
        """.strip(),
    },

    "m10_c7_cycle_grece_europe": {
        "module": 10, "ordre": 7,
        "titre": "Cycle Grèce/Europe — Le Parallèle Civilisationnel",
        "prereqs": ["m10_c3_loi_republique_liberale"],
        "texte": """
Dans "Histoire du siècle à venir" (2015), Fabry propose quatre cycles parallèles :

CYCLE A (Grèce/Europe) : la Grèce antique des cités rivales (Athènes vs Sparte) est la matrice
de l'Europe moderne des États-nations rivaux. La Ligue achéenne = l'Union européenne.
La domination macédonienne (Philippe II, Alexandre) préfigure une future hégémonie européenne.

CYCLE B (Rome/États-Unis) : Rome (cité républicaine devenue empire universel) est l'archétype
des États-Unis. Les USA connaissent la même trajectoire : naissance libérale → expansion → crise sociale
→ populisme → concentration du pouvoir.

CYCLE C (Judaïsme/Islam) : le judaïsme antique face aux Grecs/Romains = l'islam face à l'Occident.
Tension entre monothéisme communautaire et ordre cosmopolite dominant.

CYCLE D (Assyro-Perses/Turcs-Ottoman) : puissances orientales défiées puis absorbées par les cycles A et B.

Ces cycles se croisent et interagissent. L'histoire mondiale n'est pas une ligne mais une superposition
de cycles à différentes vitesses (l'Europe est en avance sur les USA dans le cycle de déclin).
        """.strip(),
    },

    "m10_c8_usa_nouvelle_rome": {
        "module": 10, "ordre": 8,
        "titre": "Les États-Unis comme Nouvelle Rome",
        "prereqs": ["m10_c7_cycle_grece_europe", "m7_c13_systeme_americain"],
        "texte": """
Pour Fabry, les USA reproduisent la trajectoire de Rome avec ~2 000 ans de décalage.

PHASE LIBÉRALE (1776-1930) : fondation constitutionnelle (équivalent de la Loi des XII Tables),
expansion continentale puis mondiale, puissance industrielle. Inégalités acceptées (mythe du self-made man).

CRISE SOCIALE (New Deal à aujourd'hui) : le New Deal de Roosevelt (années 1930) = début de la phase
interventionniste. Montée des inégalités depuis 1970, désindustrialisation, polarisation.

TRUMPISME (2016-) : figure de l'homme providentiel populiste. Trump n'est pas une anomalie
pour Fabry, mais la manifestation prévisible de la loi de la République libérale.
"Le peuple contre les élites" = les populares romains contre les optimates.

PRÉDICTION HISTORIONOMIQUE : les USA évolueraient vers une forme de principat — un exécutif fort,
des institutions formellement préservées mais vidées de substance, un nouveau César.
Cette évolution prendrait plusieurs décennies.

Note critique : cette analogie est séduisante mais téléologique — elle force les faits dans
un cadre préconçu. Les différences institutionnelles (démocratie libérale, Cour Suprême,
fédéralisme fort) sont peut-être plus résistantes que Fabry ne le croit.
        """.strip(),
    },

    "m10_c9_predictions_historionomiques": {
        "module": 10, "ordre": 9,
        "titre": "Prédictions Historionomiques et Multipolarité",
        "prereqs": ["m10_c8_usa_nouvelle_rome", "m7_c6_geopolitique"],
        "texte": """
L'Historionomie n'est pas qu'une lecture du passé — elle formule des PRÉDICTIONS testables.

MULTIPOLARITÉ TRANSITOIRE : comme à la fin de la République romaine (multi-centres de pouvoir :
César, Pompée, Crassus, puis les triumvirats), nous vivons une phase multipolaire (USA, Chine, Russie, UE).
Cette multipolarité serait transitoire, précédant l'émergence d'un nouvel ordre unipolaire.

EMPIRE UNIVERSEL À VENIR : Fabry prédit l'émergence d'une puissance hégémonique dominante —
potentiellement les USA sous forme impériale, ou une autre puissance. Cela prendrait quelques décennies.

DÉCLIN EUROPÉEN : l'Europe (Cycle A, en avance dans le cycle) est plus proche du déclin que les USA.
Crise démographique, fragmentation, manque de souveraineté stratégique.

ISLAM ET OCCIDENT : la crise d'intégration de l'islam en Europe reproduit les tensions du
judaïsme hellénistique. Résolution possible : assimilation, séparation, ou conflit ouvert.

ÉVALUATION CRITIQUE : certaines prédictions de Fabry (montée du populisme, retrait américain
de la scène mondiale, résurgence nationaliste) ont été confirmées par les événements.
D'autres restent spéculatives. La valeur heuristique est réelle même si la rigueur scientifique
est discutable.
        """.strip(),
    },

    "m10_c10_critique_historionomie": {
        "module": 10, "ordre": 10,
        "titre": "Critique et Limites de l'Historionomie",
        "prereqs": ["m10_c9_predictions_historionomiques"],
        "texte": """
L'Historionomie soulève des problèmes méthodologiques importants que tout lecteur critique doit connaître.

PROBLÈME DE SÉLECTION DES CAS : Fabry choisit les civilisations qui confirment sa théorie.
Qu'en est-il des civilisations qui ne suivent pas le cycle prédit (Chine, civilisations africaines)?
Ce biais de confirmation est le principal point faible de la méthode.

ANALOGIES FORCÉES : les parallèles Rome/USA sont suggestifs mais approximatifs.
Les différences de contexte (technologies, économie mondialisée, armes nucléaires, démocratie
représentative institutionnalisée) pourraient rendre la trajectoire très différente.

TÉLÉOLOGIE : en partant du principe que la fin est connue (déclin, empire), Fabry risque
d'interpréter tout événement comme allant dans la direction prévue. C'est non-falsifiable.

VALEUR HEURISTIQUE RÉELLE : malgré ses limites, l'Historionomie force à une LONGUE DURÉE
de réflexion que l'actualisme (tout s'explique par le présent) ne permet pas.
Elle pose les bonnes questions : quels sont les cycles longs qui structurent notre moment historique?

CADRE COMPARATIF : à utiliser comme outil parmi d'autres — non comme vérité absolue.
Les historiens professionnels (Koselleck, Hartog, Ricœur) proposent des approches du temps
historique plus nuancées et méthodologiquement robustes.
        """.strip(),
    },
})


# ══════════════════════════════════════════════════════════════════════
# MODULE 11 — ANTIQUITÉ : GRÈCE & ROME  (36 concepts — 4 trimestres)
# Accent : histoire politique et militaire
# ══════════════════════════════════════════════════════════════════════

CURRICULUM.update({

    # ── TRIMESTRE 1 — Grèce archaïque et classique ────────────────────

    "m11_c1_polis": {
        "module": 11, "ordre": 1,
        "titre": "La Polis — La Cité-État Grecque",
        "prereqs": [],
        "texte": """
La POLIS (pluriel : poleis) est l'unité politique fondamentale du monde grec.
Elle n'est pas simplement une ville : c'est une communauté de citoyens souverains
qui partagent un territoire, des dieux, des lois et des institutions.

GÉOGRAPHIE ET FRAGMENTATION : le relief montagneux de la Grèce (peu de plaines,
nombreuses vallées isolées, milliers d'îles) favorise l'émergence de cités indépendantes
plutôt qu'un État unitaire. On dénombre plus de 1 000 poleis entre le VIIIe et le IIe s. av. J.-C.

STRUCTURE POLITIQUE TYPE : l'assemblée des citoyens (ekklèsia ou apella), un conseil
(boulè ou gérousia), des magistrats annuels (archontes, éphores, stratèges).
Les formes varient : oligarchie, tyrannie, démocratie, oligarchie militaire.

LE CITOYEN (politès) : seuls les hommes libres nés de père citoyen participent à la vie politique.
Les femmes, esclaves (souvent 1/3 de la population) et métèques (étrangers résidents) sont exclus.

RIVALITÉ INTER-CITÉS : les guerres entre poleis sont constantes. Absence d'un arbitre supérieur.
La Ligue de Délos et la Ligue du Péloponnèse sont les deux grandes alliances rivales.
Cette anarchie inter-étatique fait écho à la théorie réaliste des relations internationales (Thucydide).
        """.strip(),
    },

    "m11_c2_athenes_democratie": {
        "module": 11, "ordre": 2,
        "titre": "Athènes et la Démocratie",
        "prereqs": ["m11_c1_polis"],
        "texte": """
La démocratie athénienne est une invention politique sans précédent, construite en plusieurs étapes.

SOLON (-594) : réforme des dettes (seisachtheia — "secousse des fardeaux"), abolition de l'esclavage
pour dettes, organisation des citoyens en quatre classes censitaires. Pose les bases de l'égalité juridique.

CLISTHÈNE (-508) : véritable fondateur de la démocratie. Réorganise Athènes en 10 tribus artificielles
(mélangeant les régions pour briser les solidarités claniques), crée la boulè de 500 membres
(50 par tribu, tirés au sort), instaure l'OSTRACISME : un citoyen jugé dangereux pour la démocratie
peut être exilé 10 ans par vote de l'assemblée.

PÉRICLÈS (-461 à -429) : âge d'or. Généralisation du tirage au sort pour les magistratures,
indemnités pour la participation citoyenne (misthophorie — permet aux pauvres de participer),
construction du Parthénon, hégémonie athénienne via la Ligue de Délos.

LIMITES : démocratie directe mais réservée aux citoyens (~30 000 sur 300 000 habitants).
L'assemblée peut décider de guerre, d'alliance, de condamnation à mort.
Socrate sera condamné à mort par cette démocratie en -399.
        """.strip(),
    },

    "m11_c3_sparte": {
        "module": 11, "ordre": 3,
        "titre": "Sparte — Le Modèle Militaire",
        "prereqs": ["m11_c1_polis"],
        "texte": """
Sparte (Lacédémone) est l'antithèse politique et militaire d'Athènes.
Elle représente le modèle oligarchique militarisé poussé à l'extrême.

CONSTITUTION (attribuée à Lycurgue, vers -800) : système dualiste — deux rois simultanés
(dynasties des Agiades et Eurypontides), un Conseil des Anciens (gérousia — 28 citoyens
de plus de 60 ans + les deux rois), une Assemblée (apella — vote limité à l'acclamation),
et les cinq ÉPHORES élus annuellement qui exercent le contrôle réel du pouvoir.

CLASSES SOCIALES : Spartiates (homoioi — "les égaux" — citoyens guerriers), Périèques
(hommes libres non-citoyens, artisans et commerçants), HILOTES (serfs d'État, anciens habitants
vaincus, environ 7 pour 1 Spartiate — source constante de peur d'insurrection).

L'AGÔGÊ : formation militaire obligatoire pour tous les garçons spartiates de 7 à 30 ans.
Endurance physique, obéissance, résistance à la douleur, art de la guerre. Aucune place
pour le commerce, les arts ou la philosophie.

PUISSANCE MILITAIRE : la phalange spartiate est la force la plus redoutée du monde grec.
La kryptie (chasse ritualisée aux hilotes) entraîne aussi les jeunes guerriers.
Sparte résiste à toutes les tentatives de réforme démocratique — modèle de stabilité conservatrice.
        """.strip(),
    },

    "m11_c4_guerres_mediques": {
        "module": 11, "ordre": 4,
        "titre": "Les Guerres Médiques (490–479 av. J.-C.)",
        "prereqs": ["m11_c2_athenes_democratie", "m11_c3_sparte"],
        "texte": """
Les guerres médiques opposent l'Empire perse achéménide — la plus grande puissance du monde connu —
aux cités grecques. Leur issue définit le destin de l'Occident.

CONTEXTE : Darius Ier contrôle un empire de 50 millions d'habitants, de l'Indus à l'Égée.
Les cités grecques d'Ionie (côte turque actuelle), sous domination perse, se révoltent en -499.
Athènes envoie des navires en soutien. Darius décide de punir Athènes.

MARATHON (-490) : 10 000 Athéniens sous Miltiade battent 25 000 Perses.
Victoire surprise — la phalange hoplite charge en courant pour éviter les archers perses.
Phidippidès court 42 km jusqu'à Athènes annoncer la victoire (mythe fondateur du marathon).

THERMOPYLES (-480) : Xerxès I (fils de Darius) envahit avec 200 000 hommes (estimation haute).
300 Spartiates sous Léonidas et 7 000 alliés tiennent le défilé 3 jours. Trahison de Éphialtès.
Léonidas et ses 300 meurent jusqu'au dernier. Valeur militaire comme exemple politique.

SALAMINE (-480) : Thémistocle attire la flotte perse dans le détroit étroit de Salamine.
300 trières athéniennes contre 600+ perses — dans l'espace réduit, les Perses ne peuvent manœuvrer.
Victoire décisive. Xerxès regarde la défaite depuis son trône sur la colline.

PLATÉES (-479) : victoire terrestre finale. Les Perses ne reviendront jamais.
Conséquence : Athènes devient hégémon naval, fonde la Ligue de Délos, connaît son âge d'or.
        """.strip(),
    },

    "m11_c5_ligue_delos_empire": {
        "module": 11, "ordre": 5,
        "titre": "La Ligue de Délos — De l'Alliance à l'Empire",
        "prereqs": ["m11_c4_guerres_mediques"],
        "texte": """
La Ligue de Délos (-478) est fondée officiellement pour défense commune contre la Perse.
Elle devient rapidement l'instrument de la domination impériale athénienne.

STRUCTURE INITIALE : chaque cité membre contribue soit des navires, soit une cotisation financière
(phoros). Le trésor commun est déposé sur l'île sacrée de Délos. Athènes assure le commandement.

GLISSEMENT IMPÉRIAL : sous Périclès, le trésor est transféré à Athènes (-454).
Les cotisations augmentent. Les cités qui veulent quitter la Ligue sont contraintes de rester
par la force navale athénienne. L'alliance défensive devient un empire tributaire.

USAGE DES TRIBUTS : Périclès finance la reconstruction de l'Acropole (Parthénon, Propylées,
Érechthéion) avec les fonds de la Ligue. Scandale politique — les alliés financent la gloire d'Athènes.

RÉACTIONS : Sparte et ses alliés (Ligue du Péloponnèse) voient la montée en puissance athénienne
comme une menace existentielle. Thucydide l'analysera : "C'est la puissance grandissante d'Athènes,
et la peur qu'elle inspirait à Lacédémone, qui a rendu la guerre inévitable."

Ce mécanisme — alliance défensive transformée en empire par la logique du dilemme de sécurité —
est un archétype des relations internationales que Thucydide théorise 2 500 ans avant Waltz.
        """.strip(),
    },

    "m11_c6_guerre_peloponnese": {
        "module": 11, "ordre": 6,
        "titre": "La Guerre du Péloponnèse (431–404 av. J.-C.)",
        "prereqs": ["m11_c5_ligue_delos_empire"],
        "texte": """
La guerre du Péloponnèse est la guerre civile du monde grec — elle brise l'âge d'or athénien
et épuise les deux camps. Thucydide en fait l'analyse politique la plus pénétrante de l'Antiquité.

STRATÉGIE DE PÉRICLÈS : refuser le combat terrestre (Sparte est imbattable en rase campagne),
se replier derrière les Longs Murs, dominer par la mer, harceler les côtes péloponnésiennes.
Stratégie rationnelle — mais la GRANDE PESTE (-430 à -426) tue 1/4 à 1/3 de la population
d'Athènes, dont Périclès lui-même en -429.

DÉSASTRE DE SICILE (-415 à -413) : l'expédition de Sicile est la faute stratégique majeure.
Alcibiade convainc les Athéniens d'attaquer Syracuse, grande cité alliée de Sparte.
40 000 hommes, 200 navires — anéantis. La flotte détruite, les prisonniers mourant dans les carrières.
Thucydide : catastrophe résultant de la démagogie et du déficit de jugement stratégique.

SUITE DE LA GUERRE : Sparte accepte l'aide financière perse (ironique après les guerres médiques)
pour construire une flotte. Victoire navale d'Aegospotamos (-405). Capitulation d'Athènes (-404).

CONSÉQUENCES : Sparte impose les Trente Tyrans à Athènes. La démocratie est restaurée en -403
mais Athènes ne retrouvera jamais son hégémonie. Le monde grec entre dans une ère d'instabilité.
Hégémonie de Sparte (-404 à -371) → de Thèbes (-371 à -362) → vide de puissance.
        """.strip(),
    },

    "m11_c7_thebes_macedoine": {
        "module": 11, "ordre": 7,
        "titre": "Thèbes, la Macédoine et la Fin de l'Indépendance Grecque",
        "prereqs": ["m11_c6_guerre_peloponnese"],
        "texte": """
Après l'épuisement d'Athènes et de Sparte, deux puissances montantes vont dominer la Grèce.

HÉGÉMONIE THÉBAINE (-371 à -362) : Épaminondas révolutionne la tactique militaire.
À Leuctres (-371), il brise l'aura d'invincibilité spartiate. Innovation : le bataillon sacré
(150 paires d'amants — Platon : les hommes se battent mieux devant leurs bien-aimés)
et la tactique oblique — renforcer l'aile gauche pour frapper d'abord le point fort ennemi.
Sparte ne s'en remet jamais : la population spartiate passe de ~8 000 à ~1 000 homoioi.
Mort d'Épaminondas à Mantinée (-362) = fin de l'hégémonie thébaine.

PHILIPPE II DE MACÉDOINE (-359 à -336) : la vraie révolution militaire et politique du IVe siècle.
Réforme l'armée macédonienne : sarisse (lance de 5-7 m), phalange plus profonde, cavalerie lourde
(hétaïres — compagnons) en formation oblique inspirée d'Épaminondas.
Combine diplomatie, corruption et force militaire. Conquiert la Grèce progressivement.

CHÉRONÉE (-338) : victoire décisive sur la coalition athéno-thébaine.
Le jeune Alexandre (18 ans) commande la cavalerie qui brise le bataillon sacré de Thèbes.
Fin de l'indépendance politique des cités grecques. Philippe fonde la Ligue de Corinthe.
Assassiné en -336 — son fils Alexandre hérite d'une machine de guerre parfaite.
        """.strip(),
    },

    "m11_c8_alexandre": {
        "module": 11, "ordre": 8,
        "titre": "Alexandre le Grand — La Conquête du Monde (336–323 av. J.-C.)",
        "prereqs": ["m11_c7_thebes_macedoine"],
        "texte": """
En 13 ans, Alexandre III de Macédoine conquiert un empire de 5 millions de km² —
de la Grèce à l'Inde du Nord. Aucune défaite dans une bataille rangée en carrière entière.

GRANIQUE (-334) : première victoire en Asie Mineure. Alexandre charge personnellement
avec la cavalerie, traverse la rivière sous les flèches, faillit mourir (Cléitos le Noir le sauve).
Libère les cités grecques d'Ionie.

ISSOS (-333) : Darius III avec 100 000 hommes contre 35 000 Macédoniens.
Terrain étroit qui annule l'avantage numérique perse. Alexandre brise le centre, charge
vers Darius — le Grand Roi fuit en abandonnant sa famille. Tournant de la campagne.

TARSE, SIDON, TYRE (-333 à -332) : siège de Tyre insulaire (7 mois), construction d'une
digue de 800 m depuis le continent. Maîtrise de la côte — Perse coupée de sa flotte phénicienne.

GAUGAMÈLES (-331) : bataille décisive. Darius III avec 200 000+ hommes sur terrain plat
choisi pour ses chars à faux. Alexandre crée intentionnellement une brèche dans sa ligne,
y engouffre sa cavalerie vers Darius. Le Grand Roi fuit à nouveau. Fin de l'Empire achéménide.

PERSÉPOLIS incendiée (-330). Campagnes en Bactriane, Sogdiane. Invasion de l'Inde (-326).
L'armée refuse d'aller plus loin à l'Hyphase. Alexandre meurt à Babylone (-323), 32 ans.
Cause inconnue — alcool, fièvre, poison, chagrin après mort de son ami Héphaistion.
        """.strip(),
    },

    "m11_c9_hellénisme": {
        "module": 11, "ordre": 9,
        "titre": "L'Hellénisme — Les Royaumes Successeurs",
        "prereqs": ["m11_c8_alexandre"],
        "texte": """
À la mort d'Alexandre, ses généraux (les DIADOQUES — "successeurs") se disputent l'empire pendant
40 ans de guerres. Trois grands royaumes émergent et dominent l'Orient pendant deux siècles.

GUERRES DES DIADOQUES (-323 à -281) : Ptolémée prend l'Égypte, Séleucus prend la Syrie/Perse,
Antigone et son fils Démétrius tentent de reconstituer l'empire entier — et échouent.
Ipsos (-301) : bataille de 80 000 hommes et 400+ éléphants de guerre — Antigone tué.
Couros (-281) : derniers diadoques originaux s'éliminent.

ROYAUME LAGIDE (Égypte, -305 à -30) : Ptolémée fonde une monarchie hellénisée à Alexandrie.
Bibliothèque d'Alexandrie — centre intellectuel du monde antique. Économie centralisée, bureaucratie.
La lignée se termine avec Cléopâtre VII (-51 à -30) — alliée de César puis d'Antoine, vaincue par Octave.

ROYAUME SÉLEUCIDE (Syrie/Perse, -312 à -63) : le plus vaste mais le moins cohérent.
Perd progressivement la Perse (Parthes) et l'Anatolie (Attalides de Pergame).

ROYAUME ANTIGONIDE (Macédoine, -276 à -168) : contrôle la Grèce continentale.
Vaincu par Rome à Cynoscéphales (-197) et Pydna (-168). Fin de l'indépendance macédonienne.

HÉRITAGE : la koinè grecque devient la lingua franca de l'Orient. Base du Nouveau Testament.
        """.strip(),
    },

    # ── TRIMESTRE 2 — Rome des origines à la République triomphante ───

    "m11_c10_origines_rome": {
        "module": 11, "ordre": 10,
        "titre": "Les Origines de Rome — Monarchie et Fondation",
        "prereqs": [],
        "texte": """
Les origines de Rome mêlent mythe et archéologie. La tradition place la fondation en -753,
mais les données archéologiques suggèrent un développement progressif à partir du IXe siècle.

MYTHE FONDATEUR : Romulus et Rémus, jumeaux fils de Mars et de la vestale Rhéa Silvia,
descendants d'Énée (Troyen réfugié en Italie selon Virgile). Romulus tue Rémus, fonde Rome,
enlève les Sabines pour peupler la cité. Récit politique : Rome naît de la violence et de la ruse.

MONARCHIE ROMAINE (-753 à -509) : sept rois selon la tradition (Romulus, Numa Pompilius,
Tullus Hostilius, Ancus Marcius, puis trois Étrusques : Tarquin l'Ancien, Servius Tullius,
Tarquin le Superbe). Influence étrusque décisive : architecture, religion, techniques militaires.

RÉFORME SERVIENNE (attribuée à Servius Tullius) : organisation des citoyens en centuries
selon la richesse pour le vote et le service militaire. Base du système censitaire républicain.

CHUTE DE LA MONARCHIE (-509) : Tarquin le Superbe est chassé après le viol de Lucrèce
par son fils Sextus. Les aristocrates fondent la République. Rome jure de ne plus jamais
avoir de roi (rex) — ce serment pèsera sur César et toute la fin de la République.

RÉALITÉ ARCHÉOLOGIQUE : Rome du VIIIe siècle est un village de cabanes sur le Palatin.
La cité monumentale est une construction des VIe-Ve siècles, largement étrusque.
        """.strip(),
    },

    "m11_c11_republique_romaine_institutions": {
        "module": 11, "ordre": 11,
        "titre": "La République Romaine — Institutions et Constitution",
        "prereqs": ["m11_c10_origines_rome"],
        "texte": """
La République romaine (-509 à -27) est le modèle institutionnel le plus influent de l'histoire occidentale.
Sa constitution non écrite — admirée par Polybe — répartit le pouvoir entre trois pôles.

SÉNAT (SENATUS) : 300 puis 600 membres, sénateurs à vie issus des grandes familles (patres).
Approuve les lois, contrôle les finances et la politique étrangère, nomme les généraux.
Autorité morale (auctoritas) plutôt que pouvoir légal formel — mais déterminante en pratique.

MAGISTRATURES : système annuel, collégial (pour limiter l'abus), cursus honorum hiérarchique.
Questeur → Édile → Préteur → CONSUL (deux, pouvoir suprême, commandement militaire).
Censeur (tous les 5 ans, recensement et morale publique). DICTATEUR (6 mois, pouvoirs absolus
en temps de crise — Cincinnatus le modèle : dicte, sauve Rome, retourne à ses champs).

ASSEMBLÉES POPULAIRES : comices centuriates (vote des lois, élection des hauts magistrats),
comices tributes (affaires courantes), conciles de la plèbe (tribuns de la plèbe).

TRIBUNS DE LA PLÈBE : inviolables, peuvent opposer leur veto à n'importe quelle décision
d'un magistrat. Création après la Sécession de la Plèbe (-494) — première grève de l'histoire.

SPQR (Senatus Populusque Romanus — "Le Sénat et le Peuple Romain") : formule qui résume
l'équilibre constitutionnel. Gravée sur les monuments, les légions, encore aujourd'hui sur les bouches
d'égout de Rome.
        """.strip(),
    },

    "m11_c12_conqueêtes_italie": {
        "module": 11, "ordre": 12,
        "titre": "La Conquête de l'Italie (509–264 av. J.-C.)",
        "prereqs": ["m11_c11_republique_romaine_institutions"],
        "texte": """
Avant de conquérir le monde méditerranéen, Rome doit d'abord unifier la péninsule italienne.
Ce processus de 250 ans forge les institutions militaires et diplomatiques romaines.

GUERRES SAMNITES (-343 à -290) : trois guerres contre la confédération samnite (Italie centrale).
Désastre des Fourches Caudines (-321) : une armée romaine entière est capturée et humiliée,
forcée de passer sous le joug. Rome rebuild et l'emporte. Leçon : Rome ne capitule jamais.

INVASION GAULOISE ET SACK DE ROME (-390) : les Gaulois Sénons sous Brennus écrasent les Romains
à l'Allia, pillent Rome. Seul le Capitole résiste (les oies sacrées sauvent la garnison selon la légende).
Trauma collectif — les Gaulois restent la peur primordiale romaine pendant des siècles.

PYRRHUS D'ÉPIRE (-280 à -275) : roi grec appelé par Tarente. Gagne deux batailles (Héraclée, Ausculum)
avec ses éléphants de guerre — au prix de pertes si lourdes qu'il dit "encore une telle victoire et
je suis perdu". D'où "victoire à la Pyrrhus". Rome résiste. Pyrrhus repart. Rome contrôle l'Italie du Sud.

SYSTÈME ALLIÉ : Rome ne réduit pas l'Italie en province — elle noue des alliances différenciées.
Les alliés (socii) fournissent des troupes, ont leur autonomie locale, mais pas la citoyenneté romaine.
Système souple mais qui créera la Guerre Sociale (-91 à -88) quand les alliés la réclameront.
        """.strip(),
    },

    "m11_c13_guerres_puniques": {
        "module": 11, "ordre": 13,
        "titre": "Les Guerres Puniques — Rome contre Carthage (264–146 av. J.-C.)",
        "prereqs": ["m11_c12_conqueêtes_italie"],
        "texte": """
Les trois guerres puniques sont la lutte existentielle de Rome pour la domination méditerranéenne.
Carthage — puissance commerciale et navale fondée par les Phéniciens — est son égale et son rival.

PREMIÈRE GUERRE PUNIQUE (-264 à -241) : née d'une querelle en Sicile, devient une guerre navale.
Rome, puissance terrestre, construit une flotte en quelques mois en copiant un navire carthaginois échoué.
Invente le CORVUS (passerelle à grappin) pour transformer les batailles navales en combats terrestres.
Victoire à Mylae (-260), désastre à Drepanum (-249), victoire finale aux Égades (-241).
Rome obtient la Sicile — sa première province.

DEUXIÈME GUERRE PUNIQUE (-218 à -201) — HANNIBAL : le plus grand chef militaire de l'Antiquité.
Traverse les Alpes avec 40 000 hommes et 37 éléphants en novembre. Perd la plupart des éléphants.
TRÉBIE (-218), LAC TRASIMÈNE (-217), CANNES (-216) : trois chefs-d'œuvre tactiques.
À Cannes, 50 000 à 70 000 Romains encerclés et massacrés en une journée — record de l'Antiquité.
Rome refuse de capituler. Fabius Maximus "le Temporisateur" — harcèlement, pas de bataille rangée.
SCIPION L'AFRICAIN porte la guerre en Afrique. ZAMA (-202) : Hannibal vaincu. Fin de Carthage comme puissance.

TROISIÈME GUERRE PUNIQUE (-149 à -146) : Caton l'Ancien répète à chaque discours
"Delenda est Carthago" ("Carthage doit être détruite"). Siège de 3 ans. Carthage rasée.
50 000 survivants vendus comme esclaves. Le sol semé de sel (mythe tardif). L'Afrique devient province.
        """.strip(),
    },

    "m11_c14_armee_romaine": {
        "module": 11, "ordre": 14,
        "titre": "L'Armée Romaine — Organisation et Tactique",
        "prereqs": ["m11_c11_republique_romaine_institutions"],
        "texte": """
L'armée romaine est la machine de guerre la plus efficace et la plus durable de l'Antiquité.
Son organisation évolue sur 700 ans, mais ses principes demeurent.

LÉGION RÉPUBLICAINE : initialement organisation censitaire (les riches forment la cavalerie et
l'infanterie lourde, les pauvres l'infanterie légère). Réforme de Marius (-107) : armée
professionnelle, ouverte aux prolétaires (capite censi), équipement standardisé fourni par l'État.

STRUCTURE DE LA LÉGION (après Marius) : 5 000 à 6 000 légionnaires + auxiliaires.
10 cohortes de 480 hommes → 3 manipules → 2 centuries de 80 hommes.
Centurion : officier clé de l'armée romaine, career soldier, bâton de vigne comme insigne.
La Première Cohorte (doublée) porte les aigle et les antiques distinctions.

ARMEMENT : pilum (javelot lourd de 2 m, se tord à l'impact pour ne pas être renvoyé),
gladius hispaniensis (épée courte de 50-60 cm pour le combat rapproché), scutum (bouclier bombé).
La testudo (tortue) : boucliers formant un toit sous les projectiles.

GÉNIE MILITAIRE : les Romains sont les ingénieurs de l'Antiquité. Camp légionnaire standardisé
en 4 heures (castra), routes militaires, siège systématique, machines (balistes, onagres, tours d'assaut).
Le siège de Jotapata (-67 ap. J.-C.) par Vespasien : Josèphe en fait la description précise.

DISCIPLINE : decimatio (exécution d'un légionnaire sur dix en cas de lâcheté), mais aussi
solde, primes, terrain à la retraite. L'armée crée la loyauté par l'intérêt et la peur.
        """.strip(),
    },

    "m11_c15_conquêtes_orient": {
        "module": 11, "ordre": 15,
        "titre": "La Conquête de l'Orient Hellénistique (200–63 av. J.-C.)",
        "prereqs": ["m11_c13_guerres_puniques", "m11_c9_hellénisme"],
        "texte": """
Après la victoire sur Carthage, Rome se tourne vers l'Orient hellénistique.
En 140 ans, elle absorbe la quasi-totalité du monde grec et macédonien.

MACÉDOINE ET GRÈCE : Philippe V de Macédoine avait soutenu Hannibal — Rome règle ses comptes.
CYNOSCÉPHALES (-197) : Flamininus bat les phalanges macédoniennes. La légion romaine, plus flexible
(manipules indépendants sur terrain varié), l'emporte sur la phalange rigide d'Alexandre.
PYDNA (-168) : Émile Paul détruit définitivement le royaume antigonide. 150 000 Épirotes vendus comme esclaves.
Corinthe rasée (-146) — même année que Carthage. Message clair : ne pas résister à Rome.

SÉLEUCIDES : Antiochos III tente d'exploiter la situation — battu à Magnésie (-190).
Le roi doit livrer ses éléphants et payer une indemnité massive. L'Orient grec capitule.

MITHRIDATE VI DU PONT (-120 à -63) : le résistant le plus tenace. Roi du Bosphore, parle 22 langues,
immunise contre les poisons. Massacre 80 000 Italiens en Asie Mineure un jour de -88 (les Vêpres
Asiatiques). Trois guerres mithridatiques. Vaincu par Lucullus puis POMPÉE.

POMPÉE EN ORIENT (-66 à -62) : réorganise tout l'Orient en provinces et royaumes clients.
Conquiert la Syrie séleucide, entre à Jérusalem. Crée la Province d'Orient.
Rome contrôle désormais toute la Méditerranée orientale.
        """.strip(),
    },

    "m11_c16_gracques_crise": {
        "module": 11, "ordre": 16,
        "titre": "Les Gracques et la Crise de la République (133–88 av. J.-C.)",
        "prereqs": ["m11_c13_guerres_puniques", "m11_c11_republique_romaine_institutions"],
        "texte": """
La conquête crée des richesses colossales — et des inégalités déstabilisantes.
Les Gracques tentent une réforme. Leur échec ouvre une ère de violence politique.

PROBLÈME AGRAIRE : les guerres puniques ont ruiné les paysans italiens (absents 15 ans).
Les grands propriétaires (sénateurs) ont accaparé l'ager publicus (terres publiques).
La loi Licinia (-367) limitait les concessions à 500 iugera — systématiquement contournée.
Les citoyens sans terre = prolétaires = base de l'armée de Marius = dynamite politique.

TIBERIUS GRACCHUS (-133) : tribun de la plèbe, propose une nouvelle loi agraire — redistribuer
les terres excédentaires aux pauvres. Les sénateurs font tuer son collègue tribun (veto supprimé
par vote), puis Tiberius lui-même est assassiné à coups de chaises avec 300 partisans.
Premier meurtre politique à Rome depuis des siècles. Précédent catastrophique.

CAÏUS GRACCHUS (-123 à -121) : frère de Tiberius, plus ambitieux. Loi frumentaire (blé à prix réduit),
réforme judiciaire, proposition de citoyenneté pour les alliés italiens. Trop loin : assassiné.
3 000 partisans massacrés. Le Sénat utilise le senatus consultum ultimum — état d'urgence.

MARIUS ET SYLLA : la réforme militaire de Marius (-107) crée une armée de professionnels
liée à leur général par les primes et le butin — plus à Rome. Sylla marche sur Rome deux fois
(-88, -82). Proscriptions — listes de proscrits dont les biens sont confisqués et les meurtriers
récompensés. Environ 10 000 personnes tuées. La violence est désormais l'outil normal de la politique.
        """.strip(),
    },

    "m11_c17_premier_triumvirat": {
        "module": 11, "ordre": 17,
        "titre": "Le Premier Triumvirat et César (60–44 av. J.-C.)",
        "prereqs": ["m11_c16_gracques_crise", "m11_c15_conquêtes_orient"],
        "texte": """
Le Premier Triumvirat est une alliance privée et illégale entre les trois hommes les plus puissants de Rome.
Elle signe l'arrêt de mort de la République.

TRIUMVIRAT (-60) : POMPÉE (gloire militaire, conquérant de l'Orient), CRASSUS (homme le plus riche
de Rome — sa fortune équivaut au budget annuel de l'État), JULES CÉSAR (brillant politicien populare,
endettés jusqu'au cou). Alliance mutuelle : Pompée veut que ses lois soient ratifiées, Crassus veut
des contrats d'impôt en Asie, César veut un commandement militaire.

GAULE (-58 à -51) : César part comme proconsul des Gaules. 8 ans, 800 villes prises, 1 million de morts
selon ses propres chiffres, 1 million d'esclaves. Richesse colossale. "La guerre des Gaules" — propagande
politique écrite à la troisième personne. Vercingétorix vaincu à Gergovie... non, à Alésia (-52) :
siège double (circumvallation autour d'Alésia + contrevallation contre l'armée de secours).

MORT DE CRASSUS (-53) : battu et tué à Carrhes par les Parthes (les légions capturées fournissent
des gardes pour les palais parthes). Le triumvirat perd son arbitre.

RUBICON (10 janvier -49) : le Sénat ordonne à César de dissoudre son armée avant de rentrer
(sinon il sera jugé). César franchit le Rubicon (frontière légale) avec la 13e légion.
"Alea iacta est" ("Le sort en est jeté"). Guerre civile. Pompée fuit en Grèce, est assassiné en Égypte.

DICTATURE ET IDES DE MARS (-44) : César, dictateur perpétuel, accumule tous les pouvoirs.
23 coups de poignard au Sénat le 15 mars -44. Conspirateurs : Brutus, Cassius, et 21 autres.
Ils pensaient restaurer la République. Ils déclenchent 13 années de guerres civiles supplémentaires.
        """.strip(),
    },

    "m11_c18_octave_auguste": {
        "module": 11, "ordre": 18,
        "titre": "Auguste — La Naissance de l'Empire (44–14 ap. J.-C.)",
        "prereqs": ["m11_c17_premier_triumvirat"],
        "texte": """
Octave (63 av. J.-C. – 14 ap. J.-C.) accomplit ce que César a tenté trop vite :
transformer la République en monarchie personnelle tout en préservant les formes républicaines.

DEUXIÈME TRIUMVIRAT (-43 à -33) : Octave, Marc Antoine, Lépide. Légaux cette fois (lex Titia).
Proscriptions : 2 300 chevaliers et 300 sénateurs tués, dont Cicéron (mains et tête exposées).
Philippes (-42) : Brutus et Cassius vaincus et morts. La République est définitivement enterrée.

ACTIUM (-31) : Octave contre Marc Antoine et Cléopâtre. Victoire navale d'Agrippa.
Antoine et Cléopâtre se suicident. L'Égypte devient la propriété personnelle d'Octave.
Trésor des Ptolémées finance le règlement de toutes les dettes de l'armée et les primes.

LE PRINCIPAT : Octave refuse le titre de roi ou de dictateur. En -27, il rend formellement
les pouvoirs au Sénat — qui les lui restitue aussitôt sous des formes légales multiples :
IMPERIUM PROCONSULAIRE (commandement de toutes les armées), TRIBUNICIA POTESTAS (inviolabilité,
veto, convocation du Sénat). Il prend le titre d'AUGUSTUS — "le vénérable", connotation religieuse.
Princeps (premier citoyen) — pas de roi, mais monarque en substance.

PAX ROMANA : 200 ans de paix relative dans l'empire (quelques guerres aux frontières).
RÉFORMES : armée professionnelle permanente (25 légions), garde prétorienne, flotte de mer,
recensement, réforme fiscale, reconstruction de Rome ("J'ai trouvé Rome en brique, je la laisse en marbre").
PROPAGANDE : Virgile (Énéide), Tite-Live (Ab Urbe Condita), Horace — la littérature au service du régime.
        """.strip(),
    },

    # ── TRIMESTRE 3 — Le Haut-Empire ─────────────────────────────────

    "m11_c19_julio_claudiens": {
        "module": 11, "ordre": 19,
        "titre": "Les Julio-Claudiens — Les Premiers Empereurs (14–68 ap. J.-C.)",
        "prereqs": ["m11_c18_octave_auguste"],
        "texte": """
Les quatre successeurs d'Auguste illustrent les pathologies du pouvoir personnel héréditaire
dans un système qui n'a aucun mécanisme légal de transmission ni de destitution.

TIBÈRE (14-37) : compétent et austère. Retire à Rome, laisse gouverner Séjan (préfet du prétoire)
qui fait exécuter ses rivaux. Règne de terreur sénatoriale. "Il ne faut pas toucher à la boue —
elle salit ou elle éclabousse." Meurt à 78 ans, peut-être étouffé par Macron (son successeur).

CALIGULA (37-41) : commence bien, finit en tyran paranoïaque (ou simplement malade — encéphalite?).
Nomme son cheval consul (peut-être de la provocation politique, pas de la folie).
Assassiné par la garde prétorienne après 4 ans. Première fois que l'armée fait et défait un empereur.

CLAUDE (41-54) : considéré idiot par sa famille (boiteux, begayant) — en réalité administrateur
compétent. Conquête de la Bretagne (-43). Réforme administrative, extension de la citoyenneté.
Empoisonné par sa femme Agrippine pour mettre Néron sur le trône.

NÉRON (54-68) : commence sous la tutelle de Sénèque et Burrus. Incendie de Rome (64) —
il accuse les chrétiens. Persécution. Premier martyr systématique. Reconstruit Rome (Domus Aurea).
Révoltes en Gaule et Espagne. La garde prétorienne l'abandonne. Se suicide : "Quel artiste meurt en moi !"

LEÇON POLITIQUE : le Principat n'a aucune règle de succession. Chaque transition est une crise.
Le Sénat vote des pouvoirs, l'armée fait les empereurs. Ce déséquilibre structurel est fatal.
        """.strip(),
    },

    "m11_c20_flaviens_antonins": {
        "module": 11, "ordre": 20,
        "titre": "Les Flaviens et Antonins — L'Apogée de l'Empire (69–192 ap. J.-C.)",
        "prereqs": ["m11_c19_julio_claudiens"],
        "texte": """
L'année des quatre empereurs (69 ap. J.-C.) révèle que l'armée fait les empereurs.
Les Flaviens puis les Antonins construisent le régime le plus stable de l'histoire romaine.

ANNÉE DES QUATRE EMPEREURS (69) : mort de Néron → Galba (légions d'Espagne) → Othon (prétoriens)
→ Vitellius (légions du Rhin) → VESPASIEN (légions d'Orient). Première fois qu'un secret de l'empire
est révélé : les empereurs peuvent être faits ailleurs qu'à Rome.

LES FLAVIENS (69-96) : Vespasien — pragmatique, rétablit les finances. Détruit Jérusalem (70 ap. J.-C.),
vend 97 000 Juifs comme esclaves, rase le Temple. Construit le Colisée sur le lac de la Domus Aurea.
Titus (79-81) — Éruption du Vésuve, destruction de Pompéi. Domitien (81-96) — tyrannie sénatoriale, assassiné.

LES ANTONINS (96-192) : "période des bons empereurs" selon Gibbon. Nerva, Trajan, Hadrien,
Antonin le Pieux, Marc-Aurèle, Commode. Principe de l'ADOPTION : l'empereur choisit le meilleur
successeur et l'adopte. Brise le cycle de la succession héréditaire — jusqu'à Marc-Aurèle qui revient au fils.

TRAJAN (98-117) : extension maximale de l'empire. Dace (Roumanie actuelle), Arabie, Mésopotamie.
120 millions d'habitants, 5 millions de km². Colonne Trajane — bande dessinée de marbre de 190 m.

MARC-AURÈLE (161-180) : philosophe stoïcien sur le trône. "Méditations" — journal privé.
Guerres germaniques incessantes sur le Danube. Premières pandémies (peste Antonine) qui tuent 5-10M.
Son fils COMMODE — le retour du tyran paranoïaque. Assassiné en 192.
        """.strip(),
    },

    "m11_c21_limes_frontières": {
        "module": 11, "ordre": 21,
        "titre": "Le Limes — La Défense des Frontières",
        "prereqs": ["m11_c20_flaviens_antonins"],
        "texte": """
Le LIMES (pluriel : limites) désigne l'ensemble des fortifications, routes et installations militaires
qui délimitent et défendent les frontières de l'Empire romain.

GÉOGRAPHIE DÉFENSIVE : l'Empire adopte des frontières "naturelles" — le Rhin et le Danube au nord,
le Sahara et les déserts arabes au sud et à l'est, la mer au sud et à l'ouest.
Mais ces frontières font 10 000 km — une pression constante qui absorbe 300 000+ légionnaires.

STRUCTURE DU LIMES GERMANIQUE : fossé (fossa), palissade (vallum), puis mur de pierre,
tours de guet (burgus) tous les 500 m à 1 km, forts (castella) tous les 10-15 km,
forteresses légionnaires (castra) tous les 50-100 km. Systèmes d'alarmes (signaux de feu).

MUR D'HADRIEN (122-128 ap. J.-C.) : 117 km traversant le nord de l'Angleterre.
Pierre et tourbe, largeur 3-4 m, hauteur 5-6 m. Milecastles tous les 1 500 m, 16 forts.
Conçu non comme mur absolu mais comme contrôle des flux — douane et défense combinées.

PROBLÈME STRATÉGIQUE FONDAMENTAL : l'Empire romain est une puissance d'expansion naturelle
convertie en puissance défensive. Une frontière statique est structurellement désavantageuse :
l'ennemi choisit le point d'attaque, le défenseur doit être fort partout.
Edward Luttwak ("The Grand Strategy of the Roman Empire") : l'Empire passe d'une défense
en profondeur (haute période) à une défense de la frontière (Bas-Empire), puis à une
défense mobile (armées de réserve) — chaque étape reconnaissant l'échec de la précédente.
        """.strip(),
    },

    "m11_c22_droit_romain": {
        "module": 11, "ordre": 22,
        "titre": "Le Droit Romain — Fondement de la Civilisation Occidentale",
        "prereqs": ["m11_c11_republique_romaine_institutions"],
        "texte": """
Le droit romain est l'héritage intellectuel le plus durable de Rome.
Il structure encore aujourd'hui les systèmes juridiques de l'Europe continentale, du Québec,
de l'Amérique latine et de nombreux pays d'Afrique.

LOI DES XII TABLES (-450) : premier droit écrit romain. Arrachée par la plèbe aux patriciens.
Affichée au Forum pour que tous puissent la connaître. Principe fondateur : égalité devant la loi connue.

ÉVOLUTION : ius civile (droit des citoyens romains seulement) → ius gentium (droit des peuples,
applicable aux non-citoyens dans les transactions commerciales) → ius naturale (droit naturel universel,
développé par les stoïciens et juristes comme Cicéron et Ulpien).

GRANDS JURISTES (IIe-IIIe s. ap. J.-C.) : Papinien, Ulpien, Paul, Gaius.
Leurs écrits compilés dans le Digeste de Justinien (533 ap. J.-C.) — la base du droit civil moderne.

CONCEPTS FONDATEURS : personas (personnalité juridique), dominium (propriété), obligatio (obligation),
actio (recours en justice), testamentum (testament), tutela (tutelle), societas (société commerciale).
Distinction PUBLIC/PRIVÉ (droit public = organisation de l'État, droit privé = relations entre individus).

HABEAS CORPUS avant l'heure : la provocatio ad populum — tout citoyen peut appeler de sa condamnation.
La garantie contre l'exécution arbitraire est un principe romain avant d'être anglais.
Édit de Caracalla (212 ap. J.-C.) : la citoyenneté romaine accordée à tous les hommes libres de l'Empire.
        """.strip(),
    },

    "m11_c23_religion_romaine": {
        "module": 11, "ordre": 23,
        "titre": "Religion Romaine, Culte Impérial et Christianisme",
        "prereqs": ["m11_c18_octave_auguste"],
        "texte": """
La religion romaine est fondamentalement POLITIQUE — la pax deorum (paix avec les dieux)
est une affaire d'État qui conditionne la victoire militaire et la prospérité civique.

RELIGION TRADITIONNELLE : polythéisme syncrétique. Les dieux romains sont largement adoptés
des Grecs (Jupiter = Zeus, Mars = Arès, Vénus = Aphrodite) avec des fonctions civiques précises.
Pontifes, augures, vestales — prêtres sont des magistrats. La divination (lecture des entrailles,
vol des oiseaux) est une procédure administrative avant toute décision importante.

CULTE IMPÉRIAL : Auguste est deifié après sa mort. De son vivant, son genius (esprit divin) est honoré.
Les provinces orientales le déifient dès son règne — habitude hellénistique. Domitien s'autoproclame
"dominus et deus" (seigneur et dieu) de son vivant. Cela choque les Romains traditionalistes.

CULTES À MYSTÈRES : Mithra (armée), Isis (femmes), Cybèle, Bacchus — promesses de salut individuel
et de vie après la mort. Concurrents du christianisme dans les IIe-IIIe siècles.

CHRISTIANISME : minorité persécutée sporadiquement (Néron -64, Domitien, Dèce -250, Valérien -257,
Dioclétien -303 — Grande Persécution). Problème : les chrétiens refusent le sacrifice à l'Empereur.
ÉDIT DE MILAN (313) : Constantin et Licinius accordent la tolérance. CONCILE DE NICÉE (325) :
Constantin unifie la théologie chrétienne. Théodose (380) : christianisme religion d'État.
        """.strip(),
    },

    "m11_c24_rome_orient": {
        "module": 11, "ordre": 24,
        "titre": "Rome face à l'Orient — Parthes et Sassanides",
        "prereqs": ["m11_c20_flaviens_antonins"],
        "texte": """
L'Orient représente la seule puissance qui résiste durablement à Rome.
Partout ailleurs, Rome triomphe. Face aux empires iraniens, elle atteint ses limites.

L'EMPIRE PARTHE (247 av. J.-C. – 224 ap. J.-C.) : fondé par les Arsacides, nomades iraniens.
Cavalerie lourde cuirassée (cataphractaires) et cavalerie légère à l'arc (la tactique parthe :
feindre la fuite et tirer en se retournant — "le coup du Parthe"). Aucune infanterie solide.

CARRHES (-53 av. J.-C.) : Crassus et 35 000 Romains encerclés par 10 000 cavaliers parthes
sous Suréna. 20 000 tués, 10 000 capturés. Les légions romaines sont invincibles dans leur
formation — la cavalerie parthe refuse l'engagement close et noie les légions de flèches.
Marc Antoine (-36) tente de venger Carrhes — autre désastre. Les Parthes gardent les Aigles romaines.

L'EMPIRE SASSANIDE (224-651 ap. J.-C.) : renverse les Parthes, plus agressif et centralisé.
Guerres permanentes du IIIe au VIIe siècle. VALÉRIEN (260 ap. J.-C.) : premier et seul
Empereur romain capturé vivant par l'ennemi — pris par Châhpuhr Ier à Édesse.
Humiliation absolue représentée sur les reliefs rupestres de Naqsh-e Rostam.

Julien l'Apostat (363 ap. J.-C.) tente une grande offensive — tué dans la retraite.
Les deux empires s'épuisent mutuellement jusqu'à la conquête arabe (630-650).
Cette frontière orientale immobilise durablement les meilleures légions.
        """.strip(),
    },

    "m11_c25_crise_troisieme_siecle": {
        "module": 11, "ordre": 25,
        "titre": "La Crise du IIIe Siècle — L'Anarchie Militaire (235–284 ap. J.-C.)",
        "prereqs": ["m11_c20_flaviens_antonins", "m11_c21_limes_frontières"],
        "texte": """
La crise du IIIe siècle est le moment où l'Empire romain manque de s'effondrer.
50 ans de chaos politique, militaire et économique qui remodèlent profondément la structure impériale.

DÉCLENCHEUR : assassinat de Sévère Alexandre (235) par ses propres soldats après une campagne
insuffisamment belliqueuse contre les Germains. Maximin le Thrace (235-238) : premier soldat
du rang élu par l'armée. Ouvre la boîte de Pandore.

SOLDATS-EMPEREURS : entre 235 et 285, plus de 50 prétendants au trône. Durée moyenne de règne :
18 mois. La plupart meurent assassinés par leurs propres troupes. Aucune légitimité dynastique
ou institutionnelle — seul le rapport de force entre armées compte.

CRISES SIMULTANÉES :
- Frontières percées sur le Rhin, le Danube et en Orient (Sassanides).
- Valérien capturé (260). Empire de Gallien réduit à l'Italie et les Balkans.
- Empires sécessionnistes : Empire des Gaules (260-274, Postumus puis Tetricus),
  Royaume de Palmyre (262-273, Zénobie).
- Dévaluation monétaire catastrophique : l'argent du denier tombe à 2-5%.
- Épidémie de Cyprien (249-262) : 5 000 morts/jour à Rome au pic.

CONSÉQUENCES STRUCTURELLES : abandon des grandes villes non murées, retour à l'économie de subsistance,
militarisation généralisée, fin de la classe sénatoriale comme classe dirigeante militaire (remplacée
par les chevaliers et soldats montés en grade). L'Empire survit — transformé.
        """.strip(),
    },

    "m11_c26_diocletien_tetrarchie": {
        "module": 11, "ordre": 26,
        "titre": "Dioclétien et la Tétrarchie — La Réforme de l'Empire (284–305 ap. J.-C.)",
        "prereqs": ["m11_c25_crise_troisieme_siecle"],
        "texte": """
Dioclétien (règne 284-305) est le grand réformateur. Il stabilise l'Empire et crée le cadre
du Bas-Empire — mais au prix d'une transformation profonde de la nature du régime.

LA TÉTRARCHIE (293) : "gouvernement à quatre". Deux Augustes (Dioclétien en Orient,
Maximien en Occident) + deux Césars (Galère et Constance Chlore). Chaque tétrarque
contrôle un secteur, avec sa propre armée et sa propre capitale (Nicomédie, Milan,
Thessalonique, Trèves). Rome cesse d'être la capitale effective.

Principe de succession prévu : après 20 ans, les Augustes abdiquent (Dioclétien le fera vraiment
en 305 — unique en son genre), les Césars montent en grade, de nouveaux Césars sont nommés.
Cela ne fonctionnera pas : les fils de tétrarques ne respectent pas le plan.

RÉFORMES MILITAIRES : taille de l'armée doublée (~500 000 hommes). Création de deux types :
limitanei (troupes frontalières, de moindre qualité, liées à des terres) et comitatenses (armée
de campagne mobile, l'élite).

RÉFORME FISCALE : retour à la fiscalité en nature (annona), cadastre complet (iugatio/capitatio).
Édit sur le maximum des prix (301) — premier contrôle des prix généralisé de l'histoire.
Résultat : les marchands cachent leurs marchandises. Échec économique, leçon de politique économique.

GRANDE PERSÉCUTION (303-313) : dernière et la plus violente des persécutions des chrétiens.
Destruction des édifices, brûlage des textes, exécutions. Échoue à éliminer le christianisme.
        """.strip(),
    },

    "m11_c27_constantin_christianisme": {
        "module": 11, "ordre": 27,
        "titre": "Constantin et la Christianisation de l'Empire (306–337 ap. J.-C.)",
        "prereqs": ["m11_c26_diocletien_tetrarchie", "m11_c23_religion_romaine"],
        "texte": """
Constantin I est l'un des empereurs les plus importants de l'histoire mondiale.
Sa conversion au christianisme change la trajectoire de la civilisation occidentale.

GUERRES CIVILES POST-TÉTRARCHIE (306-324) : la mort de Constance Chlore (306) déclenche
une nouvelle série de guerres civiles entre six prétendants. Constantin, proclamé par ses soldats
en Bretagne, élimine progressivement ses rivaux.

PONT MILVIUS (312) : bataille décisive contre Maxence. Eusèbe de Césarée : Constantin voit
en rêve un symbole chrétien (chi-rho) avec l'inscription "in hoc signo vinces" (par ce signe
tu vaincras). Maxence se noie dans le Tibre. Mythe fondateur de la relation entre Empire et christianisme.

ÉDIT DE MILAN (313) : avec Licinius, accorde la tolérance religieuse à tous les cultes.
Les propriétés confisquées aux chrétiens restituées. Fin des persécutions.

CONCILE DE NICÉE (325) : Constantin convoque les évêques chrétiens pour résoudre la controverse
arienne (Arius : le Christ est une créature, subordonné au Père — Athanase : le Christ est consubstantiel
au Père). Le CREDO DE NICÉE tranche pour Athanase. Constantin exile les récalcitrants.
L'État intervient dans la théologie — nouvelle ère.

FONDATION DE CONSTANTINOPLE (330) : "Nouvelle Rome" sur le Bosphore. Position stratégique parfaite.
Elle survivra à Rome de 1 000 ans (jusqu'en 1453).

BAPTÊME LIT DE MORT (337) : Constantin se fait baptiser mourant. Sa vie entière est ambiguë
— il continue les sacrifices et le culte solaire. La sincérité de sa conversion est débattue.
        """.strip(),
    },

    # ── TRIMESTRE 4 — Déclin, chute et héritage ──────────────────────

    "m11_c28_bas_empire_pressions": {
        "module": 11, "ordre": 28,
        "titre": "Le Bas-Empire — Les Pressions Barbares (337–410 ap. J.-C.)",
        "prereqs": ["m11_c27_constantin_christianisme"],
        "texte": """
Le Bas-Empire (après Constantin) est une lutte constante pour maintenir la cohérence
d'un État trop vaste contre des pressions de plus en plus fortes sur toutes les frontières.

DIVISION DE L'EMPIRE (395) : à la mort de Théodose I, l'Empire est divisé entre ses deux fils —
Arcadius (Orient) et Honorius (Occident). Division administrative devenue permanente.
Les deux parties évoluent différemment : l'Orient reste riche et urbanisé, l'Occident s'appauvrit.

LES HUNS : peuple nomade des steppes d'Asie centrale, arrivé en Europe ~370 ap. J.-C.
Sous Attila (434-453), ils ravagent la Gaule (Châlons, 451 — victoire romano-visigothique,
seule défaite d'Attila) et l'Italie (452 — sac d'Aquilée, Rome épargnée).
Mort soudaine d'Attila (453), dissolution de l'empire hun. Mais les destructions ont déplacé
tous les peuples germaniques vers l'intérieur de l'Empire.

FÉDÉRÉS ET FOEDERATI : Rome utilise de plus en plus de Barbares dans son armée —
d'abord sous commandement romain, puis des tribus entières (foederati) qui combattent
sous leur propre commandement contre solde. La distinction entre "Romain" et "Barbare" s'estompe.

ALARIC ET LE SAC DE ROME (410) : les Wisigoths, christianisés, se sont battus pour Rome
pendant des années. Alaric réclame terres et commandement — refusé. Blocus de Rome.
Le 24 août 410, Rome est saccagée pour la première fois depuis 800 ans.
Choc psychologique immense — Jérôme : "La ville qui a pris le monde entier est elle-même prise."
        """.strip(),
    },

    "m11_c29_chute_rome_occident": {
        "module": 11, "ordre": 29,
        "titre": "La Chute de l'Empire d'Occident (410–476 ap. J.-C.)",
        "prereqs": ["m11_c28_bas_empire_pressions"],
        "texte": """
La chute de Rome n'est pas un événement mais un processus de plusieurs décennies —
une dissolution progressive de l'autorité impériale en Occident au profit des royaumes barbares.

ROYAUMES BARBARES EN GAULE ET EN ESPAGNE : les Wisigoths installés en Aquitaine (-418),
les Burgondes en Savoie, les Suèves en Espagne, les Vandales en Afrique du Nord (429-439).
Ces royaumes sont officiellement fédérés (alliés) de Rome — en pratique, indépendants.

AETIUS ET LA DERNIÈRE RÉSISTANCE : le dernier grand général occidental. "Le dernier Romain."
Il maintient l'Empire par une politique d'équilibre entre tribus barbares — jouant les Huns contre
les Wisigoths, etc. Vainqueur aux Champs Catalauniques (451) contre Attila.
Assassiné par l'Empereur Valentinien III (454) dans un moment de jalousie — "Il a tué sa main droite avec sa gauche."

VANDALES — SAC DE ROME (455) : 14 jours de pillage méthodique. Les Vandales emportent
les trésors du Temple de Jérusalem (ramenés par Titus en 70 ap. J.-C.).

LES EMPEREURS FANTÔMES (455-476) : une douzaine d'empereurs en 20 ans, tous manipulés
ou éliminés par les généraux barbares. Ricimer (Wisigoth) fait et défait les empereurs.

476 — ROMULUS AUGUSTULE : Odoacre, chef hérule, dépose le jeune Romulus Augustule.
N'envoie pas d'insigne impérial à Constantinople — il n'y a plus d'Occident à administrer.
Date conventionnelle. L'Empire d'Orient (Byzance) continue jusqu'en 1453.
        """.strip(),
    },

    "m11_c30_byzance": {
        "module": 11, "ordre": 30,
        "titre": "Byzance — La Continuité de Rome en Orient (476–1453)",
        "prereqs": ["m11_c29_chute_rome_occident"],
        "texte": """
L'Empire romain d'Orient — que nous appelons Byzantin (terme moderne, jamais utilisé par eux) —
se définit comme romain jusqu'à sa fin en 1453. C'est une continuité réelle, pas un avatar.

JUSTINIEN I (527-565) : le grand tentateur de la Reconquête. Avec son général Bélisaire,
reprend l'Afrique du Nord (aux Vandales, 533), l'Italie (aux Ostrogoths, 535-554),
une partie de l'Espagne (aux Wisigoths, 554). Reconstitue brièvement l'empire méditerranéen.
La Guerre Gothique (20 ans) dévaste l'Italie plus que les Barbares ne l'avaient fait.
Le CORPUS JURIS CIVILIS (534) : compilation complète du droit romain — la base du droit civil
continental jusqu'aujourd'hui.

STRUCTURE POLITIQUE : l'Empereur byzantin est à la fois chef de l'État et chef de l'Église
(césaropapisme). Couronne à Constantinople, légitimité divine, protocole élaboré.

RÉSISTANCE ET ADAPTATIONS : face aux Perses sassanides, aux Arabes (qui enlèvent l'Égypte,
la Syrie, l'Afrique du Nord en 630-698), aux Bulgares, aux Normands, aux Croisés (1204 —
sac de Constantinople par les croisés latins), aux Turcs ottomans.

CHUTE DE CONSTANTINOPLE (29 mai 1453) : Mehmed II avec des canons (technologie nouvelle
contre des murs vieux de 1 000 ans). Constantin XI meurt les armes à la main.
La prise met fin à 2 200 ans de tradition gréco-romaine continue.
        """.strip(),
    },

    "m11_c31_causes_chute": {
        "module": 11, "ordre": 31,
        "titre": "Les Causes de la Chute de Rome — Débat Historiographique",
        "prereqs": ["m11_c29_chute_rome_occident"],
        "texte": """
Depuis Gibbon (1776), la question des causes de la chute de Rome est l'une des plus débattues
de l'histoire. Plus de 200 explications différentes ont été proposées.

EDWARD GIBBON ("Déclin et chute de l'Empire romain", 1776-1788) : deux causes principales —
le christianisme (qui a affaibli l'esprit guerrier et la cohésion civique) et les Barbares.
Thèse influente mais partielle.

EXPLICATION ÉCONOMIQUE : épuisement des ressources, dévaluation monétaire, effondrement
du commerce long-distance, retour à l'économie de subsistance. Peter Heather : les invasions barbares
sont la cause principale — le reste sont des fragilités, pas des causes.

EXPLICATION MILITAIRE : sur-extension militaire (Paul Kennedy — avant la lettre),
dépendance croissante aux foederati barbares, perte de la cohésion légionnaire.

EXPLICATION DÉMOGRAPHIQUE : pestes répétées (Antonine, Cyprienne, Justinienne) qui réduisent
la population de 25-33%. Moins de contribuables, moins de soldats, moins de colonisation.

EXPLICATION "TRANSFORMATION" (Peter Brown, Averil Cameron) : il n'y a pas de "chute"
brutale mais une TRANSFORMATION de la civilisation antique en civilisation médiévale.
La continuité est plus importante que la rupture.

PETER HEATHER (2006) : les invasions barbares sont une cause suffisante — les Huns déstabilisent
un système qui fonctionnait. Rejette les explications par les "faiblesses internes" comme
trop déterministes.
        """.strip(),
    },

    "m11_c32_historiographie_antique": {
        "module": 11, "ordre": 32,
        "titre": "Les Historiens de l'Antiquité — Hérodote, Thucydide, Tite-Live, Tacite",
        "prereqs": ["m11_c6_guerre_peloponnese", "m11_c11_republique_romaine_institutions"],
        "texte": """
L'Antiquité gréco-romaine invente l'histoire comme discipline — avec ses méthodes, ses biais
et ses chefs-d'œuvre qui restent des modèles 2 500 ans plus tard.

HÉRODOTE D'HALICARNASSE (~484-425 av. J.-C.) : "Père de l'Histoire" (Cicéron).
"Enquêtes" (Historiai) sur les Guerres Médiques. Méthode : voyager, collecter des témoignages,
comparer. Intérêt pour les mœurs étrangères (relativisme culturel avant la lettre).
Limite : crédule, mêle mythes et faits, erreurs géographiques. Mais premier à raconter
les événements humains (et non divins) de façon systématique.

THUCYDIDE D'ATHÈNES (~460-400 av. J.-C.) : "Histoire de la guerre du Péloponnèse".
Stratège athénien exilé après un échec — 20 ans pour écrire. Méthode : témoignages directs,
documentation rigoureuse, discours reconstitués. Première analyse des causes structurelles
(puissance, peur, intérêt) vs prétextes. Fondateur du réalisme en relations internationales.
"Le fort fait ce qu'il peut, le faible subit ce qu'il doit" (Dialogue des Méliens).

TITE-LIVE (~59 av. J.-C. – 17 ap. J.-C.) : "Ab Urbe Condita" (De la fondation de la ville).
142 livres, dont 35 conservés. Grande narration de l'histoire romaine des origines à Auguste.
Patriote, moral, peu critique des sources. Mine d'informations malgré ses limites.

TACITE (~56-120 ap. J.-C.) : "Annales" et "Histoires". Le plus grand stylistei de l'historiographie
latine. Vision sombre du Principat — la liberté républicaine est perdue, l'Empire est tyrannique.
"Ils font un désert et l'appellent paix." Source principale sur Tibère, Néron et la période julio-claudienne.
        """.strip(),
    },

    "m11_c33_héritage_politique": {
        "module": 11, "ordre": 33,
        "titre": "L'Héritage Politique de l'Antiquité",
        "prereqs": ["m11_c2_athenes_democratie", "m11_c22_droit_romain"],
        "texte": """
L'Antiquité gréco-romaine n'est pas un objet d'étude archéologique — c'est le fondement
des institutions politiques, juridiques et intellectuelles de l'Occident contemporain.

DÉMOCRATIE : le mot, le concept, les mécanismes (assemblée, vote, tirage au sort, mandat limité)
sont une invention athénienne. Les Révolutions américaine et française s'y réfèrent explicitement.
Les Pères Fondateurs américains (Madison, Hamilton) connaissent Thucydide et Polybe par cœur.

SÉPARATION DES POUVOIRS : Montesquieu ("De l'Esprit des Lois", 1748) tire sa doctrine
de la constitution mixte de Polybe appliquée à Rome. Les Costitutions américaine et françaises
en sont les héritières directes.

DROIT ROMAIN : les systèmes de droit civil de la France, du Québec, de l'Espagne, de l'Italie,
de l'Allemagne, du Brésil (et 70+ autres pays) sont des descendants directs du droit romain
via le Corpus Juris Civilis de Justinien et le Code Napoléon (1804).
Common law anglaise : moins directement, mais le droit romain influence via le droit canonique.

LANGUE ET PENSÉE : le latin reste la langue de l'Église catholique, de la médecine, du droit
et de la science jusqu'au XVIIIe siècle. Les langues romanes (français, espagnol, portugais,
italien, roumain) sont du latin transformé. 60% du vocabulaire anglais est d'origine latine ou grecque.

PHILOSOPHIE POLITIQUE : Platon (République, Lois), Aristote (Politique), Cicéron (République,
Lois), Marc-Aurèle (Méditations) — textes fondateurs du débat politique occidental.
        """.strip(),
    },

    "m11_c34_guerres_civiles_romaines": {
        "module": 11, "ordre": 34,
        "titre": "Les Guerres Civiles Romaines — Dynamique et Leçons",
        "prereqs": ["m11_c17_premier_triumvirat", "m11_c18_octave_auguste"],
        "texte": """
Rome connaît six grandes séquences de guerres civiles entre -88 et +197.
Leur analyse révèle des mécanismes universels de décomposition institutionnelle.

SÉQUENCE 1 — MARIUS/SYLLA (-88 à -78) : première marche sur Rome d'une armée romaine.
Sylla établit un précédent : les institutions légales peuvent être brisées par la force
si on est assez fort. La légalité formelle perd son caractère sacré.

SÉQUENCE 2 — PREMIER TRIUMVIRAT/GUERRES CÉSARIENNES (-49 à -44) :
Les institutions républicaines ne peuvent plus arbitrer entre les puissances personnelles
(généraux avec armées loyales). Le conflit est inévitable car aucune règle commune n'est
reconnue. Jules César incarne le problème : légal dans ses victoires, illégal dans son retour.

SÉQUENCE 3 — GUERRES DES SUCCESSEURS DE CÉSAR (-44 à -31) :
Antoine vs Octave — le vainqueur prend tout. Actium (-31) règle la question par la force.
Octave/Auguste crée un système qui dure 200 ans... jusqu'à ce que le même problème resurgisse.

MÉCANISMES RÉCURRENTS :
1. Accumulation de pouvoirs informels qui contournent les institutions formelles.
2. Armée qui perd sa loyauté à l'État pour une loyauté personnelle au général.
3. Violence politique légitimée par des précédents : chaque escalade rend le suivant acceptable.
4. Absence d'un tiers arbitre reconnu par tous.
5. La loi devient un instrument des forts, non une contrainte sur eux.

ACTUALITÉ : ces mécanismes — défaillances institutionnelles graduelles, capture de l'armée,
violence légitimée, effacement de l'État de droit — sont analysés par les politologues
contemporains (Levitsky & Ziblatt, "How Democracies Die", 2018).
        """.strip(),
    },

    "m11_c35_alexandrie_science": {
        "module": 11, "ordre": 35,
        "titre": "Alexandrie — Science et Savoir dans l'Antiquité",
        "prereqs": ["m11_c9_hellénisme"],
        "texte": """
La Bibliothèque d'Alexandrie représente l'apogée intellectuel du monde antique.
Elle concentre le savoir de plusieurs civilisations et produit des avancées qui ne seront
retrouvées qu'à la Renaissance ou au XVIIe siècle.

LA BIBLIOTHÈQUE (-295 av. J.-C. – IIIe s. ap. J.-C.) : fondée par Ptolémée I sous l'impulsion
de Démétrios de Phalère (disciple d'Aristote). Au maximum, 400 000 à 700 000 rouleaux de papyrus.
Adjacent au Mouseion (temple des Muses) — première institution de recherche de l'histoire.
Les navires arrivant à Alexandrie devaient remettre leurs livres pour copie.

ERATOSTHÈNE (~276-194 av. J.-C.) : mesure la circonférence de la Terre avec des bâtons et des ombres.
Résultat : ~40 000 km — exact à 1% près. Calcule l'inclinaison de l'axe terrestre.
Dresse la première carte du monde avec méridiens et parallèles.

ÉRATOSTHÈNE, ARISTARQUE, HIPPARQUE : Aristarque propose l'héliocentrisme au IIIe s. av. J.-C.
— 1 800 ans avant Copernic. Hipparque calcule la distance Terre-Lune à 5% près.

ARCHIMÈDE DE SYRACUSE (~287-212 av. J.-C.) : principe d'Archimède (poussée), vis d'Archimède,
levier, calcul du π, méthode d'exhaustion (précurseur du calcul intégral). Tué par un soldat
romain pendant le sac de Syracuse.

EUCLIDE (~300 av. J.-C.) : "Éléments" — traité de géométrie utilisé comme manuel
jusqu'au XIXe siècle. Modèle de raisonnement déductif axiomatique.

FIN DE LA BIBLIOTHÈQUE : destruction progressive (César brûle une partie en -48?,
Théophile fait détruire le Serapeum en 391, conquête arabe en 641?). La réalité est complexe —
le déclin est graduel, pas une destruction unique.
        """.strip(),
    },

    "m11_c36_relecture_historionomique": {
        "module": 11, "ordre": 36,
        "titre": "Relecture Historionomique — Vérifier Fabry avec le Détail Historique",
        "prereqs": [
            "m11_c29_chute_rome_occident",
            "m11_c34_guerres_civiles_romaines",
            "m11_c31_causes_chute",
            "m10_c10_critique_historionomie",
        ],
        "texte": """
Maintenant que tu connais le détail historique, retournons à l'Historionomie de Philippe Fabry
pour vérifier ce que la théorie tient et ce qu'elle force.

CE QUE L'HISTOIRE CONFIRME :
1. La loi de la République libérale est descriptive, pas déterministe. Rome -509 à -133 est
   effectivement une période de liberté économique et d'expansion. Les Gracques ouvrent bien
   une ère de demandes redistributives. Le parallèle est heuristiquement utile.
2. La trajectoire République → guerres civiles → homme providentiel → principat formel est réelle.
   Auguste respecte la séquence de Fabry.
3. Le socialisme impérial (panem et circenses, contrôle des prix, dévaluation, corporatisme de Dioclétien)
   est bien documenté et a bien contribué à l'affaiblissement économique.

CE QUE L'HISTOIRE NUANCE :
1. La chute n'est pas inévitable à un moment précis. L'Empire d'Orient dure 1 000 ans de plus.
   La variable institutionnelle (Byzance maintient un État fort) compte énormément.
2. Les causes externes (Huns, Sassanides, pestes) ne sont pas réductibles à la logique interne.
   Fabry sous-estime la contingence — les invasions des Huns sont un choc exogène, pas une
   conséquence du "socialisme" romain.
3. La comparaison Rome/USA projette le schéma romain sur un contexte très différent :
   armes nucléaires, démocratie institutionnalisée, économie mondialisée, absence de frontières
   terrestres vulnérables analogues.

VERDICT : l'Historionomie est un cadre de lecture, pas une loi scientifique. Utilisée avec le
détail historique que tu as maintenant, elle aide à poser les bonnes questions — pas à prédire.
        """.strip(),
    },
})


# ══════════════════════════════════════════════════════════════════════════════
# MODULE 12 — APPRENTISSAGE MOTEUR
# Structure : Baccalauréat (1-10) / Maîtrise (11-19) / Doctorat (20-28)
# ══════════════════════════════════════════════════════════════════════════════

CURRICULUM.update({

    # ── BACCALAURÉAT — Fondements ─────────────────────────────────────────────

    "m12_c1_definition_champ": {
        "module": 12, "ordre": 1,
        "titre": "Définitions et champ d'étude — contrôle, apprentissage et développement moteur",
        "prereqs": [],
        "texte": """
Le champ de l'apprentissage moteur se subdivise en trois domaines distincts mais liés :

CONTRÔLE MOTEUR : étude des mécanismes (neuromusculaires, biomécaniques, cognitifs) qui permettent
d'exécuter un mouvement. Traite du «comment» du mouvement en temps réel. Ex : comment le cerveau
coordonne-t-il les segments du corps lors d'un lancer ?

APPRENTISSAGE MOTEUR : processus par lequel la pratique et l'expérience entraînent des changements
relativement permanents dans la capacité d'exécuter des habiletés motrices. Deux critères :
(1) changement observable dans la performance ; (2) relativement permanent (distingue l'apprentissage
de la fatigue ou de la chaleur corporelle).

DÉVELOPPEMENT MOTEUR : changements dans le comportement moteur tout au long de la vie, de l'enfance
à la vieillesse. Perspective longitudinale qui intègre la maturation et l'expérience.

HABILETÉ MOTRICE : action ou tâche nécessitant un mouvement volontaire du corps et/ou des membres
pour atteindre un but (Magill, 2017). Distinction : grossière (grands groupes musculaires — marche,
saut) vs fine (petits muscles — écriture, chirurgie) ; discrète (début et fin définis — lancer) vs
continue (cycle répété — natation) vs sérielle (séquence de discrètes — décollage aviateur).

PERFORMANCE vs APPRENTISSAGE : la performance (score observable à un moment donné) est une mesure
imparfaite de l'apprentissage. L'apprentissage se mesure via des tests de rétention (après délai
sans pratique) et de transfert (nouvelle variante). Un étudiant peut performer sans avoir appris
durablement.

AUTEURS CLÉS DU CHAMP : A.T. Welford (attention et motricité), Jack Adams (théorie en boucle
fermée, 1971), Richard Schmidt (théorie du schéma, 1975), Gabriele Wulf (focus attentionnel),
Karl Newell (approche par contraintes).
        """.strip(),
    },

    "m12_c2_stades_apprentissage": {
        "module": 12, "ordre": 2,
        "titre": "Les stades d'apprentissage moteur — Fitts & Posner (1967)",
        "prereqs": ["m12_c1_definition_champ"],
        "texte": """
Fitts & Posner (1967) proposent un modèle à trois stades décrivant la progression de l'apprenant :

STADE COGNITIF : l'apprenant essaie de comprendre la tâche. Nombreuses erreurs, grande variabilité,
performance lente et discontinue. Il mobilise beaucoup d'attention consciente («Où mettez-vous la
main ? Comment orienter le pied ?»). Verbalisation fréquente, stratégie par essais-erreurs. La
rétroaction (feedback) externe est cruciale à ce stade.

STADE ASSOCIATIF : l'apprenant raffine le patron moteur. Les erreurs diminuent, la performance
devient plus cohérente. L'attention se libère partiellement — on peut commencer à parler à l'apprenant
sans le faire trébucher. Le feedback interne (proprioception) devient plus utile. Stade le plus long.

STADE AUTONOME : le mouvement est largement automatisé. Peu d'attention consciente requise —
l'expert peut converser, scanner l'environnement, anticiper. La performance est rapide, fluide,
robuste sous pression. Erreurs peu fréquentes et auto-détectables.

LIMITES DU MODÈLE : (1) Les stades sont des descriptions phénoménologiques, non des catégories
neurales strictes. (2) Un expert peut régresser au stade cognitif sur une nouvelle variante.
(3) Pas de durée définie : certains atteignent l'autonomie en heures, d'autres jamais.

IMPLICATIONS PÉDAGOGIQUES : au stade cognitif, simplifier la tâche, donner des instructions
verbales claires et peu nombreuses. Au stade associatif, augmenter la complexité progressivement.
Au stade autonome, créer de la pression et de la variabilité pour consolider.

MODÈLE DE GENTILE (1972) : alternative en deux stades — (1) acquérir l'idée du mouvement, (2)
fixer et diversifier. Met davantage l'accent sur le rôle de l'environnement (stable/régulé vs
variable/aléatoire).
        """.strip(),
    },

    "m12_c3_feedback_types": {
        "module": 12, "ordre": 3,
        "titre": "Feedback : types, timing et fréquence dans l'apprentissage moteur",
        "prereqs": ["m12_c2_stades_apprentissage"],
        "texte": """
Le feedback (rétroaction) est toute information reçue après l'exécution d'une habileté motrice.

FEEDBACK INTRINSÈQUE (sensoriel) : information sensorielle générée par le corps lui-même — vision,
audition, proprioception, kinesthésie, toucher. Disponible naturellement pendant et après l'action.
Exemple : sensation musculaire en levant un poids, voir la trajectoire d'un lancer.

FEEDBACK EXTRINSÈQUE (augmenté) : information fournie par une source externe (entraîneur, vidéo,
capteur). Deux types :
- Connaissance des résultats (CR / knowledge of results, KR) : information sur l'effet du mouvement
  sur l'environnement. «La balle est tombée 2 mètres à gauche.»
- Connaissance de la performance (CP / knowledge of performance, KP) : information sur le patron de
  mouvement lui-même. «Ton coude s'élevait trop tôt.»

TIMING : feedback immédiat (avant l'estompage sensoriel) vs feedback différé (après délai). Un
délai modéré peut favoriser l'apprentissage — il force l'apprenant à traiter ses propres sensations
(hypothèse de la guidance). Feedback en temps réel («concurrent») peut créer une dépendance.

FRÉQUENCE : feedback fréquent (100% des essais) améliore la performance à court terme mais nuit à
l'apprentissage à long terme (Winstein & Schmidt, 1990). Le feedback réduit (50%, aléatoire,
moyenné) produit une meilleure rétention. Explications : (1) le feedback fréquent inhibe les
processus d'auto-évaluation ; (2) les essais sans feedback forcent un engagement plus profond.

ERREUR vs SUCCÈS : le feedback centré sur l'erreur («détection d'erreur») est souvent plus
informatif que la confirmation du succès. L'apprenant doit développer un «mécanisme de détection
d'erreur» interne (Adams, 1971).

BANDWIDTH FEEDBACK : ne donner de feedback que lorsque l'erreur dépasse un seuil («bandwidth»).
Les performances dans la zone acceptable ne reçoivent pas de feedback — favorise l'apprentissage.
        """.strip(),
    },

    "m12_c4_pratique_variabilite": {
        "module": 12, "ordre": 4,
        "titre": "Pratique bloquée, aléatoire et variable — effet d'interférence contextuelle",
        "prereqs": ["m12_c2_stades_apprentissage"],
        "texte": """
La structure de la pratique est l'une des variables les plus étudiées en apprentissage moteur.

PRATIQUE BLOQUÉE : répétition répétée d'une seule variante avant de passer à une autre.
Ex : 30 lancers à 3m, puis 30 lancers à 5m, puis 30 lancers à 7m. Performance excellente
en acquisition. Rétention et transfert médiocres.

PRATIQUE ALÉATOIRE : les variantes s'alternent de façon imprévisible.
Ex : lancer à 3m, 7m, 5m, 3m, 5m... Performance d'acquisition plus faible. Rétention et
transfert nettement supérieurs.

EFFET D'INTERFÉRENCE CONTEXTUELLE (Shea & Morgan, 1979) : le paradoxe selon lequel une condition
d'apprentissage plus difficile (aléatoire) produit un apprentissage plus profond. Explications :
(1) Hypothèse de l'élaboration : l'alternance force des comparaisons entre variantes, encodage
plus riche. (2) Hypothèse de la reconstruction : chaque essai aléatoire force à reconstruire le
plan d'action, ce qui consolide la représentation motrice.

PRATIQUE VARIABLE : variation des paramètres de la même classe de mouvement (distances, vitesses,
angles). Favorise la généralisation (schéma moteur, Schmidt 1975). Essentielle pour les habiletés
continues et ouvertes (sports, conduite).

PRATIQUE PARTIELLE vs ENTIÈRE : pratiquer les parties séparément (fractionné) vs la tâche complète.
Le découpage est efficace quand les parties sont peu interdépendantes. Pour les tâches à timing
intégré (nager, conduire), la pratique entière est souvent supérieure.

PART-PRACTICE METHODS : segmentation (séquence), fractionnement (parties en parallèle),
simplification (tâche complète mais réduite en difficulté).

APPLICATION : pour un novice, commencer par des variantes bloquées pour établir la base, puis passer
rapidement à la pratique variable et aléatoire pour ancrer l'apprentissage.
        """.strip(),
    },

    "m12_c5_schema_moteur_schmidt": {
        "module": 12, "ordre": 5,
        "titre": "Théorie du schéma moteur — Schmidt (1975)",
        "prereqs": ["m12_c4_pratique_variabilite"],
        "texte": """
La théorie du schéma moteur de Richard Schmidt (1975) est l'une des théories les plus influentes
du contrôle et de l'apprentissage moteur du XXe siècle.

PROBLÈME DE BERNSTEIN (1967) : le corps a un nombre quasi-infini de degrés de liberté (DoF).
Comment le système nerveux central choisit-il parmi des millions de solutions musculaires possibles
pour atteindre le même but ? Et comment un mouvement jamais pratiqué exactement peut-il être exécuté ?

PROGRAMME MOTEUR GÉNÉRALISÉ (PMG) : représentation abstraite en mémoire d'une classe de mouvements
(ex : «lancer en surcharge»). Le PMG encode les relations invariantes entre les composantes (ordre
des sous-mouvements, timing relatif, structure de force relative). Ce qui change selon le contexte :
les paramètres (vitesse globale, amplitude, force).

SCHÉMA DE RAPPEL : relation entre les paramètres utilisés et les résultats produits. Appris par
accumulation d'expériences variées. Permet de sélectionner les bons paramètres pour une nouvelle
situation. Plus la pratique est variée, plus le schéma est robuste.

SCHÉMA DE RECONNAISSANCE : relation entre les paramètres utilisés et les sensations attendues.
Permet de détecter les erreurs sans feedback externe (autoévaluation sensorielle).

IMPLICATIONS POUR LA PRATIQUE : la pratique variable est supérieure à la pratique constante pour
développer le schéma (d'où la recommandation d'alternance). La règle de la variabilité.

CRITIQUES : (1) Difficile à falsifier — les PMG sont des construits hypothétiques. (2) Ne rend
pas bien compte des mouvements de très longue durée. (3) L'approche des systèmes dynamiques
(Kelso, Thelen) remet en question la nécessité d'un «programme» central.

HÉRITAGE : malgré les critiques, le PMG reste un outil conceptuel utile dans l'enseignement et
la recherche appliquée.
        """.strip(),
    },

    "m12_c6_memoire_motrice": {
        "module": 12, "ordre": 6,
        "titre": "Mémoire motrice — procédurale, déclarative, consolidation et rétention",
        "prereqs": ["m12_c5_schema_moteur_schmidt"],
        "texte": """
L'apprentissage moteur produit des changements en mémoire à long terme. Comprendre ces systèmes
est essentiel pour structurer l'enseignement et la réhabilitation.

MÉMOIRE DÉCLARATIVE (explicite) : faits et événements. «Savoir que». Accessible à la conscience.
Dépend de l'hippocampe. Ex : savoir qu'on doit plier le genou lors d'un atterrissage.

MÉMOIRE PROCÉDURALE (implicite) : habiletés et habitudes. «Savoir comment». Difficile à verbaliser.
Dépend des ganglions de la base, du cervelet, du cortex moteur. Ex : faire du vélo, taper au clavier.
Robuste à l'amnésie antérograde (les patients amnésiques apprennent quand même les habiletés motrices).

DISTINCTION FONCTIONNELLE : au stade cognitif, l'apprenant utilise la mémoire déclarative pour
guider le mouvement. À mesure que l'habileté est automatisée, le contrôle passe à la mémoire
procédurale. Trop verbaliser une habileté automatisée peut la dégrader («paradoxe de l'explicitation»).

CONSOLIDATION : processus par lequel une représentation motrice en mémoire se stabilise et devient
résistante à l'interférence. Se produit principalement pendant le sommeil (réactivations au stade
NREM). Implications : ne pas enchaîner deux habiletés nouvelles sans pause ; le sommeil post-
apprentissage est bénéfique.

RÉTENTION : mesure de l'apprentissage après un délai sans pratique. Test de rétention standard :
24-48h à plusieurs semaines. La pratique distribuée (sessions courtes espacées) produit une meilleure
rétention que la pratique massiée (longue session unique).

EFFET D'ESPACEMENT (spacing effect) : l'une des découvertes les plus robustes en sciences de
l'apprentissage. S'applique aux habiletés motrices comme aux connaissances déclaratives.

OUBLI MOTEUR : les habiletés motrices bien apprises (ex : vélo, natation) résistent remarquablement
à l'oubli sur de longues périodes — contrairement à la mémoire déclarative.
        """.strip(),
    },

    "m12_c7_transfert_apprentissage": {
        "module": 12, "ordre": 7,
        "titre": "Transfert d'apprentissage — conditions, directions et limites",
        "prereqs": ["m12_c6_memoire_motrice"],
        "texte": """
Le transfert d'apprentissage désigne l'influence de la pratique d'une habileté sur l'apprentissage
ou la performance d'une autre habileté.

TYPES DE TRANSFERT :
- Positif : la pratique de A facilite l'apprentissage de B. Ex : tennis → squash (structure
  de frappe similaire).
- Négatif : la pratique de A nuit à l'apprentissage de B. Ex : conduire en Europe vs en Angleterre
  (côté de la route), certains mouvements de ski → snowboard.
- Nul : aucune influence.
- Bilatéral (intermanuel) : entraîner le membre dominant améliore le membre non-dominant, et
  vice versa. Base du «cross-education» en réhabilitation.

THÉORIES DU TRANSFERT :
- Théorie des éléments identiques (Thorndike) : transfert proportionnel au nombre d'éléments
  communs entre les deux tâches. Très descriptive, peu prédictive.
- Théorie du schéma (Schmidt) : le transfert dépend de la généralité du schéma moteur.
  Pratique variable → schéma plus généralisable → meilleur transfert.
- Approche écologique : transfert si les affordances perceptivo-motrices sont similaires.

CONDITIONS FAVORISANT LE TRANSFERT : similarité des exigences perceptuelles (pas seulement motrices),
de la structure temporelle, de l'environnement décisionnel. Ex : simulateurs de vol — plus le
simulateur reproduit les décisions contextuelles, plus le transfert est fort.

SPÉCIFICITÉ DE L'ENTRAÎNEMENT (Specificity of Training, SAID) : on s'améliore surtout dans les
conditions exactes d'entraînement. Principe capital en préparation physique et réhabilitation.
Tension constante entre spécificité et variabilité.

TRANSFERT À LONG TERME vs COURT TERME : un entraînement croisé (ex : tennis pour améliorer le
badminton) peut créer du transfert initial mais diverger sur le long terme si les exigences
spécifiques ne sont pas travaillées.
        """.strip(),
    },

    "m12_c8_controle_ouvert_ferme": {
        "module": 12, "ordre": 8,
        "titre": "Contrôle en boucle ouverte et fermée — Adams (1971) et les limites du feedback",
        "prereqs": ["m12_c3_feedback_types"],
        "texte": """
Deux grands modes de contrôle moteur coexistent selon la durée du mouvement et la disponibilité
du feedback sensoriel :

CONTRÔLE EN BOUCLE FERMÉE (closed-loop) : le système nerveux utilise le feedback sensoriel continu
pour corriger le mouvement en cours d'exécution. Analogie du thermostat. Nécessite un délai de
traitement (~150-200ms pour les corrections visuelles, ~50-100ms pour les corrections
proprioceptives). Adéquat pour les mouvements lents (< 200ms total) ou les ajustements fins.

CONTRÔLE EN BOUCLE OUVERTE (open-loop) : le programme moteur est lancé et exécuté sans utilisation
de feedback pour le corriger. Le mouvement est trop rapide pour que le cerveau traite et intègre
le feedback. Ex : frapper une balle de baseball (150-250ms) — impossible de corriger après initiation.

THÉORIE DE ADAMS (1971) — Boucle fermée : propose deux traces en mémoire :
(1) La trace de mémoire (memory trace) : initie le mouvement.
(2) La trace perceptive (perceptual trace) : représentation du mouvement correct (construite par
pratique), sert de référence pour détecter les erreurs. Critique reçue : ne rend pas bien compte
des mouvements très rapides.

TEMPS DE RÉACTION vs TEMPS DE MOUVEMENT : le TR inclut le délai de traitement central. Pour
les mouvements de moins de 200ms, le feedback est pratiquement inutile pour corriger le mouvement
(simple time RT ~180-220ms). Le cerveau doit planifier à l'avance.

CONTRÔLE EN CASCADE et CORRECTIONS BALISTIQUES : pour des mouvements de durée intermédiaire,
des corrections sub-conscientes sont possibles via des boucles proprioceptives courtes (spinales
ou sous-corticales) — plus rapides que les corrections corticales.

IMPLICATIONS : les sports à geste rapide (combat, ballon) requièrent une planification anticipatoire
(feedforward). L'entraînement doit développer la reconnaissance des patterns pré-mouvement
(lecture du jeu, anticipation).
        """.strip(),
    },

    "m12_c9_focus_attentionnel": {
        "module": 12, "ordre": 9,
        "titre": "Focus attentionnel — interne vs externe (Wulf et al.)",
        "prereqs": ["m12_c2_stades_apprentissage"],
        "texte": """
La direction de l'attention de l'apprenant pendant la pratique a un effet considérable sur
l'apprentissage et la performance. Les travaux de Gabriele Wulf (depuis 1998) ont transformé
les recommandations pédagogiques dans ce domaine.

FOCUS INTERNE : l'attention est dirigée vers les mouvements du corps lui-même. Ex : «Contracte tes
fessiers», «Plie le genou», «Garde le coude haut». Les instructions traditionnelles des entraîneurs
sont souvent de nature interne.

FOCUS EXTERNE : l'attention est dirigée vers l'effet du mouvement sur l'environnement ou un objet.
Ex : «Vise la cible», «Pousse le sol», «Lance la balle vers le carré blanc».

HYPOTHÈSE DE L'ACTION CONTRAINTE (Constrained Action Hypothesis, Wulf 2001) : le focus interne
«contraindrait» le système moteur en le soumettant à un contrôle conscient, perturbant les
processus automatisés. Le focus externe permettrait au système de se réguler de manière plus
automatique et efficiente.

RÉSULTATS EMPIRIQUES : une méta-analyse (Wulf et al.) montre que le focus externe améliore
la précision, la force, l'endurance, et favorise l'apprentissage à long terme dans la grande majorité
des études. Effets observés en golf, natation, réhabilitation, tir, saut, équilibre.

NUANCES : l'effet est plus fort pour les apprenants intermédiaires/avancés que pour les novices
stricts (au stade cognitif, l'attention interne peut être nécessaire pour établir la représentation
de base). La distance du focus externe compte — trop loin peut devenir abstrait.

ANALOGIES ET MÉTAPHORES : les instructions par analogie («imagine que tu tires une corde» pour
le mouvement de nage) créent un focus quasi-externe tout en encodant la structure du mouvement.

APPLICATIONS PRATIQUES : reformuler les instructions d'entraînement : passer de «garde le coude
haut» à «envoyez la balle dans le coin supérieur». Utiliser des marqueurs visuels dans l'environnement.
        """.strip(),
    },

    "m12_c10_observation_apprentissage": {
        "module": 12, "ordre": 10,
        "titre": "Apprentissage par observation — démonstration, neurones miroirs et modèles",
        "prereqs": ["m12_c2_stades_apprentissage", "m12_c9_focus_attentionnel"],
        "texte": """
L'apprentissage vicariant (par observation) est un mécanisme puissant et sous-exploité dans
la pédagogie motrice.

EFFICACITÉ DE LA DÉMONSTRATION : regarder un modèle exécuter une habileté accélère l'apprentissage,
en particulier au stade cognitif. La démonstration fournit une «idée du mouvement» (Gentile) que
l'apprenant peut imiter. Elle est souvent plus efficace que les instructions verbales seules.

MODÈLE EXPERT vs APPRENANT : un modèle expert montre le résultat cible. Un modèle apprenant
(qui commet des erreurs et les corrige) peut être aussi efficace ou plus pour certaines populations,
car l'observateur traite activement les erreurs et les solutions. Le «learning model» est
particulièrement utile au stade associatif.

NEURONES MIROIRS (Rizzolatti, 1992) : découverts chez le macaque, ces neurones s'activent à la
fois lors de l'exécution d'une action et lors de l'observation de la même action chez un congénère.
Chez l'humain, des systèmes analogues ont été identifiés via IRMf — implication dans l'imitation,
la compréhension des actions, l'empathie. Rôle direct dans l'apprentissage par observation encore
débattu.

APPRENTISSAGE PAR VIDÉO : la démonstration en vidéo (ralentie, annotée, multiples angles) est
efficace pour les habiletés complexes. Permet une analyse détaillée, un retour à tout moment.
La réalité virtuelle peut simuler des perspectives à la première personne.

POINT DE VUE : la démonstration en perspective à la première personne peut être plus informative
que la troisième personne pour des mouvements de précision (ex : chirurgie, golf).

DIRECTIVES D'ATTENTION PENDANT L'OBSERVATION : orienter l'attention de l'observateur vers les
indices pertinents du modèle (focus externe) améliore la rétention. «Regarde où la balle quitte
la main» plutôt que «regarde le bras».

PRATIQUE MENTALE COUPLÉE : alterner observation et pratique physique est plus efficace que l'un
ou l'autre seul pour les habiletés nouvelles.
        """.strip(),
    },

    # ── MAÎTRISE — Approfondissement ─────────────────────────────────────────

    "m12_c11_systemes_dynamiques": {
        "module": 12, "ordre": 11,
        "titre": "Théorie des systèmes dynamiques appliquée au mouvement — Bernstein, Kelso, Thelen",
        "prereqs": ["m12_c5_schema_moteur_schmidt", "m12_c8_controle_ouvert_ferme"],
        "texte": """
La théorie des systèmes dynamiques (TSD) offre une alternative radicale aux théories cognitivistes
du contrôle moteur. Elle traite le corps en mouvement comme un système physique complexe
soumis à des lois dynamiques, sans nécessiter de «représentation centrale».

NIKOLAÏ BERNSTEIN (1896-1966) : pionnier soviétique. Problème des degrés de liberté — le corps
possède un nombre extraordinaire de DDL (articulations × muscles). La solution biomécanique n'est
pas unique. Bernstein observe que les trajectoires d'outils sont plus stables que les trajectoires
articulaires (organisation autour des effets, pas des commandes musculaires).

ATTRACTEURS ET PAYSAGES ÉNERGÉTIQUES : un système dynamique tend vers des états stables appelés
attracteurs. Le mouvement humain naturel présente des attracteurs (ex : la marche à ~1,3 m/s).
Une perturbation légère retourne à l'attracteur ; une perturbation forte peut pousser vers un autre
attracteur (transition de phase).

TRANSITIONS DE PHASE (Kelso, 1984) : expérience classique avec les doigts — à basse fréquence,
oscillation en antiphase (IA→ib, IB→ia) ; à haute fréquence, transition spontanée vers la phase
(les deux doigts ensemble). Le système «tombe» dans un autre attracteur sans instruction consciente.

PARAMÈTRE DE CONTRÔLE vs VARIABLE D'ORDRE : le paramètre de contrôle (ex : vitesse) crée la
bifurcation sans encoder le comportement cible. La variable d'ordre (ex : la relation de phase)
capture l'état macroscopique du système.

ESTHER THELEN : applique la TSD au développement moteur de l'enfant. La marche ne «attend» pas
la maturation corticale — elle émerge de l'interaction entre le tonus musculaire, la masse des
membres, l'environnement, et la gravité. Réfute les stades innés rigides.

IMPLICATIONS : l'apprentissage moteur n'est pas l'installation d'un programme — c'est le
remodelage du paysage des attracteurs par la pratique. La variabilité du mouvement n'est pas
un «bruit» à éliminer, mais une propriété fonctionnelle du système.
        """.strip(),
    },

    "m12_c12_approche_ecologique": {
        "module": 12, "ordre": 12,
        "titre": "Approche écologique-dynamique — affordances, contraintes et Newell (1986)",
        "prereqs": ["m12_c11_systemes_dynamiques"],
        "texte": """
L'approche écologique-dynamique (AED) intègre la psychologie écologique de J.J. Gibson et la
théorie des systèmes dynamiques de Bernstein pour proposer une vision relationnelle de la
perception-action.

AFFORDANCES (Gibson, 1979) : propriétés fonctionnelles de l'environnement relative aux capacités
d'action d'un organisme. Une marche d'escalier «affordance» la montée si les proportions corps-
marche le permettent. Les affordances ne sont ni dans l'environnement ni dans l'organisme — elles
sont dans la relation. L'apprenant perçoit directement les opportunités d'action, sans médiation
symbolique.

MODÈLE DE CONTRAINTES (Newell, 1986) : le comportement moteur émerge de l'interaction de trois
catégories de contraintes :
(1) Contraintes de l'organisme : morphologie, masse, force musculaire, niveau d'habileté.
(2) Contraintes de la tâche : règles, but, objet manipulé, équipement.
(3) Contraintes de l'environnement : gravité, température, surface, pression sociale.

L'entraîneur/pédagogue agit en manipulant les contraintes de tâche et d'environnement pour guider
le comportement vers des solutions fonctionnelles sans prescrire le mouvement exact.

REPRESENTATIVE LEARNING DESIGN (Brunswik, repris par Araújo & Davids) : l'entraînement doit
reproduire les couplages perception-action présents dans la performance cible. Un exercice décontextualisé
(geste technique sans décision) peut ne pas transférer.

IMPLICATIONS PRATIQUES : plutôt qu'enseigner «la bonne technique», manipuler les contraintes pour
que l'apprenant découvre lui-même les solutions efficaces (differential learning, Schöllhorn).
Ex : varier la taille de la cible, le poids de l'outil, la surface.

CRITIQUES : l'AED est puissante pour les sports ouverts et continus, mais moins développée pour
les tâches sérielles précises ou la chirurgie. La manipulation de contraintes demande une expertise
pédagogique élevée.
        """.strip(),
    },

    "m12_c13_apprentissage_implicite_explicite": {
        "module": 12, "ordre": 13,
        "titre": "Apprentissage implicite vs explicite — dissociation, robustesse et désinhibition",
        "prereqs": ["m12_c6_memoire_motrice", "m12_c9_focus_attentionnel"],
        "texte": """
La distinction entre apprentissage implicite et explicite est fondamentale pour comprendre comment
les habiletés motrices s'automatisent et résistent au stress.

APPRENTISSAGE EXPLICITE : l'apprenant acquiert des règles conscientes et verbalisa bles sur la façon
d'exécuter le mouvement. Rapide à acquérir, mais vulnerable sous pression : la conscience des règles
peut interférer avec l'exécution automatique («choking under pressure»).

APPRENTISSAGE IMPLICITE (Reber, 1967) : l'apprenant acquiert des régularités du mouvement sans
conscience des règles. Lent à acquérir, mais robuste sous pression, sous fatigue cognitive, et
chez des populations avec déficits de la mémoire de travail.

PARADIGME D'APPRENTISSAGE IMPLICITE EN SPORT : utiliser des analogies («imagine que tu tiens
un plateau» pour le lancer franc au basketball), des doubles tâches (compter mentalement pendant
la pratique), ou contraindre les capacités de travail sur les règles.

ROBUSTESSE PSYCHOLOGIQUE : l'apprentissage implicite résiste à l'anxiété compétitive. Un athlète
avec une base implicite solide ne «réanalyse» pas son geste sous pression. Maxwell, Masters & Eves
(2000) : apprentissage implicite au tennis → meilleure performance sous pression que l'explicite.

REINVESTISSEMENT (Masters, 1992) : tendance à réinvestir consciemment les règles explicites apprises
sous stress. Le «reinvestissement» perturbe les processus automatiques. Outil de mesure :
le Reinvestment Scale.

DOUBLE TÂCHE : si la performance motrice se dégrade lorsqu'une tâche cognitive secondaire est
imposée, cela suggère que la tâche motrice utilise encore des ressources attentionnelles
(peu automatisée). Mesure l'automatisation.

IMPLICATIONS CLINIQUES : en réhabilitation neurologique, les patients avec lésions du striatum
peuvent apprendre implicitement des séquences motrices malgré l'absence d'apprentissage
déclaratif associé.
        """.strip(),
    },

    "m12_c14_imagerie_mentale": {
        "module": 12, "ordre": 14,
        "titre": "Imagerie mentale et pratique imaginée — mécanismes et efficacité",
        "prereqs": ["m12_c6_memoire_motrice", "m12_c10_observation_apprentissage"],
        "texte": """
L'imagerie mentale motrice — visualiser l'exécution d'un mouvement sans le réaliser physiquement —
est un outil d'entraînement dont l'efficacité est documentée depuis les années 1960.

DÉFINITION : simulation mentale d'un mouvement ou d'une séquence d'actions. Se distingue de la
visualisation passive (regarder mentalement un film de soi) par l'aspect kinesthésique — imaginer
les sensations musculaires, la proprioception, l'effort.

PERSPECTIVE INTERNE vs EXTERNE : interne — «je vois par mes propres yeux» ; externe — «je me vois
de l'extérieur, comme sur une caméra». Les deux ont leurs avantages ; la perspective interne est
plus kinesthésique et souvent plus efficace pour des gestes précis.

THÉORIE PSYCHONEURALE MOTRICE (Jacobson, 1932) : l'imagerie mentale produit des micro-contractions
musculaires enregistrables par EMG. Les programmes moteurs sont partiellement activés sans
mouvement observable.

NEUROIMAGERIE : lors de l'imagerie motrice, des régions similaires au mouvement réel s'activent —
cortex prémoteur, cortex moteur supplémentaire, cervelet (Decety, 1996). Le cervelet contribue
à la précision temporelle de l'image mentale.

EFFICACITÉ : méta-analyses (Driskell, Copper & Moran, 1994 ; Cumming & Williams, 2012) :
l'imagerie est plus efficace que l'absence de pratique, moins efficace que la pratique physique,
mais la combinaison imagerie + pratique physique est souvent supérieure à la pratique physique seule.
Efficacité maximale pour les composantes cognitives de la tâche (précision, séquence) vs motrices
(force, vitesse).

CONDITIONS OPTIMALES : durée d'imagerie ≈ durée réelle du mouvement (imagerie rapide = moins
efficace) ; état de relaxation modéré ; alto niveau de vivacité (vividness) de l'image.

PIPP (PETTLEP) : modèle de Holmes & Collins (2001) — Physical, Environment, Task, Timing, Learning,
Emotion, Perspective. Maximise la correspondance fonctionnelle entre l'image et le réel.
        """.strip(),
    },

    "m12_c15_expertise_deliberate_practice": {
        "module": 12, "ordre": 15,
        "titre": "Expertise et pratique délibérée — Ericsson et le débat des 10 000 heures",
        "prereqs": ["m12_c4_pratique_variabilite", "m12_c6_memoire_motrice"],
        "texte": """
Comment devient-on expert ? La recherche d'Ericsson sur l'expertise motrice et cognitive a
dominé le débat depuis les années 1990.

PRATIQUE DÉLIBÉRÉE (Ericsson, Krampe & Tesch-Römer, 1993) : activité structurée, spécifiquement
conçue pour améliorer la performance. Caractéristiques : (1) tâches légèrement au-delà du niveau
actuel («zone proximale de développement», Vygotsky) ; (2) feedback immédiat et informatif ;
(3) répétition et correction ; (4) supervision par un expert. Vs pratique simple (jouer sans
objectif) et jeu (plaisir sans objectif de performance).

VIOLONISTES DE BERLIN (étude fondatrice) : Ericsson identifie que les meilleurs étudiants
accumulent ~10 000h de pratique délibérée à 20 ans, vs ~4 000h pour les moins bons. Le talent
«inné» non corroboré : c'est la pratique qui distingue. Popularisé (et simplifié) par Malcolm
Gladwell dans «Outliers» (2008).

REPRÉSENTATION MENTALE EXPERTE : l'expert dispose de représentations mentales élaborées qui
permettent d'anticiper, de détecter les erreurs, et de planifier. L'apprentissage délibéré
construit ces représentations (vs la pratique répétitive qui automatise sans les enrichir).

CRITIQUES ET LIMITES :
(1) Macnamara et al. (2014, méta-analyse) : la pratique délibérée explique ~18-26% de la variance
de performance en sport (moins que présenté). Rôle des facteurs génétiques, de l'âge de début, etc.
(2) Early Specialization vs Late Specialization : se spécialiser tôt (enfance) peut produire
de l'épuisement et des blessures de surutilisation ; la diversification précoce suivie de
spécialisation tardive (Early Diversification, Côté & Fraser-Thomas) est souvent supérieure.
(3) La pratique délibérée n'est pas la seule voie : pour certaines disciplines (ex : hockey de rue),
la pratique de jeu délibéré est aussi efficace.

CONTRIBUTIONS DURABLES : le concept met fin au déterminisme génétique naïf et justifie
l'investissement pédagogique. La structure de la pratique (feedback, difficulté, réflexion) compte.
        """.strip(),
    },

    "m12_c16_neuroplasticite_motrice": {
        "module": 12, "ordre": 16,
        "titre": "Neuroplasticité motrice — réorganisation corticale et apprentissage",
        "prereqs": ["m12_c6_memoire_motrice", "m12_c15_expertise_deliberate_practice"],
        "texte": """
Le cerveau se remodèle structurellement et fonctionnellement en réponse à l'apprentissage moteur.
La compréhension de ce phénomène a des implications profondes pour l'entraînement et la réhabilitation.

PLASTICITÉ USE-DEPENDENT : les connexions synaptiques se renforcent selon la règle hebbienne
(«neurons that fire together, wire together»). La pratique répétée consolide les synapses qui
médient les mouvements appris.

RÉORGANISATION CORTICALE : l'homoncule moteur (Penfield) n'est pas fixe. La pratique intensive
d'un doigt ou d'une main augmente la représentation corticale de cette partie dans le cortex moteur
primaire (M1). Étude de Elbert et al. (1995) : les violonistes ont une représentation plus grande
de leur main gauche (doigts) que les non-musiciens.

PLASTICITÉ SOMATOSENSORIELLE : les cortex somatosensoriels (S1, S2) se réorganisent parallèlement.
L'expertise tactile (chirurgiens, musiciens) est associée à une expansion des représentations
digitales.

LONG-TERM POTENTIATION (LTP) : mécanisme cellulaire de la plasticité — stimulation répétée d'une
synapse → augmentation durable de l'efficacité synaptique (via AMPA/NMDA). Base cellulaire de
l'apprentissage moteur et de la mémoire.

PÉRIODES CRITIQUES ET SENSIBLES : certaines capacités motrices (ex : vision binoculaire, accent
natif) bénéficient de fenêtres de plasticité préférentielle. Après la période critique, la plasticité
n'est pas nulle — elle est réduite. En dehors des périodes critiques, la plasticité reste possible
chez l'adulte mais nécessite des conditions spécifiques (attention, motivation, dopamine).

PLASTICITÉ POST-LÉSIONNELLE : après AVC ou lésion médullaire partielle, le cortex adjacent ou
l'hémisphère controlatéral peut prendre en charge certaines fonctions. La réhabilitation intensive
précoce exploite cette fenêtre de plasticité accrue post-lésion.

IMPLICATIONS : l'entraînement moteur n'est pas seulement musculaire ou technique — c'est une
intervention neurologique. La qualité et la structure de la pratique ont des effets durables sur
l'architecture cérébrale.
        """.strip(),
    },

    "m12_c17_modeles_computationnels": {
        "module": 12, "ordre": 17,
        "titre": "Modèles computationnels du contrôle moteur — contrôleurs forward et inverse (Wolpert)",
        "prereqs": ["m12_c8_controle_ouvert_ferme", "m12_c11_systemes_dynamiques"],
        "texte": """
Les modèles computationnels du contrôle moteur tentent de formaliser mathématiquement comment le
cerveau planifie et exécute les mouvements. Wolpert & Kawato (1998) proposent l'architecture MOSAIC.

MODÈLE INTERNE : représentation interne des propriétés dynamiques du corps et de l'environnement
(masse des membres, gravité, friction). Permet de simuler le comportement du système sans le bouger.

CONTRÔLEUR FORWARD (prédictif) : prédit les conséquences sensorielles et motrices d'une commande.
Si je commande «fléchir le coude à 90°», le modèle forward prédit la position et les forces résultantes.
Permet d'anticiper le feedback et de ne pas attendre les informations sensorielles (trop lentes).

CONTRÔLEUR INVERSE : calcule les commandes motrices nécessaires pour atteindre un état désiré.
Input : état actuel + état cible. Output : commandes musculaires. Problème : il n'existe souvent
pas de solution unique (redondance).

COPIE D'EFFÉRENCE (Helmholtz, Von Holst) : une copie du signal moteur envoyé aux muscles est
aussi envoyée en interne. Cette copie permet de prédire le feedback sensoriel attendu et de
distinguer les changements sensoriels auto-induits vs externes. Fondement de la distinction
«ma main bouge» vs «le monde bouge». Déficit dans la schizophrénie (hallucinations).

ARCHITECTURE MOSAIC (Mixture Of Experts, Wolpert & Kawato, 1998) : ensemble de paires
«modèle forward + contrôleur inverse» spécialisés. Un méta-contrôleur choisit le module compétent
selon le contexte. L'apprentissage = ajustement des poids du méta-contrôleur et des modèles.

OPTIMALITÉ ET THÉORIE DU CONTRÔLE OPTIMAL : le cerveau minimiserait un coût combinant l'effort
musculaire et la variance du mouvement (Scott, 2004 ; Todorov & Jordan, 2002). La trajectoire
observée correspond souvent à l'optimum prédit — élégance mathématique, mais biologiquement débattu.

LIMITES : les modèles computationnels sont puissants mais abstraits. Ils peinent à rendre compte
de l'embodiment, des émotions, et de l'environnement social.
        """.strip(),
    },

    "m12_c18_copie_efference_prediction": {
        "module": 12, "ordre": 18,
        "titre": "Copie d'efférence, prédiction sensorielle et cerveau prédictif",
        "prereqs": ["m12_c17_modeles_computationnels"],
        "texte": """
Le concept de copie d'efférence (efference copy) et de signal de corollaire est central à la
compréhension de la perception-action. Il illustre comment le cerveau prédit ses propres actions.

SIGNAL DE COROLLAIRE (corollary discharge) : copie interne du signal moteur («command efférente»)
envoyée à d'autres centres neuraux simultanément à l'envoi vers les muscles. Permet de comparer
le feedback sensoriel attendu (prédiction) vs reçu (réalité).

ANNULATION DE L'AUTO-STIMULATION : nous ne nous chatouillons pas nous-mêmes — le signal de
corollaire prédit la sensation tactile auto-induite et l'inhibe. Une perturbation de ce mécanisme
(schizophrénie) peut rendre les auto-stimulations perçues comme externes (hallucinations tactiles).

STABILITÉ DU MONDE PERÇU : quand nous bougeons les yeux (saccade), le monde ne semble pas sauter.
La copie d'efférence de la commande oculaire prédit le déplacement de l'image rétinienne, permettant
la stabilité perceptuelle («compensation saccadique»).

CERVEAU PRÉDICTIF (Predictive Processing, Clark & Friston) : cadre théorique général selon lequel
le cerveau est fondamentalement une machine prédictive qui minimise en permanence ses «erreurs de
prédiction». Les signaux sensoriels ne remontent pas simplement vers le cortex — ils sont comparés
à des prédictions descendantes («top-down»). Ce qui atteint la conscience est l'erreur résiduelle.

HIERARCHIE PRÉDICTIVE : chaque niveau du cerveau prédit les activités des niveaux inférieurs.
Le niveau supérieur corrige les prédictions du niveau inférieur. L'apprentissage = mise à jour
des modèles génératifs du cerveau pour réduire les erreurs de prédiction futures.

SURPRISE (surprisal) et ÉNERGIE LIBRE (Friston) : formulation mathématique — le cerveau minimise
l'«énergie libre» (borne supérieure de la surprise). Actions et perceptions servent toutes deux
à minimiser la surprise par rapport aux prédictions du modèle interne. Le mouvement devient
une manière d'aller «vérifier» ses prédictions.

IMPLICATIONS POUR L'APPRENTISSAGE MOTEUR : apprendre = développer de meilleures prédictions.
L'erreur de prédiction est le signal d'apprentissage (comme le signal de «reward prediction error»
dopaminergique dans l'apprentissage par renforcement).
        """.strip(),
    },

    "m12_c19_variabilite_mouvement": {
        "module": 12, "ordre": 19,
        "titre": "Variabilité du mouvement — bruit fonctionnel, stochastique resonance et rôle adaptatif",
        "prereqs": ["m12_c11_systemes_dynamiques", "m12_c17_modeles_computationnels"],
        "texte": """
La variabilité dans le mouvement humain a longtemps été considérée comme du «bruit» ou une
imperfection à éliminer. La recherche contemporaine révèle un tableau beaucoup plus nuancé.

SOURCES DE VARIABILITÉ : (1) Bruit neural — variabilité aléatoire dans le taux de décharge des
neurones. (2) Variabilité mécanique — propriétés élastiques variables des muscles/tendons.
(3) Variabilité de planification — différentes solutions sélectionnées d'un essai à l'autre.

THÉORÈME DE DEMPSTER-SHAFER appliqué au mouvement : pour une tâche donnée, il existe un «espace
de solutions» (manifold) où les performances sont équivalentes. La variabilité dans cet espace
est non-nuisible («good variability»), contrairement à la variabilité dans les directions qui
dégradent la performance («bad variability»). Latash et al., «Uncontrolled Manifold Hypothesis» (UCM).

DIFFERENTIAL LEARNING (Schöllhorn) : introduire délibérément une grande variabilité dans la
pratique (charges, angles, vitesses différents à chaque essai) accélère l'apprentissage chez
certains apprenants. Hypothèse : la variabilité force l'exploration du paysage des attracteurs
et l'auto-organisation. Données prometteuses en football et natation.

STOCHASTIC RESONANCE (résonance stochastique) : paradoxalement, ajouter du bruit à certains
systèmes non-linéaires peut améliorer leur sensibilité aux signaux faibles. Application en
proprioception : une vibration sous-sensorielle du tendon d'Achille améliore l'équilibre chez les
personnes âgées (Collins et al.). Suggère que le bruit n'est pas toujours l'ennemi.

INDICE DE VARIABILITÉ vs PERFORMANCE : chez l'expert, on observe souvent moins de variabilité
dans la variable de résultat (performance) mais une variabilité interne préservée des compensations
inter-articulaires. L'expert est stable dans ce qui compte, flexible dans le reste.

VIEILLISSEMENT : la variabilité motrice augmente avec l'âge (dégradation du bruit neural), mais
la variabilité «saine» (des compensations) diminue. Les personnes âgées deviennent moins flexibles
pour absorber les perturbations.
        """.strip(),
    },

    # ── DOCTORAT — Frontières de la recherche ─────────────────────────────────

    "m12_c20_cerveau_bayesien_controle": {
        "module": 12, "ordre": 20,
        "titre": "Inférence bayésienne et cerveau prédictif dans le contrôle moteur (Körding & Wolpert)",
        "prereqs": ["m12_c17_modeles_computationnels", "m12_c18_copie_efference_prediction"],
        "texte": """
Le cadre bayésien formalise la façon dont le cerveau intègre des informations incertaines pour
produire des estimations et des décisions motrices optimales.

THÉORÈME DE BAYES APPLIQUÉ À LA PERCEPTION-ACTION : l'estimation d'un état (ex : position d'un
membre) combine un prior (connaissance a priori sur les positions probables) et une vraisemblance
(information sensorielle disponible). L'estimée a posteriori est une moyenne pondérée où le poids
de chaque source est inversement proportionnel à sa variance.

EXPÉRIENCE DE KÖRDING & WOLPERT (2004) : sujets attrapant une balle avec feedback visuel bruité.
Les sujets intègrent le prior spatial (distribution de départ des balles) et le feedback sensoriel
précisément comme prédit par l'inférence bayésienne — démonstration directe de la statistique
bayésienne dans le contrôle moteur humain.

INTÉGRATION MULTISENSORIELLE (Ernst & Banks, 2002) : la pondération entre vision et proprioception
pour estimer la position d'un membre suit la règle bayésienne — la source la plus fiable (moindre
variance) est pondérée plus fortement. Maximise la précision de l'estimé combiné.

FILTRE DE KALMAN : modèle computationnel optimal pour estimer l'état d'un système dynamique à
partir d'observations bruitées. Appliqué au système moteur : le cervelet pourrait implémenter
quelque chose d'analogue pour estimer l'état du corps entre deux mesures sensorielles.

INCERTITUDE ET EXPLORATION : dans un cadre bayésien, l'exploration (tenter de nouvelles solutions)
est rationalement motivée quand l'incertitude sur le modèle du monde est élevée. L'apprentissage
peut être vu comme une réduction de l'incertitude sur le modèle génératif.

PRIOR MOTEUR : les humains ont des priors sur les mouvements «naturels» (ex : mouvements lents
sont moins coûteux). Ces priors biaisent la perception et l'action. Manipulation expérimentale
du prior → changements prévisibles du comportement moteur.

LIMITES : le cerveau «approxime» le calcul bayésien — il ne fait pas de probabilités exactes.
Les heuristiques et biais cognitifs coexistent avec la rigueur bayésienne.
        """.strip(),
    },

    "m12_c21_bases_neurales_circuit": {
        "module": 12, "ordre": 21,
        "titre": "Bases neurales du contrôle moteur — cortex, cervelet et ganglions de la base",
        "prereqs": ["m12_c16_neuroplasticite_motrice", "m12_c17_modeles_computationnels"],
        "texte": """
Trois grandes structures sous-corticales et corticales orchestrent le contrôle moteur, avec des
rôles distincts et complémentaires.

CORTEX MOTEUR PRIMAIRE (M1) : exécution des commandes motrices. L'homoncule de Penfield illustre
la représentation somatotopique. M1 encode principalement la direction du mouvement et la force,
pas seulement les muscles individuels. Connecté directement à la moelle épinière via le tractus
corticospinal (voie pyramidale).

CORTEX PRÉMOTEUR (PMC) ET MOTEUR SUPPLÉMENTAIRE (SMA) : planification et préparation du mouvement.
Le SMA est crucial pour les séquences motrices apprises internes (auto-initiées). Le PMC est plus
impliqué dans le guidage par des indices externes. L'imagerie mentale active fortement le SMA.

CERVELET : coordination, timing fin, apprentissage par l'erreur. La «théorie de l'apprentissage
cérébelleux» (Marr-Albus-Ito) : les fibres grimpantes transmettent le signal d'erreur (via
l'olive inférieure) qui modifie les synapses entre les fibres parallèles et les cellules de Purkinje.
Modèle d'apprentissage supervisé neuronal. Lésion : ataxie (mauvaise coordination), dyschronie,
incapacité à adapter les mouvements calibrés (ex : lancer vers une cible avec prisme).

GANGLIONS DE LA BASE (noyaux gris centraux) : sélection des actions, initiation, suppression des
mouvements indésirables. Dopamine (voie nigro-striée) : signal de «reward prediction error» (Schultz).
Déplétion de dopamine → Parkinson (hypokinésie, rigidité, tremblement au repos). Hyperactivité
(relative) → Huntington, tics, mouvements involontaires.

THALAMUS : relais entre les structures sous-corticales et le cortex. Porte d'entrée des signaux
du cervelet et des ganglions de la base vers le cortex.

INTÉGRATION : pour un mouvement appris, les ganglions de la base sélectionnent et initient le
programme. Le cervelet le surveille et ajuste la précision du timing. M1 l'exécute. Après
consolidation, le contrôle se déplace vers des boucles plus automatiques (moins corticales).

RÉHABILITATION NEUROLOGIQUE : exploiter la plasticité de ces circuits via la répétition intensive,
le feedback, la stimulation magnétique transcrânienne (TMS) et la stimulation cérébrale profonde (DBS).
        """.strip(),
    },

    "m12_c22_protocoles_recherche": {
        "module": 12, "ordre": 22,
        "titre": "Protocoles de recherche en apprentissage moteur — designs, validité et pièges",
        "prereqs": ["m12_c1_definition_champ", "m12_c6_memoire_motrice"],
        "texte": """
L'apprentissage moteur est une science expérimentale. Comprendre les designs de recherche est
essentiel pour évaluer la littérature et produire des études valides.

PARADIGME CLASSIQUE : phase d'acquisition (pratique) → test de rétention (après délai, mêmes
conditions) → test de transfert (nouvelle variante ou contexte). La rétention mesure l'apprentissage
(vs adaptation temporaire). Sans test différé, on mesure la performance, pas l'apprentissage.

DESIGN ABA vs ABAB : dans les études d'adaptation (ex : lunettes à prisme), ABA montre l'adaptation
puis le de-adaptation ; ABAB montre si la re-adaptation est plus rapide (économie d'apprentissage).

GROUPES DE CONTRÔLE : (1) groupe no-practice (mesure le niveau de base et l'effet du temps) ;
(2) groupe yoked (reçoit le même feedback qu'un autre groupe, mais sans le contexte) ; (3) sham
intervention. La sélection du bon contrôle est critique pour les inférences causales.

BLINDING : difficile en apprentissage moteur (impossible de «cacher» qu'on fait de l'exercice),
mais les évaluateurs peuvent être «blind» à la condition. Les auto-rapports sont susceptibles
aux effets d'attente.

VALIDITÉ INTERNE vs EXTERNE : les paradigmes de laboratoire (pointage sur écran, lancer de balle
standardisé) maximisent le contrôle mais minimisent l'écologie. Les études de terrain ont une
meilleure validité externe mais moins de contrôle. Le «representative learning design» tente de
concilier les deux.

TAILLE D'EFFET ET PUISSANCE : de nombreuses études en apprentissage moteur ont de petits n (n<30).
Les méta-analyses (Magill, Wulf) sont importantes pour évaluer la robustesse des effets. Les
effets de publication biaisent vers les résultats positifs.

RÉPLICATION : plusieurs effets classiques (interférence contextuelle, focus externe) ont des
effets plus modestes dans les réplications à grande échelle. La fiabilité inter-laboratoires est
une question ouverte.

MESURES : cinématique 3D (marqueurs réfléchissants + caméras infrarouges), EMG (activité musculaire),
force (plateformes, capteurs), neuroimagerie (EEG, fMRI), temps de réaction, erreur de performance.
        """.strip(),
    },

    "m12_c23_mesures_kinesio": {
        "module": 12, "ordre": 23,
        "titre": "Méthodes de mesure — cinématique, EMG et neuroimagerie dans l'étude du mouvement",
        "prereqs": ["m12_c22_protocoles_recherche"],
        "texte": """
La recherche en contrôle et apprentissage moteur repose sur un arsenal de méthodes quantitatives
pour capturer le mouvement et son substrat neural.

CINÉMATIQUE 3D : mesure la position, la vitesse et l'accélération des segments corporels dans
l'espace. Systèmes optoélectroniques (Vicon, Qualisys) : marqueurs réfléchissants + caméras
infrarouges → reconstruction 3D du squelette. Variables : amplitude articulaire, trajectoires,
timing inter-segmentaire, variabilité angulaire. Limitation : donne le mouvement, pas les forces.

ANALYSE CINÉTIQUE (dynamique) : plateformes de force → forces de réaction au sol (GRF), moments
articulaires calculés par la dynamique inverse. Complément essentiel de la cinématique pour
comprendre les couples musculaires et les demandes articulaires.

ÉLECTROMYOGRAPHIE (EMG) : mesure l'activité électrique des muscles. Surface (non-invasif, muscles
superficiels) vs intramusculaire (aiguille, muscles profonds ou petits). Variables : onset (début
d'activation), amplitude (RMS), spectre de fréquences (fatigue = shift vers basses fréquences),
patterns de co-contraction. Limitation : artéfacts de mouvement, cross-talk entre muscles.

EEG (ÉLECTROENCÉPHALOGRAPHIE) : enregistrement de l'activité électrique corticale à haute résolution
temporelle (ms). Event-Related Potentials (ERP) permettent d'isoler des composantes liées à des
événements (N2, P300 pour la décision motrice ; Bereitschaftspotential = potentiel de préparation
précédant le mouvement volontaire de ~1500ms). Limite : résolution spatiale faible.

IRMf (IRM FONCTIONNELLE) : mesure le signal BOLD (Blood Oxygen Level Dependent) — proxy de
l'activité neurale via la vascularisation. Résolution spatiale excellente (mm), temporelle faible
(s). Utilisée pour identifier les circuits impliqués dans l'apprentissage, l'imagerie, l'observation.

TMS (STIMULATION MAGNÉTIQUE TRANSCRÂNIENNE) : perturber ou stimuler un cortex ciblé pour établir
des relations causales (vs corrélatives de l'IRMf). Mapping des fonctions motrices, réhabilitation.

ANALYSE DES SÉRIES TEMPORELLES : entropie de l'approximation (ApEn), entropie d'échantillon (SampEn)
pour quantifier la complexité de la variabilité motrice — indice de santé du système de contrôle.
        """.strip(),
    },

    "m12_c24_developpement_moteur": {
        "module": 12, "ordre": 24,
        "titre": "Développement moteur — de l'enfant à l'expert, trajectoires et périodes sensibles",
        "prereqs": ["m12_c11_systemes_dynamiques", "m12_c16_neuroplasticite_motrice"],
        "texte": """
Le développement moteur couvre les changements dans les habiletés motrices depuis la naissance
jusqu'à la vieillesse, intégrant maturation biologique, expérience, et contexte environnemental.

DÉVELOPPEMENT POSTNATAL IMMÉDIAT : le nouveau-né présente des réflexes primitifs (Moro, succion,
Babinski) médiatisés par des structures sous-corticales. La maturation du cortex moteur (myélinisation
des voies corticospinales jusqu'à ~2 ans) entraîne l'inhibition progressive de ces réflexes.

SÉQUENCE DE DÉVELOPPEMENT MOTEUR : le développement suit une direction céphalo-caudale (tête
avant les jambes) et proximo-distale (tronc avant les mains). Les jalons — retournement (~4 mois),
position assise (~6 mois), marche (~12 mois) — sont robustes mais ont une variabilité normale
considérable.

ÉMERGENCE DE LA MARCHE (Thelen) : ne découle pas d'un programme inné unique — émerge de
l'interaction des contraintes (tonus, masse des membres, environnement). Preuve : stimuler
les réflexes de marche en immersion dans l'eau chez des nourrissons non marcheurs.

PÉRIODES SENSIBLES MOTRICES : fenêtres développementales où certaines habiletés s'acquièrent
plus aisément. Ex : coordination binoculaire (premier semestre), équilibre dynamique (2-5 ans),
pattern de course (5-7 ans). La privation durant une période sensible peut compromettre le
développement sans être irréversible.

SPÉCIALISATION SPORTIVE PRÉCOCE vs TARDIVE : la diversification des sports en jeune âge (6-12 ans)
préserve la motivation, réduit les blessures de surutilisation, et produit souvent de meilleures
athlètes adultes («rule of sampling», Côté & Fraser-Thomas). La spécialisation précoce peut réussir
dans les sports à pic précoce (gymnastique, plongeon) mais échoue souvent à long terme dans les
sports à pic tardif (team sports).

VIEILLISSEMENT MOTEUR : déclin progressif de la vitesse de traitement, de la force musculaire,
de l'équilibre (à partir de 60-65 ans). Augmentation de la variabilité «nuisible». L'entraînement
moteur en personne âgée maintient la plasticité corticale et réduit le déclin fonctionnel.
        """.strip(),
    },

    "m12_c25_technologies_augmentees": {
        "module": 12, "ordre": 25,
        "titre": "Technologies augmentées — réalité virtuelle, biofeedback et exosquelettes en apprentissage moteur",
        "prereqs": ["m12_c3_feedback_types", "m12_c14_imagerie_mentale", "m12_c23_mesures_kinesio"],
        "texte": """
Les technologies contemporaines transforment les possibilités d'entraînement et de réhabilitation.

RÉALITÉ VIRTUELLE (VR) : simulation immersive qui peut reproduire des environnements d'entraînement
avec contrôle précis des variables. Applications : (1) réhabilitation neuromotrice post-AVC
(environnements motivants, feedback augmenté, répétitions élevées) ; (2) entraînement à des
situations à haut risque (chirurgie, pilotage, pompiers) ; (3) manipulations perceptuelles
(adaptation prismatique en VR, altération du retour sensoriel).

TRANSFERT VR → RÉEL : variable selon la fidélité perceptivo-motrice du simulateur. Le couplage
perception-action doit être représentatif de la situation réelle. La fidélité visuelle seule
est insuffisante si la proprioception ou les forces sont absentes.

BIOFEEDBACK : information en temps réel sur des variables physiologiques normalement non-conscientes
(activité EMG, variabilité de la fréquence cardiaque, activité EEG). Applications : (1) rééducation
musculaire (biofeedback EMG en kinésithérapie) ; (2) neurofeedback pour la relaxation ou la
concentration (ondes alpha/beta en sport) ; (3) feedback de la posture en temps réel.

SONIFICATION DU MOUVEMENT : transformation de paramètres cinématiques (vitesse, trajectoire) en
sons en temps réel. Efficace pour fournir un feedback continu dans les tâches motrices sans saturer
le canal visuel. Utilisé en réhabilitation de la marche, en danse, en chirurgie.

EXOSQUELETTES : dispositifs mécaniques portés sur le corps qui peuvent guider, amplifier ou
résister le mouvement. Applications : (1) réhabilitation post-AVC ou lésion médullaire (guidage
des mouvements parétiques, activation proprioceptive) ; (2) amplification de la force (travail
industriel, militaire) ; (3) assistance à la marche chez les personnes âgées.

STIMULATION ÉLECTRIQUE FONCTIONNELLE (FES) : stimulation électrique des muscles parétiques
synchronisée avec le mouvement intentionnel. Aide à recruter les circuits moteurs résiduel post-AVC.

MACHINE LEARNING ET COACHING AUTOMATISÉ : vidéo + pose estimation (MediaPipe, OpenPose) →
feedback automatique sur la technique. Détection d'anomalies cinématiques en temps réel.
Potentiel pédagogique, limité actuellement par la validité clinique.
        """.strip(),
    },

    "m12_c26_conception_intervention": {
        "module": 12, "ordre": 26,
        "titre": "Conception d'interventions en apprentissage moteur — principes méthodologiques",
        "prereqs": ["m12_c22_protocoles_recherche", "m12_c15_expertise_deliberate_practice"],
        "texte": """
Concevoir une intervention efficace en apprentissage moteur requiert d'intégrer les principes de
la recherche fondamentale dans un contexte appliqué.

ANALYSE DE LA TÂCHE (Task Analysis) : décomposer l'habileté cible en composantes perceptuelles,
décisionnelles et motrices. Identifier les sous-habiletés critiques (goulots d'étranglement),
les exigences sensorielle et temporelle. Hiérarchie des tâches (HTA) ou analyse des affordances.

ÉVALUATION DU NIVEAU INITIAL : tests de rétention (pas de performance à chaud), mesures de
variabilité, entretiens sur la représentation mentale. L'évaluation guide la zone proximale de
développement.

DOSAGE DE LA PRATIQUE : (1) durée de session — courtes sessions fréquentes > longues sessions
rares (effet d'espacement) ; (2) ratio pratique/repos — la fatigue cognitive nuit à la qualité ;
(3) nombre total de répétitions — les effets dose-réponse sont généralement monotones mais avec
rendements décroissants.

PROGRESSIONS : du simple au complexe (décomposition), du lent au rapide (mais attention : le
mouvement lent peut différer qualitativement du mouvement rapide). Complexifier les contraintes
d'environnement progressivement (fermé → ouvert).

INDIVIDUALISATION : les caractéristiques de l'apprenant (expérience préalable, style cognitif,
niveau d'anxiété, capacité de travail en mémoire) modèrent les effets des variables d'entraînement.
Ce qui fonctionne en groupe peut ne pas fonctionner pour un individu particulier.

MAINTIEN ET PRÉVENTION DE LA RECHUTE : la rétention nécessite une pratique de maintien. La
pratique distribuée à faible fréquence après maîtrise est plus efficace que l'arrêt complet.
En réhabilitation, le transfert à la vie quotidienne est la mesure finale.

FIDELITÉ D'IMPLÉMENTATION : dans les études et les programmes pratiques, s'assurer que
l'intervention est administrée comme prévu. La dérive de fidelité est fréquente et érode
la validité des conclusions.

ÉVALUATION DE L'EFFICACITÉ : comparer avant-après, avec groupe de contrôle si possible ; mesurer
rétention ET transfert ; inclure des mesures de la satisfaction et de l'adhérence.
        """.strip(),
    },

    "m12_c27_neurorehabilitation": {
        "module": 12, "ordre": 27,
        "titre": "Neuroréhabilitation motrice — principes, AVC, lésion médullaire et plasticité",
        "prereqs": ["m12_c16_neuroplasticite_motrice", "m12_c21_bases_neurales_circuit", "m12_c25_technologies_augmentees"],
        "texte": """
La neuroréhabilitation applique les principes de l'apprentissage et de la plasticité motrice pour
récupérer la fonction après lésion du système nerveux central ou périphérique.

PRINCIPES DE LA PLASTICITÉ USE-DEPENDENT (Kleim & Jones, 2008) : 10 principes fondamentaux —
(1) Use it or lose it, (2) Use it and improve it, (3) Specificité, (4) Répétition, (5) Intensité,
(6) Timing (plasticité accrue en phase précoce post-lésion), (7) Saillance (motivation et récompense),
(8) Âge, (9) Transference, (10) Interference.

POST-AVC : fenêtre de plasticité accrue dans les premières semaines/mois. Récupération spontanée
partielle (résolution de l'œdème, recrutement de circuits latents). La rééducation intensive
précoce exploite cette fenêtre. Les «spared pathways» (voies corticospinales ipsilatérales,
voies réticulospinales) peuvent être renforcées.

THÉRAPIE PAR CONTRAINTE INDUITE (CI Therapy, Taub) : contraindre le membre sain pour forcer
l'utilisation intensive du membre parétique. Démonstration claire de la plasticité corticale
post-AVC — augmentation de la représentation M1 du membre affecté. Protocole intensif :
6h/j pendant 2 semaines.

LÉSION MÉDULLAIRE PARTIELLE : entraînement sur tapis de marche avec support de poids corporel
(Body-Weight Supported Treadmill Training, BWSTT) → activation des circuits spinaux rythmiques
(central pattern generators). La répétition du pattern de marche peut stimuler la plasticité
spinale même sans commande supra-spinale complète.

IMAGERIE MOTRICE EN RÉHABILITATION : les patients tétraplégiques peuvent utiliser l'imagerie
motrice pour «entraîner» leurs circuits sans mouvement. Effets mesurables sur la force et la
plasticité corticale (Yue & Cole, 1992).

INTERFACES CERVEAU-MACHINE (BCI) : décodage de l'intention motrice depuis les signaux EEG ou
intracorticaux → activation de prothèses, d'exosquelettes ou de la FES. Permet un feedback
moteur en boucle fermée même sans mouvement du membre naturel.

MESURES EN RÉHABILITATION : FIM (Functional Independence Measure), Fugl-Meyer (membre supérieur
post-AVC), Berg Balance Scale, 10-m Walk Test, Wolf Motor Function Test.
        """.strip(),
    },

    "m12_c28_frontieres_recherche": {
        "module": 12, "ordre": 28,
        "titre": "Frontières actuelles — sport science, IA, interface cerveau-machine et apprentissage moteur",
        "prereqs": ["m12_c20_cerveau_bayesien_controle", "m12_c27_neurorehabilitation", "m12_c25_technologies_augmentees"],
        "texte": """
Le domaine de l'apprentissage moteur est en pleine ébullition scientifique. Ce concept synthétise
les orientations de recherche les plus prometteuses et les questions ouvertes les plus urgentes.

APPRENTISSAGE MOTEUR ACCÉLÉRÉ : la stimulation tDCS (transcranienne par courant direct) et la
TMS répétitive peuvent modifier temporairement l'excitabilité corticale. Des protocoles pré-
entraînement ou post-entraînement semblent accélérer la consolidation. Les preuves sont encore
hétérogènes ; la traduction clinique prudente.

INTELLIGENCE ARTIFICIELLE ET COACHING MOTEUR : les réseaux de neurones profonds permettent
(1) l'analyse automatique de la biomécanique depuis des vidéos simples (pose estimation + analyse
critique de technique) ; (2) la personnalisation en temps réel de la difficulté et du feedback ;
(3) la prédiction du risque de blessure depuis des patterns cinématiques subtils.

JUMEAUX NUMÉRIQUES MUSCULO-SQUELETTIQUES : modèles personnalisés du système locomoteur (OpenSim,
AnyBody) permettant de simuler des interventions chirurgicales, des équipements ou des techniques
avant leur implémentation. La médecine personnalisée du mouvement.

INTERFACES CERVEAU-MACHINE CLOSED-LOOP : décodage de l'intention motrice + stimulation du système
nerveux périphérique ou cortical en boucle fermée. Permet la restauration de la sensori-motricité
chez des patients avec lésions médullaires. Le groupe de Capogrosso (2023) : patients marchant
après décodage cortical et stimulation epidurale.

APPRENTISSAGE FÉDÉRÉ ET DONNÉES MOTRICES : agrégation de données motrices à grande échelle depuis
des appareils connectés (montres, capteurs) pour entraîner des modèles de normalité motrice.
Soulève des enjeux importants de vie privée et de biais algorithmique.

PSYCHOPHYSIOLOGIE DE LA PERFORMANCE : intégration des mesures de variabilité de la fréquence
cardiaque (VFC), de la cortisol salivaire, et du profil de l'état mental (POMS) dans le suivi
de la charge d'entraînement moteur. L'«athlete monitoring» comme discipline à part entière.

QUESTIONS OUVERTES : (1) Existe-t-il un «programme moteur» ou est-ce une métaphore utile ?
(2) La pratique délibérée est-elle la seule voie vers l'expertise ? (3) Quels sont les mécanismes
précis du transfert négatif à long terme ? (4) Comment optimiser la combinaison imagerie +
pratique physique ? (5) Les BCI remplaceront-elles la kinésithérapie dans 20 ans ?
        """.strip(),
    },

})


# ── Chargement des concepts dynamiques ───────────────────────────────────────
# On fusionne les concepts ingérés (dynamic_concepts.json) dans CURRICULUM.
# Import tardif pour éviter la dépendance circulaire avec ingestion.py.

def _charger_concepts_dynamiques() -> None:
    """Fusionne les concepts dynamiques dans CURRICULUM au démarrage."""
    from pathlib import Path
    import json

    dynamic_file = Path(__file__).parent / "dynamic_concepts.json"
    if not dynamic_file.exists():
        return

    try:
        concepts = json.loads(dynamic_file.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return

    for cle, concept in concepts.items():
        if cle not in CURRICULUM:
            CURRICULUM[cle] = concept


_charger_concepts_dynamiques()


# ══════════════════════════════════════════════════════════════════════════════
# MODULE 13 — MÉCANIQUE ET LEVIERS  (10 concepts, débutant → intermédiaire)
# ══════════════════════════════════════════════════════════════════════════════

CURRICULUM.update({

    "m13_c1_levier_definition": {
        "module": 13, "ordre": 1,
        "titre": "Le levier : définition et composantes fondamentales",
        "prereqs": [],
        "texte": """
Un LEVIER est une machine simple composée d'une barre rigide qui pivote autour d'un point fixe
appelé FULCRUM (ou point d'appui). C'est l'une des six machines simples identifiées depuis
l'Antiquité (avec la poulie, le plan incliné, la vis, le coin et la roue-axe).

Trois éléments définissent tout levier :
• Le FULCRUM (F) : point fixe autour duquel la barre pivote — peut être une charnière, une
  articulation, ou simplement un bord arrondi
• La FORCE MOTRICE (ou effort, E) : la force appliquée pour déplacer quelque chose
• La RÉSISTANCE (ou charge, R) : la force à vaincre (poids, frottement, charge externe)

L'utilité du levier repose sur un principe fondamental découvert par Archimède (~250 av. J.-C.) :
en jouant sur la DISTANCE entre ces éléments, on peut déplacer une grande résistance avec une
petite force — ou au contraire, convertir une petite force en un grand déplacement rapide.

Exemples quotidiens : une bascule (balançoire), un tire-bouchon, une brouette, des ciseaux,
une pince à épiler, une pagaie de kayak — tous sont des leviers.

La clé : les leviers ne créent pas d'énergie. Ils la redistribuent entre force et distance.
Gain en force = perte en distance parcourue, et vice versa.
        """.strip(),
    },

    "m13_c2_trois_classes": {
        "module": 13, "ordre": 2,
        "titre": "Les trois classes de leviers",
        "prereqs": ["m13_c1_levier_definition"],
        "texte": """
Les leviers sont classés selon la POSITION RELATIVE du fulcrum (F), de l'effort (E) et de la
résistance (R) le long de la barre.

LEVIER DE CLASSE 1 — F entre E et R :
Le fulcrum est au centre. Exemples : bascule/balançoire, ciseaux, pince à ongles, pied-de-biche.
Anatomie : tête sur l'atlas (C1 = fulcrum, poids de la tête = R, muscles postérieurs = E).
Peut donner un avantage mécanique > ou < 1 selon la position du fulcrum.

LEVIER DE CLASSE 2 — R entre F et E :
La résistance est au centre. Le fulcrum est à une extrémité, l'effort à l'autre.
Exemples : brouette, ouvre-bouteille à levier, soulever sur la pointe des pieds (métatarses =
fulcrum, poids du corps = R au tibia, effort = mollet à l'arrière).
Toujours AM > 1 : force amplifiée, mais déplacement réduit.

LEVIER DE CLASSE 3 — E entre F et R :
L'effort est au centre. Le fulcrum est à une extrémité, la résistance à l'autre.
Exemples : pince à épiler, pagaie (haut de la pagaie = fulcrum), pelle, cuillère.
Anatomie : fléchisseurs du coude (biceps s'insère près du coude = fulcrum; main tient la charge).
Toujours AM < 1 : force diminuée, mais vitesse et amplitude augmentées. Favorise la vitesse.

RÉSUMÉ mnémotechnique : 1-2-3 = Fulcrum-Résistance-Effort (au centre dans chaque classe).
        """.strip(),
    },

    "m13_c3_fulcrum_point_appui": {
        "module": 13, "ordre": 3,
        "titre": "Le fulcrum : rôle, types et exemples",
        "prereqs": ["m13_c2_trois_classes"],
        "texte": """
Le FULCRUM (du latin : point d'appui) est le pivot autour duquel le levier tourne. Sa position
détermine la classe du levier et son avantage mécanique.

TYPES DE FULCRUM selon leur nature physique :
• CHARNIÈRE ou AXE : pivot métallique fixe (ciseaux, balançoire)
• ARTICULATION ANATOMIQUE : genou, coude, épaule — fulcrum biologique
• BORD ARRONDI : une brouette sur son rebord, un bras de levier sur une arête
• SURFACE DE CONTACT : plante du pied sur le sol (levier du mollet)

POSITION DU FULCRUM ET AVANTAGE MÉCANIQUE :
Plus le fulcrum est PROCHE de la résistance (et loin de l'effort), plus l'avantage mécanique
est grand → petite force suffit mais déplacement de l'effort est grand.
Plus le fulcrum est PROCHE de l'effort (et loin de la résistance), plus l'avantage est faible
→ force importante nécessaire, mais la résistance se déplace rapidement et sur une grande amplitude.

EXEMPLES ANATOMIQUES :
• Atlas (C1) : fulcrum pour le mouvement oui/non de la tête (classe 1)
• Métatarses (avant du pied) : fulcrum pour la marche en pointe (classe 2)
• Coude : fulcrum pour la flexion du coude avec le biceps (classe 3)
• Genou : fulcrum pour l'extension par le quadriceps (classe 3 — AM faible, vitesse élevée)

En ingénierie, déplacer le fulcrum est l'un des outils les plus puissants pour optimiser
une machine sans modifier les forces en présence.
        """.strip(),
    },

    "m13_c4_bras_levier": {
        "module": 13, "ordre": 4,
        "titre": "Bras de levier : bras moteur et bras résistant",
        "prereqs": ["m13_c3_fulcrum_point_appui"],
        "texte": """
Le BRAS DE LEVIER est la distance perpendiculaire entre le fulcrum et le point d'application
d'une force. C'est l'élément clé qui détermine l'efficacité d'un levier.

On distingue deux bras :

BRAS MOTEUR (ou bras de force, d_E) :
Distance entre le fulcrum et le point où s'applique l'EFFORT (force motrice).
Plus ce bras est long, moins il faut de force pour déplacer la résistance.

BRAS RÉSISTANT (ou bras de charge, d_R) :
Distance entre le fulcrum et le point où s'applique la RÉSISTANCE (charge).
Plus ce bras est court, plus la résistance est "proche" du fulcrum et donc facile à vaincre.

RELATION FONDAMENTALE (loi du levier d'Archimède) :
  E × d_E = R × d_R
→ Force motrice × bras moteur = Résistance × bras résistant

Exemple : vous voulez soulever une roche de 300 N avec une force de 100 N.
Si d_R = 0,5 m, alors d_E = (300 × 0,5) / 100 = 1,5 m → bras moteur 3× plus long.

BRAS DE LEVIER ANATOMIQUE :
Le bras de levier anatomique est souvent très court (muscles s'insèrent près des articulations),
ce qui explique pourquoi nos muscles doivent générer des forces bien supérieures au poids
des objets soulevés. Ex : pour tenir une masse de 5 kg dans la main, le biceps doit exercer
~35 kg de force (insertion à ~5 cm du coude, poids à ~35 cm). Avantage : vitesse et amplitude.
        """.strip(),
    },

    "m13_c5_avantage_mecanique": {
        "module": 13, "ordre": 5,
        "titre": "Avantage mécanique : formule, interprétation et compromis",
        "prereqs": ["m13_c4_bras_levier"],
        "texte": """
L'AVANTAGE MÉCANIQUE (AM) quantifie l'amplification de force qu'un levier produit.

FORMULE :
  AM = d_E / d_R  =  Résistance / Effort  =  R / E

INTERPRÉTATION :
• AM > 1 : le levier AMPLIFIE la force. Petite force → grande résistance vaincue.
  Exemple : brouette avec AM = 3 → pousser 100 N suffit pour soulever 300 N de charge.
• AM = 1 : aucune amplification. L'effort = la résistance. Levier neutre (bascule équilibrée).
• AM < 1 : le levier RÉDUIT la force mais AUGMENTE la vitesse et l'amplitude de mouvement.
  Exemple : pince à épiler avec AM = 0,3 → il faut 100 N pour exercer 30 N sur l'objet,
  mais le bout de la pince se déplace rapidement et avec précision.

LE GRAND COMPROMIS — principe de conservation :
Un levier ne crée pas d'énergie. Ce qu'on gagne en force, on le perd en distance :
  Travail fourni (E × déplacement_E) = Travail utile (R × déplacement_R)
→ AM élevé : force amplifiée, mais l'effort doit parcourir une longue distance.
→ AM faible : force réduite, mais la résistance se déplace rapidement et loin.

APPLICATION SPORTIVE :
Les leviers de classe 3 du corps humain (bras, jambes) ont des AM faibles (~0,1 à 0,3)
ce qui FAVORISE la vitesse et l'amplitude des mouvements. C'est pourquoi un bras
peut lancer une balle à 150 km/h alors que le muscle ne se contracte qu'à ~10 cm/s.
        """.strip(),
    },

    "m13_c6_moments_force": {
        "module": 13, "ordre": 6,
        "titre": "Moments de force (torque) : définition et calcul",
        "prereqs": ["m13_c4_bras_levier"],
        "texte": """
Le MOMENT DE FORCE (ou TORQUE, noté M ou τ) est la mesure de la tendance d'une force à
faire PIVOTER un objet autour d'un point. C'est l'équivalent rotatif de la force linéaire.

FORMULE :
  M = F × d  (en N·m — newton-mètre)

Où F est la force appliquée (en N) et d est le BRAS DE LEVIER — la distance PERPENDICULAIRE
entre la ligne d'action de la force et le point de pivot.

ATTENTION — la perpendicularité est cruciale :
Si la force n'est pas appliquée perpendiculairement au bras, seule sa composante
perpendiculaire génère un moment : M = F × sin(θ) × d
→ Forcer à angle droit maximise le torque. Forcer dans l'axe du levier = moment nul.

SENS DE ROTATION :
• Moment POSITIF (antihoraire, convention mathématique)
• Moment NÉGATIF (horaire)
Les deux s'additionnent algébriquement.

EXEMPLES :
• Clé à molette : 20 N appliqués à 0,30 m → M = 6 N·m
• Même 20 N mais clé de 0,60 m → M = 12 N·m (deux fois plus efficace)
• Quadriceps : force ~2000 N, bras ~0,04 m → torque = 80 N·m au genou

EN BIOMÉCANIQUE : les moments de force pilotent tous les mouvements articulaires.
Le moment musculaire doit surpasser le moment de la gravité pour qu'un mouvement ait lieu.
C'est pourquoi la POSITION du membre change radicalement la difficulté d'un exercice.
        """.strip(),
    },

    "m13_c7_equilibre_statique": {
        "module": 13, "ordre": 7,
        "titre": "Équilibre statique : conditions et applications",
        "prereqs": ["m13_c6_moments_force"],
        "texte": """
Un objet est en ÉQUILIBRE STATIQUE quand il est au repos et que rien ne le fait accélérer
ni en translation ni en rotation. Deux conditions doivent être remplies simultanément :

CONDITION 1 — Équilibre des forces :
  ΣF = 0  (la somme vectorielle de toutes les forces = zéro)
Garantit qu'il n'y a pas d'accélération linéaire (Newton 2e loi : F = ma, donc a = 0).

CONDITION 2 — Équilibre des moments :
  ΣM = 0  (la somme des moments par rapport à n'importe quel point = zéro)
Garantit qu'il n'y a pas d'accélération angulaire.

MÉTHODE PRATIQUE — analyse d'équilibre :
1. Dessiner le schéma des forces (diagramme du corps libre)
2. Choisir un point de référence (souvent le fulcrum — annule les réactions inconnues)
3. Écrire ΣM = 0 et résoudre l'inconnue
4. Vérifier ΣF = 0

EXEMPLE : Une bascule de 3 m. Enfant 30 kg à 1,5 m du centre. Père 80 kg : à quelle distance
du centre doit-il s'asseoir pour l'équilibre ?
ΣM = 0 → 30 × 1,5 = 80 × d → d = 0,5625 m du centre (côté opposé)

APPLICATION POSTURALE :
La posture debout est un problème d'équilibre statique constant. Le CENTRE DE GRAVITÉ (point
où s'applique la résultante du poids du corps) doit rester au-dessus du POLYGONE DE SUSTENTATION
(surface entre les pieds). Toute asymétrie musculaire ou structurale crée des moments de force
résiduels compensés par les muscles posturaux — source de fatigue chronique.
        """.strip(),
    },

    "m13_c8_vecteurs_force": {
        "module": 13, "ordre": 8,
        "titre": "Vecteurs de force : représentation et composition",
        "prereqs": ["m13_c7_equilibre_statique"],
        "texte": """
Une FORCE est une grandeur VECTORIELLE : elle a une intensité (magnitude), une direction,
un sens, et un point d'application. On la représente par une flèche.

QUATRE CARACTÉRISTIQUES d'un vecteur de force :
• INTENSITÉ : module de la force, exprimé en Newton (N)
• DIRECTION : l'axe (vertical, horizontal, ou à un angle θ)
• SENS : sur la droite d'action, vers quel côté (haut/bas, gauche/droite)
• POINT D'APPLICATION : où la force est appliquée sur l'objet

COMPOSITION DE FORCES — deux méthodes :
1. GRAPHIQUE (règle du parallélogramme) : on construit un parallélogramme dont les deux
   vecteurs sont des côtés adjacents — la diagonale est la RÉSULTANTE.
2. ANALYTIQUE (décomposition) : chaque force est décomposée en composantes horizontale
   et verticale :
   Fx = F × cos(θ),  Fy = F × sin(θ)
   On somme les Fx entre eux, les Fy entre eux, puis on recalcule la résultante :
   R = √(ΣFx² + ΣFy²),  θ = arctan(ΣFy / ΣFx)

FORCES EN BIOMÉCANIQUE :
Les forces agissant sur une articulation incluent : le poids du segment, les forces musculaires
(souvent obliques), les réactions articulaires. Elles sont rarement perpendiculaires aux os —
seule la composante rotatoire (perpendiculaire) génère un moment, la composante axiale
(dans l'axe de l'os) comprimer ou distrait l'articulation.
        """.strip(),
    },

    "m13_c9_corps_leviers_anatomie": {
        "module": 13, "ordre": 9,
        "titre": "Le corps humain comme système de leviers",
        "prereqs": ["m13_c5_avantage_mecanique", "m13_c8_vecteurs_force"],
        "texte": """
Le squelette humain est un système de leviers biologiques conçu pour FAVORISER LA VITESSE
ET L'AMPLITUDE au détriment de la force — contrairement à la plupart des machines industrielles.

PRINCIPAUX LEVIERS DU CORPS :

CLASSE 1 (rare) :
• Tête sur C1 : muscles postérieurs (effort) — atlas (fulcrum) — poids de la tête (résistance)
• Triceps étendant le coude : olécrane (insertion proche) crée un AM légèrement favorable

CLASSE 2 (rare, AM > 1) :
• Mollet / soulèvement sur la pointe des pieds : métatarses (fulcrum) — poids du corps
  (résistance, ancré au tibia) — tendon d'Achille (effort). AM ≈ 1,2 à 1,5.
• Muscles profonds du rachis en extension : AM favorable dû au bras résistant court

CLASSE 3 (majoritaire, AM < 1, vitesse++) :
• Biceps brachial : coude (fulcrum) — insertion à ~5 cm (effort) — main à ~35 cm (résistance)
  → AM ≈ 0,14. Force du biceps ~7× le poids tenu.
• Quadriceps : genou (fulcrum) — tendon rotulien (~4 cm) — poids du pied/jambe (~45 cm)
  → AM ≈ 0,09. Quadriceps génère ~10× le poids de la jambe.
• Deltoïde à l'épaule : AM ≈ 0,15 — compense par une force musculaire très élevée

IMPLICATION POUR L'ENTRAÎNEMENT :
La position du poids modifie le bras résistant → curl concentré (poids loin du coude à 90°)
est plus difficile en milieu de mouvement. Comprendre les leviers permet d'optimiser les angles
de travail musculaire et de diagnostiquer les points faibles d'un mouvement.
        """.strip(),
    },

    "m13_c10_machines_simples": {
        "module": 13, "ordre": 10,
        "titre": "Les six machines simples : panorama et principe de conservation",
        "prereqs": ["m13_c5_avantage_mecanique"],
        "texte": """
Les SIX MACHINES SIMPLES sont les éléments de base de toute mécanique. Identifiées depuis
Archimède et complétées par Héron d'Alexandrie (~1er siècle ap. J.-C.), elles sont à
l'origine de toutes les machines complexes.

1. LE LEVIER : barre rigide + fulcrum. AM = d_E / d_R. Trois classes. Exemples : ciseaux,
   balançoire, pied-de-biche.

2. LA POULIE : roue avec une gorge + corde. Poulie fixe : change la direction de la force
   (AM = 1). Poulie mobile : AM = 2 (supporte la charge des deux côtés de la corde).
   Palan (combinaison) : AM = nombre de brins porteurs.

3. LE PLAN INCLINÉ : surface en pente. AM = longueur / hauteur = 1/sin(θ).
   Exemples : rampe de chargement, route en lacets, biseau d'un couteau.

4. LE COIN : double plan incliné. Convertit une force dans l'axe en deux forces perpendiculaires.
   Exemples : hache, cheville, clou, ciseau de menuisier.

5. LA VIS : plan incliné enroulé autour d'un cylindre. AM = 2πr / pas de vis.
   Convertit le mouvement rotatif en translation. Exemples : vis à bois, cric, presse.

6. LA ROUE ET L'AXE : deux cylindres solidaires de rayons différents. AM = R / r.
   Exemples : tournevis (manche large / tige étroite), volant de voiture, robinet, manivelle.

PRINCIPE UNIVERSEL — CONSERVATION DU TRAVAIL :
Toutes les machines simples respectent le même principe fondamental :
  Travail fourni = Travail utile + Pertes (frottements)
  F_E × d_E = F_R × d_R  (sans frottement)

Aucune machine ne crée d'énergie. Le "miracle" du levier, de la poulie ou du plan incliné
est de REDISTRIBUER la force et le déplacement, jamais de les inventer.
        """.strip(),
    },

})


# ══════════════════════════════════════════════════════════════════════════════
# MODULE 14 — HISTORIOGRAPHIE DE LA SHOAH  (10 concepts)
# ══════════════════════════════════════════════════════════════════════════════

CURRICULUM.update({

    "m14_c1_definition_perimetre": {
        "module": 14, "ordre": 1,
        "titre": "La Shoah : définition, périmètre et chronologie",
        "prereqs": [],
        "texte": """
Le terme SHOAH (hébreu : catastrophe) désigne le génocide des Juifs d'Europe perpétré par
l'Allemagne nazie et ses alliés entre 1933 et 1945. Le terme HOLOCAUST (grec : holocauste,
sacrifice par le feu) est utilisé en anglais et dans plusieurs langues. Les deux coexistent;
"Shoah" est préféré par de nombreux historiens car il ne porte pas la connotation sacrificielle.

PÉRIMÈTRE : l'historiographie contemporaine distingue :
• Le génocide des Juifs : ~6 millions de victimes, cible principale de la politique d'extermination
• Les autres victimes du régime nazi : Roms (~500 000), personnes handicapées (~300 000 dans le
  cadre de l'Aktion T4), Polonais non-juifs (~2-3 millions), prisonniers soviétiques (~3 millions),
  homosexuels, Témoins de Jéhovah, opposants politiques

CHRONOLOGIE en trois phases distinctes :
1. EXCLUSION (1933-1939) : lois de Nuremberg (1935), discrimination légale, emigration forcée,
   Nuit de Cristal (9 nov. 1938, ~90 morts, 30 000 arrestations, 7 500 commerces détruits)
2. GHETTOÏSATION et TRAVAIL FORCÉ (1939-1941) : création de ghettos en Pologne occupée
   (Varsovie, Łódź, Cracovie), conditions létales par la faim et les maladies
3. EXTERMINATION SYSTÉMATIQUE (1941-1945) : Einsatzgruppen à l'Est (fusillades de masse),
   camp de Chelmno opérationnel dès déc. 1941, conférence de Wannsee (janv. 1942), montée en
   puissance des camps d'Aktion Reinhardt (Belzec, Sobibor, Treblinka), Auschwitz-Birkenau
   comme principal site d'extermination industrielle (1942-1944)

Le consensus des historiens s'appuie sur des sources convergentes : documentation administrative
nazie, photographies, archives soviétiques et alliées, témoignages de survivants et de
perpétrateurs, données démographiques comparatives avant/après-guerre.
        """.strip(),
    },

    "m14_c2_hierarchie_preuves": {
        "module": 14, "ordre": 2,
        "titre": "Les sources et la hiérarchie des preuves en histoire",
        "prereqs": ["m14_c1_definition_perimetre"],
        "texte": """
L'histoire repose sur une HIÉRARCHIE DES SOURCES qui permet de peser les preuves et de
détecter les falsifications. Cette hiérarchie n'est pas rigide — elle s'applique selon le
contexte et la convergence des sources.

SOURCES PRIMAIRES — produites à l'époque des faits :
• Documents administratifs nazis : ordres de transport, listes de déportation, rapports de
  construction, correspondances SS. Avantage : non produits pour la postérité, souvent
  compromettants par inadvertance. Exemples clés : rapport Korherr (1943, statistiques SS),
  télégramme Höfle (1943, chiffres par camp), protocole de la conférence de Wannsee (janv. 1942)
• Interceptions alliées déchiffrées (Ultra) : messages radio SS interceptés par les Britanniques
  en 1942-43, mentionnant des fusillades de masse et des déportations
• Photographies aériennes alliées (1944) : photos d'Auschwitz-Birkenau
• Témoignages contemporains de survivants et de perpétrateurs
• Archives soviétiques : documents capturés et libérés progressivement depuis 1990

SOURCES SECONDAIRES — analyses, synthèses, historiographie :
• Procès de Nuremberg (1945-46) : valeur mixte — documents authentiques + conditions d'obtention
  des témoignages parfois problématiques. Les documents restent utilisables; les confessions seules
  sont insuffisantes.
• Mémoires d'après-guerre : valeur inégale selon vérifiabilité et recoupement

PRINCIPE MÉTHODOLOGIQUE FONDAMENTAL :
La convergence de sources indépendantes est le critère central. Quand des documents administratifs
nazis, des photos aériennes, des témoignages de perpétrateurs, de victimes, de tiers, et des
données démographiques aboutissent aux mêmes conclusions de manière indépendante, la charge de
la preuve est considérée comme solidement établie. L'existence de fausses affirmations dans
certains témoignages (savon RIF, lampes en peau humaine — reconnus faux par les historiens
orthodoxes eux-mêmes) ne neutralise pas les preuves convergentes.
        """.strip(),
    },

    "m14_c3_intentionnalisme_fonctionnalisme": {
        "module": 14, "ordre": 3,
        "titre": "Intentionnalisme vs fonctionnalisme : le grand débat historiographique",
        "prereqs": ["m14_c2_hierarchie_preuves"],
        "texte": """
Le débat le plus substantiel de l'historiographie de la Shoah oppose deux écoles depuis les
années 1970-1980. Ce débat porte sur *quand et comment* la décision d'extermination fut prise,
non sur *si* l'extermination eut lieu.

INTENTIONNALISME (ou « programmiste ») :
Hitler avait un plan préconçu et cohérent d'extermination des Juifs, présent dès Mein Kampf
(1925) et exécuté de façon linéaire. Représentants : Lucy Dawidowicz, Daniel Goldhagen.
Point fort : cohérence idéologique de longue date. Point faible : manque d'un document
explicite d'ordre d'extermination antérieur à 1941.

FONCTIONNALISME (ou « structuralisme ») :
L'extermination émergea de façon cumulative et désordonnée, sous l'effet de pressions
bureaucratiques et de la dynamique de la guerre, sans plan central préétabli. Hitler donnait
des orientations générales; les bureaucraties nazies radicalisaient les mesures de façon
autonome. Représentants : Martin Broszat, Hans Mommsen.
Point fort : absence de document d'ordre unique. Point faible : minimise la centralité
idéologique du leadership nazi.

SYNTHÈSE CONTEMPORAINE — intentionnalisme modéré (Christopher Browning, Ian Kershaw) :
La vision dominante depuis les années 1990 : Hitler avait des intentions exterminatrices
de longue date, mais la décision opérationnelle d'extermination systématique fut prise en
plusieurs étapes entre l'été et la fin 1941, sous l'effet combiné de l'idéologie, de la
dynamique de guerre à l'Est, et de la radicalisation cumulative des acteurs locaux.

Ce débat illustre comment des historiens partageant le même corpus documentaire peuvent aboutir
à des interprétations différentes sur les mécanismes — sans que cela remette en cause les faits
de base de l'extermination.
        """.strip(),
    },

    "m14_c4_chiffres_demographie": {
        "module": 14, "ordre": 4,
        "titre": "La question des chiffres : méthodes démographiques",
        "prereqs": ["m14_c2_hierarchie_preuves"],
        "texte": """
Établir le nombre de victimes est une question empirique qui repose sur des méthodes précises.
Le chiffre de ~6 millions de Juifs tués n'est pas une estimation arbitraire — il repose sur
des calculs démographiques convergents effectués par plusieurs équipes indépendantes.

MÉTHODE DÉMOGRAPHIQUE COMPARATIVE :
On compare les populations juives par pays avant la guerre (recensements, estimations) et
après (recensements postguerre, registres d'immigration, listes de survivants). La différence,
corrigée des migrations légales et de la natalité, donne une estimation des pertes.

Exemples de pertes par pays (estimations mainstream) :
• Pologne : 2,7-3 millions (sur ~3,3 millions préguerre, soit ~90%)
• URSS : ~1 million (territoires occupés)
• Hongrie : ~550 000
• Roumanie : ~250 000-270 000
• Allemagne : ~165 000 (sur ~500 000 de 1933, dont beaucoup ont emigré)

SOURCES COMPLÉMENTAIRES :
• Rapport Korherr (mars 1943) : statisticien SS Richard Korherr comptabilise 1 873 549 Juifs
  "évacués" via les camps de l'Est jusqu'en 1942 — document interne nazi admettant l'échelle
• Données des Death Books d'Auschwitz : 135 500 décès *enregistrés* de prisonniers immatriculés.
  Ne couvre pas les personnes gazées à l'arrivée sans immatriculation (consensus: ~900 000-1,1M à
  Auschwitz seul)
• Recensements d'après-guerre : données du Joint Distribution Committee, UNRRA, Yad Vashem

FOURCHETTE ADMISE PAR L'HISTORIOGRAPHIE : 5,7 à 6,1 millions. La variation reflète
l'incertitude légitime des données préguerre pour certaines régions, non un doute sur l'ordre
de grandeur.
        """.strip(),
    },

    "m14_c5_camps_typologie": {
        "module": 14, "ordre": 5,
        "titre": "Typologie des camps nazis : distinctions essentielles",
        "prereqs": ["m14_c1_definition_perimetre"],
        "texte": """
Une confusion fréquente — souvent exploitée dans les débats — consiste à amalgamer les
différents types de camps nazis. L'historiographie distingue clairement cinq catégories.

1. CAMPS DE CONCENTRATION (KZ — Konzentrationslager) :
Internement, punition, travail forcé. Dachau (1933, premier), Buchenwald, Bergen-Belsen,
Mauthausen, Sachsenhausen. Mortalité élevée par mauvais traitements, faim, maladies, exécutions
— mais objectif principal non l'extermination immédiate de tous les arrivants.

2. CAMPS D'EXTERMINATION (Vernichtungslager) — Aktion Reinhardt :
Belzec, Sobibor, Treblinka. Objectif unique : tuer tous les arrivants dans les heures suivant
leur arrivée. Pas d'immatriculation, pas de travail forcé durable. Quelques centaines de
prisonniers juifs forcés à faire fonctionner les installations (Sonderkommando). Estimations :
Belzec ~430 000, Sobibor ~170 000, Treblinka ~900 000 victimes.

3. CAMPS MIXTES (concentration + extermination) :
Auschwitz-Birkenau : sélection à l'arrivée — une partie immatriculée pour le travail (et
soumise aux conditions des KZ), l'autre gazée immédiatement. Majdanek : principalement
camp de travail avec installations d'extermination secondaires. Chelmno : premier camp
utilisant des camions à gaz (déc. 1941), ~340 000 victimes.

4. CAMPS DE TRANSIT :
Westerbork (Pays-Bas), Drancy (France), Mechelen (Belgique) — points de rassemblement avant
déportation vers l'Est.

5. CAMPS DE TRAVAIL FORCÉ :
Réseau de sous-camps liés à l'industrie de guerre (I.G. Farben à Monowitz/Auschwitz III,
mines, usines). Mortalité forte mais objectif économique, non exterminatoire.

Cette distinction est centrale : elle explique pourquoi les Death Books d'Auschwitz ne
reflètent qu'une fraction des décès totaux.
        """.strip(),
    },

    "m14_c6_chambres_gaz_preuves": {
        "module": 14, "ordre": 6,
        "titre": "Les chambres à gaz : convergence des preuves",
        "prereqs": ["m14_c2_hierarchie_preuves", "m14_c5_camps_typologie"],
        "texte": """
L'existence et le fonctionnement des chambres à gaz homicides constituent le point le plus
contesté par les révisionnistes. L'historiographie s'appuie sur plusieurs catégories de preuves
indépendantes.

DOCUMENTATION ADMINISTRATIVE :
• Commandes de Zyklon B à la firme Degesch : quantités excédant largement les besoins de
  désinfestation connue (Auschwitz commandait ~95% de la production nationale à certains moments)
• Devis et plans de construction des crématoires signés par la firme Topf und Söhne, avec
  correspondances internes mentionnant des "Gasprüfer" (testeurs de gaz)
• Document de la réunion de janvier 1943 entre le SS-Sturmbannführer Bischoff et Topf &
  Söhne, mentionnant la "Vergasungskeller" (salle de gazage)

TÉMOIGNAGES CROISÉS DE PERPÉTRATEURS :
• Rudolf Höss, commandant d'Auschwitz : descriptions détaillées et cohérentes du processus.
  Certes obtenues en captivité (argument de torture valide à considérer), mais cohérentes avec
  les documents techniques
• Johann Paul Kremer (médecin SS à Auschwitz) : journal contemporain (1942) mentionnant
  des "actions spéciales" — écrit en temps réel, non sous contrainte postguerre
• Témoignages du Sonderkommando (prisonniers forçés à travailler dans les crématoires) :
  Scrolls de Sonderkommando d'Auschwitz, enterrés en 1944, retrouvés en 1945 et 1952

PREUVES FORENSIQUES :
• Analyses du Leuchter Report (1988, révisionniste) réfutées par Jan Markiewicz (1994) :
  des traces de Zyklon B ont été retrouvées dans les chambres à gaz, les différences de
  concentration s'expliquent par les conditions d'usage (courte exposition, nombreuses victimes
  vs longue exposition dans les chambres de désinfestation)
• Analyses architecturales des ruines de Birkenau confirment des structures cohérentes avec
  l'usage décrit

DONNÉES DÉMOGRAPHIQUES :
Le volume des disparitions documentées (trains entrants, absence de traces de réinstallation)
est cohérent avec l'extermination sur place.
        """.strip(),
    },

    "m14_c7_einsatzgruppen_fusillades": {
        "module": 14, "ordre": 7,
        "titre": "Les Einsatzgruppen et les fusillades de masse à l'Est",
        "prereqs": ["m14_c1_definition_perimetre"],
        "texte": """
Avant la mise en place des camps d'extermination, la principale méthode d'assassinat de masse
fut les FUSILLADES À CIEL OUVERT par les Einsatzgruppen (unités mobiles de tuerie SS) et leurs
auxiliaires, notamment en URSS occupée à partir de juin 1941.

ÉCHELLE ET ORGANISATION :
Quatre Einsatzgruppen (A, B, C, D) suivirent la Wehrmacht dans les territoires soviétiques
occupés. Assistés par la police d'ordre (Ordnungspolizei), les auxiliaires locaux (ukrainiens,
baltes, roumains selon les secteurs), ils organisèrent des fusillades systématiques de
communautés juives entières.

SITES MAJEURS :
• Babi Yar (Kiev, 29-30 sept. 1941) : 33 771 Juifs tués en deux jours — documenté par
  les rapports opérationnels (Ereignismeldungen) des Einsatzgruppen eux-mêmes, envoyés
  au RSHA à Berlin
• Ponary (Lituanie) : ~70 000 victimes
• Rumbula (Lettonie, nov.-déc. 1941) : ~25 000 en deux jours
• Forêt de Katowice, Bełżec (avant le camp), et centaines d'autres sites

DOCUMENTATION :
Les Ereignismeldungen (rapports d'événements) sont des documents internes SS envoyés à Berlin,
chiffrés (maintenant déchiffrés par les Alliés) et retrouvés dans les archives. Ils comptabilisent
les victimes avec précision administrative — ces rapports constituent parmi les preuves les plus
directes de l'extermination puisque ce sont des documents opérationnels nazis non destinés à la
propagande. Total estimé des Einsatzgruppen et opérations connexes : ~1,5 à 2 millions de victimes.

PROCÈS DE NUREMBERG DES EINSATZGRUPPEN (1947-48) :
22 chefs condamnés. Transcriptions incluant documents originaux et témoignages croisés.
        """.strip(),
    },

    "m14_c8_revisionnisme_phenomene": {
        "module": 14, "ordre": 8,
        "titre": "Le révisionnisme comme phénomène historiographique",
        "prereqs": ["m14_c2_hierarchie_preuves"],
        "texte": """
Le terme RÉVISIONNISME en histoire désigne la révision légitime des interprétations historiques
à la lumière de nouvelles preuves. Le révisionnisme de la Shoah s'approprie ce terme mais opère
différemment : il part de conclusions (l'extermination n'a pas eu lieu à l'échelle affirmée) et
cherche des arguments à l'appui, plutôt que de suivre les preuves.

FIGURES ET ORGANISATIONS PRINCIPALES :
• Paul Rassinier (France, 1950s) : premier à contester systématiquement les chiffres
• Robert Faurisson (France) : conteste l'existence des chambres à gaz homicides
• Fred Leuchter : auteur du Leuchter Report (1988), analyse chimique des crématoires d'Auschwitz
  — réfuté par des chimistes forensiques indépendants (Markiewicz, 1994)
• Ernst Zündel (Canada) : diffusion, procès au Canada (1985, 1988)
• CODOH (Committee for Open Debate on the Holocaust, USA) : organisation de diffusion

MÉTHODES RHÉTORIQUES CARACTÉRISTIQUES :
1. Hyperscrutiniser les témoignages pour trouver des contradictions réelles ou mineures
2. Utiliser des calculs techniques apparemment précis (thermodynamique, chimie) avec des
   paramètres sélectionnés de façon défavorable aux témoignages
3. Exiger un "document unique" d'ordre d'extermination — critère que l'histoire ne peut
   satisfaire pour aucun génocide
4. Isoler les preuves au lieu d'évaluer leur convergence
5. Utiliser des faux témoignages reconnus pour disqualifier les vrais

RÉPONSES HISTORIOGRAPHIQUES :
Le débat Faurisson–Vidal-Naquet (1980s), les expertises forensiques post-Leuchter,
et l'ouverture des archives soviétiques (1990s) ont fourni des réponses documentées point
par point. Le consensus académique n'a pas bougé — les contestations ont été réfutées sur
le terrain des preuves, pas seulement rejetées.
        """.strip(),
    },

    "m14_c9_proces_nuremberg": {
        "module": 14, "ordre": 9,
        "titre": "Les procès de Nuremberg : valeur et limites historiques",
        "prereqs": ["m14_c2_hierarchie_preuves"],
        "texte": """
Les PROCÈS DE NUREMBERG (1945-1949) constituent à la fois une source historique majeure
et un objet légitime de critique méthodologique.

PROCÈS PRINCIPAL — Tribunal militaire international (nov. 1945 – oct. 1946) :
24 accusés de haut rang (Göring, Ribbentrop, Keitel, Speer...). Premier usage du concept
de "crime contre l'humanité." Verdict : 12 condamnations à mort, 3 acquittements.

VALEUR HISTORIQUE :
• Des milliers de documents nazis originaux versés aux archives — accessibles aux historiens
  depuis. C'est la source documentaire principale, pas les témoignages.
• Établissement d'une chronologie et d'une structure organisationnelle documentée
• Les acquittements (Schacht, Papen, Fritzsche) montrent que le tribunal n'était pas une
  condamnation automatique

LIMITES ET CRITIQUES LÉGITIMES :
• Absence de contre-parties alliées jugées (bombes atomiques, bombardements de Dresde, etc.)
  — critique de la "justice des vainqueurs" valide sur le plan du droit international
• Certains témoignages obtenus sous pression ou avec méthodes coercitives, notamment par
  les Soviétiques
• Chiffres initiaux excessifs pour certains camps (4 millions pour Auschwitz, proclamé par
  l'URSS, réduit à 1,1-1,5 million par l'historiographie ultérieure)

DISTINCTION ESSENTIELLE :
La critique des méthodes du tribunal (valide) ne porte pas sur la valeur des documents
authentiques qui y ont été versés. Les documents nazis eux-mêmes — Wannsee, Korherr, Höfle,
Ereignismeldungen — ont été produits par les Allemands, non par les Alliés.

PROCÈS ULTÉRIEURS : procès Eichmann (Jérusalem, 1961), procès de Francfort (1963-65),
procès Demjanjuk (Munich, 2011) ont ajouté des couches de documentation supplémentaires.
        """.strip(),
    },

    "m14_c10_epistemologie_histoire": {
        "module": 14, "ordre": 10,
        "titre": "Épistémologie historique : comment établir la vérité sur un événement passé",
        "prereqs": ["m14_c2_hierarchie_preuves", "m14_c8_revisionnisme_phenomene"],
        "texte": """
La question de la Shoah illustre des enjeux épistémologiques fondamentaux : comment établit-on
qu'un événement passé a eu lieu, quand ceux qui l'ont commis voulaient en effacer les traces?

CRITÈRES DE VÉRITÉ EN HISTOIRE :
1. CONVERGENCE DES SOURCES : des sources indépendantes (administratives nazies, témoins
   alliés, survivants, perpétrateurs, données démographiques) convergent vers les mêmes faits
2. COHÉRENCE INTERNE : les explications alternatives doivent rendre compte de *toutes* les
   preuves, pas seulement de celles qui les favorisent
3. ABSENCE D'EXPLICATION ALTERNATIVE CRÉDIBLE : la thèse de transit massif vers l'Est requiert
   des preuves de réinstallation qui n'existent pas dans aucune archive soviétique ouverte
4. CHARGE DE LA PREUVE : elle incombe à celui qui conteste le consensus — et doit répondre
   à l'ensemble des preuves, non seulement à leurs lacunes

LE PROBLÈME DE L'ABSENCE DE DOCUMENT UNIQUE :
Exiger un ordre écrit d'Hitler pour l'extermination est un critère que l'histoire ne peut
satisfaire pour aucun génocide. Les ordres criminels sont rarement écrits explicitement.
Ce que l'on a : des documents de mise en œuvre cohérents (Wannsee, Korherr, commandes
de Zyklon, plans de construction), qui constituent des preuves circonstancielles convergentes.

ASYMÉTRIE DE L'ARGUMENT RÉVISIONNISTE :
L'argument "absence de preuve = preuve d'absence" est un sophisme. L'absence d'un document
unique d'ordre ne prouve pas l'absence d'ordre. En revanche, la présence de nombreux documents
d'exécution convergents constitue une preuve positive substantielle.

ANALOGIE AVEC D'AUTRES CRIMES HISTORIQUES :
Les méthodes utilisées pour établir la réalité de la Shoah sont les mêmes que pour tout autre
événement historique majeur — croisement de sources, analyse critique, archéologie forensique.
Ce n'est pas une exception méthodologique : c'est de l'histoire ordinaire appliquée à un
événement extraordinaire.
        """.strip(),
    },

})


# ══════════════════════════════════════════════════════════════════════
# MODULE 15 — ARCHITECTURE RAILWAY  (8 concepts)
# Comprendre les logiciels maison déployés sur Railway
# ══════════════════════════════════════════════════════════════════════

CURRICULUM.update({

    "m15_c1_railway_cest_quoi": {
        "module": 15, "ordre": 1,
        "titre": "Railway — C'est quoi?",
        "prereqs": [],
        "texte": """
Railway est une plateforme d'hébergement cloud qui permet de déployer des applications web sans gérer de serveurs.
Analogie : Railway est comme un immeuble à appartements — toi tu mets ton meuble (ton code), eux gèrent la plomberie et l'électricité (les serveurs).
Chaque application déployée s'appelle un SERVICE. Un projet Railway peut contenir plusieurs services.
Railway lit ton code depuis GitHub, le compile, et le rend accessible sur Internet via une URL automatique.
Avantage principal : zéro configuration de serveur. Déploiement en quelques clics ou automatique à chaque push GitHub.
        """.strip(),
    },

    "m15_c2_services_jjs": {
        "module": 15, "ordre": 2,
        "titre": "Tes Services Railway",
        "prereqs": ["m15_c1_railway_cest_quoi"],
        "texte": """
Services actifs sur ton compte Railway JJSaguenay :
SCIENTIA CHARLES — app web quiz personnel (scientia-production-ca9c.up.railway.app)
SCIENTIA MAGGIE — app web quiz conjointe (scientia-conjointe-production.up.railway.app)
CC BOT — bot covered calls MSTR (communication IBKR → Telegram)
PORTAIL VOCAL — portail vocal JJS (en migration de Render)
JJS COMPTA — logiciel de comptabilité maison (nouveau)
CRM JJS / PORTAIL DE LA FORGE — gestion membres, remplace GymDesk (nouveau)
Chaque service a ses propres variables d'environnement (secrets) et sa propre base de données.
        """.strip(),
    },

    "m15_c3_variables_environnement": {
        "module": 15, "ordre": 3,
        "titre": "Variables d'Environnement",
        "prereqs": ["m15_c2_services_jjs"],
        "texte": """
Une variable d'environnement est un paramètre secret que l'application lit au démarrage, sans que tu le mettes dans le code.
Exemples : API_KEY, DATABASE_URL, BOT_TOKEN, SMTP_PASSWORD.
Pourquoi ne pas les mettre dans le code? Le code va sur GitHub (public ou semi-public). Un secret dans le code = risque de fuite.
Sur Railway : Settings → Variables → ajouter une clé/valeur. L'app redémarre et peut lire la nouvelle variable.
Règle d'or : si c'est un mot de passe, un token ou une URL de base de données → variable d'environnement, jamais dans le code.
        """.strip(),
    },

    "m15_c4_github_railway_deploiement": {
        "module": 15, "ordre": 4,
        "titre": "GitHub → Railway : Le Déploiement",
        "prereqs": ["m15_c3_variables_environnement"],
        "texte": """
Flux de déploiement : tu modifies du code → tu fais un commit → tu pushes sur GitHub → Railway détecte le changement → redéploiement automatique.
Un COMMIT est une sauvegarde nommée de ton code à un moment précis. Comme une photo de l'état du projet.
Un PUSH envoie les commits locaux vers GitHub (le serveur distant).
Déploiement = Railway prend le nouveau code, le compile (si nécessaire) et remplace l'ancienne version par la nouvelle.
Si le déploiement échoue, Railway garde l'ancienne version en ligne. Aucune interruption de service si le code est cassé.
Sur Railway : onglet Deployments → voir l'historique. Un carré vert = succès. Rouge = échec → lire les logs.
        """.strip(),
    },

    "m15_c5_logs_debogage": {
        "module": 15, "ordre": 5,
        "titre": "Lire les Logs Railway",
        "prereqs": ["m15_c4_github_railway_deploiement"],
        "texte": """
Les logs sont le journal de bord de ton application — chaque ligne raconte ce qui s'est passé.
Sur Railway : sélectionner un service → onglet Logs → voir en temps réel ou historique.
Lignes clés à reconnaître :
ERROR ou EXCEPTION → problème. Lire la ligne suivante pour comprendre la cause.
Listening on port 3000 (ou 8080) → l'app a démarré correctement.
Database connected → la base de données est accessible.
KeyError / undefined / null → une variable ou clé est manquante — souvent une variable d'environnement oubliée.
Méthode : chercher le premier ERROR dans les logs. Tout ce qui suit est la conséquence, pas la cause.
        """.strip(),
    },

    "m15_c6_bases_de_donnees": {
        "module": 15, "ordre": 6,
        "titre": "Bases de Données : SQLite vs PostgreSQL",
        "prereqs": ["m15_c2_services_jjs"],
        "texte": """
Une base de données stocke les informations de façon structurée : membres, transactions, résultats de quiz.
SQLite : fichier unique (.db). Simple, zéro configuration. Idéal en développement ou pour un usage solo.
Limitation : si Railway redémarre, les données dans SQLite sont perdues (car le système de fichiers est éphémère).
PostgreSQL : serveur de base de données dédié. Persistant, robuste, fait pour la production avec plusieurs utilisateurs.
Sur Railway : Add Service → Database → PostgreSQL → Railway crée une URL de connexion automatique.
Règle pratique : SQLite pour tester et développer. PostgreSQL dès que des données réelles et permanentes sont en jeu.
Scientia Charles utilise actuellement SQLite (scientia.db) — acceptable car c'est un quiz personnel.
        """.strip(),
    },

    "m15_c7_tester_avant_prod": {
        "module": 15, "ordre": 7,
        "titre": "Tester Avant de Mettre en Production",
        "prereqs": ["m15_c5_logs_debogage", "m15_c6_bases_de_donnees"],
        "texte": """
Production = ce que les vraies personnes utilisent. Erreur en production = clients affectés, données potentiellement perdues.
Règle absolue (données personnelles) : jamais tester avec les vraies données de membres. Créer des données fictives.
Stratégie de test à 3 niveaux :
1. LOCAL — tester sur ton ordinateur avec données fictives. Aucun risque.
2. STAGING — déployer sur un service Railway séparé (ex. : portail-forge-test). Tester avec quelques vrais comptes.
3. PRODUCTION — déployer seulement quand les niveaux 1 et 2 sont validés.
Questions à poser avant chaque déploiement : Que se passe-t-il si ça plante? Les données sont-elles sauvegardées? Qui est affecté?
        """.strip(),
    },

    "m15_c8_architecture_portail_forge": {
        "module": 15, "ordre": 8,
        "titre": "Architecture du Portail de la Forge",
        "prereqs": ["m15_c7_tester_avant_prod"],
        "texte": """
Le Portail de la Forge est le CRM JJS — il remplace GymDesk pour la gestion des membres.
Architecture cible :
FRONTEND (interface) → ce que tu vois dans le navigateur. HTML/CSS/JavaScript.
BACKEND (serveur) → Python/Flask ou Node.js sur Railway. Reçoit les requêtes, lit/écrit dans la base de données.
BASE DE DONNÉES → PostgreSQL sur Railway. Contient : membres, ceintures, présences, paiements.
API → le protocole de communication entre le frontend et le backend. Format JSON.
Données sensibles dans ce système : noms, coordonnées, informations de paiement des membres.
Exigence minimale avant ouverture aux membres : authentification sécurisée + sauvegarde automatique quotidienne.
        """.strip(),
    },

})


# ══════════════════════════════════════════════════════════════════════
# MODULE 16 — BITCOIN & CRYPTOMONNAIES  (8 concepts)
# Comprendre le Bitcoin, MSTR, IBIT et les covered calls
# ══════════════════════════════════════════════════════════════════════

CURRICULUM.update({

    "m16_c1_bitcoin_protocole": {
        "module": 16, "ordre": 1,
        "titre": "Bitcoin — Le Protocole, Pas le Prix",
        "prereqs": [],
        "texte": """
Bitcoin est un protocole de réseau pair-à-pair qui permet le transfert de valeur sans intermédiaire.
Créé en 2008 par Satoshi Nakamoto (identité inconnue). Le livre blanc : « Bitcoin: A Peer-to-Peer Electronic Cash System ».
Le bloc genesis (3 janvier 2009) contient le titre du Times de Londres : « Chancellor on brink of second bailout for banks » — un message politique sur la raison d'être de Bitcoin.
Bitcoin (BTC) = l'actif natif du réseau. Offre maximale fixée à 21 millions d'unités. Aucune autorité centrale ne peut en créer davantage.
La rareté est programmée dans le code (pas par une décision humaine), ce qui distingue BTC de toutes les monnaies fiat.
Distinguer : Bitcoin (le protocole réseau) vs BTC (l'unité monétaire) vs bitcoin (usage courant pour les deux).
        """.strip(),
    },

    "m16_c2_bitcoin_vs_altcoins": {
        "module": 16, "ordre": 2,
        "titre": "Bitcoin vs Altcoins vs Tokens",
        "prereqs": ["m16_c1_bitcoin_protocole"],
        "texte": """
Bitcoin = le seul crypto-actif avec une offre dure de 21M, décentralisation maximale, et 15+ ans de track record sans faille.
Altcoins (Ethereum, Solana, etc.) = autres blockchains avec leurs propres règles. Plus de flexibilité, moins de décentralisation, moins de sécurité prouvée.
Tokens = actifs créés sur des blockchains existantes. Peuvent représenter n'importe quoi (actions, NFTs, stablecoins).
Stablecoins (USDC, USDT) = tokens indexés sur le dollar américain. Utiles pour les transactions mais pas pour le stockage de valeur.
Positionnement de Charles : exposition concentrée sur Bitcoin via MSTR, MSTE.TO et IBIT. Pas d'altcoins. Thèse : BTC est dans une catégorie à part.
        """.strip(),
    },

    "m16_c3_etf_bitcoin": {
        "module": 16, "ordre": 3,
        "titre": "ETF Bitcoin : IBIT, MSTE.TO",
        "prereqs": ["m16_c2_bitcoin_vs_altcoins"],
        "texte": """
Un ETF (Exchange-Traded Fund) est un fonds qui se négocie en bourse comme une action ordinaire.
ETF Bitcoin = le fonds achète du vrai BTC et émet des parts en bourse. Tu possèdes des parts du fonds, pas du BTC directement.
IBIT (iShares Bitcoin Trust, BlackRock) : le plus grand ETF Bitcoin spot aux États-Unis. Lancé janvier 2024. Actifs sous gestion > 50G$.
MSTE.TO (TSX, Canada) : ETF répliquant l'exposition MSTR sur le TSX. Accessible dans le CELI canadien sans risque de change immédiat.
Avantage ETF vs BTC direct : pas de garde (custody) à gérer, fiscalité simplifiée, accessible dans les comptes enregistrés (CELI).
Inconvénient : frais de gestion annuels, pas de vrai BTC en ta possession.
        """.strip(),
    },

    "m16_c4_mstr_strategy": {
        "module": 16, "ordre": 4,
        "titre": "Strategy (MSTR) — La Proxy Bitcoin",
        "prereqs": ["m16_c3_etf_bitcoin"],
        "texte": """
Strategy Inc (ticker MSTR, anciennement MicroStrategy) est une société cotée en bourse qui détient du Bitcoin comme réserve principale.
Fondée par Michael Saylor. En 2020, Saylor décide d'allouer le bilan de l'entreprise à Bitcoin — thèse : protection contre l'inflation du dollar.
Au sommet : Strategy détient > 500 000 BTC (la plus grande réserve corporative au monde).
mNAV (multiple de la valeur nette des actifs) : ratio entre la capitalisation boursière de MSTR et la valeur de ses BTC.
mNAV > 1 = prime. Tu paies plus que la valeur du BTC. mNAV < 1 = décote (rare, opportunité).
Pourquoi MSTR amplifie BTC : effet de levier via la dette et l'émission d'actions. Quand BTC monte, MSTR monte plus fort. Même chose à la baisse.
Charles détient ~124,58 MSTR dans son CELI.
        """.strip(),
    },

    "m16_c5_covered_calls_mstr": {
        "module": 16, "ordre": 5,
        "titre": "Covered Calls sur MSTR",
        "prereqs": ["m16_c4_mstr_strategy"],
        "texte": """
Un covered call : tu détiens des actions MSTR (« covered ») et tu vends le droit à quelqu'un d'autre de te les acheter à un prix fixé (strike) avant une date donnée (expiration).
En échange, tu reçois une prime (cash immédiat). Si MSTR reste sous le strike, tu gardes tes actions ET la prime. Si MSTR dépasse le strike, tes actions sont « appelées » (rachetées) au prix du strike.
OTM (Out of the Money) : strike > prix actuel. Tu paries que MSTR ne montera pas jusqu'au strike. Prime plus petite, mais risque de cession plus faible.
DTE (Days To Expiration) : durée de vie de l'option. 30-45 DTE est commun pour les covered calls.
Risque principal : si MSTR explose à la hausse, tu ne profites pas de la hausse au-dessus du strike.
Objectif de Charles : générer un revenu passif régulier sur sa position MSTR dans le CELI.
        """.strip(),
    },

    "m16_c6_halving_cycles": {
        "module": 16, "ordre": 6,
        "titre": "Le Halving et les Cycles Bitcoin",
        "prereqs": ["m16_c1_bitcoin_protocole"],
        "texte": """
Le halving est une réduction de 50% de la récompense des mineurs, programmée tous les ~210 000 blocs (~4 ans).
Objectif : réduire progressivement l'émission de nouveaux BTC vers zéro (vers 2140).
Halvings historiques : 2012 (50→25), 2016 (25→12,5), 2020 (12,5→6,25), 2024 (6,25→3,125 BTC/bloc).
Impact historique : chaque halving a été suivi d'un cycle haussier majeur (12-18 mois après).
Thèse : la réduction de l'offre nouvelle combinée à une demande stable ou croissante → hausse des prix.
Attention : les cycles passés ne garantissent pas les cycles futurs. Le marché maturationne et les corrélations changent.
        """.strip(),
    },

    "m16_c7_fiscalite_crypto_canada": {
        "module": 16, "ordre": 7,
        "titre": "Fiscalité Crypto au Canada (ARC)",
        "prereqs": ["m16_c3_etf_bitcoin"],
        "texte": """
Au Canada, les cryptomonnaies sont traitées comme une marchandise (commodity), pas comme une monnaie.
Chaque disposition (vente, échange, utilisation) est un événement imposable. Tu dois déclarer le gain ou la perte.
Gain en capital = prix de vente − coût de base rajusté (CBR). 50% du gain est inclus dans le revenu imposable (inclusion actuelle).
CELI : les gains réalisés dans un CELI ne sont PAS imposables. Les ETF comme IBIT ou MSTE.TO dans le CELI → croissance tax-free.
Attention CELI + options : l'ARC surveille les activités de trading actif dans le CELI. Les covered calls répétés pourraient être requalifiés comme revenu d'entreprise (imposable). Risque à documenter.
Tenue de livres : garder un registre de chaque transaction (date, montant, prix en CAD au moment de la transaction).
        """.strip(),
    },

    "m16_c8_bitcoin_souverainete": {
        "module": 16, "ordre": 8,
        "titre": "Bitcoin comme Actif de Souveraineté",
        "prereqs": ["m16_c1_bitcoin_protocole", "m16_c7_fiscalite_crypto_canada"],
        "texte": """
Au-delà de la spéculation : Bitcoin est un actif qu'aucun gouvernement, banque ou tiers ne peut saisir ou geler si tu le détiens en auto-garde (cold wallet).
Auto-garde (self-custody) : tu contrôles tes propres clés privées. « Not your keys, not your coins ». Portefeuille hardware recommandé : Ledger, Trezor.
Fragmentation de l'ordre mondial : quand des pays sanctionnent d'autres pays ou gèlent des réserves (ex. : gel des réserves russes en 2022), Bitcoin devient une alternative crédible de réserve de valeur souveraine.
Thèse de Charles : exposition via ETF (CELI, simplicité) + conviction long terme sur la rareté et la décentralisation.
Bitcoin n'est pas parfait (scalabilité, volatilité, énergie). Mais c'est le seul actif numérique avec une décentralisation et une immuabilité prouvées sur 15+ ans.
        """.strip(),
    },

})


# ══════════════════════════════════════════════════════════════════════
# MODULE 17 — JSON POUR NON-PROGRAMMEURS  (7 concepts)
# ══════════════════════════════════════════════════════════════════════

CURRICULUM.update({

    "m17_c1_json_cest_quoi": {
        "module": 17, "ordre": 1,
        "titre": "JSON — C'est Quoi?",
        "prereqs": [],
        "texte": """
JSON (JavaScript Object Notation) est le format universel d'échange de données entre outils numériques.
Quand Claude parle à Gmail, quand GymDesk envoie une réservation, quand Railway retourne une erreur — tout ça passe en JSON.
Ce n'est pas du code. C'est un format de texte structuré, lisible par les humains ET les machines.
Exemple minimal :
  {"nom": "Nicolas Tremblay", "cours": "Thématique JJB", "heure": "18h00"}
Ce que tu viens de lire, c'est une réponse JSON. Nicolas Tremblay est inscrit au cours Thématique JJB à 18h.
Pourquoi c'est important pour toi : chaque fois qu'un agent Claude utilise un outil (Gmail MCP, Calendar, GymDesk), il reçoit une réponse en JSON. Quand un outil plante, l'erreur est aussi en JSON. Lire le JSON, c'est lire ce que les agents se disent entre eux.
Analogie : imagine une conversation téléphonique entre deux robots. Toi, tu écoutes leur conversation. JSON, c'est la langue qu'ils parlent.
        """.strip(),
    },

    "m17_c2_objets_tableaux": {
        "module": 17, "ordre": 2,
        "titre": "Objets et Tableaux — Les Deux Briques",
        "prereqs": ["m17_c1_json_cest_quoi"],
        "texte": """
JSON n'a que deux structures : les OBJETS et les TABLEAUX.
OBJET : une collection de paires clé → valeur, entourée d'accolades { }.
  {"prenom": "Patrick", "email": "patrickfaubert12@gmail.com", "actif": true}
La clé est toujours entre guillemets. La valeur suit après les deux points.
TABLEAU : une liste ordonnée de valeurs, entourée de crochets [ ].
  ["Nicolas Tremblay", "David McRae", "Patrick Faubert"]
Ou un tableau d'objets — c'est le cas le plus courant dans les vraies réponses :
  [
    {"nom": "Nicolas Tremblay", "ceinture": "bleu"},
    {"nom": "Patrick Faubert", "ceinture": "marron"}
  ]
Règle mémorisation : ACCOLADES { } = objet (un seul élément décrit). CROCHETS [ ] = tableau (plusieurs éléments).
Dans les réponses de Gmail MCP : la liste des courriels trouvés est un tableau d'objets. Chaque objet décrit un courriel.
        """.strip(),
    },

    "m17_c3_types_valeurs": {
        "module": 17, "ordre": 3,
        "titre": "Les Types de Valeurs",
        "prereqs": ["m17_c2_objets_tableaux"],
        "texte": """
Dans un objet JSON, chaque valeur a un type. Il en existe 6 :
STRING (texte) : entre guillemets doubles. Exemple : "Jiu-Jitsu Saguenay"
NUMBER (nombre) : sans guillemets. Entier ou décimal. Exemple : 158.67 ou 3
BOOLEAN (vrai/faux) : true ou false, sans guillemets. Exemple : "actif": true
NULL (absence de valeur) : null. Exemple : "profil": null — signifie qu'il n'y a pas de profil.
OBJET : accolades imbriquées dans un autre objet.
TABLEAU : crochets imbriqués dans un objet.
Exemples concrets tirés de nos sessions :
  "montant": 158.67          → NUMBER (mensuel de Patrick Faubert)
  "nom": "Patrick Faubert"   → STRING
  "profil_complet": false    → BOOLEAN (fiche manquante)
  "derniere_visite": null    → NULL (jamais venu ou donnée absente)
Quand tu lis une réponse d'API et que tu vois null quelque part, ça signifie : donnée absente ou non fournie. Ce n'est pas une erreur, c'est une information.
        """.strip(),
    },

    "m17_c4_json_imbrique": {
        "module": 17, "ordre": 4,
        "titre": "JSON Imbriqué — Lire la Profondeur",
        "prereqs": ["m17_c3_types_valeurs"],
        "texte": """
Les vraies réponses d'API ne sont jamais plates — elles sont imbriquées. Un objet contient des objets qui contiennent d'autres objets.
Exemple : réponse du CC Bot (IBKR) pour une position couverte :
  {
    "position": {
      "symbole": "MSTR",
      "quantite": 124.58,
      "option_vendue": {
        "strike": 350,
        "expiration": "2026-05-16",
        "prime": 4.20
      }
    },
    "statut": "actif"
  }
Comment lire ça ? Commence par le niveau le plus haut et descends.
Niveau 1 : position (un objet) + statut (une string "actif")
Niveau 2 dans "position" : symbole, quantite, option_vendue
Niveau 3 dans "option_vendue" : strike, expiration, prime
La technique : cherche les accolades { } qui s'ouvrent et se ferment. Chaque paire = un niveau.
Exercice mental : quand tu vois une réponse longue, trouve d'abord les clés du niveau 1, puis descends dans celle qui t'intéresse.
        """.strip(),
    },

    "m17_c5_reponse_api_gmail": {
        "module": 17, "ordre": 5,
        "titre": "Lire une Vraie Réponse — Gmail MCP",
        "prereqs": ["m17_c4_json_imbrique"],
        "texte": """
Voici ce que le MCP Gmail retourne quand Claude cherche les réservations GymDesk :
  {
    "threads": [
      {
        "id": "18f3a2c...",
        "snippet": "Nicolas Tremblay booked Thématique JJB on 22/04/2026",
        "messages": [
          {
            "from": "noreply@gymdesk.com",
            "subject": "Nicolas Tremblay booked Thématique JJB on 22/04/2026",
            "date": "2026-04-20T14:32:00Z"
          }
        ]
      }
    ],
    "resultSizeEstimate": 1
  }
Comment lire ça :
- "threads" est un tableau → plusieurs courriels possibles
- Chaque thread a un "id" (identifiant unique), un "snippet" (aperçu du texte), et des "messages"
- "resultSizeEstimate": 1 → Gmail a trouvé 1 résultat
- La date "2026-04-20T14:32:00Z" est au format ISO 8601 — le "Z" signifie fuseau UTC (pas l'heure de Saguenay)
Quand Claude me dit "j'ai trouvé 3 réservations pour ce cours", il a lu exactement ce genre de structure et compté les éléments dans le tableau "threads".
        """.strip(),
    },

    "m17_c6_json_vs_code": {
        "module": 17, "ordre": 6,
        "titre": "JSON vs Code — La Différence",
        "prereqs": ["m17_c4_json_imbrique"],
        "texte": """
Confusion fréquente : JSON ressemble à du code, mais ce n'est pas du code.
JSON = données structurées. Comme un formulaire rempli. Il décrit, il ne fait rien.
Code = instructions exécutables. Il fait quelque chose.
Analogie : un menu de restaurant (JSON) vs la recette de cuisine (code). Le menu décrit les plats, la recette dit comment les préparer.
JSON ne peut pas :
- Faire des calculs
- Prendre des décisions
- S'exécuter
JSON peut :
- Décrire n'importe quelle structure de données
- Être lu par n'importe quel langage (Python, JavaScript, Ruby...)
- Être transmis entre systèmes (API → MCP → Claude)
Dans notre contexte : les skills Scientia sont en Python (code). Les réponses des MCPs sont en JSON (données). CLAUDE.md est du Markdown (texte formaté). Ce sont trois choses différentes.
Quand tu lis une réponse d'agent et que tu ne sais pas si c'est "du code" ou des données — si c'est entouré d'accolades { } ou de crochets [ ], c'est du JSON.
        """.strip(),
    },

    "m17_c7_erreurs_format_json": {
        "module": 17, "ordre": 7,
        "titre": "Erreurs Courantes de Format JSON",
        "prereqs": ["m17_c5_reponse_api_gmail"],
        "texte": """
Quand un agent reçoit du JSON malformé, il plante avec une erreur de parsing. Reconnaître ces erreurs aide à comprendre d'où vient le problème.
Erreur 1 — Virgule manquante ou en trop :
  {"nom": "Patrick" "email": "..."} ← manque une virgule après "Patrick"
  {"nom": "Patrick", "email": "...",} ← virgule en trop à la fin (certains parseurs acceptent, d'autres non)
Erreur 2 — Guillemets incorrects :
  {"nom": 'Patrick'} ← guillemets simples invalides en JSON. Toujours des guillemets doubles " "
Erreur 3 — Accolades ou crochets non fermés :
  {"athletes": ["Nicolas", "Patrick"} ← le crochet ] n'est pas fermé avant l'accolade }
Erreur 4 — Valeur non reconnue :
  {"actif": True} ← True avec majuscule est invalide. JSON exige true (minuscule)
Erreur 5 — Troncature :
  {"athletes": ["Nicolas", ... ← réponse coupée (souvent par une limite de taille)
Quand tu vois "JSON parse error", "Unexpected token", ou "Invalid JSON" dans une erreur d'agent — cherche un de ces cinq problèmes dans la réponse brute.
        """.strip(),
    },

})


# ══════════════════════════════════════════════════════════════════════
# MODULE 18 — LIRE UNE ERREUR D'AGENT  (6 concepts)
# ══════════════════════════════════════════════════════════════════════

CURRICULUM.update({

    "m18_c1_anatomie_erreur": {
        "module": 18, "ordre": 1,
        "titre": "Anatomie d'un Message d'Erreur",
        "prereqs": [],
        "texte": """
Un message d'erreur a toujours la même structure, quelle que soit la technologie. Apprendre à la lire, c'est apprendre à localiser la panne sans comprendre le code.
Les 4 parties d'une erreur :
TYPE : la catégorie d'erreur. Exemple : "FileNotFoundError", "AuthenticationError", "TimeoutError". Le type te dit QUO I a planté.
MESSAGE : la description humaine. Exemple : "No such file or directory: 'profils.json'". Le message te dit POURQUOI.
LOCALISATION : le fichier et la ligne où ça s'est passé. Exemple : "File curriculum.py, line 847". La localisation te dit OÙ.
STACK TRACE : la séquence d'appels qui a mené à l'erreur. Comme les étapes d'un récit remontant jusqu'à la cause.
Erreur réelle de nos sessions :
  FileNotFoundError: [Errno 2] No such file or directory:
  '/sessions/gracious-ecstatic-darwin/mnt/Claude/plans-de-cours/profil_faubert.json'
Lecture : type = FileNotFoundError (fichier introuvable), message = le chemin exact qui manque. Diagnostic immédiat : le fichier n'existe pas à cet emplacement — soit le nom est faux, soit le dossier est différent.
        """.strip(),
    },

    "m18_c2_codes_http": {
        "module": 18, "ordre": 2,
        "titre": "Codes HTTP — Le Langage des APIs",
        "prereqs": ["m18_c1_anatomie_erreur"],
        "texte": """
Quand un MCP (Gmail, Calendar, GymDesk) communique avec son serveur, il utilise des codes HTTP pour indiquer le résultat. Ces codes sont universels.
Codes 2xx — Succès :
  200 OK → ça a marché
  201 Created → un élément a été créé (ex : draft Gmail créé)
Codes 4xx — Problème de ton côté :
  400 Bad Request → la requête est malformée (mauvais format, paramètre manquant)
  401 Unauthorized → pas authentifié (token manquant ou expiré)
  403 Forbidden → authentifié, mais pas la permission
  404 Not Found → la ressource n'existe pas (mauvais ID de thread Gmail, mauvais endpoint)
  429 Too Many Requests → tu as dépassé la limite de fréquence de l'API (rate limit)
Codes 5xx — Problème du côté serveur :
  500 Internal Server Error → le serveur de Gmail/Railway/etc. a planté, pas ton code
  503 Service Unavailable → le service est temporairement hors ligne
Règle pratique : 4xx = c'est réparable de ton côté. 5xx = attendre que le serveur revienne.
Exemple concret : si le CC Bot retourne 401, c'est que le token IBKR a expiré. Si tu vois 429, le bot a fait trop de requêtes trop vite.
        """.strip(),
    },

    "m18_c3_types_erreurs_agent": {
        "module": 18, "ordre": 3,
        "titre": "Quatre Types d'Erreurs d'Agent",
        "prereqs": ["m18_c2_codes_http"],
        "texte": """
Les erreurs dans un workflow Claude tombent dans quatre catégories. Les identifier, c'est pointer vers la bonne solution.
TYPE 1 — Erreur d'authentification (Auth)
  Symptôme : "401 Unauthorized", "Invalid token", "Permission denied"
  Cause : clé API expirée, mauvais compte, scope insuffisant
  Solution : renouveler le token, vérifier les permissions du compte
TYPE 2 — Erreur de format / données
  Symptôme : "JSON parse error", "Missing required field", "Invalid parameter"
  Cause : les données envoyées ne correspondent pas à ce qu'attend l'outil
  Solution : vérifier le format, corriger le paramètre
TYPE 3 — Erreur de ressource introuvable
  Symptôme : "404 Not Found", "FileNotFoundError", "No results"
  Cause : mauvais chemin, mauvais ID, fichier déplacé ou renommé
  Solution : vérifier le chemin exact, corriger l'identifiant
TYPE 4 — Erreur de réseau / timeout
  Symptôme : "Connection timeout", "Service unavailable", "Read timeout"
  Cause : serveur lent, connexion internet coupée, service en maintenance
  Solution : réessayer plus tard, vérifier la connexion
Exemple de nos sessions : "Resource deadlock avoided" sur le fichier @socialwithaayan → TYPE 4 (le système de fichiers était verrouillé).
        """.strip(),
    },

    "m18_c4_stack_trace": {
        "module": 18, "ordre": 4,
        "titre": "Stack Trace — Lire Sans Coder",
        "prereqs": ["m18_c3_types_erreurs_agent"],
        "texte": """
La stack trace (trace de pile) est la liste des étapes qui ont mené à l'erreur, du plus récent au plus ancien. Elle fait peur à première vue — mais tu n'as besoin de lire que deux choses.
Exemple :
  Traceback (most recent call last):
    File "app.py", line 142, in generer_pdf
      rapport = creer_rapport(athletes)
    File "pdf_generator.py", line 38, in creer_rapport
      data = json.loads(profil_texte)
    File "<string>", line 1, in loads
  json.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
Ce que tu lis :
1. LA PREMIÈRE LIGNE : "Traceback (most recent call last)" → c'est une trace de pile, ok.
2. LA DERNIÈRE LIGNE : "json.JSONDecodeError: Expecting value: line 1 column 1" → le type d'erreur et le message. C'est tout ce dont tu as besoin pour diagnostiquer.
Le reste (les "File" intermédiaires) te dit où ça s'est passé dans le code — utile pour un développeur, pas nécessaire pour toi.
Règle : dans une stack trace, lis la première ligne (titre) et la dernière ligne (erreur réelle). Le reste est contexte.
        """.strip(),
    },

    "m18_c5_diagnostic_vs_resolution": {
        "module": 18, "ordre": 5,
        "titre": "Diagnostiquer vs Résoudre",
        "prereqs": ["m18_c4_stack_trace"],
        "texte": """
Ta valeur en tant qu'orchestrateur d'agents n'est pas de résoudre les erreurs de code — c'est de les diagnostiquer correctement pour que l'agent (ou le développeur) puisse les résoudre.
Diagnostiquer = identifier QUI a planté, QUOI a planté, et POURQUOI.
Résoudre = modifier le code, la configuration, ou la donnée.
Tu peux diagnostiquer sans résoudre. C'est déjà énorme.
Exemple de bon diagnostic :
  "L'erreur est dans la génération du PDF, pas dans la recherche Gmail. L'agent a bien récupéré 3 réservations, mais plante quand il essaie de créer le fichier. Le message dit 'Permission denied' — le dossier Plans de cours est peut-être en lecture seule."
Ce diagnostic permet à l'agent de savoir exactement où chercher et quoi corriger.
Exemple de mauvais diagnostic :
  "Ça marche pas."
La progression : d'abord tu vois une erreur et tu la rapportes intégralement. Ensuite tu identifies le type (auth, format, fichier, réseau). Ensuite tu localises l'étape qui a planté dans le workflow. C'est le chemin pour devenir un meilleur chef d'orchestre.
        """.strip(),
    },

    "m18_c6_erreurs_de_nos_sessions": {
        "module": 18, "ordre": 6,
        "titre": "Erreurs Réelles — Nos Sessions",
        "prereqs": ["m18_c5_diagnostic_vs_resolution"],
        "texte": """
Revue des vraies erreurs rencontrées dans nos workflows, avec leur diagnostic.
ERREUR 1 — Fichier sante/ vide (0 bytes)
  Symptôme : la note trouble-testosterone-today.md était vide dans sante/
  Diagnostic : deux dossiers coexistaient (sante/ et santé/ avec accent). Le fichier existait dans santé/ (avec accent) mais pas dans sante/. Erreur de type "ressource introuvable" causée par une ambiguïté de nom de dossier.
  Résolution : copier le contenu de santé/ vers sante/.
ERREUR 2 — Fichier verrouillé (@socialwithaayan)
  Symptôme : "Resource deadlock avoided" au Read et au bash cat
  Diagnostic : macOS avait un verrou sur le fichier (flag uchg). Type réseau/système — pas une erreur de code.
  Résolution : chflags nouchg depuis le terminal Mac.
ERREUR 3 — Patrick Faubert sans profil
  Symptôme : 4 tentatives de recherche Gmail, aucun profil trouvé
  Diagnostic : le profil n'existait pas. Ce n'était pas une erreur de recherche — c'était l'absence réelle de donnée.
  Leçon : distinguer "je n'ai pas trouvé" (erreur de recherche) de "ça n'existe pas" (donnée absente).
Ces trois cas illustrent les types 3 (ressource), 4 (système/verrou), et un faux positif (donnée absente ≠ erreur).
        """.strip(),
    },

})


# ══════════════════════════════════════════════════════════════════════
# MODULE 19 — ANATOMIE D'UN WORKFLOW CLAUDE  (7 concepts)
# ══════════════════════════════════════════════════════════════════════

CURRICULUM.update({

    "m19_c1_mcp_cest_quoi": {
        "module": 19, "ordre": 1,
        "titre": "MCP — Le Pont Entre Claude et Tes Outils",
        "prereqs": [],
        "texte": """
MCP signifie Model Context Protocol. C'est le standard qui permet à Claude de parler à des outils externes : Gmail, Google Calendar, GymDesk, Railway, et d'autres.
Sans MCP, Claude peut seulement lire ce que tu lui envoies dans la conversation. Avec un MCP, Claude peut aller chercher de l'information dans tes vrais outils — lire tes courriels, créer des événements, générer des fichiers.
Analogie : Claude est un consultant très intelligent. Sans MCP, tu lui apportes tous tes documents et il les lit. Avec MCP, il a accès direct à ta base de données, ton courriel, ton calendrier.
Les MCPs que tu utilises actuellement dans Cowork :
- Gmail MCP → chercher/lire/créer des courriels
- Google Calendar MCP → lire/créer des événements
- Google Drive MCP → lire/écrire des fichiers
- Canva MCP → créer et modifier des designs
Chaque MCP est une connexion sécurisée et autorisée — tu l'as approuvé explicitement. Claude ne peut pas accéder à ces outils sans ta permission.
Un MCP = un outil externe rendu accessible à Claude. Plus tu en as, plus Claude peut agir dans ton vrai environnement.
        """.strip(),
    },

    "m19_c2_skill_cest_quoi": {
        "module": 19, "ordre": 2,
        "titre": "Skill — Une Procédure Mémorisée",
        "prereqs": ["m19_c1_mcp_cest_quoi"],
        "texte": """
Un skill est un fichier d'instructions que Claude lit avant d'exécuter une tâche complexe. C'est l'équivalent d'un manuel de procédure que tu écris une fois et que Claude consulte chaque fois.
Dans ton setup actuel, tu as une dizaine de skills dans le dossier .claude/skills/ :
- plan-de-cours : comment récupérer les réservations GymDesk, chercher les profils Gmail, générer le PDF
- curateur-actualite : comment générer une revue d'actualité, quelles sources cibler, quel format produire
- vault-ingest : comment transformer un fichier raw/ en note wiki structurée
- tend-the-vault : comment analyser le journal et proposer des connexions entre notes
Sans skill, tu devrais réexpliquer la procédure complète à chaque conversation. Avec un skill, Claude sait exactement quoi faire — les étapes, les règles, les cas d'exception.
La différence entre un bon et un mauvais skill : un bon skill est précis sur les cas d'exception et les décisions à prendre. Un mauvais skill est vague et force Claude à improviser, ce qui produit des résultats inconsistants.
Tu as le pouvoir de créer, modifier et améliorer tes skills. C'est exactement ce que fait le skill-creator.
        """.strip(),
    },

    "m19_c3_tool_call": {
        "module": 19, "ordre": 3,
        "titre": "Tool Call — Une Action d'Agent",
        "prereqs": ["m19_c1_mcp_cest_quoi"],
        "texte": """
Un tool call (appel d'outil) est l'action concrète qu'effectue Claude quand il utilise un MCP ou un outil. C'est une étape invisible pour toi, mais fondamentale.
Quand Claude cherche tes réservations GymDesk, voici ce qui se passe :
1. Claude décide qu'il a besoin de chercher dans Gmail
2. Il formule un tool call : "chercher les courriels de gymdesk.com avec la date 22/04/2026"
3. Le MCP Gmail envoie cette requête à l'API Gmail
4. Gmail retourne une réponse JSON avec les courriels trouvés
5. Claude lit la réponse et continue son travail
Tout ça se passe en quelques secondes. Tu vois le résultat ("J'ai trouvé 3 inscriptions") sans voir les étapes intermédiaires.
Pourquoi c'est utile de savoir ça :
- Si une étape plante, tu peux demander "à quel tool call exactement ça a planté?"
- Tu peux évaluer si Claude a formulé le bon tool call (bonne requête de recherche)
- Tu peux identifier des inefficacités (5 tool calls là où 2 suffiraient)
Chaque tool call coûte du temps et de la capacité. Un workflow efficace minimise le nombre d'appels tout en obtenant toutes les informations nécessaires.
        """.strip(),
    },

    "m19_c4_context_window": {
        "module": 19, "ordre": 4,
        "titre": "Context Window — La Mémoire de Travail",
        "prereqs": ["m19_c3_tool_call"],
        "texte": """
Le context window (fenêtre de contexte) est la quantité d'information que Claude peut traiter en une seule conversation. C'est sa "mémoire de travail" — il peut tout voir dans la fenêtre, mais rien en dehors.
Capacité actuelle : Claude Sonnet 4 peut traiter environ 200 000 tokens (un token ≈ 0,75 mot). C'est long — un roman complet fait environ 100 000 tokens.
Ce que Claude garde en mémoire pendant une conversation :
- Tout ce que tu as dit
- Tout ce qu'il a répondu
- Tous les résultats de tool calls (réponses des MCPs)
- Le contenu des fichiers qu'il a lus
Ce que Claude ne garde PAS entre les conversations :
- Rien. Chaque conversation repart à zéro.
C'est pour ça que CLAUDE.md existe dans ton vault — c'est un fichier de contexte persistant que Claude lit au début de chaque session pour se rappeler qui tu es, quels sont tes projets, ta terminologie.
Symptôme d'une fenêtre trop remplie : quand une conversation devient très longue, Claude peut "oublier" des instructions données au début. C'est un signe que le context window approche sa limite.
        """.strip(),
    },

    "m19_c5_claude_md_mega_prompt": {
        "module": 19, "ordre": 5,
        "titre": "CLAUDE.md — Ton Mega-Prompt Persistant",
        "prereqs": ["m19_c4_context_window"],
        "texte": """
CLAUDE.md est le fichier de mémoire persistante de ton système. Claude le lit automatiquement au début de chaque session Cowork.
Ce qu'il contient actuellement :
- Qui tu es (Charles Roy, Saguenay, investisseur, entraîneur JJS)
- Tes projets en cours (CC Bot, Scientia, vault Obsidian)
- Ta terminologie personnelle (CELI, MSTR, MSTE.TO, CC Bot, kill switch)
- Tes préférences (langue française, style direct, pas d'émojis)
- Tes overrides spécifiques (livraison curateur → vault Obsidian, pas Kindle)
Sans CLAUDE.md, tu devrais réexpliquer ton contexte à chaque nouvelle conversation. Avec CLAUDE.md, Claude arrive "briefé" — il sait déjà tout ce qui est dans ce fichier.
C'est la première couche de ton système d'orchestration. Plus CLAUDE.md est précis et à jour, mieux Claude peut agir de façon cohérente sans que tu aies à répéter.
Comment l'améliorer : quand quelque chose change (nouveau projet, nouvelle préférence, nouvelle terminologie), dis-le pour que le fichier soit mis à jour. CLAUDE.md périmé = Claude qui agit sur de vieilles informations.
        """.strip(),
    },

    "m19_c6_mcp_connectes": {
        "module": 19, "ordre": 6,
        "titre": "Les MCPs de Ton Écosystème",
        "prereqs": ["m19_c1_mcp_cest_quoi", "m19_c5_claude_md_mega_prompt"],
        "texte": """
Cartographie des MCPs actifs dans ton setup Cowork, ce qu'ils permettent et leurs limites.
Gmail MCP
  → Lire, chercher, créer des brouillons d'emails
  → Utilisé pour : récupérer réservations GymDesk, chercher profils athlètes, envoyer des livres sur BOOX
  → Limite : ne peut pas envoyer directement (seulement créer des brouillons pour la plupart des actions)
Google Calendar MCP
  → Lire et créer des événements
  → Utilisé pour : vérifier l'horaire avant de générer un plan de cours
Google Drive MCP
  → Lire et écrire des fichiers Google Docs/Sheets
  → Moins utilisé actuellement — ton vault est local (Obsidian), pas Drive
Canva MCP
  → Créer et modifier des designs Canva depuis Claude
  → Utilisé pour : affiche, contenu visuel JJS
Cowork File System
  → Accès direct aux fichiers de ton Mac (dossier sélectionné = /mnt/Claude)
  → C'est le plus important : tout ton vault Obsidian, tous tes fichiers, accessibles directement
Chaque MCP a été autorisé par toi. Claude ne peut pas dépasser les permissions que tu lui as accordées.
        """.strip(),
    },

    "m19_c7_workflow_bout_en_bout": {
        "module": 19, "ordre": 7,
        "titre": "Un Workflow de Bout en Bout — Plan de Cours",
        "prereqs": ["m19_c3_tool_call", "m19_c2_skill_cest_quoi"],
        "texte": """
Décortiquons le workflow plan-de-cours pour voir tous les concepts en action.
1. Déclencheur : tu dis "sors le plan de cours pour ce soir"
2. Claude lit le skill plan-de-cours → il reçoit les instructions complètes de la procédure
3. Tool call 1 : Gmail MCP → cherche "from:gymdesk.com booked 22/04/2026"
   → Réponse JSON : liste des réservations avec noms et types de cours
4. Claude filtre les résultats : sépare Thématique JJB 18h, Kickboxing 18h, Compétition 19h, MMA 19h
5. Pour chaque athlète : tool calls 2-10+ → Gmail MCP cherche "subject:Profil athlète [prenom]"
   → Réponse JSON : le contenu de chaque fiche profil
6. Claude analyse les profils et prépare les données (niveau, objectifs, frustrations, pairings)
7. Tool call final : Write → génère le PDF avec reportlab et le sauvegarde dans Plans de cours/
8. Claude te présente le lien vers le fichier
Ce workflow mobilise : 1 skill, 10-15 tool calls, 2 MCPs (Gmail + Filesystem), 1 bibliothèque Python (reportlab). Durée : 2-4 minutes. Si tu devais faire ça manuellement : 30-45 minutes.
Là où tu interviens : définir le cours (si ambigu), valider les pairings proposés, envoyer le formulaire aux athlètes sans fiche.
        """.strip(),
    },

})


# ══════════════════════════════════════════════════════════════════════
# MODULE 20 — CONCEVOIR UN WORKFLOW MULTI-AGENTS  (7 concepts)
# ══════════════════════════════════════════════════════════════════════

CURRICULUM.update({

    "m20_c1_decomposer_tache": {
        "module": 20, "ordre": 1,
        "titre": "Décomposer une Tâche en Étapes Agentiques",
        "prereqs": [],
        "texte": """
La compétence centrale du chef d'orchestre d'agents : prendre une tâche complexe et la découper en étapes que des agents peuvent exécuter.
Mauvaise façon de briefer un agent :
  "Prépare mon cours de ce soir."
C'est ambigu — quel cours? à quelle heure? quel type de livrable?
Bonne façon — décomposition en étapes :
  1. Identifier le cours (type + heure + date)
  2. Récupérer les réservations GymDesk pour ce cours
  3. Pour chaque inscrit, chercher son profil athlète dans Gmail
  4. Synthétiser les profils en 3-4 lignes par athlète
  5. Proposer des pairings logiques basés sur le niveau et les objectifs
  6. Générer un PDF et le sauvegarder
Chaque étape est une action concrète et vérifiable. On sait quand elle est complète.
Critères d'une bonne étape agentique :
- Une seule action claire (chercher, filtrer, générer, sauvegarder)
- Un résultat identifiable (réservations trouvées, profil récupéré, fichier créé)
- Une façon de savoir si elle a échoué (aucun résultat, fichier manquant, erreur retournée)
Exercice : prends ta prochaine tâche complexe. Avant de me la donner, découpe-la en 5-8 étapes. Tu verras immédiatement où sont les ambiguïtés.
        """.strip(),
    },

    "m20_c2_sequentiel_parallele": {
        "module": 20, "ordre": 2,
        "titre": "Séquentiel vs Parallèle — Quand Utiliser Quoi",
        "prereqs": ["m20_c1_decomposer_tache"],
        "texte": """
Certaines étapes doivent se faire dans un ordre précis. D'autres peuvent se faire en même temps. La distinction change la vitesse d'un workflow.
SÉQUENTIEL : étape B dépend du résultat de l'étape A. Tu ne peux pas commencer B sans A.
  Exemple : tu ne peux pas chercher le profil de Nicolas Tremblay (étape 2) avant de savoir qu'il est inscrit (étape 1).
PARALLÈLE : plusieurs étapes peuvent se lancer en même temps sans dépendre les unes des autres.
  Exemple : une fois que tu as la liste des 4 athlètes inscrits, tu peux chercher les 4 profils en parallèle — pas besoin d'attendre le profil de Nicolas pour commencer celui de Patrick.
Dans le plan de cours : récupérer les réservations (séquentiel, d'abord) → chercher tous les profils (parallèle possible) → générer le PDF (séquentiel, après).
Pourquoi ça compte : un workflow 100% séquentiel avec 10 étapes prend 10x le temps d'une étape. Un workflow intelligent regroupe les étapes parallèles et réduit drastiquement le temps total.
Quand tu conçois un workflow, pose-toi la question : "Est-ce que cette étape A besoin du résultat de l'étape précédente?" Si non → parallèle possible.
        """.strip(),
    },

    "m20_c3_points_validation": {
        "module": 20, "ordre": 3,
        "titre": "Points de Validation Humaine",
        "prereqs": ["m20_c2_sequentiel_parallele"],
        "texte": """
Un workflow tout-automatique est efficace mais risqué. Un workflow avec trop de validation humaine est sûr mais lent. La compétence est de placer les points de validation au bon endroit.
Quand insérer une validation humaine :
- Avant une action irréversible (supprimer un fichier, envoyer un courriel, publier un post)
- Quand la décision requiert un jugement de valeur (prioriser une tâche, choisir un ton)
- Quand l'agent n'a pas les informations pour décider (ambiguïté, données manquantes)
- Quand l'enjeu est élevé (argent, réputation, relations)
Quand ne PAS insérer de validation :
- Actions répétitives bien définies (chercher des courriels, lire des fichiers)
- Transformations standards (formater un texte, calculer une somme)
- Étapes de collecte d'information (sans modification)
Exemple plan de cours : validation AVANT la génération des pairings (tu veux vérifier qui est vraiment là) mais PAS pour chaque recherche de profil Gmail (action standard, tu veux que ce soit automatique).
Règle pratique : automatise la collecte, valide les décisions.
        """.strip(),
    },

    "m20_c4_exceptions": {
        "module": 20, "ordre": 4,
        "titre": "Gérer les Cas d'Exception",
        "prereqs": ["m20_c3_points_validation"],
        "texte": """
Un workflow bien conçu anticipe ce qui peut mal tourner. Les exceptions non anticipées arrêtent le workflow — les exceptions anticipées sont gérées gracieusement.
Types d'exceptions courants dans nos workflows :
- Profil athlète manquant → lister l'athlète dans "fiches manquantes" plutôt que de planter
- Aucune réservation trouvée → informer l'utilisateur plutôt que générer un PDF vide
- Fichier déjà existant → overwrite ou nommer différemment, pas crasher
- MCP qui ne répond pas → attendre et réessayer, ou informer que le service est indisponible
La différence entre un skill fragile et un skill robuste : le skill robuste a des "chemins alternatifs" pour chaque exception prévue. Exemple dans plan-de-cours : si aucun profil trouvé après 4 tentatives → pas d'erreur, juste une note "fiche manquante — envoyer le formulaire à [email]".
Comment améliorer un skill existant : après chaque utilisation, note les exceptions rencontrées qui n'étaient pas anticipées. Ajoute une règle dans le skill pour les gérer. Après quelques itérations, le skill devient très robuste.
        """.strip(),
    },

    "m20_c5_briefer_agent": {
        "module": 20, "ordre": 5,
        "titre": "Briefer un Agent Correctement",
        "prereqs": ["m20_c1_decomposer_tache"],
        "texte": """
La qualité du brief détermine la qualité du résultat. Un agent reçoit exactement ce que tu lui donnes — ni plus, ni moins.
Les 5 éléments d'un bon brief :
1. CONTEXTE : qui tu es, quel est l'objectif global
   "Je suis entraîneur JJS. Je prépare un cours de Thématique JJB pour ce soir 18h."
2. TÂCHE : ce que tu veux que l'agent fasse concrètement
   "Génère un plan de cours avec les profils des athlètes inscrits et des pairings logiques."
3. CONTRAINTES : ce qu'il ne faut PAS faire, les limites
   "Ne propose pas de drills ou de techniques. Juste les profils et les pairings."
4. FORMAT : à quoi doit ressembler le livrable
   "Un PDF dans Plans de cours/, nommé Profils_equipes_2026-04-22_18h00.pdf"
5. DÉFINITION DE SUCCÈS : comment tu sais que c'est réussi
   "Un PDF lisible avec 3-4 lignes par athlète et 2-3 phrases de justification pour les pairings."
Ce qui améliore un brief : les exemples concrets ("comme la semaine dernière"), les contre-exemples ("pas comme dans le PDF du 10 avril où les pairings étaient trop vagues"), et les références à des sessions passées.
        """.strip(),
    },

    "m20_c6_evaluer_sortie": {
        "module": 20, "ordre": 6,
        "titre": "Évaluer la Sortie d'un Agent",
        "prereqs": ["m20_c5_briefer_agent"],
        "texte": """
Un agent produit toujours quelque chose. Ta compétence d'orchestrateur est de savoir évaluer si cette sortie est correcte, sans nécessairement comprendre comment elle a été produite.
Les 4 questions à se poser face à une sortie d'agent :
1. COMPLÉTUDE : est-ce que tout ce qui devait être fait est là?
   → Le PDF contient-il tous les athlètes inscrits? Les 4 sections requises?
2. EXACTITUDE : les informations sont-elles correctes?
   → Les noms correspondent-ils aux inscriptions? Les pairings respectent-ils les niveaux?
3. FORMAT : le livrable est-il dans le bon format au bon endroit?
   → Le PDF est-il dans Plans de cours/? Le nom est-il correct?
4. COHÉRENCE : le résultat est-il cohérent avec les sessions précédentes?
   → Est-ce que ça ressemble à ce qu'on a produit le mois dernier?
Ce que tu ne dois PAS vérifier : comment l'agent a formulé ses requêtes Gmail, quel code Python il a utilisé pour générer le PDF, le nombre de tool calls. C'est le "comment" — pas ta responsabilité.
Ton rôle : évaluer le "quoi" (le résultat) et donner un feedback précis sur ce qui manque ou est incorrect.
        """.strip(),
    },

    "m20_c7_iterer_skill": {
        "module": 20, "ordre": 7,
        "titre": "Itérer sur un Skill — L'Amélioration Continue",
        "prereqs": ["m20_c6_evaluer_sortie", "m20_c4_exceptions"],
        "texte": """
Un skill n'est jamais parfait à la première version. Il s'améliore par itérations successives. C'est le processus qui transforme un workflow fragile en système robuste.
Le cycle d'amélioration d'un skill :
1. Utiliser le skill → identifier ce qui n'a pas fonctionné comme prévu
2. Formuler une règle précise pour ce cas ("si le profil n'est pas trouvé après 4 requêtes, ne pas déclarer absent avant d'avoir essayé le prénom seul")
3. Ajouter la règle dans le skill
4. Réutiliser → valider que le cas est maintenant géré
Exemples d'itérations réelles sur plan-de-cours :
- V1 : cherchait le profil avec le nom exact seulement → ratait les accents manquants
- V2 : ajout de 4 stratégies de recherche (nom complet, prénom, nom, recherche large)
- V3 : ajout de la note "fiches manquantes" pour les athlètes sans profil
- V4 : ajout du cas où plusieurs cours tournent en même temps → un PDF par cours
Chaque itération rend le skill plus robuste et réduit les cas où tu dois intervenir manuellement.
Mesure de maturité d'un skill : si tu utilises le skill 10 fois sans devoir corriger la sortie, il est mature. En dessous, il y a encore des itérations à faire.
        """.strip(),
    },

})


# ══════════════════════════════════════════════════════════════════════
# MODULE 21 — BASH ET TERMINAL — L'ESSENTIEL  (7 concepts)
# ══════════════════════════════════════════════════════════════════════

CURRICULUM.update({

    "m21_c1_terminal_cest_quoi": {
        "module": 21, "ordre": 1,
        "titre": "Terminal — C'est Quoi?",
        "prereqs": [],
        "texte": """
Le terminal (aussi appelé console, shell, ou ligne de commande) est une interface en texte pour donner des instructions directes à l'ordinateur — sans passer par une interface graphique.
Sur Mac, l'application s'appelle "Terminal" (dans Applications → Utilitaires) ou "iTerm2" si tu l'as installé.
Bash est la langue que tu parles dans ce terminal. C'est un ensemble de commandes avec une syntaxe précise. Chaque commande = une instruction.
Pourquoi c'est important pour toi :
- Tout ce que Claude exécute dans le sandbox passe par Bash
- Les scripts du CC Bot, les déploiements Railway, les corrections de fichiers — tout est Bash
- Quand je te montre une commande dans notre conversation (ex : chflags nouchg), c'est du Bash que tu executes dans ton terminal Mac
Tu l'as déjà utilisé : quand tu as collé les commandes chflags pour débloquer les fichiers Obsidian, c'était du Bash dans ton terminal.
La courbe d'apprentissage est courte pour l'essentiel. Tu n'as pas besoin de maîtriser Bash — tu as besoin de reconnaître ce qu'une commande fait, de la lire, et de l'exécuter en sécurité.
        """.strip(),
    },

    "m21_c2_navigation": {
        "module": 21, "ordre": 2,
        "titre": "Navigation — Se Repérer dans les Fichiers",
        "prereqs": ["m21_c1_terminal_cest_quoi"],
        "texte": """
Trois commandes suffisent pour naviguer dans le système de fichiers depuis le terminal.
pwd (print working directory) — Où suis-je?
  Tape pwd, le terminal affiche le chemin complet du dossier où tu te trouves.
  Exemple : /Users/charles/Documents/Obsidian/Claude
ls (list) — Quoi est ici?
  Tape ls, le terminal liste le contenu du dossier courant.
  ls -la affiche aussi les fichiers cachés (ceux qui commencent par un point) et les permissions.
cd (change directory) — Aller quelque part
  cd NomDuDossier → entrer dans un sous-dossier
  cd .. → remonter d'un niveau
  cd ~ → aller directement dans ton dossier personnel (/Users/charles)
  cd /chemin/absolu → aller directement à un chemin spécifique
Exemple concret — naviguer vers ton vault :
  cd ~/Documents/Obsidian/Claude
  ls
  → tu vois : Domaines/ Journal/ Plans de cours/ Projets/ ...
Astuce : appuie sur Tab pour auto-compléter les noms de fichiers et dossiers. Tape cd Dom puis Tab → le terminal complète en cd Domaines/.
        """.strip(),
    },

    "m21_c3_lire_ecrire_fichiers": {
        "module": 21, "ordre": 3,
        "titre": "Lire et Inspecter des Fichiers",
        "prereqs": ["m21_c2_navigation"],
        "texte": """
Quatre commandes pour inspecter des fichiers sans les modifier.
cat — Afficher tout le contenu d'un fichier
  cat profil.md → affiche tout le fichier dans le terminal
  Limite : si le fichier est long, le texte défile trop vite.
head — Voir le début d'un fichier
  head -20 profil.md → affiche les 20 premières lignes
  Utile pour vérifier le frontmatter d'une note Obsidian ou l'en-tête d'un script.
tail — Voir la fin d'un fichier
  tail -50 app.log → affiche les 50 dernières lignes
  C'est la commande pour lire les logs Railway ou les logs d'erreur — les dernières lignes contiennent les événements les plus récents.
  tail -f app.log → suit le fichier en temps réel (le -f = follow). Appuie Ctrl+C pour arrêter.
wc -l — Compter les lignes
  wc -l curriculum.py → affiche le nombre de lignes du fichier
  Utile pour vérifier qu'un fichier a bien été rempli (0 lignes = vide).
Exemple concret de nos sessions : pour vérifier si trouble-testosterone-today.md était vide →
  wc -l trouble-testosterone-today.md
  → 0 trouble-testosterone-today.md (confirmé : vide)
        """.strip(),
    },

    "m21_c4_chercher": {
        "module": 21, "ordre": 4,
        "titre": "Chercher — grep et find",
        "prereqs": ["m21_c3_lire_ecrire_fichiers"],
        "texte": """
Deux commandes de recherche essentielles.
grep — Chercher du texte À L'INTÉRIEUR des fichiers
  grep "Patrick Faubert" *.md → cherche ce texte dans tous les fichiers .md du dossier courant
  grep -r "Profil athlète" . → cherche récursivement dans tous les sous-dossiers
  grep -i "patrick" *.md → recherche insensible à la casse (trouve Patrick, patrick, PATRICK)
  grep -l "Patrick" . → affiche seulement les noms de fichiers qui contiennent le texte (pas le contenu)
find — Chercher des FICHIERS par nom ou propriété
  find . -name "*.md" → trouve tous les fichiers .md dans le dossier courant et ses sous-dossiers
  find . -name "profil*" → trouve tous les fichiers dont le nom commence par "profil"
  find . -empty → trouve tous les fichiers vides (0 bytes) — utile pour détecter des notes corrompues
  find . -newer fichier.md → trouve tous les fichiers modifiés plus récemment qu'un fichier de référence
Exemple concret : pour vérifier si un profil de Patrick Faubert existait quelque part dans le vault →
  grep -r -i "patrick faubert" ~/Documents/Obsidian/Claude
  → aucun résultat = confirmation qu'il n'y a pas de profil
        """.strip(),
    },

    "m21_c5_variables_env": {
        "module": 21, "ordre": 5,
        "titre": "Variables d'Environnement — Les Clés Secrètes",
        "prereqs": ["m21_c1_terminal_cest_quoi"],
        "texte": """
Les variables d'environnement sont des valeurs stockées dans le système d'exploitation qui sont accessibles à tous les programmes qui tournent. C'est là où on stocke les clés d'API, les tokens, et les configurations sensibles — pas dans le code.
Pourquoi pas dans le code : si tu mets une clé API directement dans un fichier Python, et que tu pousses ce fichier sur GitHub, ta clé est publique. Tout le monde peut l'utiliser et abuser de ton compte.
Comment voir les variables actuelles dans le terminal :
  env → liste toutes les variables d'environnement
  echo $NOM_VARIABLE → affiche la valeur d'une variable spécifique
  echo $PATH → affiche le PATH (liste des dossiers où le système cherche les commandes)
Sur Railway, tes variables sont dans le panneau "Variables" de chaque service. Exemples de ce qu'on y stocke pour le CC Bot :
  IBKR_HOST, IBKR_PORT → connexion à Interactive Brokers
  TELEGRAM_TOKEN → le token du bot Telegram
  ANTHROPIC_API_KEY → la clé pour appeler Claude depuis le bot
Quand quelqu'un (ou un script) dit "ajouter la variable X dans Railway" — c'est ça : stocker une valeur sensible dans l'environnement d'exécution, pas dans le code source.
        """.strip(),
    },

    "m21_c6_logs_railway": {
        "module": 21, "ordre": 6,
        "titre": "Lire les Logs Railway",
        "prereqs": ["m21_c3_lire_ecrire_fichiers", "m21_c5_variables_env"],
        "texte": """
Les logs sont le journal de bord d'une application. Chaque événement — démarrage, requête, erreur, action — est enregistré avec un horodatage. Lire les logs, c'est comprendre ce qui s'est passé dans ton CC Bot ou ton Scientia.
Comment accéder aux logs Railway :
  Interface web → railway.com → ton projet → ton service → onglet "Logs"
  Ou depuis le terminal avec le CLI Railway : railway logs --tail (suit en temps réel)
Structure d'une ligne de log typique :
  2026-04-22 14:32:01 [INFO] Connexion IBKR établie. Port 7497.
  2026-04-22 14:32:03 [INFO] Position MSTR : 124.58 unités. Delta : 0.42
  2026-04-22 14:35:10 [ERROR] Timeout connexion IBKR. Retry dans 30s.
Les niveaux de log :
  [INFO] → information normale, tout va bien
  [WARNING] → attention, quelque chose d'inhabituel mais pas critique
  [ERROR] → une erreur s'est produite, l'action n'a pas pu être complétée
  [CRITICAL] → erreur grave, le service peut s'arrêter
Stratégie de lecture : cherche les [ERROR] d'abord. Ensuite, remonte le log pour voir l'[INFO] juste avant — il te dit ce que le bot essayait de faire quand il a planté.
        """.strip(),
    },

    "m21_c7_commandes_pratiques": {
        "module": 21, "ordre": 7,
        "titre": "Les 10 Commandes Que Tu Utiliseras",
        "prereqs": ["m21_c4_chercher", "m21_c6_logs_railway"],
        "texte": """
Récapitulatif des commandes qui reviennent dans nos sessions, avec leur usage exact.
pwd → Où suis-je? (vérifier avant d'agir)
ls -la → Quoi est là, y compris les fichiers cachés et leurs permissions
cd ~/Documents/Obsidian/Claude → Aller directement dans ton vault
cat fichier.md → Lire un fichier complet
head -20 fichier.md → Voir les 20 premières lignes (frontmatter d'une note)
tail -50 app.log → Voir les 50 dernières lignes de logs
grep -r "texte" . → Chercher du texte dans tous les fichiers du dossier courant
find . -name "*.md" -empty → Trouver les fichiers markdown vides
wc -l fichier.py → Compter les lignes d'un fichier (vérifier qu'il n'est pas vide)
chflags nouchg fichier → Débloquer un fichier verrouillé par macOS (utilisé pour les fichiers Obsidian)
Commandes à connaître mais utiliser avec prudence :
rm fichier → Supprimer un fichier (IRRÉVERSIBLE — pas de corbeille)
mv source destination → Déplacer ou renommer un fichier
cp source destination → Copier un fichier
Règle d'or : avant d'utiliser rm ou mv, confirme avec pwd et ls que tu es exactement là où tu penses être. Une commande rm dans le mauvais dossier ne se rattrape pas.
        """.strip(),
    },

})


# ══════════════════════════════════════════════════════════════════════
# MODULE 22 — GOUVERNANCE DE L'IA  (7 concepts)
# Cadres réglementaires et normatifs pour les systèmes d'IA :
# Loi 25 (Québec), AIDA (Canada, projet), ISO 42001, NIST AI RMF,
# EU AI Act, principes de l'OCDE, et synthèse comparative.
# ══════════════════════════════════════════════════════════════════════

CURRICULUM.update({

    "m22_c1_loi25_quebec": {
        "module": 22, "ordre": 1,
        "titre": "Loi 25 — Québec (vie privée et IA)",
        "prereqs": [],
        "texte": """
La Loi 25 (officiellement « Loi modernisant des dispositions législatives en matière de protection des renseignements personnels ») est la réforme québécoise de la vie privée. Elle s'applique aux organismes publics ET aux entreprises privées qui détiennent des renseignements personnels sur des Québécois.
Entrée en vigueur en TROIS phases :
  22 septembre 2022 — Phase 1 : nomination obligatoire d'un responsable de la protection des renseignements personnels (RPRP), obligation de signaler les incidents de confidentialité à la CAI (Commission d'accès à l'information) et aux personnes concernées.
  22 septembre 2023 — Phase 2 : la majorité des nouvelles obligations entrent en vigueur (consentement, transparence, évaluations des facteurs relatifs à la vie privée, droits des personnes).
  22 septembre 2024 — Phase 3 : droit à la portabilité des données.
Implications pour l'IA — DEUX articles clés :
  Article 12.1 : obligation d'INFORMER la personne lorsqu'une décision la concernant est prise UNIQUEMENT sur la base d'un traitement automatisé. La personne peut demander à être informée des renseignements utilisés et à présenter ses observations à un humain qui peut réviser la décision.
  Article 8.1 (transparence des algorithmes) : obligation de fournir des explications sur les facteurs et paramètres principaux ayant mené à la décision.
Sanctions administratives : jusqu'à 10 millions $ ou 2 % du chiffre d'affaires mondial. Sanctions pénales : jusqu'à 25 millions $ ou 4 % du chiffre d'affaires mondial. Plus sévère que la LPRPDE fédérale.
Pour une entreprise québécoise utilisant l'IA pour de la sélection de candidats, du crédit ou de la tarification : la Loi 25 est OBLIGATOIRE et déjà en vigueur.
        """.strip(),
    },

    "m22_c2_aida_canada": {
        "module": 22, "ordre": 2,
        "titre": "AIDA — Canada (projet de loi)",
        "prereqs": ["m22_c1_loi25_quebec"],
        "texte": """
AIDA (Artificial Intelligence and Data Act / Loi sur l'intelligence artificielle et les données) est le projet de loi fédéral canadien qui créerait le PREMIER cadre national spécifique à l'IA. AIDA fait partie du projet de loi C-27 (Loi de 2022 sur la mise en œuvre de la Charte du numérique), déposé en juin 2022.
Statut au 25 avril 2026 : TOUJOURS PROPOSÉ. Le projet de loi a fait face à de fortes critiques (vague, processus précipité, manque de consultation) et n'a PAS été adopté à la dissolution du Parlement. Toute entreprise canadienne doit donc surveiller son évolution mais NE PEUT PAS encore se conformer à un texte qui n'est pas en vigueur.
Concepts clés du texte proposé :
  Cible les « high-impact AI systems » (systèmes d'IA à incidence élevée) — terme dont la définition précise serait laissée aux règlements.
  Création d'un poste de COMMISSAIRE À L'IA ET AUX DONNÉES, hébergé à Innovation, Sciences et Développement économique Canada (ISDE).
  Obligations attendues : évaluation de l'incidence, mesures d'atténuation des biais, mécanismes de surveillance, transparence, tenue de registres.
  Sanctions : jusqu'à 25 millions $ ou 5 % du revenu brut mondial pour les violations les plus graves, plus des infractions criminelles distinctes pour usage malveillant.
Document d'accompagnement (« companion document » publié en mars 2023) : sert de guide d'intention et précise que le gouvernement vise un alignement avec l'EU AI Act et le NIST AI RMF.
Critique principale : la définition de « high-impact » est renvoyée aux règlements, ce qui crée de l'incertitude pour les entreprises pendant des années après l'adoption.
        """.strip(),
    },

    "m22_c3_iso_42001": {
        "module": 22, "ordre": 3,
        "titre": "ISO/IEC 42001 — Management de l'IA",
        "prereqs": [],
        "texte": """
ISO/IEC 42001:2023 est la PREMIÈRE norme internationale CERTIFIABLE pour les systèmes de management de l'IA (AIMS — AI Management System). Publiée le 18 décembre 2023 par l'Organisation internationale de normalisation et la Commission électrotechnique internationale.
Différence avec un cadre comme NIST AI RMF : ISO 42001 est une NORME DE MANAGEMENT certifiable par un organisme tiers accrédité. Une entreprise peut obtenir un certificat ISO 42001 et l'afficher comme preuve de gouvernance, comme elle le fait déjà avec ISO 27001 (sécurité) ou ISO 9001 (qualité).
Structure type High-Level Structure (HLS) — alignée avec ISO 27001 et ISO 9001 :
  Contexte de l'organisation, leadership, planification, support, opération, évaluation de la performance, amélioration. Cycle Plan-Do-Check-Act.
Annexe A : 38 contrôles couvrant 9 domaines :
  Politiques liées à l'IA, organisation interne, ressources, évaluation des incidences, cycle de vie du système d'IA, données pour l'IA, information aux parties intéressées, utilisation des systèmes d'IA, relations avec les tiers.
Annexe B : guide d'implémentation des contrôles. Annexe C : objectifs et risques liés à l'IA. Annexe D : usage à travers les domaines.
Avantage stratégique : pour une entreprise québécoise vendant des services d'IA à des clients européens ou internationaux, une certification ISO 42001 facilite la démonstration de conformité au-delà de la Loi 25 et anticipe AIDA. La norme est VOLONTAIRE mais devient un signal de marché de plus en plus attendu dans les appels d'offres B2B.
        """.strip(),
    },

    "m22_c4_nist_ai_rmf": {
        "module": 22, "ordre": 4,
        "titre": "NIST AI RMF — Cadre américain",
        "prereqs": [],
        "texte": """
Le NIST AI Risk Management Framework (AI RMF 1.0) est le cadre VOLONTAIRE américain de gestion des risques liés à l'IA, publié par le National Institute of Standards and Technology le 26 janvier 2023. Mandaté par le National AI Initiative Act de 2020.
Différence avec une loi : ce n'est pas un texte contraignant. C'est une boîte à outils de référence largement adoptée comme « état de l'art » par les régulateurs, les assureurs et les acheteurs B2B.
QUATRE FONCTIONS centrales (à mémoriser) :
  GOVERN — Cultiver une culture de gestion des risques d'IA dans l'organisation. Politiques, rôles, responsabilités, formation.
  MAP — Cadrer le contexte d'utilisation. Qui sont les parties prenantes? Quels sont les risques spécifiques de ce système d'IA?
  MEASURE — Évaluer, analyser et suivre les risques identifiés. Métriques quantitatives et qualitatives.
  MANAGE — Prioriser et traiter les risques. Allouer les ressources, planifier les réponses aux incidents.
SEPT caractéristiques d'une IA digne de confiance (« trustworthy AI ») :
  Validité et fiabilité, sûreté, sécurité et résilience, responsabilité et transparence, explicabilité et interprétabilité, protection de la vie privée, équité avec biais maîtrisés.
Le NIST AI RMF Generative AI Profile (juillet 2024) ajoute un profil spécifique pour l'IA générative : risques de confabulation, contenu CBRN, personnalisation pour la cybercriminalité, contenu obscène, désinformation, violation de propriété intellectuelle.
Le RMF est fortement INTEROPÉRABLE avec ISO 42001 : une entreprise peut utiliser le RMF comme méthode opérationnelle ET viser une certification ISO 42001 comme preuve formelle.
        """.strip(),
    },

    "m22_c5_eu_ai_act": {
        "module": 22, "ordre": 5,
        "titre": "EU AI Act — Règlement européen",
        "prereqs": [],
        "texte": """
Le Règlement (UE) 2024/1689 sur l'intelligence artificielle (« EU AI Act ») est la PREMIÈRE loi globale et contraignante au monde sur l'IA. Adopté en mai 2024, entré en vigueur le 1er août 2024. Application phasée jusqu'au 2 août 2027.
PORTÉE EXTRATERRITORIALE — c'est ce qui le rend pertinent pour le Canada : le règlement s'applique à tout fournisseur ou utilisateur dont les sorties d'un système d'IA sont utilisées dans l'UE, peu importe où il est établi. Une entreprise québécoise dont le SaaS d'IA a des clients européens DOIT s'y conformer.
APPROCHE BASÉE SUR LES RISQUES — quatre niveaux :
  RISQUE INACCEPTABLE (interdit) : notation sociale par les gouvernements, manipulation cognitive ciblant les enfants, identification biométrique à distance en temps réel dans l'espace public (sauf exceptions), reconnaissance d'émotions au travail ou à l'école, scraping non ciblé de visages, prédiction de criminalité individuelle.
  RISQUE ÉLEVÉ : IA pour le recrutement, le crédit, l'éducation, la justice, l'application de la loi, la migration, les infrastructures critiques, les dispositifs médicaux. Obligations lourdes : évaluation de la conformité, gestion des risques, qualité des données, documentation technique, surveillance humaine, robustesse, marquage CE.
  RISQUE LIMITÉ : chatbots, deepfakes, systèmes de reconnaissance d'émotions hors interdictions. Obligation de TRANSPARENCE (informer l'utilisateur qu'il interagit avec une IA).
  RISQUE MINIMAL : tout le reste. Aucune obligation, codes de conduite volontaires.
Calendrier : interdictions applicables le 2 février 2025; règles GPAI (modèles à usage général) le 2 août 2025; obligations principales pour systèmes à risque élevé le 2 août 2026; pleine application le 2 août 2027.
Sanctions : jusqu'à 35 millions € ou 7 % du chiffre d'affaires mondial annuel pour les pratiques interdites — plus sévère que le RGPD.
        """.strip(),
    },

    "m22_c6_oecd_principles": {
        "module": 22, "ordre": 6,
        "titre": "Principes de l'OCDE sur l'IA",
        "prereqs": [],
        "texte": """
Les Principes de l'OCDE sur l'IA sont les premiers principes intergouvernementaux sur l'IA digne de confiance. Adoptés le 22 mai 2019 par les 38 pays membres de l'OCDE et plusieurs partenaires (47+ pays au total, incluant le Canada). Mis à jour le 3 mai 2024 pour intégrer l'IA générative.
Ce ne sont PAS des lois — c'est du « droit souple » (soft law). Mais ils servent de SOCLE COMMUN qui a influencé l'EU AI Act, le NIST AI RMF, AIDA, et les principes du G20 (qui les a repris en juin 2019).
CINQ PRINCIPES fondés sur des valeurs (à connaître) :
  1. CROISSANCE INCLUSIVE, développement durable et bien-être — l'IA doit bénéficier aux personnes et à la planète.
  2. VALEURS CENTRÉES SUR L'HUMAIN ET ÉQUITÉ — respect des droits humains, primauté du droit, démocratie, diversité, équité, justice sociale.
  3. TRANSPARENCE ET EXPLICABILITÉ — possibilité de comprendre, de contester et de challenger les décisions issues de systèmes d'IA.
  4. ROBUSTESSE, SÛRETÉ ET SÉCURITÉ — fonctionnement fiable et résilience tout au long du cycle de vie.
  5. RESPONSABILITÉ — les acteurs de l'IA sont responsables du fonctionnement adéquat des systèmes selon leur rôle.
CINQ RECOMMANDATIONS aux gouvernements : investir dans la R&D, favoriser un écosystème numérique pour l'IA, créer un environnement réglementaire favorable, bâtir des compétences humaines, coopérer internationalement.
Mise à jour 2024 : ajout de garde-fous spécifiques contre la mésinformation, la désinformation et l'usage malveillant de l'IA générative; renforcement des références aux droits humains et à la sécurité de l'information.
Pourquoi ils comptent : ils forment le langage commun entre régulateurs nationaux. Connaître les 5 principes permet de RECONNAÎTRE leur déclinaison dans n'importe quelle loi nationale (Loi 25, AIDA, EU AI Act).
        """.strip(),
    },

    "m22_c7_synthese_gouvernance": {
        "module": 22, "ordre": 7,
        "titre": "Synthèse — Quel cadre pour quelle situation",
        "prereqs": ["m22_c1_loi25_quebec", "m22_c2_aida_canada", "m22_c3_iso_42001", "m22_c4_nist_ai_rmf", "m22_c5_eu_ai_act", "m22_c6_oecd_principles"],
        "texte": """
Hiérarchie des cadres et stratégie d'application pour une organisation québécoise.
DROIT DUR (obligatoire, sanctions) :
  Loi 25 — DÉJÀ EN VIGUEUR. Toute organisation traitant des renseignements personnels au Québec doit s'y conformer. Pertinente pour l'IA via les articles 8.1 et 12.1 (décisions automatisées, transparence des algorithmes).
  EU AI Act — EN VIGUEUR mais application phasée. S'applique extraterritorialement si vos systèmes ont une sortie utilisée dans l'UE. Risque élevé = obligations lourdes à partir du 2 août 2026.
  AIDA — PROJET. Surveillez son évolution. Pas d'obligation actuelle, mais alignement utile car le projet vise la convergence avec EU AI Act et NIST RMF.
DROIT SOUPLE (non contraignant, influence forte) :
  OCDE — socle international. Sert de boussole pour interpréter les autres cadres.
NORMES VOLONTAIRES (certifiables, signal de marché) :
  ISO/IEC 42001 — certificat délivré par tiers accrédité. Utile pour B2B, appels d'offres, exportation vers l'UE.
CADRES OPÉRATIONNELS (méthodologies internes) :
  NIST AI RMF — méthode pour gouverner, cartographier, mesurer et gérer les risques d'IA. Voluntary mais devenu standard de facto.
ROUTE PRATIQUE pour une PME québécoise utilisant ou développant de l'IA :
  ÉTAPE 1 — Conformité Loi 25 (obligatoire) : nommer un RPRP, faire les évaluations des facteurs relatifs à la vie privée, prévoir l'information sur les décisions automatisées.
  ÉTAPE 2 — Adopter NIST AI RMF comme méthode opérationnelle interne (aucun coût, structure éprouvée).
  ÉTAPE 3 — Selon la stratégie commerciale : viser ISO 42001 si exportation/B2B, ou se contenter du RMF.
  ÉTAPE 4 — Si exposition européenne : cartographier les systèmes d'IA selon les niveaux de risque de l'EU AI Act et anticiper août 2026.
  ÉTAPE 5 — Surveiller AIDA et ajuster quand le texte sera adopté.
La règle d'or : la conformité IA n'est PAS un projet ponctuel; c'est un système de management continu (d'où l'utilité de structures comme ISO 42001 ou le RMF).
        """.strip(),
    },

})


# ── Surcharge par variable d'environnement ────────────────────────────────────
# Si CURRICULUM_USER=conjointe, toutes les variables sont remplacées par celles
# de curriculum_conjointe.py. L'app.py et content_generator.py n'ont pas besoin
# d'être modifiés — ils importent depuis curriculum.py comme d'habitude.

import os as _os
if _os.getenv("CURRICULUM_USER") == "conjointe":
    from curriculum_conjointe import (  # type: ignore
        CURRICULUM,
        NOMS_MODULES,
        DOMAINES_MODULES,
        SOUS_GROUPES,
        PARCOURS_CONSEILLES,
    )
