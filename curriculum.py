from __future__ import annotations

"""
Scientia — Curriculum Gouvernance de l'IA
Conçu pour Dominic-André Leclerc, fondateur de Nord Paradigm.

13 modules approfondis, ~58 concepts, mélange français-anglais
selon la source native du cadre étudié (Loi 25/CAI/CNIL en français;
EU AI Act/NIST/Singapore/UK ICO/Agentic/AIGP en anglais).

Chaque concept contient :
- un texte de référence dense (200-600 mots),
- les métadonnées (module, ordre, prérequis, langue),
- éventuellement la source d'ingestion si concept dynamique.

Module 99 sert de bucket aux concepts ingérés via ingestion.py.
"""

CURRICULUM: dict = {}


# ══════════════════════════════════════════════════════════════════════════════
# Les modules sont définis plus bas via CURRICULUM.update({...}).
# Ordre logique d'apprentissage :
#   1. Fondations
#   2. Loi 25 et la CAI
#   3. Cadre fédéral canadien et provinces
#   4. EU AI Act
#   5. NIST AI RMF
#   6. ISO/IEC 42001
#   7. CNIL — guide opérationnel
#   8. Singapore Model AI Governance Framework
#   9. UK ICO et Data (Use & Access) Act 2025
#  10. Mise en œuvre pratique
#  11. Agentic AI Governance
#  12. AI Governance Profession (IAPP AIGP)
#  13. Synthèse stratégique pour PME québécoise
# ══════════════════════════════════════════════════════════════════════════════


# ══════════════════════════════════════════════════════════════════════════════
# MODULE 1 — FONDATIONS DE LA GOUVERNANCE D'IA  (5 concepts, FR)
# ══════════════════════════════════════════════════════════════════════════════

CURRICULUM.update({

    "m1_c1_pourquoi_gouverner_ia": {
        "module": 1, "ordre": 1, "langue": "fr",
        "titre": "Pourquoi gouverner l'IA",
        "prereqs": [],
        "texte": """
PROBLÈME CENTRAL — L'IA introduit des risques que les régimes juridiques classiques (responsabilité civile, contrats, vie privée, droit de la consommation) ne couvrent pas adéquatement. Trois propriétés des systèmes d'IA expliquent pourquoi un cadre dédié devient nécessaire.

PREMIÈRE PROPRIÉTÉ — L'OPACITÉ. Un modèle d'apprentissage profond peut compter des milliards de paramètres et produire une décision sans que ni le concepteur ni l'utilisateur ne puissent expliquer le raisonnement précis. Le droit classique présuppose qu'on peut reconstituer une chaîne de causalité; l'IA brise cette présupposition. Conséquence juridique : difficulté à prouver une faute, à contester une décision, à attribuer une responsabilité.

DEUXIÈME PROPRIÉTÉ — L'AUTOMATISATION À L'ÉCHELLE. Un système d'IA peut traiter des millions de dossiers en quelques secondes. Une discrimination subtile (par exemple un biais de 2 % contre un groupe protégé) qui passerait inaperçue chez un humain produit, à l'échelle, des effets disparates massifs. La régulation doit donc s'attaquer aux EFFETS STATISTIQUES et non seulement aux intentions individuelles.

TROISIÈME PROPRIÉTÉ — LE COUPLAGE AVEC LES DONNÉES. Un modèle est aussi bon que les données qui l'ont entraîné. Or, ces données reflètent souvent des inégalités historiques (sous-représentation, étiquetage biaisé, prélèvement non consenti). Gouverner l'IA, c'est nécessairement gouverner aussi les données — d'où l'imbrication entre lois sur la vie privée (Loi 25, RGPD) et lois sur l'IA (EU AI Act, future loi fédérale canadienne).

QUATRE FAMILLES DE RISQUES (taxonomie largement adoptée) :
1. RISQUES POUR LES DROITS FONDAMENTAUX — discrimination dans l'embauche, le crédit, le logement, la justice, l'accès aux services publics; surveillance disproportionnée; restriction de l'autonomie individuelle. Cas documentés : COMPAS aux États-Unis, Apple Card (limites de crédit accordées aux femmes inférieures à celles de leurs maris), reconnaissance faciale moins précise sur les peaux foncées.
2. RISQUES DE SÉCURITÉ PHYSIQUE — IA dans les dispositifs médicaux, les véhicules autonomes, les systèmes de contrôle industriel, les infrastructures critiques.
3. RISQUES SYSTÉMIQUES — manipulation à grande échelle (deepfakes électoraux, désinformation), concentration du marché, dépendance économique.
4. RISQUES POUR L'ÉCOSYSTÈME INFORMATIONNEL — pollution informationnelle, érosion de la confiance, atteinte à la propriété intellectuelle, effondrement progressif de la qualité des données d'entraînement.

DEUX DÉFAILLANCES DE MARCHÉ justifient l'intervention publique :
A. ASYMÉTRIE D'INFORMATION — l'utilisateur final (employé évalué par un algorithme RH, demandeur de prêt) n'a pas l'information ni l'expertise pour évaluer le système qui le juge.
B. EXTERNALITÉS — les coûts d'une IA défaillante (discrimination, pollution, accidents) ne sont pas internalisés par le producteur. Sans règle, le producteur sous-investit dans la sécurité.

QUATRE OBJECTIFS DE LA GOUVERNANCE DE L'IA, communs à tous les cadres : (1) garantir la sécurité et la fiabilité; (2) protéger les droits fondamentaux; (3) maintenir la responsabilité humaine et la possibilité de contester; (4) préserver la confiance dans les institutions et les marchés.
        """.strip(),
    },

    "m1_c2_typologie_outils": {
        "module": 1, "ordre": 2, "langue": "fr",
        "titre": "Cartographie des outils de gouvernance",
        "prereqs": ["m1_c1_pourquoi_gouverner_ia"],
        "texte": """
La gouvernance de l'IA combine QUATRE FAMILLES D'INSTRUMENTS aux statuts juridiques distincts. Confondre ces familles est l'erreur la plus fréquente des dirigeants : on entend « on est conforme NIST » comme si c'était équivalent à « on est conforme Loi 25 ». Ce n'est pas le cas.

FAMILLE 1 — DROIT DUR (HARD LAW). Texte juridique contraignant, adopté par un Parlement, exécutoire devant les tribunaux, assorti de sanctions civiles, administratives ou pénales. Exemples : Loi 25 du Québec (en vigueur), EU AI Act (en vigueur, application phasée), RGPD pour le volet données. Caractéristique clé : on ne peut pas y déroger contractuellement.

FAMILLE 2 — DROIT SOUPLE (SOFT LAW). Principes, déclarations, recommandations adoptés par des organisations internationales ou des autorités publiques sans force contraignante directe. Exemples : Principes de l'OCDE sur l'IA (2019, mis à jour 2024) et son OECD Due Diligence Guidance for Responsible AI (février 2026); Recommandation de l'UNESCO sur l'éthique de l'IA (2021); Code de conduite volontaire canadien sur les systèmes d'IA générative avancée (septembre 2023). Aucune obligation, mais influence forte sur les textes ultérieurs de droit dur.

FAMILLE 3 — NORMES TECHNIQUES (STANDARDS). Documents techniques produits par ISO, IEEE, CEN-CENELEC, NIST. Volontaires, mais souvent incorporés par référence dans le droit dur — l'EU AI Act renvoie explicitement à des normes harmonisées CEN-CENELEC pour démontrer la conformité. Exemples : ISO/IEC 42001 (management de l'IA, certifiable), ISO/IEC 23894 (gestion des risques d'IA), ISO/IEC 22989 (terminologie). Caractéristique clé : certifiables par un tiers.

FAMILLE 4 — CADRES OPÉRATIONNELS (FRAMEWORKS). Méthodologies de mise en œuvre, ni lois ni normes certifiables, mais des outils de référence largement adoptés. Exemples : NIST AI Risk Management Framework, OWASP AI Security and Privacy Guide, MITRE ATLAS, Singapore Model AI Governance Framework, AI Verify, IAPP AIGP Body of Knowledge.

POURQUOI LA DISTINCTION COMPTE en pratique :
A. Une certification ISO 42001 ne dispense PAS de la conformité Loi 25. Le certificat est un signal de qualité; la loi est obligatoire indépendamment.
B. Adopter NIST AI RMF n'a aucune valeur juridique en soi, mais le suivre rigoureusement constitue un argument fort pour démontrer la « due diligence » devant un régulateur ou un juge.
C. Les Principes de l'OCDE n'imposent rien, mais ils servent de socle d'interprétation dans presque toutes les lois nationales.

HIÉRARCHIE D'IMPACT JURIDIQUE (du plus contraignant au moins contraignant) :
1. Constitution / Charte (droits fondamentaux qui s'imposent à toute loi)
2. Lois ordinaires (Loi 25, EU AI Act)
3. Règlements d'application
4. Lignes directrices d'autorités publiques (CAI au Québec, CNIL en France, ICO au Royaume-Uni, EDPB en Europe)
5. Normes techniques harmonisées
6. Codes de conduite sectoriels
7. Cadres opérationnels (NIST RMF, Singapore MGF)
8. Déclarations internationales (OCDE, UNESCO, G20)

INSTRUMENTS HYBRIDES émergents : la « bac à sable réglementaire » (regulatory sandbox) — l'EU AI Act crée des sandboxes nationaux où une PME peut tester un système d'IA à haut risque sous supervision allégée. Le Québec a mis sur pied des bacs à sable similaires en santé et en finance.

LEÇON STRATÉGIQUE : aucune entreprise ne sera concernée par UNE seule approche. Une PME québécoise vendant un outil RH d'IA en Europe est régulée par la Loi 25 (principes), l'EU AI Act (risques) et indirectement par les règles sectorielles d'embauche. La gouvernance interne doit être suffisamment générique pour répondre simultanément à plusieurs logiques.
        """.strip(),
    },

    "m1_c3_approches_reglementaires": {
        "module": 1, "ordre": 3, "langue": "fr",
        "titre": "Trois grandes approches réglementaires",
        "prereqs": ["m1_c2_typologie_outils"],
        "texte": """
Les régulateurs ont essayé TROIS GRANDES STRATÉGIES pour encadrer l'IA. Chacune a ses forces et ses faiblesses, et les principaux régimes étudiés dans ce curriculum se positionnent différemment sur ce spectre.

APPROCHE 1 — RÉGULATION PAR LES RISQUES (RISK-BASED). Le système est classé selon le niveau de risque qu'il pose; les obligations augmentent avec le risque. Le cas paradigmatique est l'EU AI Act, qui distingue quatre niveaux : risque inacceptable (interdit), risque élevé (obligations lourdes), risque limité (obligations de transparence), risque minimal (rien).
  FORCES : proportionnalité, focalisation des ressources réglementaires sur les vrais enjeux, évite de paralyser les usages anodins.
  FAIBLESSES : la classification est elle-même un travail réglementaire complexe et contesté. Le modèle de fondation (GPT, Claude, Llama) peut servir indifféremment à un usage minimal et à un usage à haut risque — d'où l'ajout d'un régime spécifique GPAI dans l'EU AI Act.

APPROCHE 2 — RÉGULATION PAR LES PRINCIPES (PRINCIPLES-BASED). Le législateur fixe des principes généraux (équité, transparence, responsabilité, sûreté) et laisse aux acteurs le soin de les opérationnaliser, sous le contrôle ex post d'un régulateur. C'est l'approche des Principes de l'OCDE, du Code de conduite volontaire canadien, et largement de la Loi 25 québécoise (qui pose des obligations générales sans prescrire de méthode technique).
  FORCES : flexibilité face à une technologie qui évolue plus vite que la loi; permet l'adaptation sectorielle.
  FAIBLESSES : insécurité juridique pour les entreprises qui ne savent pas si leur méthode est jugée suffisante; risque d'inégalité entre grandes entreprises (qui se paient des juristes) et PME.

APPROCHE 3 — RÉGULATION SECTORIELLE (USE-CASE BASED). Le législateur n'adopte pas de loi transversale sur l'IA mais adapte chaque réglementation sectorielle. La FDA encadre l'IA médicale, la FTC encadre les pratiques commerciales déloyales, l'EEOC encadre la discrimination à l'embauche. Le Royaume-Uni a explicitement choisi cette voie en 2023 avec sa « pro-innovation approach », réaffirmée et durcie partiellement par le Data (Use and Access) Act 2025.
  FORCES : règles précises adaptées aux risques sectoriels; aucune duplication.
  FAIBLESSES : zones grises pour les IA polyvalentes; lenteur d'adaptation; les usages émergents (chatbots, assistants productivité) tombent souvent entre deux chaises.

POSITIONNEMENT DES RÉGIMES couverts dans ce curriculum :
  EU AI Act = risques + horizontal + détaillé (la version la plus prescriptive).
  Loi 25 = principes + transversale (vie privée, pas IA-spécifique mais s'y applique).
  NIST AI RMF = principes opérationnalisés (volontaire).
  ISO 42001 = principes + management (volontaire, certifiable).
  OCDE = principes purs (soft law).
  Singapore MGF = principes pratiques + sectoriels par exemples.
  UK ICO + DUAA 2025 = sectoriel + assouplissement de l'ADM.
  Cadre fédéral canadien = mixte; Directive on ADM (sectoriel public), Code volontaire (principes), régulation fédérale en cours d'élaboration.

QUATRIÈME APPROCHE ÉMERGENTE — L'AUTORÉGULATION CONCURRENTIELLE. Les grands fournisseurs de modèles (Anthropic, OpenAI, Google DeepMind, Meta, Mistral) publient des « policies » internes (Acceptable Use, Responsible Scaling Policy, frontier safety frameworks). Ce ne sont ni des lois ni des normes; ce sont des engagements unilatéraux. Le risque : transformer la gouvernance en discrétion privée. La parade : référencer ces engagements dans le droit dur (l'EU AI Act le fait via le GPAI Code of Practice signé en avril 2026 par les grands fournisseurs).

LEÇON STRATÉGIQUE — Tendance observée par Fasken et l'IAPP en 2026 : les organisations multinationales harmonisent leur gouvernance interne sur le STANDARD LE PLUS ÉLEVÉ APPLICABLE (typiquement l'EU AI Act) et l'appliquent à toutes leurs juridictions, plutôt que de maintenir des politiques différentes par pays. Pour une PME québécoise exposée à plusieurs marchés, c'est la stratégie la plus économique sur 3-5 ans.
        """.strip(),
    },

    "m1_c4_principes_ocde": {
        "module": 1, "ordre": 4, "langue": "fr",
        "titre": "Principes de l'OCDE et Due Diligence Guidance",
        "prereqs": ["m1_c3_approches_reglementaires"],
        "texte": """
Les Principes de l'OCDE sur l'IA (« OECD AI Principles ») sont la première RECOMMANDATION INTERGOUVERNEMENTALE sur l'IA digne de confiance. Adoptés le 22 mai 2019 par le Conseil de l'OCDE, ils ont été endossés par les 38 pays membres puis par 9 partenaires additionnels, totalisant 47+ adhérents (dont le Canada). Première mise à jour majeure le 3 mai 2024 pour intégrer l'IA générative. Une OECD Due Diligence Guidance for Responsible AI complémentaire a été publiée le 19 février 2026.

STATUT JURIDIQUE — c'est une RECOMMANDATION du Conseil de l'OCDE, instrument de droit souple. Aucune sanction directe en cas de non-respect. Mais les pays adhérents s'engagent politiquement à les promouvoir et à en tenir compte dans leur droit national.

POURQUOI LES CONNAÎTRE — DEUX RAISONS :
1. Les Principes de l'OCDE ont été REPRIS QUASI MOT POUR MOT par les Principes du G20 (juin 2019), ce qui leur donne une portée diplomatique mondiale.
2. Ils ont SERVI DE MATRICE pour les textes contraignants ultérieurs : EU AI Act (préambule cite explicitement l'OCDE), NIST AI RMF (caractéristiques de trustworthy AI alignées), Loi 25 (l'esprit des articles 8.1 et 12.1 reflète les principes 3 et 5).

LES CINQ PRINCIPES (1.1 à 1.5 dans le texte) :

PRINCIPE 1.1 — CROISSANCE INCLUSIVE, DÉVELOPPEMENT DURABLE ET BIEN-ÊTRE. L'IA devrait bénéficier aux personnes et à la planète. On ne juge pas un système d'IA seulement sur sa performance technique, mais sur ses bénéfices sociétaux et environnementaux.

PRINCIPE 1.2 — RESPECT DE L'ÉTAT DE DROIT, DES DROITS HUMAINS, DES VALEURS DÉMOCRATIQUES, ET DE LA DIVERSITÉ, INCLUANT L'ÉQUITÉ. C'est le principe le plus dense : non-discrimination, dignité humaine, protection de la vie privée, processus équitable, justice sociale, préservation des cultures. Mise à jour 2024 : ajout explicite de la « primauté du droit » et de la lutte contre la mésinformation.

PRINCIPE 1.3 — TRANSPARENCE ET EXPLICABILITÉ. Trois éléments : (a) divulgation responsable; (b) information aux personnes affectées; (c) capacité à contester (« meaningful explanation » suffisante pour permettre à une personne d'attaquer une décision défavorable). Influence directe sur l'article 8.1 de la Loi 25 et sur les articles 13-14 du RGPD.

PRINCIPE 1.4 — ROBUSTESSE, SÛRETÉ ET SÉCURITÉ. Tout au long du cycle de vie. Inclut traçabilité (data lineage), gestion des risques cyber, capacité à fonctionner correctement en cas d'usage non prévu, sortie de service contrôlée. Mise à jour 2024 : ajout d'exigences spécifiques pour les modèles génératifs (filtrage des sorties, watermarking, prévention de l'usage à des fins CBRN).

PRINCIPE 1.5 — RESPONSABILITÉ. Les acteurs de l'IA doivent être responsables (« accountable ») du fonctionnement adéquat des systèmes selon leur rôle. Inclut documentation, traçabilité, mécanismes d'audit, allocation claire des responsabilités le long de la chaîne de valeur (concepteur, déployeur, utilisateur).

LES CINQ RECOMMANDATIONS aux gouvernements (2.1 à 2.5) :
2.1 Investir dans la R&D en IA fiable.
2.2 Favoriser un écosystème numérique pour l'IA.
2.3 Créer un environnement réglementaire et politique favorable à l'IA digne de confiance.
2.4 Bâtir des compétences humaines et préparer la transition du marché du travail.
2.5 Coopérer internationalement.

OECD DUE DILIGENCE GUIDANCE FOR RESPONSIBLE AI (19 février 2026) — instrument pratique d'application des principes. Adapte le cadre OECD de Responsible Business Conduct (RBC) à l'IA. Endossé par tous les pays membres + 17 partenaires + l'UE.

LE CADRE EN SIX ÉTAPES :
1. INTÉGRER la conduite responsable dans les politiques et systèmes de management.
2. IDENTIFIER les impacts négatifs réels et potentiels dans les opérations, la chaîne d'approvisionnement et les relations d'affaires.
3. CESSER, PRÉVENIR ou ATTÉNUER ces impacts.
4. SUIVRE l'efficacité des mesures.
5. COMMUNIQUER sur la manière dont les impacts sont gérés.
6. RÉPARER ou COOPÉRER à la réparation lorsqu'une organisation a causé ou contribué à un impact négatif.

UTILITÉ POUR UNE PME — la Due Diligence Guidance fournit une méthode opérationnelle là où les Principes restent abstraits. Les six étapes sont compatibles avec NIST AI RMF (GOVERN-MAP-MEASURE-MANAGE) et avec ISO 42001 (PDCA + Annexe A). Une organisation qui veut démontrer une « due diligence raisonnable » à un régulateur peut citer explicitement le respect du cadre OECD.

UTILISATION PRATIQUE — quand on lit n'importe quelle loi nationale sur l'IA, identifier en marge à quel principe OCDE chaque article répond. Exercice utile : prendre le texte de l'EU AI Act, encadrer les obligations de transparence (Art. 13, 50, 52) et les rattacher au principe 1.3; encadrer les obligations de robustesse (Art. 9, 15) et les rattacher au principe 1.4. Cela révèle la cohérence sous-jacente de tous les régimes.
        """.strip(),
    },

    "m1_c5_unesco_ethique": {
        "module": 1, "ordre": 5, "langue": "fr",
        "titre": "UNESCO — Recommandation sur l'éthique de l'IA",
        "prereqs": ["m1_c2_typologie_outils"],
        "texte": """
La RECOMMANDATION DE L'UNESCO SUR L'ÉTHIQUE DE L'IA, adoptée à l'unanimité par les 193 États membres le 23 novembre 2021 lors de la 41e Conférence générale, est le PREMIER STANDARD MONDIAL SUR L'ÉTHIQUE DE L'IA. Statut juridique : recommandation, instrument de droit souple. Mais sa portée — 193 États, 4 ans de négociation multilatérale — lui donne un poids politique unique.

POURQUOI L'UNESCO PLUTÔT QUE L'OCDE — la division du travail est claire :
A. OCDE → orientation économique et de coopération entre pays développés (47 adhérents).
B. UNESCO → orientation droits humains, culture, éducation, inclusivité globale (193 États, dont des pays du Sud peu présents à l'OCDE).

La Recommandation UNESCO complète l'OCDE en y ajoutant une perspective DROITS HUMAINS et de DIVERSITÉ CULTURELLE absente du cadre OCDE plus économique.

LES QUATRE VALEURS FONDATRICES :
1. RESPECT, PROTECTION ET PROMOTION DES DROITS HUMAINS, DES LIBERTÉS FONDAMENTALES ET DE LA DIGNITÉ HUMAINE.
2. ÉPANOUISSEMENT DE L'ENVIRONNEMENT ET DES ÉCOSYSTÈMES.
3. GARANTIE DE LA DIVERSITÉ ET DE L'INCLUSIVITÉ.
4. VIVRE DANS DES SOCIÉTÉS PACIFIQUES, JUSTES ET INTERCONNECTÉES.

LES DIX PRINCIPES (approche centrée sur les droits humains) :
1. PROPORTIONNALITÉ ET CARACTÈRE NON-NUISIBLE — l'usage de l'IA ne devrait pas dépasser ce qui est nécessaire à l'objectif légitime visé; évaluation des risques avant déploiement.
2. SÛRETÉ ET SÉCURITÉ — les dommages non désirés (sûreté) et les vulnérabilités aux attaques (sécurité) doivent être adressés.
3. ÉQUITÉ ET NON-DISCRIMINATION — les acteurs doivent éviter, prévenir et atténuer la discrimination résultant de l'IA.
4. DURABILITÉ — l'évaluation des impacts environnementaux des systèmes d'IA tout au long de leur cycle de vie.
5. DROIT À LA VIE PRIVÉE ET PROTECTION DES DONNÉES — protection durant tout le cycle de vie; cadres de protection adéquats.
6. SUPERVISION HUMAINE ET DÉTERMINATION HUMAINE — les humains doivent maintenir une supervision significative, particulièrement pour les décisions à fort impact.
7. TRANSPARENCE ET EXPLICABILITÉ — les utilisateurs et populations affectées méritent une IA transparente et explicable.
8. RESPONSABILITÉ ET REDEVABILITÉ — lignes claires de responsabilité pour les impacts.
9. SENSIBILISATION ET LITTÉRATIE — les sociétés doivent développer la littératie en IA et l'engagement critique.
10. GOUVERNANCE MULTI-ACTEURS ET ADAPTATIVE ET COLLABORATION — respect du droit international et de la souveraineté nationale; participation diversifiée.

DOMAINES D'ACTION POLITIQUE (mise en œuvre) — onze chapitres opérationnels couvrant : gouvernance des données et qualité, environnement et écosystèmes, genre et inégalités sociales, éducation et recherche, santé et bien-être social, culture et patrimoine, travail et emploi, médias et désinformation. Chacun fournit des recommandations spécifiques aux États membres.

OUTILS D'IMPLÉMENTATION publiés par l'UNESCO depuis 2021 :
A. READINESS ASSESSMENT METHODOLOGY (RAM) — outil d'auto-évaluation pour les États sur leur niveau de préparation à l'IA éthique.
B. ETHICAL IMPACT ASSESSMENT (EIA) — méthode d'évaluation d'impact éthique pour les projets d'IA, complémentaire aux EFVP/DPIA et à la FRIA de l'EU AI Act.

DIFFÉRENCE OCDE / UNESCO POUR UNE ORGANISATION CANADIENNE :
A. OCDE → axe B2B, technocratique, économique. Préféré pour démontrer une « due diligence » devant des régulateurs nord-américains.
B. UNESCO → axe droits humains, inclusivité culturelle, sustainability. Préféré pour démontrer un engagement éthique élargi, particulièrement en relation avec des partenaires de pays en développement, des ONG, ou pour un positionnement public.

POSITIONNEMENT POUR NORD PARADIGM — citer les Principes UNESCO dans une politique d'IA d'entreprise apporte deux choses : (1) crédibilité auprès de partenaires institutionnels et publics; (2) référence à la diversité culturelle québécoise (préservation du français, identité distincte) qui s'aligne naturellement avec le principe d'inclusivité culturelle de l'UNESCO.

LIMITES — non-contraignant, pas de mécanisme d'enforcement, absence de sanctions. C'est un PLANCHER ÉTHIQUE et un cadre pédagogique, pas un substitut au droit dur.
        """.strip(),
    },

})


# ══════════════════════════════════════════════════════════════════════════════
# MODULE 2 — LOI 25 ET LA CAI  (7 concepts, FR)
# ══════════════════════════════════════════════════════════════════════════════

CURRICULUM.update({

    "m2_c1_loi25_vue_ensemble": {
        "module": 2, "ordre": 1, "langue": "fr",
        "titre": "Loi 25 — vue d'ensemble et calendrier",
        "prereqs": ["m1_c4_principes_ocde"],
        "texte": """
La Loi 25 (avant adoption : Projet de loi 64) est officiellement la « Loi modernisant des dispositions législatives en matière de protection des renseignements personnels », sanctionnée le 22 septembre 2021. Elle modifie deux lois antérieures :
A. La Loi sur l'accès aux documents des organismes publics et sur la protection des renseignements personnels (« Loi sur l'accès », pour le secteur public).
B. La Loi sur la protection des renseignements personnels dans le secteur privé (« LPRPSP » — P-39.1, pour les entreprises privées).

CHAMP D'APPLICATION TRÈS LARGE — la Loi 25 couvre :
1. Tous les organismes publics du Québec (ministères, organismes paragouvernementaux, municipalités, commissions scolaires, établissements de santé).
2. Toutes les entreprises privées qui exploitent une entreprise au Québec et qui détiennent ou traitent des renseignements personnels concernant des résidents du Québec, peu importe où l'entreprise a son siège.
3. Effet extraterritorial : une entreprise hors Québec qui offre des produits ou services à des résidents du Québec est également visée — la portée se rapproche du RGPD européen.

NOTION CLÉ DE « RENSEIGNEMENT PERSONNEL » : tout renseignement qui concerne une personne physique et qui permet de l'identifier directement ou indirectement. Cela inclut les identifiants techniques (adresse IP, identifiants publicitaires, données biométriques) — pas seulement nom et adresse.

ENTRÉE EN VIGUEUR EN TROIS PHASES — TOUTES MAINTENANT EN VIGUEUR :

PHASE 1 — 22 SEPTEMBRE 2022 :
A. Désignation obligatoire du RPRP (Responsable de la protection des renseignements personnels). Par défaut, c'est la personne ayant la plus haute autorité (président, directeur général). Peut être délégué.
B. Obligation de signaler à la CAI et aux personnes concernées tout INCIDENT DE CONFIDENTIALITÉ présentant un risque sérieux de préjudice.
C. Tenue d'un REGISTRE DES INCIDENTS conservé pendant 5 ans.
D. Cadre pour la communication de RP à des tiers à des fins commerciales.

PHASE 2 — 22 SEPTEMBRE 2023 (la phase la plus dense) :
A. Politique de confidentialité publique, claire, accessible, en langage simple.
B. EFVP (Évaluation des facteurs relatifs à la vie privée) obligatoire pour tout projet impliquant l'acquisition, le développement ou la refonte d'un système de traitement de RP.
C. Règles de consentement renforcées : manifeste, libre, éclairé, à des fins spécifiques. Pour les renseignements sensibles : EXPLICITE.
D. Droits étendus : rectification, cessation de la diffusion, désindexation (« droit à l'oubli »), accès, droit d'être informé d'une décision automatisée (Art. 12.1).
E. Règles de transparence sur l'utilisation de témoins (cookies) à des fins de profilage.
F. Communications hors Québec : évaluation préalable du niveau de protection accordé par la juridiction étrangère.
G. Sanctions administratives pécuniaires de la CAI jusqu'à 10 millions $ ou 2 % du chiffre d'affaires mondial. Sanctions pénales jusqu'à 25 millions $ ou 4 %.

PHASE 3 — 22 SEPTEMBRE 2024 :
A. DROIT À LA PORTABILITÉ. Toute personne peut exiger, dans un format structuré, technologiquement courant, que ses RP lui soient communiqués ou transmis directement à un autre tiers.

ARTICULATION AVEC LE FÉDÉRAL — la LPRPDE fédérale s'applique au Québec uniquement aux activités fédérales (banques, télécoms, transport interprovincial). Pour la quasi-totalité des entreprises locales, c'est la Loi 25 qui prime. Si la régulation fédérale en cours d'élaboration aboutit, le Québec demandera à la CAI de demeurer l'autorité de référence pour ses résidents.

POURQUOI LA LOI 25 EST CRUCIALE POUR L'IA — bien qu'elle ne soit pas une « loi sur l'IA », elle régule les CONDITIONS D'ENTRÉE de l'IA dans tout traitement de RP : consentement à l'utilisation de données pour l'entraînement, transparence sur les décisions automatisées (Art. 8.1, 12.1), évaluation d'incidence préalable (EFVP), responsabilité du RPRP. Pratiquement, on ne peut pas déployer d'IA basée sur des données personnelles au Québec sans toucher à la Loi 25.
        """.strip(),
    },

    "m2_c2_loi25_rprp_efvp": {
        "module": 2, "ordre": 2, "langue": "fr",
        "titre": "Loi 25 — gouvernance interne (RPRP, EFVP, registres)",
        "prereqs": ["m2_c1_loi25_vue_ensemble"],
        "texte": """
La Loi 25 ne se contente pas d'imposer des obligations comportementales; elle exige une INFRASTRUCTURE DE GOUVERNANCE interne. Trois éléments structurent cette infrastructure : le RPRP, les EFVP, et les registres.

LE RPRP (RESPONSABLE DE LA PROTECTION DES RENSEIGNEMENTS PERSONNELS) — Article 3.1 LPRPSP :
A. Désignation OBLIGATOIRE depuis le 22 septembre 2022.
B. Par défaut, c'est la personne ayant la plus haute autorité dans l'entreprise (président, propriétaire). Peut être DÉLÉGUÉ par écrit à un employé ou à un tiers.
C. Le titre et les coordonnées du RPRP doivent être PUBLIÉS sur le site web de l'entreprise (Art. 3.2). Une simple adresse courriel suffit, mais elle doit être fonctionnelle et surveillée.
D. Rôles attendus : superviser le programme de protection, coordonner les EFVP, gérer les incidents, tenir les registres, traiter les demandes des personnes (accès, rectification, cessation, portabilité).
E. Différence avec le DPO européen (RGPD Art. 37-39) : le DPO doit être indépendant, libre de tout conflit d'intérêts. La Loi 25 n'impose pas explicitement ces protections.

LES EFVP (ÉVALUATIONS DES FACTEURS RELATIFS À LA VIE PRIVÉE) — Article 3.3 LPRPSP, en vigueur depuis le 22 septembre 2023.
A. Obligation de réaliser une EFVP AVANT TOUT PROJET d'acquisition, de développement ou de refonte d'un système d'information ou de prestation électronique de services impliquant la collecte, l'utilisation, la communication, la conservation ou la destruction de RP.
B. Application IA — déployer un nouveau modèle de scoring de crédit, de tri de CV, de chatbot avec rétention de conversations, ou d'analyse vidéo en magasin DÉCLENCHE l'obligation d'EFVP.
C. Contenu attendu (la CAI a publié un guide en septembre 2023) :
   - Description du système, finalités, nécessité;
   - Cartographie des flux de RP;
   - Identification des risques pour la vie privée;
   - Analyse des mesures de mitigation (techniques, organisationnelles, contractuelles);
   - Décision motivée d'aller de l'avant ou non, conditions de mise en œuvre.
D. L'EFVP doit être proportionnée à la sensibilité, à la finalité et au volume des renseignements concernés.
E. Conservation : la loi n'impose pas de durée explicite; en pratique, conserver l'EFVP au moins 3 ans après la fin du projet.

LES REGISTRES — la Loi 25 impose plusieurs registres distincts :
1. REGISTRE DES INCIDENTS (Art. 3.8). Conservation : 5 ans après la date de l'incident.
2. REGISTRE DES COMMUNICATIONS hors Québec (Art. 17). Évaluation préalable du niveau de protection.
3. REGISTRE DES UTILISATIONS À DES FINS SECONDAIRES (Art. 12).
4. REGISTRE DES DÉCISIONS AUTOMATISÉES — non explicitement requis mais fortement recommandé pour démontrer la conformité aux articles 8.1 et 12.1.

INTERACTIONS — le RPRP supervise les EFVP, qui alimentent les registres, qui sont utilisés par le RPRP pour répondre aux demandes des personnes et aux enquêtes de la CAI. Une organisation mature documente cette articulation dans une POLITIQUE INTÉGRÉE DE GOUVERNANCE DES DONNÉES.

ERREURS FRÉQUENTES :
A. Désigner le RPRP mais ne pas publier ses coordonnées sur le site web — non-conformité formelle facile à constater.
B. Réaliser une EFVP « formelle » qui ne fait que cocher des cases sans véritable analyse des risques. La CAI a explicitement déclaré en 2025-2026 que ce n'est pas suffisant.
C. Confondre le registre des incidents (Art. 3.8) et le registre des activités de traitement (registre type Art. 30 RGPD, qui n'est pas requis par la Loi 25 mais souvent attendu par les partenaires européens).
D. Omettre de mettre à jour l'EFVP quand le projet évolue significativement.

LIEN AVEC L'IA — pour un projet d'IA, l'EFVP est l'instrument de premier rang. Elle doit examiner spécifiquement : (i) sources de données d'entraînement et leur licéité; (ii) risques de biais; (iii) transparence offerte aux personnes affectées; (iv) capacité de contester une décision automatisée; (v) mesures de surveillance humaine. C'est dans l'EFVP qu'on documente la conformité aux articles 8.1 et 12.1.
        """.strip(),
    },

    "m2_c3_loi25_consentement_droits": {
        "module": 2, "ordre": 3, "langue": "fr",
        "titre": "Loi 25 — consentement et droits des personnes",
        "prereqs": ["m2_c1_loi25_vue_ensemble"],
        "texte": """
La Loi 25 a profondément renforcé les règles de CONSENTEMENT et a créé ou consolidé une demi-douzaine de droits subjectifs au bénéfice des personnes. Ces règles encadrent la « licéité » de toute collecte, utilisation et communication de renseignements personnels — y compris pour entraîner ou faire fonctionner un système d'IA.

QUATRE QUALITÉS REQUISES DU CONSENTEMENT (Art. 14 LPRPSP) :
1. MANIFESTE — démarche claire de la personne. Le silence, l'inaction, ou les paramètres par défaut ne valent pas consentement.
2. LIBRE — pas de pression, pas de chantage, pas de conditionnement à l'accès à un service essentiel.
3. ÉCLAIRÉ — la personne doit comprendre la finalité, les destinataires, la durée, les conséquences possibles.
4. DONNÉ À DES FINS SPÉCIFIQUES — un consentement « pour toute utilisation que nous jugerons utile » est NUL.

CONSENTEMENT EXPLICITE pour les RP SENSIBLES (Art. 12 al. 4) — santé, biométrie, opinion politique ou religieuse, orientation sexuelle, données génétiques. Acte AFFIRMATIF distinct (case à cocher non pré-cochée, signature, déclaration enregistrée).

EXCEPTIONS AU CONSENTEMENT (souvent invoquées à tort) :
A. Nécessité contractuelle — le RP est nécessaire à l'exécution du contrat. « Nécessaire » s'entend strictement.
B. Obligation légale.
C. Intérêt légitime de l'organisation, dans des conditions très restreintes (Art. 12 al. 3).
D. Recherche, étude, statistique d'intérêt public, sous encadrement strict.
E. Sécurité publique, prévention de fraude, situations urgentes.

DROITS DES PERSONNES (Art. 27 et suivants) :

DROIT D'ACCÈS — confirmation et communication des RP. Réponse dans les 30 jours, gratuite. En IA, ce droit s'étend aux DONNÉES UTILISÉES pour entraîner un modèle si elles sont identifiables — point délicat pour les modèles génératifs.

DROIT DE RECTIFICATION — corriger un RP inexact, incomplet ou équivoque. En IA, peut imposer la mise à jour des prédictions ou recommandations.

DROIT À LA CESSATION DE LA DIFFUSION et DROIT À LA DÉSINDEXATION (Art. 28.1) — ensemble, « droit à l'oubli ». La personne peut exiger la cessation de la diffusion ou la désindexation par les moteurs de recherche d'un renseignement diffusé en contravention de la loi ou contre sa volonté, lorsque le préjudice est sérieux.

DROIT À LA PORTABILITÉ (Art. 27 al. 2, en vigueur depuis le 22 septembre 2024) — transmission dans un format technologiquement courant et structuré, ou transmission directe à un autre tiers désigné.

DROIT D'OPPOSITION ET DROIT DE RETRAIT — retrait du consentement à tout moment.

DROIT D'ÊTRE INFORMÉ D'UNE DÉCISION AUTOMATISÉE (Art. 12.1) — couvert en détail dans le concept dédié.

DÉLAIS — réponse aux demandes dans les 30 jours, par écrit, dans la langue choisie par la personne. Refus possible mais doit être motivé.

CONTRAT vs CONSENTEMENT — un consommateur qui s'abonne à un service N'A PAS nécessairement consenti à l'utilisation de ses données pour entraîner un modèle d'IA. Si l'entraînement est une finalité secondaire, un consentement spécifique est requis. La CAI a été particulièrement vigilante sur ce point depuis 2024.

DONNÉES DES MINEURS (Art. 4.1) — pour un mineur de moins de 14 ans, c'est le titulaire de l'autorité parentale qui consent. De 14 à 18 ans, le mineur peut consentir lui-même mais l'organisation doit prêter une attention particulière à la clarté du consentement.

POINT CRITIQUE POUR L'IA — le « consentement éclairé » exige de la personne qu'elle comprenne les conséquences. Pour un système d'IA, cela signifie qu'on doit pouvoir décrire de façon intelligible : ce que le système fait, sur quelles données il s'appuie, quelles décisions il influence, quels biais ou limites sont connus.
        """.strip(),
    },

    "m2_c4_loi25_decisions_automatisees": {
        "module": 2, "ordre": 4, "langue": "fr",
        "titre": "Loi 25 — décisions automatisées (Art. 8.1 et 12.1)",
        "prereqs": ["m2_c3_loi25_consentement_droits"],
        "texte": """
Les articles 8.1 et 12.1 de la Loi 25 (sur le secteur privé : LPRPSP; transposés à l'identique pour le secteur public) sont LE CŒUR DE LA RÉGULATION QUÉBÉCOISE DE L'IA. Ils encadrent les « décisions fondées exclusivement sur un traitement automatisé » des renseignements personnels. En vigueur depuis le 22 septembre 2023.

ARTICLE 12.1 — TRANSPARENCE ET DROIT DE CONTESTATION DES DÉCISIONS AUTOMATISÉES.

Texte simplifié : « Toute personne concernée par une décision fondée EXCLUSIVEMENT sur un traitement automatisé doit être informée de ce fait au plus tard au moment où elle est informée de la décision. À sa demande, elle doit être informée des renseignements personnels utilisés pour rendre la décision, des raisons et des principaux facteurs et paramètres ayant mené à la décision, et de son droit de faire rectifier les renseignements utilisés. Elle doit aussi se voir donner l'occasion de présenter ses observations à un membre du personnel en mesure de réviser la décision. »

CONDITION DÉCLENCHANTE — le mot « EXCLUSIVEMENT » est crucial. Si la décision est ASSISTÉE par une IA mais qu'un humain l'évalue substantiellement avant de la rendre, l'article 12.1 ne s'applique pas. Mais attention : la CAI suit l'esprit du RGPD (Art. 22) et exige une intervention humaine SIGNIFICATIVE, pas seulement une signature de validation perfunctoire (« rubber-stamping »). Une revue humaine purement formelle ne sort pas du champ de 12.1.

EXEMPLES TYPIQUES de décisions visées :
A. Refus automatique d'une demande de prêt sur la base d'un score algorithmique.
B. Tarification dynamique d'une prime d'assurance déterminée par un modèle.
C. Élimination automatique d'un CV par un système ATS sans revue humaine préalable.
D. Refus d'une transaction par carte de crédit sur fondement d'un modèle anti-fraude.
E. Décision d'éligibilité à un programme social calculée automatiquement.

QUATRE OBLIGATIONS distinctes contenues dans 12.1 :
1. INFORMATION sur le caractère automatisé — au moment de la décision.
2. INFORMATION SUR LES RP UTILISÉS, sur demande.
3. INFORMATION SUR LES RAISONS, FACTEURS ET PARAMÈTRES PRINCIPAUX, sur demande — exigence d'EXPLICABILITÉ.
4. POSSIBILITÉ DE PRÉSENTER DES OBSERVATIONS à un humain habilité à RÉVISER la décision.

ARTICLE 8.1 — TRANSPARENCE DES TECHNOLOGIES D'IDENTIFICATION, DE LOCALISATION, DE PROFILAGE.

Texte simplifié : « Une organisation qui recueille des RP au moyen d'une technologie comprenant des fonctions d'identification, de localisation ou de profilage doit informer la personne concernée du recours à cette technologie ainsi que des moyens offerts, le cas échéant, pour activer ces fonctions. »

CHAMP D'APPLICATION — TROIS CATÉGORIES :
A. IDENTIFICATION — reconnaissance faciale, reconnaissance vocale, biométrie en général.
B. LOCALISATION — GPS, BLE, Wi-Fi triangulation, IP, beacons.
C. PROFILAGE — toute analyse algorithmique de comportement, préférences, traits de personnalité, risques, basée sur des RP.

LE PROFILAGE — DÉFINITION QUÉBÉCOISE — toute évaluation d'aspects personnels (situation économique, comportement, préférences, performance professionnelle, état de santé, etc.) au moyen d'un traitement automatisé de RP. Très large; couvre la quasi-totalité des modèles d'IA prédictifs sur données personnelles.

OBLIGATION SPÉCIFIQUE — informer ACTIVEMENT la personne du recours à la technologie ET des moyens d'activer ou désactiver ses fonctions. Cela impose souvent un mécanisme d'opt-in ou opt-out clair.

INTERACTION 8.1 / 12.1 — l'article 8.1 s'applique en AMONT (au moment de la collecte / activation); l'article 12.1 s'applique en AVAL (au moment de la décision rendue). Un même système d'IA peut donc déclencher les deux.

POINT JURIDIQUE FRÉQUEMMENT CONTESTÉ — qu'est-ce qu'un « principal facteur ou paramètre »? La loi ne fournit pas de seuil. La CAI a indiqué que l'explication doit être SIGNIFICATIVE et SUFFISANTE pour permettre à la personne de contester. Solutions techniques : SHAP values, LIME, attention maps, contrefactuels, ou divulgation des CATÉGORIES de variables (sans nécessairement leur poids exact).

DIFFÉRENCE AVEC LE RGPD — l'article 22 du RGPD INTERDIT par défaut la décision exclusivement automatisée sauf trois exceptions; au Québec, elle est PERMISE moyennant transparence et droit de contestation.

CONFORMITÉ PRATIQUE — pour un système d'IA déployé au Québec, voici les questions à se poser : (1) La décision est-elle exclusivement automatisée ou y a-t-il une revue humaine substantielle? (2) Si exclusivement automatisée : informe-t-on la personne au moment de la décision? (3) Peut-on, sur demande, fournir les RP utilisés et les principaux facteurs? (4) Existe-t-il un canal opérationnel de révision humaine, et le personnel concerné est-il formé pour la mener? (5) L'EFVP du système documente-t-elle ces choix?
        """.strip(),
    },

    "m2_c5_loi25_incidents_sanctions": {
        "module": 2, "ordre": 5, "langue": "fr",
        "titre": "Loi 25 — incidents, sanctions, jurisprudence CAI",
        "prereqs": ["m2_c1_loi25_vue_ensemble"],
        "texte": """
La Loi 25 a complètement repensé le régime de SANCTIONS. Avant 2022, les pouvoirs de la CAI étaient surtout consultatifs. Depuis 2023, la CAI dispose d'un arsenal qui rivalise — en montants — avec celui des autorités européennes au titre du RGPD.

INCIDENTS DE CONFIDENTIALITÉ — Article 3.5 et suivants. Définition : « tout accès, utilisation ou communication non autorisé par la loi, ainsi que toute perte ou tout autre événement portant atteinte à la protection des renseignements personnels ». Le concept est plus large que la simple « fuite » : un employé qui consulte sans nécessité un dossier client constitue un incident.

OBLIGATION DE NOTIFICATION :
A. Prendre les mesures raisonnables pour réduire les risques (Art. 3.5).
B. Évaluer le RISQUE SÉRIEUX DE PRÉJUDICE (RSP). Critères : sensibilité des RP, conséquences appréhendées, probabilité d'utilisation préjudiciable.
C. Si RSP — notifier la CAI ET les personnes concernées « avec diligence ». La pratique : 72 heures pour la CAI (par analogie avec le RGPD).
D. Tenir le REGISTRE DES INCIDENTS, conservé 5 ans.

CONTENU DE LA NOTIFICATION (Règlement de la CAI sur les incidents, en vigueur depuis 2023) :
- Description de l'incident, date, nature des RP touchés;
- Nombre estimé de personnes touchées;
- Mesures prises pour atténuer le risque;
- Mesures que la personne peut prendre elle-même;
- Coordonnées du RPRP.

DEUX RÉGIMES DE SANCTIONS distincts :

RÉGIME 1 — SANCTIONS ADMINISTRATIVES PÉCUNIAIRES (SAP) — Art. 90.1 et 90.2. Imposées directement par la CAI. Plafonds :
A. 10 millions $ OU 2 % du chiffre d'affaires mondial — le PLUS ÉLEVÉ.
B. Doublé en cas de récidive dans les 5 ans.
Type d'infractions visées : non-désignation du RPRP, défaut de notification, refus d'accès, défaut d'EFVP, manquement à la transparence des décisions automatisées.

RÉGIME 2 — SANCTIONS PÉNALES — Art. 91 et suivants. Imposées par les tribunaux :
A. 25 millions $ OU 4 % du chiffre d'affaires mondial — le PLUS ÉLEVÉ.
B. Visent les infractions « volontaires » ou « graves ».

PLUS SÉVÈRE QUE LA LPRPDE FÉDÉRALE — la LPRPDE prévoyait des amendes maximales de 100 000 $. La Loi 25 a multiplié par 250 les plafonds. C'est l'un des régimes les plus sévères au Canada et l'un des plus alignés avec le RGPD européen.

POUVOIRS D'ENQUÊTE de la CAI :
A. Inspections sur place sans mandat dans les locaux ouverts au public, avec mandat ailleurs.
B. Demandes de production de documents.
C. Interrogatoires sous serment.
D. Décisions exécutoires : ordonnance de cesser, de corriger, de communiquer.
E. Pouvoir de désigner un enquêteur spécial.

TENDANCE DOMINANTE 2025-2026 — la CAI passe d'un mode d'application centré sur les LIGNES DIRECTRICES à un mode d'application centré sur les ENQUÊTES. Plusieurs signaux :
A. La CAI investigue activement les organisations qui déploient de l'IA SANS EFVP préalable. C'est devenu le motif d'enquête le plus courant en 2025-2026.
B. Avis publics sur la reconnaissance faciale dans les lieux ouverts au public, en lien avec l'article 8.1.
C. Lignes directrices sur les EFVP, précisant qu'une analyse purement formelle ne suffit pas.
D. Décisions sur la nécessité d'un consentement spécifique pour l'entraînement de modèles à partir de données clients.
E. Coordination internationale : signature en février 2026 d'une déclaration commune avec environ 60 autorités sur les contenus générés par IA.

PRINCIPAUX POINTS D'ATTENTION pour l'IA en 2026 :
1. Utilisation de données client pour entraîner des modèles sans consentement spécifique → mise en demeure probable.
2. Conformité aux articles 8.1 et 12.1 dans les chatbots et systèmes de recommandation.
3. EFVP des projets d'IA qui se contentent de cocher des cases sans analyse réelle des biais et des impacts disparates.
4. Communications hors Québec de RP dans les architectures cloud.
5. Notification d'incidents impliquant des fournisseurs cloud — l'obligation incombe à l'entreprise québécoise même si le sous-traitant est à l'origine de la fuite.

ROUTE PRATIQUE — en cas d'incident lié à un système d'IA :
ÉTAPE 1 : ISOLER le système (couper l'accès, suspendre les inférences).
ÉTAPE 2 : DOCUMENTER l'incident (date, nature, RP touchés, nombre de personnes, mesures prises).
ÉTAPE 3 : ÉVALUER LE RSP (consultation interne, conseil juridique).
ÉTAPE 4 : NOTIFIER la CAI avec diligence (72 heures si possible) et les personnes affectées.
ÉTAPE 5 : INSCRIRE au registre des incidents.
ÉTAPE 6 : POST-MORTEM technique et organisationnel; mise à jour des EFVP et des contrôles.
        """.strip(),
    },

    "m2_c6_cai_principes_ia_generative": {
        "module": 2, "ordre": 6, "langue": "fr",
        "titre": "Principes de la CAI sur l'IA générative",
        "prereqs": ["m2_c1_loi25_vue_ensemble"],
        "texte": """
La Commission d'accès à l'information du Québec (CAI) a publié des PRINCIPES DE DÉVELOPPEMENT ET D'UTILISATION DE L'INTELLIGENCE ARTIFICIELLE GÉNÉRATIVE. Ce document complète l'ensemble du corpus existant de la CAI : guide EFVP (septembre 2023), guide sur les incidents de confidentialité, brief « L'IA au travail : pour un meilleur encadrement » (janvier 2025).

POURQUOI UN DOCUMENT SPÉCIFIQUE À L'IA GÉNÉRATIVE — la Loi 25 ne distingue pas l'IA classique de l'IA générative. Mais l'IA générative pose des questions distinctes :
A. Données d'entraînement massives, souvent recueillies sans consentement.
B. Sorties produites pouvant contenir ou inférer des RP.
C. Risque de fuite mémorisée (modèle qui régurgite des données d'entraînement).
D. Impossibilité technique d'effacer une donnée d'un modèle déjà entraîné.
E. Hallucinations qui peuvent affecter des personnes nommées.

PRINCIPES STRUCTURANTS dégagés par la CAI :

PRINCIPE 1 — NÉCESSITÉ ET PROPORTIONNALITÉ. Avant tout déploiement d'IA générative traitant des RP, l'organisation doit démontrer que l'IA générative est NÉCESSAIRE et qu'aucune solution moins intrusive (système de règles, IA prédictive simple, traitement humain) ne peut atteindre l'objectif. Le test est strict.

PRINCIPE 2 — TRANSPARENCE RENFORCÉE. Pour l'IA générative, la transparence va au-delà de l'article 12.1 :
- Information aux personnes que le contenu qu'elles consomment est généré ou assisté par IA.
- Étiquetage des sorties (watermarking, métadonnées).
- Documentation publique des modèles utilisés et de leurs limites.

PRINCIPE 3 — LICÉITÉ DES DONNÉES D'ENTRAÎNEMENT. L'organisation qui entraîne ou réentraîne (« fine-tune ») un modèle à partir de données québécoises doit pouvoir démontrer la BASE LÉGALE de cette utilisation. Le « web scraping » sans consentement spécifique est PRESQUE TOUJOURS NON CONFORME pour des données identifiables.

PRINCIPE 4 — DROITS DES PERSONNES sur les sorties. Si un modèle génère du contenu identifiant ou caractérisant une personne, celle-ci conserve ses droits (accès, rectification, cessation de la diffusion). Pour les hallucinations négatives sur une personne nommée, l'organisation doit prévoir un mécanisme rapide de retrait.

PRINCIPE 5 — SUPERVISION HUMAINE PROPORTIONNELLE. Plus la décision a un impact significatif sur la personne, plus la supervision humaine doit être substantielle. Pour un usage à enjeux faibles (suggestion de courriel), supervision allégée; pour un usage à enjeux élevés (résumé médical, évaluation RH), revue humaine substantielle obligatoire.

PRINCIPE 6 — JOURNAL DES UTILISATIONS. L'organisation doit conserver les TRACES de l'utilisation du système (qui, quand, sur quelles données, pour quelle décision). Sans journal, impossible de répondre aux demandes des personnes ni aux enquêtes de la CAI.

PRINCIPE 7 — ÉVALUATION DES RISQUES SPÉCIFIQUES. L'EFVP d'un projet d'IA générative doit couvrir les risques propres : hallucinations, fuite mémorisée, biais amplifiés, génération de contenus dangereux, dépendance excessive (« automation bias »).

ARTICULATION AVEC L'EFVP CLASSIQUE — les principes IA générative ne remplacent pas l'EFVP. Ils l'enrichissent. Une EFVP pour un projet d'IA générative doit explicitement traiter ces sept dimensions.

ARTICULATION AVEC L'EU AI ACT — le régime GPAI de l'EU AI Act (Art. 51-55) impose des obligations similaires aux fournisseurs de modèles. Une organisation qui fournit ou intègre un modèle GPAI dans un produit destiné au Québec doit cumuler les exigences européennes (côté fournisseur du modèle) et québécoises (côté traitement de RP).

UTILISATION PRATIQUE pour Nord Paradigm — ces principes sont la BASE D'UN GABARIT DE QUESTIONS pour Brèche Pro lorsque le client utilise de l'IA générative. Chaque principe → 3-5 questions de diagnostic. Si une réponse est manquante ou faible, c'est un point de gouvernance à renforcer.
        """.strip(),
    },

    "m2_c7_cai_application_2026": {
        "module": 2, "ordre": 7, "langue": "fr",
        "titre": "Tendances d'application de la CAI en 2026",
        "prereqs": ["m2_c5_loi25_incidents_sanctions"],
        "texte": """
Au 25 avril 2026, la CAI est entrée dans une phase de DURCISSEMENT DE L'APPLICATION. Le passage de la « pédagogie » à « l'enquête » est documenté par plusieurs signaux convergents. Comprendre ces tendances permet à une PME québécoise de calibrer son investissement en gouvernance d'IA.

SIGNAL 1 — ENQUÊTES SUR DÉPLOIEMENTS IA SANS EFVP. Selon les rapports d'intelligence sectoriels d'avril 2026, la CAI investigue activement les organisations qui implémentent des outils d'IA SANS avoir réalisé d'EFVP au préalable. C'est devenu la première cause d'enquête formelle. Implication : pour une PME, l'absence d'EFVP est aujourd'hui le risque de non-conformité le plus probable.

SIGNAL 2 — VIGILANCE SUR LE CONSENTEMENT POUR L'ENTRAÎNEMENT. Plusieurs organisations qui ont voulu utiliser des données client pour entraîner des modèles propriétaires ont dû ajuster leurs CGU et offrir un opt-out clair après pression de la CAI. Le « consentement enfoui dans les CGU » ne tient plus.

SIGNAL 3 — ACCENT SUR L'EFFECTIVITÉ DE LA REVUE HUMAINE pour l'article 12.1. La CAI est passée d'une lecture FORMELLE (« y a-t-il une signature humaine ? ») à une lecture SUBSTANTIELLE (« la personne qui signe a-t-elle réellement le pouvoir et l'information pour réviser ? »). Conséquence : un humain qui valide en 5 secondes 200 décisions d'IA par jour ne sort PAS du champ de 12.1.

SIGNAL 4 — COORDINATION INTERNATIONALE. La CAI a co-signé en février 2026, avec environ 60 autorités de protection des données dans le monde, une déclaration sur les contenus générés par IA. Implication : les positions de la CAI s'alignent de plus en plus sur celles de l'EDPB européen, du commissaire fédéral canadien (OPC), de la CNIL française, de l'ICO britannique, et d'autorités asiatiques.

SIGNAL 5 — ENGAGEMENT AVEC LES GRANDS FOURNISSEURS. Le précédent ICO britannique de 2025-2026 — engagement avec 11 fournisseurs majeurs de modèles de fondation — préfigure ce que la CAI pourrait faire. Les rapports d'avril 2026 mentionnent que la CAI a commencé à interagir avec certains fournisseurs cloud sur les conditions de traitement des RP.

SIGNAL 6 — APPLICATION EXTRATERRITORIALE. La CAI affirme de plus en plus son extraterritorialité face à des entreprises basées hors Québec mais offrant leurs produits à des résidents québécois. Il est probable qu'on verra dans les 12-24 mois les premières grandes décisions visant des entreprises sans présence physique au Québec.

LE PROBLÈME DE L'INVENTAIRE EN ENTREPRISE — un thème récurrent dans les rapports d'intelligence : LA PLUPART DES ORGANISATIONS NE SAVENT PAS QUELS SYSTÈMES D'IA ELLES UTILISENT. Le « shadow IA » (employés utilisant ChatGPT, Claude, Copilot sans gouvernance) explose. Pour un client de Nord Paradigm, c'est souvent le PREMIER LIVRABLE : une cartographie qui révèle 3 à 10 fois plus de systèmes que ce que la direction pensait avoir.

RÉPONSE STRATÉGIQUE pour une PME québécoise :
A. CARTOGRAPHIER MAINTENANT (cf. M10 c1) — chaque système d'IA utilisé en interne ou intégré dans un produit.
B. PRIORISER les systèmes traitant des RP de Québécois ou produisant des décisions affectant des personnes.
C. EFVP RÉTROACTIVES sur les systèmes existants à risque modéré ou élevé. Imparfait, mais beaucoup mieux que rien.
D. RPRP DÉSIGNÉ ET PUBLIÉ. Vérifier que les coordonnées sont actives et surveillées.
E. PROCESSUS POUR L'ART. 12.1 — pour chaque décision exclusivement automatisée : mécanisme de notification, canal de révision humaine substantielle, formation du personnel.
F. CONSENTEMENT POUR L'ENTRAÎNEMENT — si les données clients alimentent un modèle, opt-in spécifique avec finalité claire.

POSITIONNEMENT NORD PARADIGM — le service Brèche (analyse de risque IA gratuite) est conçu pour répondre exactement à cette pression réglementaire. Dans les 12-24 mois, la demande pour des EFVP de qualité va croître fortement, parce que les organisations qui n'en ont pas sont les plus exposées aux enquêtes de la CAI.

INDICATEUR À SURVEILLER — la première grande décision publique de la CAI sanctionnant une organisation pour défaut d'EFVP dans un projet d'IA. Quand elle viendra (probablement 2026 ou 2027), elle créera un précédent et accélérera la demande pour des EFVP rigoureuses.
        """.strip(),
    },

})


# ══════════════════════════════════════════════════════════════════════════════
# MODULE 3 — CADRE FÉDÉRAL CANADIEN ET PROVINCES  (6 concepts, FR)
# ══════════════════════════════════════════════════════════════════════════════

CURRICULUM.update({

    "m3_c1_canada_paysage_federal": {
        "module": 3, "ordre": 1, "langue": "fr",
        "titre": "Paysage fédéral canadien — vue d'ensemble",
        "prereqs": ["m1_c3_approches_reglementaires"],
        "texte": """
Au 25 avril 2026, le Canada N'A PAS de loi fédérale horizontale sur l'IA. La régulation fédérale de l'IA est en cours d'élaboration et reste fragmentée. Trois instruments forment le PAYSAGE FÉDÉRAL ACTUEL :

INSTRUMENT 1 — DIRECTIVE SUR LA PRISE DE DÉCISIONS AUTOMATISÉE (Directive on Automated Decision-Making) du Conseil du Trésor. CONTRAIGNANTE pour les institutions fédérales (ministères, agences). Mise à jour entrée en vigueur le 24 juin 2025; les systèmes existants ont jusqu'au 24 juin 2026 pour se conformer aux nouvelles exigences. Couvre le concept dédié.

INSTRUMENT 2 — STRATÉGIE D'IA POUR LA FONCTION PUBLIQUE FÉDÉRALE 2025-2027. Document stratégique non contraignant. Quatre priorités : expertise centralisée, infrastructure sécurisée, gouvernance des données, confiance du public. Établit l'orientation pour les institutions fédérales et le Registre canadien des systèmes décisionnels automatisés.

INSTRUMENT 3 — CODE DE CONDUITE VOLONTAIRE pour le développement et la gestion responsables des systèmes d'IA générative avancée (septembre 2023). VOLONTAIRE, signé par environ une dizaine d'organisations canadiennes (BlackBerry, Cohere, IBM Canada, Mila, OpenText, TELUS, et d'autres). Couvre le concept dédié.

CE QUI N'EXISTE PAS EN AVRIL 2026 :
A. Pas de loi fédérale horizontale sur l'IA en vigueur. La législation fédérale qui aurait introduit AIDA est tombée avec la prorogation du Parlement en 2025. Une nouvelle approche est en consultation; le statut exact évolue.
B. Pas d'autorité fédérale dédiée à l'IA — pas d'équivalent canadien de l'AI Office européen.
C. Pas de tribunal spécialisé pour les décisions algorithmiques.

LACUNE COMBLÉE PARTIELLEMENT par :
A. La LPRPDE fédérale (Loi sur la protection des renseignements personnels et les documents électroniques) — applicable aux activités fédérales (banques, télécoms, transport interprovincial).
B. La LOI CANADIENNE SUR LES DROITS DE LA PERSONNE — interdit la discrimination, applicable même quand l'agent décisionnel est un système automatisé.
C. Le CODE CRIMINEL — pour les usages malveillants graves.
D. Lois sectorielles fédérales (banques, télécoms, transport, sécurité publique).
E. Le COMMISSAIRE À LA PROTECTION DE LA VIE PRIVÉE DU CANADA (OPC) — qui peut publier des lignes directrices et coordonner avec ses homologues internationaux.

SIGNAL FÉVRIER 2026 — RÉSULTATS DU SPRINT NATIONAL D'ISDE. Le 3 février 2026, ISDE (Innovation, Sciences et Développement économique Canada) a publié les résultats d'une consultation nationale (« sprint ») sur la réglementation de l'IA. Préoccupations dominantes : vie privée, sécurité, transparence, responsabilité, gouvernance, biais systémiques, impacts environnementaux. Un GROUPE DE TRAVAIL SUR LA STRATÉGIE D'IA est en consultation pour la prochaine stratégie nationale. Malgré l'activité, le Canada continue de ne pas avoir de législation fédérale contraignante sur l'IA.

CONSÉQUENCE STRATÉGIQUE — la FRAGMENTATION RÉGLEMENTAIRE S'ACCÉLÈRE. Pendant que le fédéral piétine, les provinces avancent : Loi 25 au Québec, AI-in-hiring disclosure en Ontario (1er janvier 2026), Enhancing Digital Security and Trust Act en Ontario, lignes directrices sur les scribes IA en Ontario et Colombie-Britannique. Pour une organisation pancanadienne, la conformité devient une affaire de COMPATIBILITÉ AVEC PLUSIEURS RÉGIMES.

DEUX SCÉNARIOS PROSPECTIFS :
SCÉNARIO A — REPRISE DE L'INITIATIVE FÉDÉRALE. Une nouvelle loi fédérale sur l'IA est introduite, plus alignée avec l'EU AI Act ou avec l'approche par les risques. Échéance plausible : 2027-2028.
SCÉNARIO B — STATU QUO PROLONGÉ. Le fédéral promeut le Code volontaire et l'adoption de normes ISO 42001 pendant que les provinces continuent leurs initiatives. Le marché s'aligne sur le standard le plus élevé applicable (souvent l'EU AI Act).

POSITION D'INVESTISSEMENT pour une PME canadienne :
1. Conformité IMMÉDIATE Loi 25 (provincial Québec) — obligation actuelle.
2. Adoption NIST AI RMF — méthode opérationnelle gratuite, alignée avec les obligations probables d'une future loi fédérale.
3. SURVEILLANCE des évolutions ISDE et OPC.
4. ADHÉSION au Code volontaire si pertinent (signal réputationnel).
5. SI EXPOSITION EUROPÉENNE — anticiper l'EU AI Act, plus prescriptif que tout ce qui est probable côté canadien.
6. SUIVI des règles provinciales sectorielles (Ontario, Colombie-Britannique) si présence pancanadienne.

REMARQUE TERMINOLOGIQUE — les documents de Nord Paradigm évitent désormais de citer « C-27 » ou « AIDA » par leur nom historique, et utilisent l'expression « régulation fédérale de l'IA en cours d'élaboration ». La raison : éviter de figer l'analyse sur un texte dépassé et garder une terminologie applicable au prochain projet législatif.
        """.strip(),
    },

    "m3_c2_directive_adm_aia": {
        "module": 3, "ordre": 2, "langue": "fr",
        "titre": "Directive sur la prise de décisions automatisée et outil AIA",
        "prereqs": ["m3_c1_canada_paysage_federal"],
        "texte": """
La DIRECTIVE SUR LA PRISE DE DÉCISIONS AUTOMATISÉE du Secrétariat du Conseil du Trésor du Canada est l'instrument FÉDÉRAL CONTRAIGNANT le plus important sur l'IA. Bien qu'elle s'applique uniquement aux institutions fédérales, elle constitue une RÉFÉRENCE OPÉRATIONNELLE pour les ateliers de Nord Paradigm : « le Gouvernement du Canada lui-même exige des évaluations d'incidence algorithmique avant de déployer de l'IA. »

CHAMP D'APPLICATION :
A. Tous les ministères et agences fédéraux assujettis à la Politique sur les services et le numérique.
B. Couvre les systèmes décisionnels qui automatisent partiellement OU totalement des décisions administratives, y compris ceux fondés sur l'IA.
C. Les autres organismes non assujettis sont « encouragés » à s'y conformer comme bonne pratique.

VERSION ACTUELLE — mise à jour effective le 24 JUIN 2025. Les systèmes existants ont jusqu'au 24 JUIN 2026 pour se conformer aux exigences nouvelles ou modifiées. Échéance proche; toutes les institutions fédérales travaillent activement à l'alignement.

DÉFINITIONS CLÉS :
A. « SYSTÈME DÉCISIONNEL AUTOMATISÉ » — toute technologie qui assiste OU remplace le jugement d'un décideur humain. Inclut machine learning, statistiques, analyse de données.
B. « DÉCISION ADMINISTRATIVE » — décision prise dans l'exercice d'une autorité légale qui affecte les droits, privilèges ou intérêts d'individus spécifiques.

MÉCANISME CENTRAL — L'ÉVALUATION D'INCIDENCE ALGORITHMIQUE (EIA / AIA, « Algorithmic Impact Assessment »). Questionnaire en ligne OPEN-SOURCE (hébergé sur GitHub). Évalue :
- Impacts sur les droits et libertés.
- Impacts sur la santé et la sécurité.
- Impacts économiques.
- Sensibilité des données.
- Complexité du système.
- Réversibilité des décisions.

L'AIA produit un NIVEAU D'IMPACT (I à IV). Les obligations augmentent avec le niveau.

CADRE EN QUATRE NIVEAUX (Annexe C de la Directive) :

NIVEAU I — IMPACT FAIBLE. Notification que la décision a été prise par un système automatisé. Audit trail. Aucun examen par les pairs. Aucune obligation d'explication. Approbation : aucune autorité spécifique requise.

NIVEAU II — IMPACT MODÉRÉ. Notification + EXPLICATION en langage simple + RECOURS HUMAIN sur demande. Plan de contingence. Approbation : Directeur.

NIVEAU III — IMPACT ÉLEVÉ. Tout ce qui précède + EXAMEN PAR LES PAIRS + INTERVENTION HUMAINE OBLIGATOIRE AVANT la décision + plan de surveillance. Approbation : sous-ministre adjoint / VP.

NIVEAU IV — IMPACT TRÈS ÉLEVÉ. Tout ce qui précède + AUDIT INDÉPENDANT par un tiers ou examen équivalent. Approbation : sous-ministre.

EXIGENCES TRANSVERSALES (s'appliquent à tous les niveaux) :
A. NOTIFICATION du recours à un système automatisé — toujours requis.
B. AUDIT TRAIL — toujours requis. Conservation des données de décision.
C. RECOURS — les ministères doivent informer les clients des options pour contester une décision automatisée. Les recours doivent être en temps opportun, efficaces, et faciles d'accès.
D. RAPPORTAGE — publication d'information sur les systèmes dans le REGISTRE CANADIEN DES SYSTÈMES DÉCISIONNELS AUTOMATISÉS (Government of Canada AI Register), accessible publiquement.

L'OUTIL AIA — disponible publiquement et OPEN-SOURCE sur GitHub. Toute organisation (publique ou privée) peut l'utiliser pour évaluer ses propres systèmes. Pour Nord Paradigm, c'est un OUTIL PRÊT À L'EMPLOI pour amorcer une cartographie de risque dans une mission Brèche, indépendamment du fait que le client soit fédéral ou non.

ARTICULATION AVEC LES AUTRES RÉGIMES :
A. LOI 25 ART. 12.1 — la Directive fédérale et l'article 12.1 québécois imposent des obligations similaires (transparence + recours humain). Une organisation fédérale opérant au Québec doit satisfaire les deux.
B. EU AI ACT — la classification en 4 niveaux est conceptuellement alignée avec la classification par niveaux de risque de l'EU AI Act. Une organisation peut RÉUTILISER son AIA pour amorcer une analyse EU AI Act.
C. NIST AI RMF — l'AIA correspond largement à la fonction MAP du RMF. Une organisation peut intégrer l'AIA comme livrable concret de la phase MAP.
D. CODE VOLONTAIRE — la Directive fédérale opérationnalise les principes du Code (responsabilité, transparence, surveillance humaine).

UTILISATION POUR UN ATELIER NORD PARADIGM :
1. Présenter l'AIA comme MODÈLE GOUVERNEMENTAL ÉPROUVÉ.
2. Faire compléter l'AIA pour 1-2 systèmes du client.
3. Le résultat (niveau I-IV) sert de POINT D'ANCRAGE pour discuter des obligations applicables.
4. La majorité des systèmes d'IA d'une PME tombent au niveau II ou III. Cela fixe les attentes en matière de revue humaine, de plan de contingence, et de documentation.

LIMITE — la Directive est INTERNE au gouvernement fédéral; elle n'a pas de portée juridique sur les entreprises privées. Mais comme RÉFÉRENCE PRATIQUE et OUTIL OPÉRATIONNEL, elle est très utile.
        """.strip(),
    },

    "m3_c3_code_volontaire_canada": {
        "module": 3, "ordre": 3, "langue": "fr",
        "titre": "Code de conduite volontaire (Canada) — l'instrument intérimaire",
        "prereqs": ["m3_c1_canada_paysage_federal"],
        "texte": """
En l'absence de loi fédérale horizontale sur l'IA adoptée, le gouvernement fédéral canadien s'est doté en septembre 2023 d'un instrument intérimaire : le « CODE DE CONDUITE VOLONTAIRE visant un développement et une gestion responsables des systèmes d'IA générative avancée ». Le code n'a aucune force contraignante directe — c'est un engagement public unilatéral de signataires. Mais il joue trois rôles importants.

LES TROIS RÔLES DU CODE :
A. SIGNAL POLITIQUE — fixe l'orientation gouvernementale et démontre que le Canada n'est pas inactif en attendant une loi fédérale.
B. ENGAGEMENT RÉPUTATIONNEL — les signataires s'engagent publiquement à respecter ses six principes; un manquement attire l'attention médiatique.
C. PRÉFIGURATION RÉGLEMENTAIRE — le contenu du code reflète largement ce qui pourrait devenir contraignant via une future loi fédérale. Le suivre, c'est se mettre en bonne position.

LES SIX PRINCIPES (à mémoriser) :

PRINCIPE 1 — RESPONSABILITÉ. L'organisation est responsable de la conception, du développement et du déploiement responsables. Implique : politiques internes, formation du personnel, allocation claire des responsabilités le long de la chaîne de valeur.

PRINCIPE 2 — SÉCURITÉ. Tests rigoureux pré-déploiement, surveillance post-déploiement, mesures techniques et organisationnelles pour prévenir les dommages. Inclut spécifiquement la prévention de l'usage malveillant (fraude, désinformation, exploitation).

PRINCIPE 3 — JUSTICE ET ÉQUITÉ. Tests pour identifier et atténuer les biais discriminatoires; documentation des données d'entraînement; mécanismes de redressement.

PRINCIPE 4 — TRANSPARENCE. Publication d'une description du système, de ses limites, de ses sources de données dans la mesure du possible; étiquetage des contenus générés par IA.

PRINCIPE 5 — SURVEILLANCE HUMAINE ET MONITORING. Mécanismes permettant à un humain d'intervenir, de désactiver, de réviser. Suivi continu en service.

PRINCIPE 6 — VALIDATION. Vérification que le système répond à sa finalité déclarée et n'a pas de comportements imprévus dommageables.

DEUX RÔLES DISTINCTS — le code distingue les responsabilités selon qu'on est :
A. DÉVELOPPEUR de système d'IA générative avancée.
B. DÉPLOYEUR (utilisateur final qui le met en service).

Pour chaque principe, le code énumère les MESURES ATTENDUES de chacun — utile car la chaîne de valeur d'IA implique souvent plusieurs entreprises.

SIGNATAIRES — la liste évolue. Au lancement (septembre 2023), une dizaine d'entreprises canadiennes ont signé : BlackBerry, Cohere, IBM Canada, Mila, OpenText, TELUS, et d'autres. La signature est ouverte aux organisations qui en font la demande.

L'ADOPTION reste relativement lente — selon les rapports d'ISDE, beaucoup d'organisations préfèrent attendre une loi contraignante plutôt que de prendre des engagements unilatéraux.

LIMITE — le code se concentre sur l'IA GÉNÉRATIVE AVANCÉE. Il ne couvre pas exhaustivement les systèmes d'IA classiques (modèles supervisés, classification, scoring), même si plusieurs principes s'y appliquent par analogie.

ARTICULATION AVEC LE NIST AI RMF — les six principes du code se cartographient bien sur les sept caractéristiques de trustworthy AI du RMF :
- Responsabilité ↔ Accountability & Transparency
- Sécurité ↔ Safe + Secure & Resilient
- Justice ↔ Fair (with managed bias)
- Transparence ↔ Explainable & Interpretable + Privacy-Enhanced
- Surveillance humaine ↔ une partie de Accountability
- Validation ↔ Valid & Reliable

Cela signifie qu'une organisation qui implante le NIST AI RMF répond simultanément au code volontaire canadien — pas besoin de duplicateur d'efforts.

INTERACTION AVEC LE BLETCHLEY DECLARATION et le PROCESSUS DE HIROSHIMA DU G7. Le code canadien a été développé en parallèle de l'engagement de l'UK Bletchley (novembre 2023) et du processus de Hiroshima (octobre 2023). Le texte canadien est aligné avec ces deux processus internationaux.

UTILITÉ POUR UNE PME QUÉBÉCOISE :
A. SIGNAL DE SÉRIEUX vis-à-vis des partenaires gouvernementaux (le code est cité dans plusieurs appels d'offres fédéraux comme bonne pratique attendue).
B. PRÉPARATION À LA RÉGULATION FÉDÉRALE FUTURE — couvrir les six principes, c'est anticiper l'essentiel des obligations probables.
C. COMPLÉMENT À LA LOI 25 — le code traite des aspects que la Loi 25 ne couvre pas (sécurité technique, gestion des biais, validation), même si elles ne sont pas obligatoires.
D. POSITIONNEMENT INTERNATIONAL — démontrer une gouvernance responsable est de plus en plus exigé par les clients européens et américains.

POSITION CRITIQUE — un instrument volontaire de droit souple n'a pas la même force qu'une loi. Plusieurs voix de la société civile demandent qu'une loi fédérale soit adoptée pour précisément donner force exécutoire à ces principes. Le code est un PLANCHER éthique et un outil pédagogique, pas un substitut au droit dur.
        """.strip(),
    },

    "m3_c4_strategie_ia_federale": {
        "module": 3, "ordre": 4, "langue": "fr",
        "titre": "Stratégie d'IA pour la fonction publique fédérale 2025-2027",
        "prereqs": ["m3_c1_canada_paysage_federal"],
        "texte": """
La STRATÉGIE D'IA POUR LA FONCTION PUBLIQUE FÉDÉRALE 2025-2027 est le document d'orientation stratégique du gouvernement du Canada pour l'adoption de l'IA dans ses propres opérations. Publiée en juin 2025, elle complète la Directive sur la prise de décisions automatisée (qui régit l'usage) en orientant l'INVESTISSEMENT et la TRANSFORMATION sur 24-36 mois.

POURQUOI EN PARLER POUR UN AUDITOIRE PRIVÉ — trois raisons :
A. La stratégie SIGNALE l'orientation fédérale en matière d'IA. Les attentes envers les fournisseurs de l'État découlent largement de cette stratégie.
B. Les organisations privées qui RÉPONDENT AUX APPELS D'OFFRES FÉDÉRAUX sont évaluées selon des critères dérivés de cette stratégie. Comprendre la stratégie, c'est comprendre comment se positionner.
C. La stratégie ESQUISSE le cadre que la prochaine réglementation fédérale pourrait reprendre.

LES QUATRE PRIORITÉS de la stratégie :

PRIORITÉ 1 — EXPERTISE CENTRALISÉE. Création de centres d'expertise IA dans les ministères clés (Patrimoine, Santé, Sécurité publique, Statistique Canada, ESDC). Approche : éviter la dispersion des efforts et créer une masse critique. Implique des programmes de formation, des communautés de pratique, et des standards techniques communs.

PRIORITÉ 2 — INFRASTRUCTURE SÉCURISÉE. Hébergement de l'IA dans des environnements approuvés, conformes aux règles canadiennes de souveraineté des données. Discussion en cours sur la création d'un « cloud souverain » canadien pour l'IA, en parallèle des partenariats avec des fournisseurs internationaux qualifiés. Implications : exigences accrues sur les fournisseurs cloud.

PRIORITÉ 3 — GOUVERNANCE DES DONNÉES. Ouverture des données gouvernementales pour l'entraînement, dans le respect de la vie privée. Inventaire des actifs de données, qualité et représentativité. Articulation avec les obligations de la LPRPDE et des lois provinciales. Investissement dans des techniques de protection (différentielle, anonymisation, données synthétiques).

PRIORITÉ 4 — CONFIANCE DU PUBLIC. Transparence accrue sur l'utilisation de l'IA par l'État. Élargissement du REGISTRE CANADIEN DES SYSTÈMES DÉCISIONNELS AUTOMATISÉS pour inclure davantage de systèmes. Communications proactives, consultations publiques, mécanismes de redressement.

INSTRUMENTS COMPLÉMENTAIRES :
A. RAPPORT DU GROUPE DE TRAVAIL SUR LA STRATÉGIE D'IA — en cours en 2026, dirigé en partie par des figures comme Yoshua Bengio (Canadien, pionnier de l'IA, auteur du International AI Safety Report 2026).
B. SPRINT NATIONAL D'ISDE (résultats publiés 3 février 2026) — consultation auprès du milieu sur les futures orientations.
C. INVESTISSEMENTS dans Mila (Montréal), Vector (Toronto), Amii (Edmonton) — les trois instituts d'IA pancanadiens du programme CIFAR.

POSITIONNEMENT INTERNATIONAL — la stratégie aligne le Canada sur les pratiques de :
A. États-Unis (AI Strategy de l'administration américaine).
B. Royaume-Uni (UK AI Strategy + Data (Use & Access) Act 2025).
C. Singapour (Model AI Governance Framework et programme AI Verify).
D. France (Stratégie nationale française pour l'IA).

ENJEU SOULEVÉ PAR LE WEF (mars 2026) — la transformation organisationnelle par l'IA exige que la GOUVERNANCE soit construite EN AMONT, pas en aval. Le rapport du WEF identifie cinq leviers : expérience client, opérations, R&D, stratégie, talents. La gouvernance de l'IA est traitée comme une PRÉCONDITION transversale, pas comme un module d'audit.

PROBLÈME DOCUMENTÉ par la KPMG Global AI Pulse Survey (avril 2026) et l'enquête de Writer.com : 75 % des dirigeants admettent que leur stratégie d'IA est « plus pour le show » qu'opérationnelle. Forrester prévoit que les entreprises reportent 25 % des budgets IA prévus pour 2026 vers 2027 par manque de capacité d'exécution. La stratégie fédérale canadienne entend EXEMPLIFIER une approche d'exécution mature.

POUR NORD PARADIGM :
A. POSITIONNEMENT DE L'OFFRE — la stratégie fédérale donne le VOCABULAIRE pour parler à des clients de moyenne et grande taille au Canada.
B. APPELS D'OFFRES — connaître la stratégie permet de répondre à des RFP fédéraux et provinciaux de manière crédible.
C. CONNEXION À CIFAR / MILA / AMII — construire des partenariats avec ces institutions pour les missions techniques pointues.

LIMITE — la stratégie est INTERNE à la fonction publique. Elle n'a pas force de loi sur les entreprises privées. Mais elle CRÉE LE CONTEXTE RÉGLEMENTAIRE FUTUR.
        """.strip(),
    },

    "m3_c5_provinces_fragmentation": {
        "module": 3, "ordre": 5, "langue": "fr",
        "titre": "Initiatives provinciales et fragmentation réglementaire",
        "prereqs": ["m3_c1_canada_paysage_federal"],
        "texte": """
En l'absence d'une loi fédérale horizontale sur l'IA, les PROVINCES COMBLENT LE VIDE par des initiatives sectorielles. Cette fragmentation crée une COMPLEXITÉ DE CONFORMITÉ pour toute organisation pancanadienne — chaque province adopte des règles différentes pour des problèmes similaires.

PANORAMA DES INITIATIVES PROVINCIALES (au 25 avril 2026) :

QUÉBEC — LA POSITION D'AVANT-GARDE :
A. Loi 25 (P-39.1) — couvre tout traitement de RP. Articles 8.1 et 12.1 sur les décisions automatisées en vigueur depuis le 22 septembre 2023.
B. CAI Quebec — autorité d'application active, principes IA générative publiés.
C. Plan d'action gouvernemental sur l'IA (en élaboration) — orientations sectorielles santé, éducation, justice.

ONTARIO — RÉGULATION SECTORIELLE EN ACCÉLÉRATION :
A. Workers for Workers Four Act (2026) — exigence de DIVULGATION DE L'IA DANS LES OFFRES D'EMPLOI publiées en Ontario, en vigueur depuis le 1er JANVIER 2026. PREMIÈRE EXIGENCE CANADIENNE DE TRANSPARENCE IA À FORCE DE LOI. Toute offre d'emploi qui utilise un système d'IA pour le tri ou l'évaluation des candidats doit le divulguer dans l'annonce.
B. Enhancing Digital Security and Trust Act (adopté fin 2024) — fixe des exigences de responsabilité pour l'usage de l'IA dans le secteur public ontarien. Règlements d'application encore en attente.
C. Principes IA responsable de l'Ontario (janvier 2026) — Information and Privacy Commissioner of Ontario (IPC) et Ontario Human Rights Commission (OHRC) ont publié conjointement six principes pour l'usage responsable de l'IA dans le secteur public.

COLOMBIE-BRITANNIQUE :
A. Office of the Information and Privacy Commissioner of BC — guidance sur l'IA, en coordination avec l'IPC ontarien.
B. RÈGLEMENTS DE L'OSFI (Bureau du surintendant des institutions financières) sous la Guideline E-23 — encadrent l'usage de l'IA dans les institutions financières. Concerne aussi les institutions hors C.-B. mais avec pleine portée pour les filiales.
C. Cas Zhang (jurisprudence majeure) — voir le concept dédié.

ONTARIO + COLOMBIE-BRITANNIQUE — LIGNES DIRECTRICES CONJOINTES (janvier 2026) :
A. AI Scribes en santé — les commissaires de l'Ontario et de la C.-B. ont publié une GUIDANCE COMMUNE sur l'usage des « scribes IA » (outils qui enregistrent et transcrivent les interactions patient-prestataire). Risques identifiés : confidentialité, consentement, qualité des données, sécurité, vie privée.

ALBERTA, MANITOBA, SASKATCHEWAN — initiatives plus limitées, principalement par adaptation des lois existantes sur la vie privée.

ATLANTIQUE — les lois provinciales sur la vie privée (Nouveau-Brunswick, Nouvelle-Écosse) commencent à intégrer des considérations IA, sans modules dédiés.

CONSÉQUENCE STRATÉGIQUE — DEUX SCÉNARIOS de COÛT DE CONFORMITÉ :

SCÉNARIO 1 — PME LOCALE QUÉBÉCOISE. Concerne uniquement la Loi 25. Coût modéré.

SCÉNARIO 2 — ENTREPRISE PANCANADIENNE. Multi-juridiction : Loi 25 + LPRPDE + Workers for Workers Four Act (Ontario) + Enhancing Digital Security and Trust Act + lignes directrices BC + AI Scribes guidance + sectoriel financier (OSFI E-23) si applicable. La complexité explose.

STRATÉGIE EN ÉMERGENCE — l'« HARMONISATION VERS LE STANDARD LE PLUS ÉLEVÉ ». Identifiée par Fasken Martineau DuMoulin LLP dans son analyse mars 2026 des tendances. Les organisations multi-juridictions adoptent comme baseline le STANDARD APPLICABLE LE PLUS STRICT (typiquement l'EU AI Act pour les organisations exportant en Europe; sinon la Loi 25 et l'Ontario Workers Act pour les organisations canadiennes pures), et l'appliquent à toutes leurs opérations. Avantage : une seule politique, un seul programme d'audit. Inconvénient : sur-conformité sur certaines juridictions.

EXEMPLE PRATIQUE — un éditeur d'outil RH d'IA actif en Ontario et au Québec :
- Au Québec : Loi 25 art. 12.1 (transparence + recours humain pour décisions exclusivement automatisées).
- En Ontario : Workers for Workers Four Act (divulgation dans l'offre d'emploi).
- En Europe : EU AI Act haute risque (Annexe III, emploi).
La stratégie d'harmonisation : adopter le standard EU AI Act haute risque à l'échelle pancanadienne. Cela couvre simultanément les exigences provinciales canadiennes.

VEILLE À MAINTENIR :
A. Évolution de la régulation fédérale (ISDE).
B. Consultations provinciales (Québec — orientation IA en santé; Ontario — règlements de l'Enhancing Digital Security Act; BC — actualisation des règles OSFI E-23).
C. Premières grandes décisions des autorités (CAI Québec, IPC Ontario) sanctionnant des organisations.
D. Coordination internationale via OPC fédéral (joint statements multinationaux).

POUR NORD PARADIGM — la fragmentation est une OPPORTUNITÉ COMMERCIALE. Plus la complexité augmente, plus les PME sans expertise interne ont besoin d'un cabinet de conseil pour les guider. Brèche Pro et Prisme se positionnent précisément sur cette demande.
        """.strip(),
    },

    "m3_c6_jurisprudence_zhang_opc": {
        "module": 3, "ordre": 6, "langue": "fr",
        "titre": "Jurisprudence Zhang (BC) et coordination OPC",
        "prereqs": ["m3_c1_canada_paysage_federal"],
        "texte": """
La jurisprudence canadienne sur l'IA est encore embryonnaire au 25 avril 2026, mais la décision ZHANG en Colombie-Britannique constitue le PREMIER PRÉCÉDENT CANADIEN sur les hallucinations d'IA dans un contexte juridique. Couplée à la coordination internationale via le Commissariat à la protection de la vie privée du Canada (OPC), elle dessine le paysage de la responsabilité émergente.

L'AFFAIRE ZHANG — DÉCISION MARQUANTE EN C.-B.

CONTEXTE — affaire civile en Colombie-Britannique. Un avocat a déposé un avis de demande contenant des AUTORITÉS JURIDIQUES INEXISTANTES, fabriquées par ChatGPT (« hallucinations »). Les autorités citées avaient l'apparence de citations légitimes (noms d'arrêts, numéros, juridictions) mais ne correspondaient à aucune décision réelle.

DÉCISION DE LA COUR :
A. Constatation que les hallucinations juridiques sont « ALARMANTLY PREVALENT » — d'une étude citée : 69 % avec ChatGPT 3.5, 88 % avec Llama 2.
B. Les LLM échouent souvent à corriger les présupposés juridiques erronés des utilisateurs.
C. Les LLM ne peuvent pas toujours prédire quand ils produisent une hallucination.
D. La juge a ORDONNÉ à l'avocate de PAYER PERSONNELLEMENT les frais du client. Les frais ne sont pas absorbés par le cabinet ni par l'assurance professionnelle — c'est une SANCTION PERSONNELLE.

QUESTIONS LAISSÉES EN SUSPENS :
A. La COUR FÉDÉRALE DU CANADA a, en parallèle, émis des EXIGENCES DE VÉRIFICATION ET DE DIVULGATION de l'usage d'outils IA dans les procédures, mais le cadre exact d'autres juridictions provinciales reste à clarifier.
B. La question de savoir si l'usage d'IA pour préparer des documents juridiques doit être DIVULGUÉ AU CLIENT (consentement éclairé) reste ouverte.
C. La question de savoir si la responsabilité personnelle s'étend aux SUPÉRIEURS HIÉRARCHIQUES de l'avocat fautif n'est pas tranchée.

PORTÉE ÉLARGIE DE LA DÉCISION — implications hors du contentieux :

A. POUR LES AVOCATS — toute utilisation d'IA pour la recherche juridique exige une VÉRIFICATION HUMAINE INDÉPENDANTE de chaque citation. Le « j'ai fait confiance à ChatGPT » n'est pas une défense.

B. POUR LES PROFESSIONNELS LIBÉRAUX (médecins, comptables, ingénieurs) — par analogie, les hallucinations dans des avis professionnels engageront probablement la responsabilité personnelle.

C. POUR LES ORGANISATIONS DÉPLOYANT DE L'IA EN INTERNE — la décision Zhang signale qu'on ne peut pas SE CACHER DERRIÈRE L'OUTIL. La responsabilité reste avec l'humain qui utilise et signe.

D. POUR LES FOURNISSEURS D'IA (Anthropic, OpenAI, etc.) — le devoir d'avertissement (« warning ») sur les hallucinations fait partie de la responsabilité produit. Les avertissements génériques (« Claude can make mistakes ») sont probablement INSUFFISANTS pour des usages à enjeux élevés.

E. POUR LE BARREAU DU QUÉBEC ET LES ORDRES PROFESSIONNELS — pression pour adopter des règles déontologiques explicites sur l'usage de l'IA.

COORDINATION INTERNATIONALE VIA L'OPC FÉDÉRAL.

L'OPC (Commissariat à la protection de la vie privée du Canada) est l'autorité fédérale en matière de vie privée (LPRPDE). Il participe activement à la COORDINATION INTERNATIONALE :

ACTION 1 — DÉCLARATION CONJOINTE INTERNATIONALE SUR LES CONTENUS GÉNÉRÉS PAR IA (FÉVRIER 2026). L'OPC s'est joint à environ 60 autorités de protection des données dans le monde (incluant la CNIL, l'EDPB européen, l'ICO britannique, la CAI québécoise) pour publier une déclaration commune sur les implications vie privée des images et vidéos générées par IA. Principes énoncés :
- L'usage d'images de personnes pour entraîner des modèles génératifs requiert une base légale.
- La création d'images de personnes nommées sans consentement est presque toujours illégale.
- Les contenus génératifs doivent être étiquetés.
- Les personnes doivent avoir un mécanisme de recours rapide.

ACTION 2 — COOPÉRATION AVEC LES PROVINCES — l'OPC coopère avec la CAI (Québec), l'IPC (Ontario), l'OIPC (C.-B.) pour harmoniser les approches.

ACTION 3 — ENGAGEMENT AVEC LES FOURNISSEURS DE MODÈLES DE FONDATION — l'OPC suit l'exemple britannique (ICO engageant 11 fournisseurs majeurs) et entame des dialogues avec les fournisseurs principaux.

POUR NORD PARADIGM — TROIS ENSEIGNEMENTS :
1. CONSEILLER AUX CLIENTS de DOCUMENTER l'usage d'IA dans leurs livrables professionnels (avis juridique, rapport médical, expertise technique). La traçabilité est désormais une question de RESPONSABILITÉ PERSONNELLE.
2. INTRODUIRE DANS BRÈCHE PRO un module de questions sur l'usage d'IA dans les fonctions à enjeu (juridique, comptable, médical, RH) — la décision Zhang sert de cas concret.
3. CITER LA DÉCLARATION CONJOINTE OPC dans les recommandations sur les contenus génératifs (étiquetage, consentement, mécanisme de recours).

VEILLE — surveiller :
A. Premières décisions de la CAI ou des tribunaux québécois sur les hallucinations d'IA.
B. Modifications des règles déontologiques du Barreau du Québec et de la CMQ (Collège des médecins).
C. Évolution de la jurisprudence canadienne — d'autres cas similaires sont attendus dans les 12-24 mois.
        """.strip(),
    },

})


# ══════════════════════════════════════════════════════════════════════════════
# MODULE 4 — EU AI ACT  (6 concepts, EN)
# ══════════════════════════════════════════════════════════════════════════════

CURRICULUM.update({

    "m4_c1_eu_ai_act_overview": {
        "module": 4, "ordre": 1, "langue": "en",
        "titre": "EU AI Act — overview and extraterritoriality",
        "prereqs": ["m1_c3_approches_reglementaires"],
        "texte": """
Regulation (EU) 2024/1689, commonly called the EU AI Act, is the world's first comprehensive horizontal AI law. Definitively adopted by the European Parliament on 13 March 2024 and by the Council on 21 May 2024, published in the Official Journal of the European Union on 12 July 2024, entered into force on 1 August 2024. Phased application until 2 August 2027.

LEGAL CHARACTER — it is a REGULATION (not a directive). Important consequence: it applies DIRECTLY in all 27 Member States without requiring transposition law, except for some provisions on national authorities and sanctions where a national margin remains. The regulator is unified at the European level via the AI Office (DG CNECT, European Commission).

STATED OBJECTIVES (recitals):
A. Promote the uptake of trustworthy AI in the internal market.
B. Ensure a high level of protection of health, safety, fundamental rights, democracy, the rule of law, and the environment.
C. Support innovation through legal certainty and regulatory sandboxes.

DEFINITION OF AN « AI SYSTEM » (Art. 3, 1) — aligned with the updated 2023 OECD definition: a machine-based system designed to operate with varying levels of autonomy, that may exhibit adaptiveness after deployment, and that, for explicit or implicit objectives, infers from the input it receives how to generate outputs (predictions, content, recommendations, decisions) that influence physical or virtual environments. Broad definition but excludes traditional purely deterministic software.

SCOPE (Art. 2):
A. PROVIDERS who place an AI system on the EU market or put it into service, wherever they are established.
B. DEPLOYERS established in the EU.
C. PROVIDERS AND DEPLOYERS established outside the EU when the outputs produced by their system are used in the EU.
D. IMPORTERS and DISTRIBUTORS of AI systems in the EU.
E. MANUFACTURERS of products incorporating an AI system and placing it on the market under their own name.
F. AUTHORIZED REPRESENTATIVES in the EU for providers established outside the EU.

EXTRATERRITORIALITY — this is the provision that makes the EU AI Act relevant to Canadian companies. Criterion C above means that a Quebec SME whose AI outputs are used by a European customer must comply, regardless of whether the SME has any physical presence in Europe.

CONCRETE EXAMPLES of extraterritoriality:
A. A Montreal SME sells a candidate-scoring SaaS to a recruitment firm in France. The system's outputs influence hiring in Europe. The SME is a provider under the EU AI Act.
B. A Canadian research institute publishes an open-source model downloadable in Europe and used by European hospitals. Subject to specific obligations for open-source models.
C. A Quebec content moderation platform serves public forums in Europe. The system is likely limited risk (transparency) or high risk depending on use.

SCOPE EXCLUSIONS:
A. AI systems exclusively for military, defence, or national security purposes.
B. Research, development, prototyping activities BEFORE market placement.
C. Individuals using an AI system in the course of personal non-professional activities.
D. Free and open-source components, unless placed on the market or put into service as a high-risk system or systemic-risk GPAI.
E. AI models provided in the context of published scientific research.

FOUR-LEVEL RISK ARCHITECTURE — cornerstone of the regulation:
LEVEL 1 — UNACCEPTABLE RISK → PROHIBITION (Art. 5).
LEVEL 2 — HIGH RISK → HEAVY OBLIGATIONS (Art. 6-49).
LEVEL 3 — LIMITED RISK → TRANSPARENCY OBLIGATIONS (Art. 50, 52).
LEVEL 4 — MINIMAL RISK → NO LEGAL OBLIGATIONS; voluntary codes of conduct.
+ PARALLEL REGIME for general-purpose AI models (GPAI), Art. 51-55, regardless of the risk level of the downstream application.

ARTICULATION WITH THE GDPR — the EU AI Act DOES NOT REPLACE the GDPR. Both regimes coexist. When an AI system processes personal data, the GDPR applies in addition to the EU AI Act. The GDPR governs data processing; the EU AI Act governs the AI system as a regulated object. An AI can be GDPR-compliant but not EU AI Act-compliant, and vice-versa.

INTERNATIONAL POSITIONING — the EU AI Act establishes a DE FACTO GLOBAL STANDARD, as the GDPR did for privacy. International providers often prefer to apply a single (highest) compliance level to their entire customer base rather than manage multiple regimes. « Brussels effect »: European regulation becomes a global norm through commercial diffusion.

ENFORCEMENT READINESS GAP (April 2026) — as of March 2026, only 8 of 27 EU Member States had established single contact points for AI Act enforcement. This indicates significant variance in national implementation readiness and may create coordination uncertainty for organizations operating across multiple Member States.
        """.strip(),
    },

    "m4_c2_eu_ai_act_prohibited": {
        "module": 4, "ordre": 2, "langue": "en",
        "titre": "EU AI Act — prohibited practices (Article 5)",
        "prereqs": ["m4_c1_eu_ai_act_overview"],
        "texte": """
Article 5 of the EU AI Act lists AI practices that are PROHIBITED on EU territory. This article entered into force on 2 February 2025, six months after the Regulation took effect. It represents the UNACCEPTABLE risk category — where no mitigation, no human oversight, no regulatory supervision can render the use acceptable.

PRINCIPLE — the prohibition reflects the idea that some AI uses are by nature incompatible with the EU's fundamental values (human dignity, autonomy, non-discrimination, democracy, rule of law). In these cases, the regulator does not ask « how can this system be used safely? » but « should this system exist? »

DETAILED LIST OF EIGHT PROHIBITED PRACTICES:

PROHIBITION 1 — Cognitive manipulation (Art. 5(1)(a)). System that deploys subliminal techniques beyond a person's consciousness, or manifestly manipulative or deceptive techniques, with the purpose or effect of materially distorting a person's behaviour by causing them to make a decision they would not otherwise make, causing or likely to cause significant harm. Examples: video game interfaces designed to push compulsive purchases by exploiting cognitive biases; chatbots that emotionally manipulate vulnerable persons.

PROHIBITION 2 — Exploitation of vulnerabilities (Art. 5(1)(b)). System that exploits the vulnerabilities of an individual or group due to age, disability, or social/economic situation, with the purpose or effect of materially distorting their behaviour and causing significant harm. Examples: predatory advertising targeting individuals in financial distress; connected toys that manipulate children.

PROHIBITION 3 — Social scoring (Art. 5(1)(c)). Evaluation or classification of persons by public authorities OR on their behalf based on social behaviour or personal characteristics, leading to detrimental treatment in unrelated contexts or disproportionate to the original behaviour. Targeted: Chinese-style social credit systems. Prohibited in Europe whether deployed by the State or on its behalf.

PROHIBITION 4 — Individual criminal risk assessment (Art. 5(1)(d)). System that predicts the likelihood of a specific person committing a crime, based solely on profiling or assessment of personality traits. Exception: systems supporting human assessment based on objective and verifiable facts directly linked to criminal activity. Targeted: COMPAS and similar recidivism prediction systems.

PROHIBITION 5 — Untargeted facial recognition scraping (Art. 5(1)(e)). Creation or expansion of facial recognition databases through untargeted scraping of images from the Internet or CCTV. Targeted: Clearview AI and similar firms. Prohibition covers the act of database building, not just its use.

PROHIBITION 6 — Emotion recognition in workplaces and schools (Art. 5(1)(f)). AI system that infers a person's emotions in workplaces or educational establishments, except for medical or safety reasons. Example targeted: systems that monitor facial expressions of employees in videoconference or students in classrooms.

PROHIBITION 7 — Sensitive biometric categorization (Art. 5(1)(g)). System that categorizes persons based on their biometric data to infer race, political opinion, union membership, religious or philosophical conviction, sex life, or sexual orientation. Narrow exceptions for law enforcement.

PROHIBITION 8 — Real-time remote biometric identification in publicly accessible spaces for law enforcement purposes (Art. 5(1)(h)). The most politically contested and complex prohibition. Three strict exceptions: targeted search for specific victims (kidnapping, trafficking, sexual exploitation of children); prevention of a specific, substantial, imminent threat to life or physical safety; localization or identification of a suspect for a serious offence (closed list). Cumulative conditions: prior judicial authorization, necessity, proportionality, limited duration and area.

TECHNICAL SCOPE — prohibitions target use, not technology per se. A facial recognition model is not prohibited; its DEPLOYMENT for real-time remote biometric identification in publicly accessible spaces for law enforcement IS.

SANCTIONS for Article 5 violations — the most severe in the regulation (Art. 99): up to 35 million EUR OR 7 % of worldwide annual turnover — whichever is HIGHER. More severe than the GDPR maximum (4 %).

IMPLICATIONS FOR QUEBEC — a Quebec provider cannot sell a system that matches one of these practices to a European customer. Nor, since February 2025, can it deploy outputs used in Europe. Compliance requires UPSTREAM FILTERING of system use cases: architecture, customer contracts, terms of use, and technically, geographic kill-switches and API restrictions.

CHECK FOR YOUR PRODUCT: if your AI system performs identification, scoring, profiling, or behavioural manipulation on Europeans, walk through Article 5(1)(a)-(h) and verify NONE applies. If one might apply, design changes or service restriction is required before EU deployment.
        """.strip(),
    },

    "m4_c3_eu_ai_act_high_risk_typology": {
        "module": 4, "ordre": 3, "langue": "en",
        "titre": "EU AI Act — high-risk systems typology",
        "prereqs": ["m4_c1_eu_ai_act_overview"],
        "texte": """
The « high-risk AI system » category is the operational core of the EU AI Act. It is defined by Articles 6 and 7, and concretized by TWO DISTINCT ANNEXES (I and III) listing covered use cases.

TWO ROUTES TO QUALIFY AS HIGH RISK (Art. 6):

ROUTE 1 — ANNEX I: AI systems integrated into PRODUCTS subject to EU harmonization legislation. List covering 12 regulated categories: machinery, toys, lifts, radio equipment, personal protective equipment, medical devices, in vitro diagnostic medical devices, marine equipment, motor vehicles, civil aviation, railways, and certain industrial equipment. Qualification follows product regulation.

ROUTE 2 — ANNEX III: AI systems deployed in specific USE CASES considered high risk regardless of product. This is the new route that most broadly affects non-industrial companies.

ANNEX III — EIGHT DOMAINS of high-risk use cases:

DOMAIN 1 — BIOMETRIC IDENTIFICATION AND CATEGORIZATION not prohibited under Art. 5. Includes remote biometric identification (other than that prohibited at Art. 5(1)(h)) and biometric categorization based on sensitive attributes if not prohibited at Art. 5(1)(g).

DOMAIN 2 — CRITICAL INFRASTRUCTURE. AI used as a safety component in the management and operation of critical digital infrastructure, road traffic, water, gas, heating, electricity supply.

DOMAIN 3 — EDUCATION AND VOCATIONAL TRAINING. Four cases: (1) admission or assignment; (2) learning outcomes evaluation and pathway guidance; (3) appropriate education level evaluation; (4) detection of prohibited behaviour during exams.

DOMAIN 4 — EMPLOYMENT, WORKER MANAGEMENT, AND ACCESS TO SELF-EMPLOYMENT. Two major cases: (1) recruitment, screening, candidate evaluation (CV filtering, automated interviews, video tests); (2) decisions affecting work conditions, promotion, dismissal, task allocation, performance monitoring and evaluation.

DOMAIN 5 — ACCESS TO ESSENTIAL PRIVATE SERVICES and PUBLIC SERVICES AND BENEFITS. Four cases: (1) eligibility for public benefits and essential public services; (2) creditworthiness evaluation and credit scoring (except fraud detection); (3) life and health insurance risk evaluation; (4) emergency call prioritization and medical triage.

DOMAIN 6 — LAW ENFORCEMENT. Six cases covering: assessment of risk of being a victim of crime; polygraphs and similar tools; reliability of evidence; profiling. Strict restrictions on use by police authorities.

DOMAIN 7 — MIGRATION, ASYLUM, AND BORDER CONTROL. Four cases: polygraphs, migration risk assessment, asylum application examination, identification in border management context.

DOMAIN 8 — ADMINISTRATION OF JUSTICE AND DEMOCRATIC PROCESSES. Two cases: (1) supporting judicial decision-making in researching and interpreting facts and law; (2) influence on the result of an election or referendum or on voting behaviour, except purely administrative or logistical systems.

LOW-IMPACT EXEMPTION (Art. 6(3)). An Annex III system can NOT be considered high risk if it does NOT pose significant risk of harm to health, safety, or fundamental rights, because it does not materially influence the outcome of decision-making. Four cumulative conditions:
A. Narrow procedural task (e.g., format transformation).
B. Improvement of the result of a previously completed human activity.
C. Pattern detection or deviation from prior decision-making, without replacing or influencing previously completed human assessment without proper review.
D. Preparatory task to an assessment of relevant cases.

The exemption is delicate to handle: subject to interpretation; the provider must DOCUMENT the justification (Art. 6(4)). Authorities can challenge. If an Annex III system claiming exemption actually performs profiling of natural persons, the exemption does NOT apply — it remains high risk.

ADAPTATION POWER (Art. 7). The European Commission can, by delegated acts, add or modify use cases in Annex III based on listed risk criteria (vulnerability of persons, dependence on outputs, extent of use, etc.). The list is therefore DYNAMIC.

SPECIFIC EXAMPLES FOR A QUEBEC COMPANY:
A. Recruitment SaaS sold in Europe: DOMAIN 4. High risk.
B. Credit scoring platform used by European lenders: DOMAIN 5. High risk.
C. Educational assistant grading European students' work: DOMAIN 3. High risk.
D. Pure fraud detection tool (anti-fraud only, no creditworthiness scoring): explicitly excluded from Domain 5.
E. General-purpose customer service chatbot: not Annex III, so in principle limited risk.

OPERATIONAL CONSEQUENCE — the first decision for any AI provider exposed to the European market is: IS MY SYSTEM IN ANNEX III? If yes, the detailed obligations of Articles 8-49 apply (next concept). The initial mapping is crucial; it conditions the cost and complexity of compliance.
        """.strip(),
    },

    "m4_c4_eu_ai_act_high_risk_obligations": {
        "module": 4, "ordre": 4, "langue": "en",
        "titre": "EU AI Act — high-risk system obligations",
        "prereqs": ["m4_c3_eu_ai_act_high_risk_typology"],
        "texte": """
Once a system is qualified as high risk, Articles 8-49 impose a range of obligations distributed among providers, importers, distributors, and deployers. This is the prescriptive heart of the EU AI Act and the most expensive part to implement.

NINE TECHNICAL AND ORGANIZATIONAL REQUIREMENTS for providers (Art. 8-15):

REQUIREMENT 1 — RISK MANAGEMENT SYSTEM (Art. 9). Continuous and iterative process throughout the lifecycle: identification, estimation, evaluation of known and reasonably foreseeable risks; adoption of appropriate measures; testing; documentation. Must be reviewed regularly.

REQUIREMENT 2 — DATA GOVERNANCE (Art. 10). Training, validation, and test data relevant, representative, free of errors, and complete with respect to the intended purpose. Thorough examination of possible biases. Documented procedures for collection, labelling, aggregation, pre-processing.

REQUIREMENT 3 — TECHNICAL DOCUMENTATION (Art. 11 and Annex IV). Drafted BEFORE market placement, updated thereafter. Annex IV lists 9 mandatory sections: general description, detailed description, human oversight, operation, data used, risk management, modifications, standards used, declaration of conformity.

REQUIREMENT 4 — AUTOMATIC LOGGING (Art. 12). Built-in logging capabilities to ensure traceability of operation throughout the lifetime. Mandatory for biometric systems.

REQUIREMENT 5 — TRANSPARENCY AND INSTRUCTIONS FOR DEPLOYERS (Art. 13). Clear, complete, up-to-date instructions for use: provider identity, expected performance, human oversight measures, required computational resources, expected lifetime, maintenance.

REQUIREMENT 6 — HUMAN OVERSIGHT (Art. 14). The system must be designed to allow effective human oversight. Natural persons in charge must understand capabilities and limitations, monitor operation, correctly interpret outputs, intervene if necessary (« STOP »).

REQUIREMENT 7 — ACCURACY, ROBUSTNESS, CYBERSECURITY (Art. 15). Documented appropriate level of accuracy, resilience to errors and inconsistencies, protection against attacks (data poisoning, model evasion, model inversion).

REQUIREMENT 8 — QUALITY MANAGEMENT SYSTEM (Art. 17). Documented, structurally similar to ISO 9001 + ISO 42001 + ISO 27001 combined.

REQUIREMENT 9 — POST-MARKET MONITORING (Art. 72). Formal plan, continuous data collection on real operation, risk management updates.

ADMINISTRATIVE OBLIGATIONS FOR PROVIDERS:
A. REGISTRATION in the European database for high-risk systems (Art. 49 and 71) before market placement.
B. CONFORMITY ASSESSMENT (Art. 43). Three routes: (1) internal control for most Annex III systems; (2) involving a notified body for some biometric systems; (3) specific modules for systems integrated in regulated products (Annex I).
C. EU DECLARATION OF CONFORMITY and CE MARKING.
D. NOTIFICATION OF SERIOUS INCIDENTS to national authorities.
E. AUTHORIZED REPRESENTATIVE in the EU for non-EU providers (Art. 22).

DEPLOYER OBLIGATIONS (Art. 26):
A. Use the system in accordance with instructions and intended purpose.
B. Assign human oversight to competent persons.
C. Ensure input data is relevant to the intended purpose.
D. Monitor operation and notify incidents to the provider and national authorities.
E. Retain automatically generated logs (Art. 12) for at least 6 months.
F. When the deployer is an employer or provides public services, INFORM affected persons BEFORE the system is put into service.
G. Conduct a FUNDAMENTAL RIGHTS IMPACT ASSESSMENT (FRIA, Art. 27) before deployment, for public deployers or those providing certain essential services.

PRESUMPTION OF CONFORMITY — a system that respects HARMONIZED STANDARDS published by CEN-CENELEC (under finalization as of April 2026) benefits from a presumption of conformity to the corresponding requirements (Art. 40). Practical route to reduce conformity demonstration cost.

ARTICULATION WITH THE GDPR AND LOI 25 — a high-risk system that processes personal data must also satisfy the GDPR (and Loi 25 if deployed in Quebec). The DPIA / EFVP and FRIA can be combined into a single integrated assessment, provided that all dimensions of each framework are covered.

INDICATIVE COST — high-risk system compliance for an SME typically represents 6-18 months of work and from several hundred thousand to several million dollars depending on technical complexity and data scope. This is why some Canadian providers choose NOT to sell certain products in Europe — the market does not justify the cost.

INVESTMENT POSITION for a Quebec SME: above all, RUN A MAPPING to identify whether you are concerned by Annex III. If yes, choose between full compliance and commercial reorientation. If no, verify whether the system enters the transparency obligations (limited risk).
        """.strip(),
    },

    "m4_c5_eu_ai_act_gpai": {
        "module": 4, "ordre": 5, "langue": "en",
        "titre": "EU AI Act — GPAI regime and Code of Practice",
        "prereqs": ["m4_c1_eu_ai_act_overview"],
        "texte": """
The arrival of foundation models (GPT-4, Claude, Gemini, Llama, Mistral) forced European legislators to add, mid-negotiation, a specific regime for GENERAL-PURPOSE AI (GPAI) — Articles 51-55 of the EU AI Act, complemented by Annexes XI to XIII. This regime applies INDEPENDENTLY of the risk level of the downstream application.

DEFINITION OF A GENERAL-PURPOSE AI MODEL (Art. 3, 63) — an AI model, including when trained with a large amount of data using self-supervision at scale, that displays significant generality and is capable of competently performing a wide range of distinct tasks, and that can be integrated into a variety of downstream systems or applications.

TWO CATEGORIES:

CATEGORY A — STANDARD GPAI. Any model that meets the definition but does not reach the systemic-risk threshold. Baseline obligations.

CATEGORY B — GPAI WITH SYSTEMIC RISK (Art. 51). Models with « high-impact capabilities » measured by their training compute, by default at the threshold of 10^25 cumulative floating-point operations (FLOP). At adoption, this threshold corresponded to a small number of models: GPT-4, likely Claude 3 Opus, Gemini Ultra. Threshold may be adjusted by delegated acts. The Commission may also designate additional models via reasoned decision.

OBLIGATIONS FOR ALL GPAI (Art. 53):

A. TECHNICAL DOCUMENTATION per Annex XI: model description (including architecture, parameters, training data in aggregated form), evaluation process, energy consumption, intended uses and restricted uses.
B. INFORMATION FOR DOWNSTREAM INTEGRATORS — provide AI system providers integrating the model with sufficient information to understand capabilities and limitations and to assume their own obligations.
C. EU COPYRIGHT POLICY — including a policy to identify and respect rights reservations expressed via opt-out mechanisms compliant with Article 4(3) of Directive 2019/790.
D. PUBLIC SUFFICIENTLY DETAILED SUMMARY of training data used, per a template provided by the AI Office.

OPEN-SOURCE EXEMPTION (Art. 53(2)). Obligations A and B do NOT apply to open-source models whose parameters, architecture, and usage information are publicly available, except when they are also systemic-risk GPAI. But obligations C (copyright) and D (data summary) always apply.

ADDITIONAL OBLIGATIONS FOR SYSTEMIC-RISK GPAI (Art. 55):

A. MODEL EVALUATION per state-of-the-art protocols and standardized tools, including adversarial testing (« red teaming ») to identify and mitigate systemic risks.
B. EVALUATION AND MITIGATION of EU-level systemic risks arising from development, market placement, or use of the model.
C. TRACKING, DOCUMENTING, AND NOTIFYING without delay to the AI Office and national competent authorities serious incidents and corrective measures.
D. APPROPRIATE LEVEL OF CYBERSECURITY for the model and its physical infrastructure.

CODE OF PRACTICE (Art. 56). The AI Office coordinated the development of a GPAI Code of Practice with FINAL VERSION SUBMITTED TO THE COMMISSION ON 1 APRIL 2026. Adherence to the Code creates a presumption of compliance. Major providers (OpenAI, Anthropic, Google, Meta, Mistral, Cohere) participated in drafting. A SIGNATORY TASKFORCE has been established under the AI Office, chaired by AI Office staff, to facilitate coherent application of the Code across signatories. Active as of April 2026.

For signatories, Commission enforcement will focus on Code adherence monitoring and may treat Code commitments as mitigating factors in fine calculations. Compliance via the Code reduces regulatory uncertainty compared to other routes.

CALENDAR AND ENTRY INTO FORCE:
A. GPAI obligations applicable from 2 AUGUST 2025.
B. Models already on the market before that date benefit from a compliance grace period until 2 August 2027.

VALUE CHAIN KEY CONCEPT — the EU AI Act introduces the distinction between:
A. GPAI MODEL provider (e.g., Anthropic providing Claude).
B. AI SYSTEM provider based on the model (e.g., a Quebec SME building a legal assistant using Claude via the API).
C. SYSTEM DEPLOYER (e.g., the law firm using the assistant).

Each has distinct obligations. The SME integrating Claude into a high-risk system must:
1. Ensure Anthropic provided information compliant with Art. 53(1)(b);
2. Fulfill its own obligations as the high-risk system provider (Art. 16);
3. The deployer law firm applies Art. 26.

This is a chain of responsibilities where each party covers its scope.

WHY THIS REGIME IS CRUCIAL — GPAI models are not themselves limited- or high-risk systems under Art. 6, since they have no specific purpose. Without the GPAI regime, they would have escaped the regulation. Adding this regime closes that loophole and imposes upstream obligations that flow through the entire ecosystem.

POSITIONING for a Canadian SME:
A. If you CONSUME a GPAI model in your product: verify the provider (Anthropic, OpenAI, etc.) provides Art. 53 documentation; keep attestations in your compliance file.
B. If you DEVELOP a proprietary GPAI: this regime applies to you as soon as it is placed on the European market, open-source or not. Documentation, copyright, data summary.
C. If your model crosses the 10^25 FLOP threshold: systemic-risk GPAI regime, very heavy obligations — legal counsel recommended.
        """.strip(),
    },

    "m4_c6_eu_ai_act_sanctions_omnibus": {
        "module": 4, "ordre": 6, "langue": "en",
        "titre": "EU AI Act — sanctions, calendar, Omnibus",
        "prereqs": ["m4_c1_eu_ai_act_overview"],
        "texte": """
The EU AI Act sanctions regime and institutional governance determine the PROBABILITY and COST of non-compliance. These two dimensions are as important as the obligations themselves to calibrate a compliance program.

LAYERED GOVERNANCE — the EU AI Act creates a multi-tier institutional architecture:

EU LEVEL — AI OFFICE. Hosted at DG CNECT of the European Commission, operational since February 2024. Specifically competent for GPAI: investigation, evaluation, sanctions on GPAI providers. Coordination with national authorities. Drafting of codes of practice.

EU LEVEL — EUROPEAN AI BOARD. Composed of Member State representatives. Coordinates, advises the Commission, harmonizes application.

EU LEVEL — ADVISORY FORUM and SCIENTIFIC PANEL OF INDEPENDENT EXPERTS. Provide technical expertise, particularly for systemic-risk GPAI.

NATIONAL LEVEL — NATIONAL COMPETENT AUTHORITIES. Each Member State designates at minimum a market surveillance authority and a notifying authority (for notified bodies). These authorities apply the regulation for systems other than GPAI.

CRITICAL READINESS GAP (April 2026): only 8 of 27 EU Member States had established single contact points for AI Act enforcement. This indicates significant variance in national implementation readiness.

SANCTION CATEGORIES (Art. 99):

CATEGORY 1 — Art. 5 prohibited practices: up to 35 million EUR OR 7 % of total worldwide annual turnover — whichever is HIGHER.

CATEGORY 2 — High-risk system, GPAI, transparency obligation breaches: up to 15 million EUR OR 3 % of worldwide turnover.

CATEGORY 3 — Incorrect, incomplete, or misleading information to authorities: up to 7.5 million EUR OR 1 % of worldwide turnover.

SPECIFIC CATEGORY — SMEs and STARTUPS (Art. 99(6)): caps are calculated taking the LOWER of the two amounts (instead of the higher for large enterprises). Important distinction.

GPAI SANCTIONS (Art. 101). The AI Office may impose on GPAI providers: up to 15 million EUR OR 3 % of worldwide turnover. Detailed procedure including a contradictory phase.

COMPLETE APPLICATION CALENDAR (Art. 113):

A. 1 AUGUST 2024 — Regulation enters into force.
B. 2 FEBRUARY 2025 — applicability of general provisions (Chapter I) and PROHIBITED PRACTICES (Chapter II, Art. 5). Authorities can investigate and sanction Art. 5 practices from this date.
C. 2 AUGUST 2025 — applicability of GPAI rules (Chapter V), governance (Chapter VII), sanctions (Chapter XII partially), notified bodies (Chapter III, Section 4).
D. 2 AUGUST 2026 — applicability of MOST of the regulation, including obligations on Annex III HIGH-RISK SYSTEMS. Pivot date for most companies.
E. 2 AUGUST 2027 — applicability of obligations on high-risk systems integrated in Annex I regulated products (machinery, medical devices, etc.). Final phase.

GPAI models placed on the market BEFORE 2 August 2025 benefit from an additional grace period for full compliance until 2 August 2027 (Art. 111(3)).

THE AI ACT OMNIBUS (Simplification Package, 2026) — CRITICAL PLANNING UPDATE.

The Commission's Digital Omnibus on AI proposes targeted amendments to: reinforce AI Office powers, centralize oversight of GPAI-based systems, reduce governance fragmentation, extend SME and SMC simplifications, and broaden compliance support. Stated purpose is innovation-friendly simplification, not substantive rollback.

TRILOGUE STATUS (as of 1 May 2026): the second political trilogue (Parliament, Council, Commission) on 28 April 2026 ended WITHOUT AGREEMENT. Next trilogue scheduled 13 MAY 2026.

HARD DEADLINE: if the Omnibus is NOT FORMALLY ADOPTED before 2 August 2026, the original high-risk obligations and timeline take effect on that date as drafted.

PLANNING IMPLICATION: organizations exposed to EU high-risk obligations CANNOT delay readiness on the assumption the Omnibus passes. Treat Omnibus relief as contingent until adopted; build to the original 2 August 2026 timeline.

Civil society perspectives are split. Innovation-focused commentators support the package. Rights-focused groups (Jacques Delors Centre, Amnesty International) characterize it as moving in the wrong direction on protections.

RECOURSE OPTIONS — providers and deployers have a right to:
A. Administrative review before the sanctioning authority.
B. Judicial review before national courts (first instance) then Court of Justice of the EU for questions of EU law interpretation.
C. For GPAI sanctioned by the AI Office: review before the General Court of the EU then CJEU.

COMPLIANCE POSTURE SHIFT (April 2026) — signal intelligence indicates a shift from « what is AI? » definitional debates to concrete audit readiness. The defensible posture: build inventory, documentation, model classification, human oversight, and incident-response processes NOW regardless of Omnibus outcome. Organizations that pause compliance programs due to possible timeline changes face enforcement exposure.

INTERACTION WITH OTHER SANCTIONS — the same fact may trigger CUMULATIVELY several regimes:
A. GDPR sanction for unlawful personal data processing.
B. EU AI Act sanction for AI system non-compliance.
C. National consumer-law sanction for unfair commercial practices.
D. Civil action for damages by affected persons.

CUMULATIVE RISK is what motivates investment in robust compliance programs: a single incident can generate parallel proceedings.

FOR A QUEBEC SME — practical math:
A. No European exposure → EU AI Act sanctions don't apply, but reputational risk of known non-compliance remains.
B. European exposure → maximum sanction often exceeds contract value. Cyber insurers increasingly require compliance demonstration before insuring AI risks.
C. EU market presence → registration in the EU database and authorized representative designation are concrete administrative obligations to plan.
        """.strip(),
    },

})


# ══════════════════════════════════════════════════════════════════════════════
# MODULE 5 — NIST AI RISK MANAGEMENT FRAMEWORK  (5 concepts, EN)
# ══════════════════════════════════════════════════════════════════════════════

CURRICULUM.update({

    "m5_c1_nist_rmf_origin_structure": {
        "module": 5, "ordre": 1, "langue": "en",
        "titre": "NIST AI RMF — origin, structure, voluntary status",
        "prereqs": ["m1_c3_approches_reglementaires"],
        "texte": """
The NIST AI Risk Management Framework (AI RMF 1.0) is the leading operational reference framework for AI risk management in the United States. Published by the National Institute of Standards and Technology on 26 JANUARY 2023, it constitutes the first major structured framework in the U.S. on the subject.

GENESIS — the AI RMF was mandated by the NATIONAL AI INITIATIVE ACT OF 2020 (Title LI of Public Law 116-283), which specifically charged NIST with developing a voluntary framework for AI risk management. Development period: 2021-2023, with extensive public consultation (workshops, successive drafts, comments from hundreds of organizations).

LEGAL STATUS — VOLUNTARY. The RMF has no binding force in itself. It does not create legal obligations. But this qualification is misleading for three reasons:

A. STATE OF THE ART — the RMF is widely recognized as the operational reference. An organization that ignores its recommendations exposes itself to negligence claims in case of incident.
B. REGULATORY REFERENCE — several U.S. sectoral laws (Equal Employment Opportunity Commission, Consumer Financial Protection Bureau) refer to the RMF in their guidelines.
C. COMMERCIAL REQUIREMENT — increasingly, RFPs, B2B contracts, and vendor evaluations require demonstration of RMF conformity. Cyber insurance carriers are starting to require it.

PHILOSOPHY — the RMF takes a classic RISK-MANAGEMENT approach (Plan-Do-Check-Act) rather than a prescriptive one. It does not say « do X »; it says « identify risks, measure them, manage them according to your context. » This flexibility is its strength and its weakness: it allows sector adaptation but leaves organizations with substantial design effort.

TWO-PART STRUCTURE:

PART 1 — FOUNDATIONS (« Foundational Information »). Presents the conceptual framework: what is an AI risk? Why manage it? What characteristics define trustworthy AI?

PART 2 — CORE. Describes the functions and categories of actions to implement. Four functions: GOVERN, MAP, MEASURE, MANAGE.

PROFILES — NIST has published several application profiles adapting the RMF to specific contexts:
A. NIST AI RMF GENERATIVE AI PROFILE (NIST AI 600-1), July 2024 — adaptation to generative AI.
B. NIST AI RMF CRITICAL INFRASTRUCTURE PROFILE (concept note April 2026) — sectoral guidance for AI in IT, OT, and ICS environments.

COMPLEMENTARY PUBLICATIONS — beyond the RMF itself, NIST publishes a wide range of documents:
A. NIST SP 1270 — guide on biases in AI.
B. NIST AI 100-1 — explainability.
C. NIST AI 100-3 — taxonomy of AI concepts.
D. NIST IR 8312 — evaluation characteristics.
E. NIST IR 8596 (draft Dec 2025) — Cyber AI Profile, mapping CSF 2.0 to AI security adoption.
F. NIST GCR 26-069 (January 2026) — framework for evaluating whether AI standards achieve their stated goals of promoting innovation and public trust.

These documents are freely available and constitute an operational reference library.

DIFFERENCE WITH ISO/IEC 42001 — the RMF is an OPERATIONAL FRAMEWORK, ISO 42001 is a MANAGEMENT STANDARD. The RMF says HOW to manage technical and organizational risks day-to-day; ISO 42001 says how to STRUCTURE the organization to do it in an audited and certifiable way. Both are complementary.

INTERNATIONAL POSITION — although American by origin, the RMF has worldwide influence. Most major sectoral governance frameworks emerging since 2023 (banking, health, defence) reference it. Canadian, Australian, British, Japanese, Brazilian regulators use it as a thought matrix. The RMF is interoperable with the OECD Principles (explicit alignment in the text).

UPDATE CYCLE — NIST anticipates regular revisions. Version 1.0 remains the stable reference; additions come via « profiles » and complementary publications rather than structural overhauls. This stability is an asset for organizations investing in the RMF.

GSA-NIST AI EVALUATION STANDARDS PARTNERSHIP (March 2026) — GSA and NIST announced a joint initiative to develop practical evaluation standards for AI tools in federal government operations. This shifts the ecosystem from abstract risk management to procurement-ready assessment criteria. It signals maturation of the NIST AI governance ecosystem from voluntary frameworks to operational evaluation tools.

NIST AI AGENT STANDARDS INITIATIVE (February 2026) — NIST announced an initiative to establish standards for interoperable and secure AI agent systems, responding to rapid enterprise deployment of agentic AI. This complements the broader AI RMF by addressing specific challenges of autonomous systems (covered in detail in M11).

FOR A QUEBEC SME — why adopt the RMF:
A. FREE — no licensing fee, no mandatory audit.
B. PROVEN STRUCTURE — tested by hundreds of thousands of organizations.
C. ALIGNMENT — covers Loi 25 implicit expectations (governance, EFVP, transparency, oversight), Canadian voluntary code principles, and 70-80 % of probable obligations of any future federal Canadian AI law.
D. MARKET SIGNAL — provider of a credibility signal in RFPs.
E. DOCUMENTATION — provides templates and examples to start fast.

LIMITATION — the RMF is NOT a substitute for legal compliance. Following the RMF without conducting an EFVP under Loi 25 is not enough for Quebec compliance. The RMF is an OPERATIONAL TOOL, not a legal framework.
        """.strip(),
    },

    "m5_c2_nist_rmf_trustworthy_characteristics": {
        "module": 5, "ordre": 2, "langue": "en",
        "titre": "NIST AI RMF — seven characteristics of trustworthy AI",
        "prereqs": ["m5_c1_nist_rmf_origin_structure"],
        "texte": """
Part 1 of the NIST AI RMF identifies SEVEN CHARACTERISTICS that define a « trustworthy AI ». These characteristics are the CONCEPTUAL COMPASS of the framework: every action of the GOVERN-MAP-MEASURE-MANAGE functions ultimately aims to strengthen or balance them.

PRINCIPLE OF BALANCE — the seven characteristics are sometimes in TENSION with each other. Maximizing transparency can compromise security (exposing vulnerabilities). Maximizing fairness can decrease overall accuracy. The RMF does not provide a recipe for resolving these tensions; it requires that they be MADE EXPLICIT and CONSCIOUSLY ARBITRATED.

THE SEVEN CHARACTERISTICS (numbered 3.1 to 3.7 in the RMF):

CHARACTERISTIC 1 — VALID AND RELIABLE.
Definition: the AI system produces outputs that conform to its intended purpose (validity) and remain stable and accurate under varied conditions (reliability).
Measures: error rates, true positive/negative rates, robustness measures against drift, out-of-distribution accuracy.
Failure examples: medical chatbot giving correct information 95% of the time but hallucinating on critical cases; scoring model that degrades silently when data distribution shifts.

CHARACTERISTIC 2 — SAFE.
Definition: the system should not, under defined conditions, lead to a state where human life, health, property, or the environment are endangered.
Measures: formal analyses, adversarial simulations, fail-safes, kill switches.
Examples: autonomous vehicles, collaborative robots, medical AI, industrial control.

CHARACTERISTIC 3 — SECURE AND RESILIENT.
Definition: the system resists attacks (data poisoning, prompt injection, model evasion, model extraction) and continues to operate correctly under unforeseen disturbances.
Measures: penetration testing, red teaming, conformity to cyber standards (ISO 27001, NIST CSF 2.0).
Note: the boundary between safety and security blurs for AI — a system that is safe under normal conditions can become dangerous under attack.

CHARACTERISTIC 4 — ACCOUNTABLE AND TRANSPARENT.
Definition: it is possible to identify who is responsible for the system at each stage, and the general logic of the system is documented.
Measures: decision logs, technical documentation, governance models, contractual responsibility chains.
Note: accountability is ORGANIZATIONAL; transparency is INFORMATIONAL. Both are necessary.

CHARACTERISTIC 5 — EXPLAINABLE AND INTERPRETABLE.
Definition: a human affected by a decision can obtain an intelligible explanation, and the internal mechanism of the system can be inspected by an expert.
Measures: SHAP values, LIME, attention maps, counterfactuals, model cards.
Distinction: EXPLAINABILITY addresses affected persons (« why was this decision applied to me? »); INTERPRETABILITY addresses experts (« how does this model work? »).

CHARACTERISTIC 6 — PRIVACY-ENHANCED.
Definition: the system respects privacy expectations throughout its lifecycle, prioritizing advanced protection techniques.
Measures: differential privacy, federated learning, anonymization, data minimization, secure multiparty computation.
Direct link to Loi 25 and GDPR: regulatory privacy compliance is integral to this characteristic.

CHARACTERISTIC 7 — FAIR WITH HARMFUL BIAS MANAGED.
Definition: the system operates without introducing or amplifying unfair harms, particularly toward protected or vulnerable groups.
Measures: disparate impact analyses, subgroup tests, independent audits, training data balancing.
CRUCIAL DISTINCTION — there is NOT ONE single fairness: disparate impact, equality of odds, demographic parity, individual fairness are mutually incompatible in most cases. You must EXPLICITLY CHOOSE which notion of fairness the system targets — a documented and justified choice.

OPERATIONAL USE — for each AI use case, the organization must:
A. EXPLICIT which characteristics are priority for this context. A medical triage model prioritizes validity-reliability-safety-fairness; a general-purpose virtual assistant prioritizes transparency-privacy-fairness.
B. DEFINE OPERATIONAL METRICS for each priority characteristic.
C. ESTABLISH ACCEPTABILITY THRESHOLDS; below, the system is not deployed.
D. DOCUMENT TENSIONS between characteristics and the trade-offs made (e.g., « to reach 90 % overall accuracy, we tolerate a 3-point gap between groups A and B; this gap is acceptable in light of [justification] »).
E. PERIODICALLY REVIEW as the system evolves and risk understanding sharpens.

ALIGNMENT WITH OECD AND EU AI ACT — the seven NIST characteristics map finely onto OECD principles and onto the technical requirements of the EU AI Act (Art. 9-15). A system compliant with the RMF is in very good position to demonstrate compliance with the other two frameworks, provided that specific formalities (documentation, certification, etc.) are respected.
        """.strip(),
    },

    "m5_c3_nist_rmf_govern_map_measure_manage": {
        "module": 5, "ordre": 3, "langue": "en",
        "titre": "NIST AI RMF — GOVERN, MAP, MEASURE, MANAGE",
        "prereqs": ["m5_c2_nist_rmf_trustworthy_characteristics"],
        "texte": """
Part 2 of the NIST AI RMF — the « Core » — describes concrete actions to take via FOUR INTERDEPENDENT FUNCTIONS: GOVERN, MAP, MEASURE, MANAGE. Each function is subdivided into CATEGORIES, themselves subdivided into SUBCATEGORIES (operational actions). In total, the Core contains 19 categories and approximately 70 subcategories.

OVERALL LOGIC — the four functions are not sequential but ITERATIVE. GOVERN is the permanent context; MAP, MEASURE, MANAGE form a cycle that repeats throughout the AI system's lifecycle.

FUNCTION 1 — GOVERN (« Cultivate a culture of AI risk management »).
This is the TRANSVERSAL and PERMANENT function. It establishes the organizational conditions for the other three functions to operate correctly.

Six main categories:
GOVERN 1 — Policies, processes, procedures, and practices are in place for risk management.
GOVERN 2 — Responsibilities are defined and documented (RACI). Personnel trained.
GOVERN 3 — Diversity, equity, accessibility considered in team composition.
GOVERN 4 — Stakeholder engagement (affected, users, external experts).
GOVERN 5 — Third-party and supply-chain risk management process.
GOVERN 6 — Risk management of the AI value chain integrated into overall enterprise governance.

Concrete examples: AI policy approved by the board; monthly multidisciplinary AI committee (technical, legal, compliance, business); annual training program for AI-developing or -using personnel; governance requirements in contracts with AI providers.

FUNCTION 2 — MAP (« Frame context and identify risks »).
Applies to each SPECIFIC AI system. Aims to understand WHY we are building this system, FOR WHOM, in WHAT CONTEXT.

Five main categories:
MAP 1 — Context established: purpose, stakeholders, intended and unintended use cases, assumptions.
MAP 2 — AI system categorization based on technical characteristics.
MAP 3 — Capabilities, uses, objectives, and expected benefits documented.
MAP 4 — Risks and benefits mapped onto the seven characteristics of trustworthy AI.
MAP 5 — Impacts on individuals, groups, communities, organizations, society identified.

Typical tools: scoping workshops, impact matrices, affected-user personas, scenario analysis, sectoral risk lists.

FUNCTION 3 — MEASURE (« Evaluate, analyze, track risks »).
Quantify or qualify the risks identified in MAP. Without MEASURE, you don't know whether risks are major or marginal.

Four main categories:
MEASURE 1 — Appropriate methods identified and applied.
MEASURE 2 — Trustworthy AI characteristics evaluated.
MEASURE 3 — Mechanisms in place to track risks over time.
MEASURE 4 — Operator and affected-party feedback integrated.

Typical tools: validation tests, bias audits, red teaming, A/B tests, performance indicators by subgroup, continuous drift monitoring, user feedback mechanisms.

FUNCTION 4 — MANAGE (« Prioritize, treat, communicate risks »).
Allocate resources to address risks evaluated in MEASURE.

Four main categories:
MANAGE 1 — AI risks prioritized based on assessments.
MANAGE 2 — Risks treated according to context, capabilities, and strategy.
MANAGE 3 — Residual risks documented and communicated.
MANAGE 4 — Risks monitored and processes improved.

Typical risk-treatment approaches:
A. AVOID — do not develop or deploy the system.
B. TRANSFER — insurance, subcontracting with contractual commitments.
C. REDUCE — technical mitigations (filtering, retraining, monitoring) and organizational (training, procedures).
D. ACCEPT — residual risk documented and accepted by the competent authority.

TYPICAL OPERATIONAL CYCLE for a new AI project:
STEP 1 — GOVERN: verify that AI policy, roles, and training are in place BEFORE starting.
STEP 2 — MAP: scoping workshop with stakeholders; identify purpose, context, preliminary risks.
STEP 3 — MEASURE: pre-deployment tests on priority characteristics.
STEP 4 — MANAGE: arbitration review; GO / NO-GO decision; mitigations to put in place.
STEP 5 — Deployment.
STEP 6 — Post-deployment: continuous MEASURE (monitoring); continuous MANAGE (mitigation updates); MAP revised if context changes.

INTERACTION WITH ISO 42001 — the RMF is INCORPORATABLE into an ISO 42001 management system. ISO's HLS structure (Plan-Do-Check-Act) serves as an organizational governance frame (extended equivalent of GOVERN), while MAP-MEASURE-MANAGE feed into ISO operational processes. An organization can thus present its (certified) ISO 42001 compliance pointing to its RMF implementation (operational method).

ARTIFACTS PRODUCED by an organization seriously implementing the RMF:
A. Enterprise AI POLICY.
B. INVENTORY of AI systems.
C. IMPACT ASSESSMENTS per system (MAP).
D. TEST and METRICS reports (MEASURE).
E. RISK REGISTER and treatment plans (MANAGE).
F. Periodic reports to the AI committee and board.
G. Training materials and annual reviews.

FOR A QUEBEC SME — PRAGMATIC 90-DAY START:
- Weeks 1-2: adopt a one-page AI POLICY; appoint an AI LEAD (could be the RPRP).
- Weeks 3-6: INVENTORY all AI systems in service or under development.
- Weeks 7-10: rapid MAP and MEASURE on the 2-3 most-risky systems.
- Weeks 11-13: MANAGE — mitigation decisions; monitoring setup.
- Month 4+: industrialization, training, annual internal audits.
        """.strip(),
    },

    "m5_c4_nist_genai_profile": {
        "module": 5, "ordre": 4, "langue": "en",
        "titre": "NIST GenAI Profile — adapting the RMF to generative AI",
        "prereqs": ["m5_c3_nist_rmf_govern_map_measure_manage"],
        "texte": """
NIST AI 600-1 (« Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile »), published 26 July 2024, adapts the RMF to the specifics of generative AI. It was developed pursuant to Executive Order 14110 (October 2023) and is to date the most important sectoral profile of the RMF.

WHY A DEDICATED PROFILE — generative AI poses risks that classical predictive AI systems do not pose, or poses them at a qualitatively different scale. These risks require specific mitigations that the base RMF covers insufficiently.

THE TWELVE GEN-AI-SPECIFIC RISKS identified by the profile:

RISK 1 — CBRN INFORMATION (Chemical, Biological, Radiological, Nuclear). Generative AI can facilitate the production of dangerous weapons or agents by synthesizing knowledge previously compartmentalized in specialized publications. Mitigations: prompt filtering, refusal of high-risk outputs, model access limitation.

RISK 2 — CONFABULATION (« hallucination »). Confident production of factually incorrect content. One of the most systemic risks. Mitigations: grounding via retrieval (RAG), citations, explicit uncertainty indication, user training.

RISK 3 — DANGEROUS, VIOLENT, OR HATEFUL CONTENT. Generation of violent, harassing, non-consensually sexualized, or terrorist content. Mitigations: classifier-based filtering, red teaming, in-line moderation.

RISK 4 — PERSONALLY IDENTIFIABLE INFORMATION (PII) IN OUTPUTS. The model may reproduce personal data seen during training. Mitigations: differential privacy at training, output filtering, on-request deletion.

RISK 5 — INFORMATION INTEGRITY. Disinformation, misinformation, automated propaganda at scale. Mitigations: watermarking, content provenance, narrative coherence, platform partnerships.

RISK 6 — ENVIRONMENTAL IMPACTS. Massive energy consumption of training and inference, water consumption for cooling. Mitigations: footprint transparency, optimization, cloud provider choice.

RISK 7 — HUMAN LABOUR IMPACTS. Deskilling, deresponsibilization, mental health harm. Mitigations: human-centered design, training, ethical guardrails.

RISK 8 — MISLEADING OR DECEPTIVE INFORMATION (« deepfakes », identity impersonation). Mitigations: cryptographic authentication, watermarking, allowlists of trusted sources.

RISK 9 — INTELLECTUAL PROPERTY VIOLATION. Output that substantially reproduces protected works. Mitigations: contractualized training sources, opt-out, citations, retraction mechanisms.

RISK 10 — OBSCENE CONTENT INVOLVING MINORS (CSAM). Zero tolerance. Mitigations: hard filtering, NCMEC reporting, auditable retention, moderator training.

RISK 11 — CYBER ABUSE. Social engineering, malicious code generation, phishing automation. Mitigations: refusal of offensive use cases, API monitoring.

RISK 12 — DANGERS OF OVER-RELIANCE (« automation bias »). Excessive trust in AI outputs, loss of human expertise. Mitigations: built-in skepticism mechanisms, requirement of human authority, training in critical evaluation.

RECOMMENDED ACTIONS by the profile — reorganized over the four RMF functions:

GOVERN ADAPTED:
A. GenAI policy distinct from general AI policy.
B. Ethics committee with authority to block a deployment.
C. Public commitment on responsible use.
D. Evaluation of GPAI model providers (documentation quality, transparency).

MAP ADAPTED:
A. Identification of high-risk use cases (CBRN, manipulation, dignity harm).
B. Mapping of dependencies on external proprietary models.
C. Abuse-scenario modelling (« threat modeling »).

MEASURE ADAPTED:
A. Robustness tests against adversarial prompts (jailbreaks).
B. Systematic output evaluation via continuous red teaming.
C. Quantitative metrics on the 12 risks (hallucination rate, refusal rate, PII leakage rate).
D. Bias evaluation in generated outputs.

MANAGE ADAPTED:
A. Immediate disabling mechanisms (kill switches).
B. Accelerated incident notification protocols (24-72 hours).
C. Coordinated communication with users and authorities.
D. Incident documentation for continuous improvement.

ARTICULATION WITH THE EU AI ACT (GPAI regime) — the NIST GenAI profile and the EU AI Act GPAI regime overlap substantially. An organization implementing the NIST profile already covers most operational GPAI obligations (specific EU AI Act administrative obligations remain to be added).

FOR A GENERATIVE AI INTEGRATOR (typical case of a Quebec SME building a product based on Claude, GPT, or an open-source model):
A. EVALUATE the model provider (Anthropic, OpenAI, etc.) on its own GAI practices.
B. DELIMIT use cases your product allows and prohibits (acceptable-use policy).
C. FILTER upstream (prompt validation) and downstream (output validation).
D. INFORM users about the generative-AI nature of the product, its limits, expected error rate.
E. CONTINUOUSLY MONITOR problematic use cases.
F. RESPOND quickly to incidents and reports.

LIMITATIONS OF THE PROFILE — the GAI profile is voluntary and general. It does not substitute for sector-specific requirements (health, finance, defence). It will evolve with state of the art; consult NIST updates regularly.
        """.strip(),
    },

    "m5_c5_nist_extensions_2026": {
        "module": 5, "ordre": 5, "langue": "en",
        "titre": "NIST 2026 extensions — Critical Infrastructure, Agents, Evaluation",
        "prereqs": ["m5_c1_nist_rmf_origin_structure"],
        "texte": """
In 2025-2026, NIST has substantially extended the AI RMF ecosystem with three complementary strands: a CRITICAL INFRASTRUCTURE PROFILE, an AI AGENT STANDARDS INITIATIVE, and EVALUATION FRAMEWORKS. Together they signal that NIST is moving from « voluntary framework » to « operational toolkit ready for procurement and enforcement integration. »

STRAND 1 — CRITICAL INFRASTRUCTURE PROFILE (concept note 7 April 2026).

CONTEXT — AI is increasingly used as a safety component in critical infrastructure: power grids, water treatment, transportation, hospitals, telecommunications, financial systems. The base RMF was not specific enough to address the unique requirements of IT (information technology), OT (operational technology), and ICS (industrial control systems) environments.

OBJECTIVES OF THE PROFILE:
A. Adapt the seven trustworthy characteristics to OT/ICS realities (where reliability and safety dominate, not necessarily explainability).
B. Address the convergence between cyber and AI risks in industrial contexts.
C. Provide a SECTORAL VOCABULARY shared among AI vendors, infrastructure operators, and regulators (FERC, NERC, EPA, etc.).
D. Align with the NIST CYBERSECURITY FRAMEWORK 2.0 (CSF 2.0) used in critical infrastructure.

KEY CHARACTERISTICS of the profile (still in development as of April 2026):
A. STRONG EMPHASIS on safety-critical considerations (the « Safe » characteristic is dominant).
B. INTEGRATED with the NIST CYBER AI PROFILE (NIST IR 8596, December 2025 draft) for the cyber dimension.
C. COVERAGE of supply-chain risks (pre-trained model components, third-party data).
D. REQUIREMENT for high-resilience monitoring (drift, adversarial inputs).

POSITIONING for a Canadian SME — the Critical Infrastructure Profile is relevant for organizations selling AI to:
A. Energy sector clients (Hydro-Québec, Énergir, etc.).
B. Telecom operators.
C. Hospital networks.
D. Water utilities.
E. Transport agencies (STM, RTM, AMT).

In Canada, OSFI (Office of the Superintendent of Financial Institutions) is moving in a similar direction with its E-23 Guideline on AI in financial institutions, which can be read as a Canadian sectoral analog.

STRAND 2 — AI AGENT STANDARDS INITIATIVE (announced February 2026).

CONTEXT — agentic AI (autonomous AI agents that act with minimal human supervision) emerged as a distinct technology category in 2024-2025. The base RMF assumed human-in-the-loop oversight, which is reduced or absent in agentic deployments. NIST responded with a dedicated initiative.

OBJECTIVES:
A. Establish standards for INTEROPERABLE AND SECURE AI agent systems.
B. Address risks specific to autonomy: emergent behaviour, unintended actions, system access scope creep, accountability dilution.
C. Coordinate with international efforts (Singapore Model AI Governance Framework for Agentic AI, January 2026; Microsoft Agent Governance Toolkit, April 2026).

This initiative does NOT replace the AI RMF; it COMPLEMENTS it for agent-specific challenges. Detailed coverage in M11.

POSITIONING — the NIST agent standards initiative signals that agentic AI is moving from ad-hoc guidance to formal standardization. Organizations deploying agents now have an emerging vocabulary aligned with the broader AI RMF.

STRAND 3 — EVALUATION FRAMEWORKS.

NIST has released two key documents in 2025-2026:

A. NIST GCR 26-069 « EVALUATING AI STANDARDS DEVELOPMENT » (15 January 2026). Authored by Dr. Julia Lane (NYU). Proposes a THEORY-OF-CHANGE METHODOLOGY for evaluating whether AI standards achieve their stated goals (innovation, public trust). Notable criticism received: the framework does not adequately address adversarial environments, limiting its ability to evaluate security effectiveness. Feedback channel: ai-standards@nist.gov.

B. GSA-NIST AI EVALUATION STANDARDS FOR FEDERAL OPERATIONS (announcement March 2026). Joint initiative between GSA (General Services Administration) and NIST to develop practical evaluation standards for AI tools in federal government operations. Shifts the ecosystem from abstract risk management to PROCUREMENT-READY ASSESSMENT CRITERIA. Federal agencies will use these to evaluate AI vendors during contract awards.

PROCUREMENT IMPLICATION — once these criteria are formalized, all U.S. federal RFPs will include AI evaluation requirements derived from them. Canadian companies bidding on federal contracts (or on contracts with U.S.-affiliated companies) should align their compliance documentation with these emerging criteria.

CONSEQUENCE FOR NORD PARADIGM — these three strands signal that the NIST ecosystem is consolidating into:
A. THE FRAMEWORK (RMF 1.0) — base reference.
B. SECTORAL PROFILES (GenAI, Critical Infrastructure, Agents) — adaptations.
C. EVALUATION TOOLS — practical assessment for procurement and audit.

This consolidation makes NIST a STRONGER ANCHOR for client engagements than it was in 2023-2024. Recommendation: structure Brèche Pro and Prisme assessments around the NIST RMF + applicable sectoral profile, plus reference to the evaluation criteria as future-proofing.

PROSPECTS — by 2027-2028, NIST is likely to release a RMF version 2.0 incorporating learnings from the profiles. Organizations building today on RMF 1.0 should have a smooth migration path.
        """.strip(),
    },

})


# ══════════════════════════════════════════════════════════════════════════════
# MODULE 6 — ISO/IEC 42001 — SYSTÈME DE MANAGEMENT DE L'IA  (3 concepts, FR)
# ══════════════════════════════════════════════════════════════════════════════

CURRICULUM.update({

    "m6_c1_iso42001_norme_certifiable": {
        "module": 6, "ordre": 1, "langue": "fr",
        "titre": "ISO/IEC 42001 — norme de management certifiable",
        "prereqs": ["m1_c2_typologie_outils"],
        "texte": """
ISO/IEC 42001:2023 est la PREMIÈRE NORME INTERNATIONALE CERTIFIABLE pour les systèmes de management de l'IA. Publiée le 18 décembre 2023 conjointement par l'ISO et la CEI (Commission électrotechnique internationale), elle marque l'arrivée de l'IA dans la famille des normes de management aux côtés d'ISO 9001 (qualité, 1987), ISO 14001 (environnement, 1996), ISO 27001 (sécurité, 2005) et ISO 27701 (vie privée, 2019).

NATURE — c'est une NORME DE MANAGEMENT, pas une norme technique. Elle ne dit PAS comment construire un modèle d'IA performant; elle dit comment STRUCTURER UNE ORGANISATION pour gérer l'IA de façon responsable, mesurable et auditable.

CONCEPT CLÉ — l'AIMS (« AI Management System ») — système de management de l'IA. C'est le périmètre couvert par la norme : politiques, processus, ressources, contrôles utilisés pour gérer l'IA de manière intégrée à la stratégie de l'organisation.

STATUT JURIDIQUE — VOLONTAIRE. Aucune obligation légale d'être certifié. Mais :
A. Plusieurs régulateurs (en particulier l'EU AI Act) accepteront probablement la certification ISO 42001 comme PRÉSOMPTION DE CONFORMITÉ partielle aux exigences techniques.
B. Le marché B2B exige de plus en plus une certification ISO 42001 dans les appels d'offres, comme il exige déjà ISO 27001 pour la sécurité.
C. Les assureurs cyber tarifient à la baisse les organisations certifiées.

STRUCTURE EN HIGH-LEVEL STRUCTURE (HLS) — comme toutes les normes de management ISO modernes, ISO 42001 suit le modèle Plan-Do-Check-Act et la structure HLS commune. Cela permet l'INTÉGRATION avec d'autres systèmes de management que l'organisation pourrait déjà avoir (qualité, sécurité, vie privée, environnement).

LES 10 CHAPITRES PRINCIPAUX (numérotation HLS standard) :

CHAPITRE 1 — Domaine d'application.
CHAPITRE 2 — Références normatives.
CHAPITRE 3 — Termes et définitions (renvoie à ISO/IEC 22989).
CHAPITRE 4 — CONTEXTE DE L'ORGANISATION. Comprendre l'environnement interne et externe, identifier les parties intéressées, définir le périmètre de l'AIMS.
CHAPITRE 5 — LEADERSHIP. Engagement de la direction, politique d'IA, rôles et responsabilités. La direction doit OBJECTIVEMENT s'engager.
CHAPITRE 6 — PLANIFICATION. Identification des risques et opportunités, objectifs de l'AIMS, planification des changements.
CHAPITRE 7 — SUPPORT. Ressources, compétences, sensibilisation, communication, information documentée.
CHAPITRE 8 — OPÉRATION. Planification et contrôle opérationnels, évaluation des incidences, gestion du cycle de vie des systèmes d'IA.
CHAPITRE 9 — ÉVALUATION DE LA PERFORMANCE. Surveillance, mesure, analyse, audits internes, revue de direction.
CHAPITRE 10 — AMÉLIORATION. Non-conformités, actions correctives, amélioration continue.

PRINCIPE CARDINAL — Plan-Do-Check-Act (PDCA) :
PLAN — Chap. 4-7 : poser les fondations, planifier.
DO — Chap. 8 : exécuter les opérations.
CHECK — Chap. 9 : évaluer la performance.
ACT — Chap. 10 : améliorer en continu.

PROCESSUS DE CERTIFICATION — typiquement en cinq phases :
PHASE 1 — DIAGNOSTIC INITIAL (« gap analysis »). 1-2 semaines pour identifier l'écart entre l'état actuel et les exigences ISO 42001.
PHASE 2 — IMPLÉMENTATION. 3-12 mois selon la maturité de départ. Mise en place des politiques, procédures, contrôles, formation.
PHASE 3 — AUDIT INTERNE. L'organisation s'audite elle-même pour identifier les non-conformités.
PHASE 4 — AUDIT DE CERTIFICATION par un organisme accrédité. Deux étapes : Stage 1 (revue documentaire) + Stage 2 (audit terrain). Pour une PME, environ 5-10 jours-homme d'auditeur.
PHASE 5 — SURVEILLANCE et RECERTIFICATION. Audits de surveillance annuels; recertification complète tous les 3 ans.

COÛT — pour une PME québécoise, la certification représente typiquement :
A. Implémentation interne : 6-12 mois × 0,3-1,0 ETP × salaire chargé = 50 000 $ à 150 000 $ d'effort interne.
B. Conseil externe (souvent nécessaire au début) : 30 000 $ à 100 000 $.
C. Audit de certification : 15 000 $ à 40 000 $ pour une PME.
D. Surveillance annuelle : 8 000 $ à 20 000 $.
TOTAL d'entrée : 100 000 $ à 290 000 $; coût annuel récurrent : 8 000 $ à 30 000 $.

ORGANISMES CERTIFICATEURS au Canada — BSI, DNV, TÜV SÜD, TÜV Rheinland, Bureau Veritas, SGS, AFNOR, et plusieurs autres ouvrent leur portefeuille à ISO 42001 depuis 2024.

DIFFÉRENCE AVEC NIST AI RMF — le RMF est un CADRE OPÉRATIONNEL gratuit; ISO 42001 est une NORME CERTIFIABLE payante. On peut implémenter le RMF sans certification (et c'est déjà beaucoup); on peut aussi viser la certification ISO 42001 pour démontrer la maturité. Les deux sont complémentaires :
- LE RMF répond à : « Comment gérons-nous concrètement les risques de chaque système ? »
- ISO 42001 répond à : « Comment notre ORGANISATION est-elle structurée pour le faire de façon répétable ? »

CIRCONSTANCES JUSTIFIANT LA CERTIFICATION pour une PME :
A. Marché B2B exigeant des preuves de gouvernance.
B. Exposition européenne (présomption partielle de conformité EU AI Act).
C. Volonté de signaler la maturité face aux concurrents.
D. Préparation à la régulation fédérale canadienne et autres lois en gestation.

CIRCONSTANCES NE LA JUSTIFIANT PAS (à court terme) :
A. PME sans exposition B2B significative — mieux vaut investir en RMF + Loi 25.
B. Phase d'expérimentation où les processus sont encore mouvants.
C. Une seule application d'IA, peu critique — la lourdeur d'un AIMS formel est disproportionnée.

POSITION D'INVESTISSEMENT — pour une PME québécoise, la séquence rationnelle est :
1. Mois 0-12 : conformité Loi 25 + adoption NIST AI RMF + Code volontaire canadien.
2. Mois 12-24 : si justifié par le marché, démarrer un projet ISO 42001 en s'appuyant sur les structures déjà en place.
3. Mois 24-36 : audit de certification.
        """.strip(),
    },

    "m6_c2_iso42001_annexe_a_controles": {
        "module": 6, "ordre": 2, "langue": "fr",
        "titre": "ISO 42001 — Annexe A et 38 contrôles",
        "prereqs": ["m6_c1_iso42001_norme_certifiable"],
        "texte": """
La force opérationnelle d'ISO/IEC 42001:2023 réside dans son ANNEXE A — un référentiel de 38 CONTRÔLES regroupés en 9 OBJECTIFS DE CONTRÔLE. Cette annexe joue le même rôle que l'Annexe A d'ISO 27001 pour la sécurité de l'information : elle décrit ce que l'organisation DOIT (ou peut) mettre en place pour atteindre ses objectifs de gouvernance d'IA.

NATURE DES CONTRÔLES — chaque contrôle énonce une mesure organisationnelle, technique ou contractuelle attendue. Ils ne sont pas tous obligatoires : l'organisation détermine, dans sa DÉCLARATION D'APPLICABILITÉ (« Statement of Applicability »), lesquels s'appliquent à elle, et justifie les exclusions.

LES NEUF DOMAINES DE CONTRÔLES :

DOMAINE A.2 — POLITIQUES LIÉES À L'IA (3 contrôles).
A.2.2 Politique d'IA documentée.
A.2.3 Alignement avec les autres politiques de l'organisation.
A.2.4 Revue périodique de la politique d'IA.
Objectif : que l'organisation ait une position formelle et cohérente sur l'IA, articulée à sa stratégie globale.

DOMAINE A.3 — ORGANISATION INTERNE (3 contrôles).
A.3.2 Rôles et responsabilités définis (RACI).
A.3.3 Notification des autorités et des parties intéressées.
A.3.4 Mécanismes pour signaler les préoccupations (« whistleblowing »).
Objectif : que les bonnes personnes soient identifiées avec les bonnes autorités, et que les remontées de préoccupations soient possibles.

DOMAINE A.4 — RESSOURCES POUR LES SYSTÈMES D'IA (5 contrôles).
A.4.2 Documentation des ressources.
A.4.3 Ressources de calcul et de stockage.
A.4.4 Ressources humaines compétentes.
A.4.5 Ressources de données.
A.4.6 Outils et infrastructures.
Objectif : avoir l'inventaire et la gestion des moyens nécessaires au cycle de vie de l'IA.

DOMAINE A.5 — ÉVALUATION DES IMPACTS DES SYSTÈMES D'IA (4 contrôles).
A.5.2 Processus d'évaluation des impacts.
A.5.3 Documentation des évaluations.
A.5.4 Évaluation des impacts sur les individus et groupes.
A.5.5 Évaluation des impacts sociétaux.
Objectif : avant tout déploiement, comprendre les conséquences possibles. Recoupe directement les EFVP de la Loi 25 et les FRIA de l'EU AI Act.

DOMAINE A.6 — CYCLE DE VIE DU SYSTÈME D'IA (4 contrôles).
A.6.1 Objectifs et critères pour le développement responsable.
A.6.2 Processus de cycle de vie documentés.
A.6.3 Exigences techniques et opérationnelles.
A.6.4 Validation, vérification, déploiement, surveillance.
Objectif : industrialiser la qualité et la conformité tout au long du développement, du déploiement, et du retrait du système.

DOMAINE A.7 — DONNÉES POUR LES SYSTÈMES D'IA (5 contrôles).
A.7.2 Processus de gestion des données pour l'IA.
A.7.3 Acquisition de données.
A.7.4 Qualité des données pour l'IA.
A.7.5 Provenance et traçabilité.
A.7.6 Préparation des données.
Objectif : la qualité de l'IA dépend de la qualité des données. Domaine crucial pour gérer les biais, la conformité vie privée, et la traçabilité.

DOMAINE A.8 — INFORMATION AUX PARTIES INTÉRESSÉES (3 contrôles).
A.8.2 Informations système-spécifiques.
A.8.3 Information externe.
A.8.4 Réception et traitement des informations entrantes.
Objectif : transparence interne et externe sur l'usage de l'IA. Articule directement avec les obligations de transparence de la Loi 25 (Art. 8.1, 12.1) et de l'EU AI Act (Art. 50, 13).

DOMAINE A.9 — UTILISATION DES SYSTÈMES D'IA (3 contrôles).
A.9.2 Processus pour l'usage responsable.
A.9.3 Objectifs définis pour l'utilisation.
A.9.4 Utilisation conforme aux objectifs.
Objectif : que les systèmes soient utilisés conformément à leur finalité prévue, sans dérive d'usage.

DOMAINE A.10 — RELATIONS AVEC LES TIERS et CLIENTS (3 contrôles).
A.10.2 Allocation des responsabilités.
A.10.3 Fournisseurs.
A.10.4 Clients.
Objectif : la chaîne de valeur de l'IA implique presque toujours plusieurs entités. Domaine qui traite des contrats, de la due diligence des fournisseurs, et de l'information aux clients.

DÉCLARATION D'APPLICABILITÉ (« Statement of Applicability ») — document central exigé par la norme. Liste les 38 contrôles, indique pour chacun s'il s'applique ou non, justifie les exclusions, et renvoie au document interne qui décrit sa mise en œuvre. C'est le DOCUMENT PRINCIPAL examiné lors de l'audit.

ANNEXES NORMATIVES SUPPLÉMENTAIRES :
ANNEXE B — Guide d'implémentation par contrôle. Pour chaque contrôle, B donne des explications, exemples, et bonnes pratiques. Lecture indispensable lors de la mise en œuvre.
ANNEXE C — Objectifs et risques d'IA. Liste indicative des risques à considérer dans l'évaluation.
ANNEXE D — Application sectorielle. Considérations pour des secteurs spécifiques.

ARTICULATION AVEC NIST AI RMF — la cartographie est riche :
A. Le DOMAINE A.2 (Politiques) ↔ GOVERN du RMF.
B. Les DOMAINES A.5 (Évaluation des impacts) et A.6 (Cycle de vie) ↔ MAP, MEASURE, MANAGE du RMF.
C. Le DOMAINE A.7 (Données) ↔ ce qui n'est pas explicitement dans le RMF mais bien couvert par les sept caractéristiques (en particulier équité, vie privée).
D. Le DOMAINE A.8 (Information) ↔ les caractéristiques de transparence et d'explicabilité du RMF.

INTÉGRATION AVEC ISO 27001 et ISO 27701 — environ 40 % des contrôles d'ISO 42001 trouvent un équivalent direct dans ISO 27001 (sécurité) et ISO 27701 (vie privée). Une organisation déjà certifiée 27001/27701 économise une quantité substantielle d'effort en visant 42001.

COÛT D'IMPLÉMENTATION — selon la complexité de l'organisation et l'inventaire des systèmes d'IA, l'implémentation des 38 contrôles représente typiquement 4-9 mois de travail dédié, avec un effort intense sur les domaines A.5 (évaluations), A.6 (cycle de vie), A.7 (données) — qui sont les plus exigeants techniquement.
        """.strip(),
    },

    "m6_c3_iso42001_articulation": {
        "module": 6, "ordre": 3, "langue": "fr",
        "titre": "ISO 42001 — articulation avec ISO 27001, 9001, 27701",
        "prereqs": ["m6_c2_iso42001_annexe_a_controles"],
        "texte": """
Pour la plupart des organisations, ISO 42001 ne s'implémente pas dans un vide. Elle vient s'ajouter à des systèmes de management déjà en place — qualité (9001), sécurité (27001), vie privée (27701), environnement (14001). L'INTÉGRATION de ces normes est la clé d'une mise en œuvre efficace et économique.

LE PRINCIPE D'INTÉGRATION HLS — toutes les normes de management ISO modernes partagent la même structure de haut niveau (HLS) : 10 chapitres parallèles, vocabulaire commun, principes communs. Cela permet de construire un SYSTÈME DE MANAGEMENT INTÉGRÉ (« Integrated Management System » — IMS) qui couvre simultanément plusieurs domaines avec des processus uniques.

ARTICULATION ISO 42001 + ISO 27001 (Sécurité de l'information).

POURQUOI 27001 EST PRÉREQUIS DE FACTO POUR 42001 — un système d'IA traite par définition de l'information, et donc présente des risques de sécurité de l'information. Sans contrôles de sécurité, on ne peut pas démontrer la sûreté ni la cybersécurité d'un système d'IA. La majorité des organismes certificateurs encouragent fortement la certification 27001 préalable ou simultanée.

CHEVAUCHEMENT IDENTIFIABLE — les contrôles d'ISO 42001 qui se cartographient directement sur 27001 :
A. Gestion des accès aux données et aux modèles.
B. Chiffrement des données d'entraînement et des modèles.
C. Détection et réponse aux incidents.
D. Sauvegardes et continuité.
E. Sécurité des fournisseurs (cloud, API tierces).

ÉCONOMIES D'ÉCHELLE — une organisation qui certifie 27001 puis 42001 réutilise environ 40-50 % de l'effort documentaire et procédural. L'audit combiné est plus efficace que deux audits séparés.

ARTICULATION ISO 42001 + ISO 27701 (Vie privée, extension de 27001).

ISO 27701 est une extension de 27001 spécifiquement pour la vie privée. Elle est particulièrement pertinente pour les organisations soumises au RGPD ou à la Loi 25.

CHEVAUCHEMENT FORT avec les éléments « vie privée » d'ISO 42001 :
A. Gestion du consentement.
B. Droits des personnes (accès, rectification, opposition, portabilité).
C. Évaluations des impacts sur la vie privée (DPIA / EFVP).
D. Notification d'incidents impliquant des RP.

RECOMMANDATION — pour une organisation qui traite massivement des RP, la séquence optimale est : 27001 → 27701 → 42001. Chaque norme s'appuie sur la précédente.

ARTICULATION ISO 42001 + ISO 9001 (Qualité).

ISO 9001 est la norme de management de la qualité, déjà en place dans des centaines de milliers d'organisations dans le monde. Elle structure la rigueur opérationnelle générale.

CHEVAUCHEMENT MOYEN — ISO 9001 fournit une base de gouvernance et de processus que 42001 réutilise :
A. Documentation et maîtrise documentaire.
B. Audits internes.
C. Revues de direction.
D. Actions correctives et amélioration continue.
E. Compétence et formation du personnel.

L'EFFORT INCRÉMENTAL pour ajouter 42001 à une organisation déjà 9001 est plus faible que pour une organisation qui n'a aucune norme de management préexistante.

ARTICULATION AVEC AUTRES NORMES DE LA FAMILLE ISO IA :

ISO/IEC 23894:2023 — Gestion des risques en IA. Norme TECHNIQUE complémentaire qui détaille les méthodes de gestion des risques applicables aux systèmes d'IA. Non certifiable, mais très utile comme support technique pour le DOMAINE A.5 d'ISO 42001.

ISO/IEC 23053:2022 — Cadre de référence pour les systèmes d'IA utilisant l'apprentissage automatique. Vocabulaire et architecture.

ISO/IEC 22989:2022 — Concepts et terminologie liés à l'IA. Référence terminologique pour ISO 42001.

ISO/IEC 25059:2023 — Modèle de qualité pour les systèmes d'IA. Aide à définir les métriques de qualité (précision, robustesse, équité).

ISO/IEC TR 24028:2020 — Vue d'ensemble de la fiabilité de l'IA. Document technique pour comprendre les enjeux.

ISO/IEC TR 24368:2022 — Aspects éthiques et sociétaux. Guide non certifiable mais utile.

LE FUTUR ISO/IEC 42005 (en développement) — guide spécifique pour l'évaluation des impacts d'IA, très attendu pour structurer la mise en œuvre du DOMAINE A.5 d'ISO 42001.

STRATÉGIE D'INTÉGRATION POUR UNE PME QUÉBÉCOISE :

SCÉNARIO 1 — Aucune certification préalable. Choix recommandé : démarrer simultanément 27001 et 27701 (vie privée + sécurité), puis 42001 12-18 mois plus tard. Effort total : 18-24 mois et 200 000-400 000 $.

SCÉNARIO 2 — Déjà 9001. Ajouter 27001 + 27701 + 42001 en parallèle ou séquentiellement; réutiliser l'infrastructure documentaire de 9001. Effort total réduit de 30-40 %.

SCÉNARIO 3 — Déjà 27001/27701. Ajouter 42001 en bénéficiant des 40-50 % de chevauchement. Effort : 6-9 mois, 60 000-120 000 $.

SCÉNARIO 4 — Pas de certification mais maturité élevée (RMF déjà en place). Possible de viser directement 42001, en formalisant les pratiques RMF dans la structure normative. Risque : si la sécurité informationnelle est faible, l'audit identifiera des non-conformités majeures.

ARTICULATION AVEC LES CADRES NON-ISO :
A. NIST AI RMF — utilisé comme méthode de mise en œuvre des contrôles ISO 42001.
B. NIST CSF 2.0 — articulé avec ISO 27001 sur la cybersécurité.
C. Code de conduite volontaire canadien — couvert par les contrôles ISO 42001.
D. Loi 25 et RGPD — couverts par ISO 27701 + les contrôles vie privée d'ISO 42001.
E. EU AI Act — la certification ISO 42001 est susceptible de constituer une PRÉSOMPTION DE CONFORMITÉ partielle pour les systèmes à haut risque, à condition de compléter la documentation administrative spécifique du règlement.

POSITION D'INVESTISSEMENT — pour la majorité des PME québécoises, l'objectif réaliste à 24 mois est :
1. Loi 25 conforme (obligation immédiate).
2. NIST AI RMF + Code volontaire (méthode opérationnelle).
3. Si exposition européenne ou exigence B2B : ISO 27001 + ISO 27701 d'abord, puis ISO 42001.
4. Si la régulation fédérale canadienne est adoptée : ajustement marginal du dispositif déjà en place.
        """.strip(),
    },

})


# ══════════════════════════════════════════════════════════════════════════════
# MODULE 7 — CNIL — GUIDE OPÉRATIONNEL  (7 concepts, FR)
# ══════════════════════════════════════════════════════════════════════════════

CURRICULUM.update({

    "m7_c1_cnil_avant_deploiement": {
        "module": 7, "ordre": 1, "langue": "fr",
        "titre": "CNIL — avant le déploiement (poser les bonnes questions)",
        "prereqs": ["m1_c2_typologie_outils"],
        "texte": """
La CNIL (Commission Nationale de l'Informatique et des Libertés), autorité française de protection des données, a publié depuis 2023-2024 une SÉRIE DE GUIDES OPÉRATIONNELS sur l'IA. Contrairement aux cadres comme le NIST RMF (qui est un cadre transversal) ou les Principes OCDE (qui sont des valeurs), la CNIL adopte une approche par PHASE DU CYCLE DE VIE de l'IA. Ce module suit cette logique : 7 concepts, un par phase.

POURQUOI ÉTUDIER LA CNIL DEPUIS LE QUÉBEC :
A. La Loi 25 québécoise s'inspire fortement du RGPD. Les méthodes opérationnelles de la CNIL sont DIRECTEMENT TRANSPOSABLES dans un EFVP québécois.
B. La CAI Quebec et la CNIL coopèrent dans des déclarations conjointes internationales (ex : déclaration février 2026 sur les contenus générés par IA).
C. La CNIL a une dizaine d'années d'avance sur la jurisprudence par rapport à la CAI; ses positions préfigurent souvent celles que prendra la CAI.
D. Les guides CNIL sont rédigés en FRANÇAIS et utilisent un VOCABULAIRE TECHNIQUE adapté qui est plus accessible que les sources américaines.

PHASE 1 — AVANT LE DÉPLOIEMENT : POSER LES BONNES QUESTIONS.

Le guide CNIL « Asking the right questions before using an AI system » (en version française : « Poser les bonnes questions avant d'utiliser un système d'IA ») établit le test de NÉCESSITÉ et de PROPORTIONNALITÉ.

QUESTIONS À POSER AVANT MISE EN ŒUVRE :

QUESTION 1 — DÉFINIR L'OBJECTIF (FINALITÉ) PRÉCIS DU SYSTÈME D'IA.
- Quel problème concret le système résout-il?
- Pour quels usages SECONDAIRES est-il prévu?
- Quels usages devraient être INTERDITS (« hors-périmètre »)?

QUESTION 2 — ÉVALUER LA NÉCESSITÉ.
- L'IA est-elle STRICTEMENT NÉCESSAIRE pour atteindre l'objectif?
- Une SOLUTION MOINS INTRUSIVE existe-t-elle (système de règles, IA prédictive simple, traitement humain)?
- Si oui, pourquoi privilégier l'IA?

QUESTION 3 — IDENTIFIER LES PERSONNES AFFECTÉES.
- Qui sera affecté?
- Y a-t-il des POPULATIONS VULNÉRABLES (enfants, patients, employés, demandeurs de prestations)?
- Quelle est la PORTÉE DE L'IMPACT (légal, financier, physique)?

QUESTION 4 — DÉTERMINER LE NIVEAU D'IMPLICATION HUMAINE.
- La décision finale est-elle prise par l'humain ou par le système?
- Quel mécanisme de revue humaine?
- Qui peut intervenir et arrêter le système?

QUESTION 5 — CLARIFIER LES RÔLES.
- Qui est le RESPONSABLE DU TRAITEMENT (au sens RGPD/Loi 25) — celui qui décide des finalités?
- Qui est le SOUS-TRAITANT — celui qui exécute techniquement?
- Qui est le DÉPLOYEUR (utilisateur final) — celui qui met en service?

QUESTION 6 — DOCUMENTER LES RESPONSABILITÉS.
- Politiques internes, chartes éthiques, RACI.
- Procédures d'incident.
- Formation du personnel.

QUESTION 7 — INSTAURER UNE GOUVERNANCE INTERNE.
- Politique IA approuvée par la direction.
- Comité IA si l'organisation a la masse critique.
- Personne responsable nommée (équivalent du RPRP / DPO).

LE TEST DE PROPORTIONNALITÉ — L'AVANTAGE SIGNIFICATIF apporté par l'IA dépasse-t-il les RISQUES ADDITIONNELS qu'elle introduit par rapport à une solution alternative?

Cas typique : un outil de tri de CV par IA est-il PROPORTIONNÉ à l'objectif (efficacité de recrutement) compte tenu des risques de biais discriminatoire? La CNIL impose de RAISONNER cette balance avant le déploiement, pas après.

PARTIES PRENANTES À CONSULTER :
A. RESPONSABLE DU TRAITEMENT — porte la responsabilité juridique.
B. PERSONNES NATURELLEMENT RESPONSABLES du développement et de la maintenance.
C. INDIVIDUS DONT LES DONNÉES SONT TRAITÉES — directement ou via des représentants.

LIVRABLE TYPIQUE D'UNE PHASE 1 RÉUSSIE :
- Note de cadrage (« scoping memo ») de 2-5 pages.
- Décision motivée GO / NO-GO / GO conditionnel.
- Plan de gouvernance interne.
- Identification des risques préliminaires (qui seront approfondis en phase suivante).

LIEN AVEC LA LOI 25 — la phase 1 du guide CNIL est l'équivalent de la PARTIE 1 D'UNE EFVP québécoise. Sans cette phase, l'EFVP qui suit est mal cadrée et risque d'être superficielle.

ERREUR FRÉQUENTE — sauter la phase 1 et démarrer directement par les aspects techniques. Conséquence : on déploie un système qu'on n'aurait pas dû déployer (parce qu'il n'était pas nécessaire) ou qu'on aurait dû configurer différemment (parce que les rôles n'étaient pas clairs).
        """.strip(),
    },

    "m7_c2_cnil_collecte_donnees": {
        "module": 7, "ordre": 2, "langue": "fr",
        "titre": "CNIL — collecte et qualification des données d'entraînement",
        "prereqs": ["m7_c1_cnil_avant_deploiement"],
        "texte": """
PHASE 2 — GOUVERNANCE DES DONNÉES D'ENTRAÎNEMENT.

Le guide CNIL « Collecting and qualifying training data » est l'un des plus opérationnels. Il s'attaque au problème central de l'IA : LA QUALITÉ ET LA LICÉITÉ DES DONNÉES qui alimentent le modèle.

POURQUOI CETTE PHASE EST CRITIQUE — un modèle d'IA n'est jamais meilleur que les données sur lesquelles il a été entraîné. Si les données sont biaisées, illégalement collectées, ou de mauvaise qualité, le système qui en résulte hérite de ces défauts. Et il les amplifie à l'échelle.

QUATRE CHANTIERS À MENER :

CHANTIER 1 — DISTINGUER DONNÉES PERSONNELLES ET NON PERSONNELLES.

Les données personnelles (RP au sens de la Loi 25 ou « personal data » au sens du RGPD) sont soumises à un régime juridique distinct. Pour chaque dataset d'entraînement :
A. CARTOGRAPHIER les données qui permettent d'identifier directement ou indirectement une personne (nom, adresse, IP, identifiant publicitaire, données biométriques).
B. ÉVALUER si la pseudonymisation ou l'anonymisation a été correctement effectuée. La CNIL et la CAI ont une définition STRICTE de l'anonymisation : si on peut ré-identifier la personne par recoupement, ce n'est pas anonyme.
C. POUR LES DONNÉES PERSONNELLES — vérifier la BASE LÉGALE (consentement, contrat, obligation légale, intérêt légitime). La quasi-totalité des cas d'IA repose sur le CONSENTEMENT, et celui-ci doit être MANIFESTE, LIBRE, ÉCLAIRÉ, À DES FINS SPÉCIFIQUES (cf. M2 c3).

CHANTIER 2 — IMPLÉMENTER UNE GOUVERNANCE DES DONNÉES.

A. QUALITÉ — exactitude, complétude, cohérence, fraîcheur.
B. REPRÉSENTATIVITÉ — les données reflètent-elles bien la POPULATION qui sera affectée par le système?
C. ÉQUILIBRE — y a-t-il des sous-représentations qui produiront des biais?

EXEMPLE CONCRET — un modèle de scoring de crédit entraîné sur des données historiques où les femmes ont moins emprunté que les hommes (parce qu'elles n'avaient pas d'accès au crédit) reproduira et amplifiera ce biais. La CNIL exige une analyse explicite de cette représentativité.

CHANTIER 3 — IDENTIFIER ET ATTÉNUER LES BIAIS.

A. BIAIS DE SOUS-REPRÉSENTATION — minorités absentes ou sous-représentées dans les données.
B. BIAIS DE SUR-REPRÉSENTATION — sur-représentation de certains résultats (ex : population masculine, blanche, urbaine).
C. BIAIS HISTORIQUES — les données reflètent des inégalités structurelles passées.
D. BIAIS DE COLLECTE — manière dont les données ont été obtenues (par exemple via des plateformes en ligne) qui exclut certaines populations.

MÉTHODES D'ATTÉNUATION :
- Rééquilibrage des données (oversampling, undersampling).
- Augmentation des données (synthetic data) — avec prudence.
- Utilisation de techniques d'apprentissage robustes aux biais.
- Tests par sous-groupe systématiques.

CHANTIER 4 — DOCUMENTER LA PROVENANCE ET LES TRANSFORMATIONS.

A. PROVENANCE — d'où viennent les données? (sources internes, partenaires, données publiques, achetées).
B. CONSENTEMENT (si applicable) — comment et quand le consentement a été obtenu.
C. TRANSFORMATIONS — toutes les manipulations effectuées : nettoyage, normalisation, étiquetage, agrégation.
D. POLITIQUE DE RÉTENTION — combien de temps les données d'entraînement sont-elles conservées? Quand et comment sont-elles supprimées?

DEUX TECHNIQUES À CONSIDÉRER POUR PROTÉGER LA VIE PRIVÉE :

A. ANONYMISATION — supprimer toute donnée identifiante. Définition stricte : impossibilité de ré-identifier par recoupement avec d'autres sources.
B. CONFIDENTIALITÉ DIFFÉRENTIELLE — ajouter du bruit mathématique aux données pour empêcher la ré-identification individuelle tout en préservant les statistiques agrégées.
C. DONNÉES SYNTHÉTIQUES — générer des données artificielles qui imitent les propriétés statistiques des données réelles, sans référer à des personnes réelles.
D. APPRENTISSAGE FÉDÉRÉ — entraîner le modèle sans centraliser les données (les calculs se font localement, seuls les paramètres du modèle remontent).

PIÈGES FRÉQUENTS :
A. UTILISER DES DONNÉES « SCRAPED » DU WEB — sans consentement spécifique, c'est presque toujours non conforme. Plusieurs procédures de la CNIL et de la CAI sanctionnent ce type de pratique.
B. CONFONDRE PSEUDONYMISATION ET ANONYMISATION — la pseudonymisation conserve la possibilité de ré-identifier; l'anonymisation l'élimine.
C. NE PAS DOCUMENTER les transformations — impossible de répondre aux demandes de personnes (« quelles données ont été utilisées pour décider à mon sujet? »).
D. UTILISER DES DONNÉES SECONDAIRES sans nouvelle base légale spécifique. Une finalité secondaire (entraîner un modèle) est rarement couverte par le consentement initial.

LIVRABLE TYPIQUE — DATA SHEET (« Datasheet for Datasets ») couvrant : motivation, composition, processus de collecte, prétraitement, utilisations prévues, distribution, maintenance. Document recommandé par l'EU AI Act Art. 10 pour les systèmes à haut risque.

LIEN AVEC LA LOI 25 — chaque dataset utilisé pour entraîner un modèle doit être documenté dans l'EFVP du projet, avec justification de la base légale et description des biais identifiés et atténués.
        """.strip(),
    },

    "m7_c3_cnil_developpement_algorithme": {
        "module": 7, "ordre": 3, "langue": "fr",
        "titre": "CNIL — développement et entraînement de l'algorithme",
        "prereqs": ["m7_c2_cnil_collecte_donnees"],
        "texte": """
PHASE 3 — DÉVELOPPEMENT ET ENTRAÎNEMENT DE L'ALGORITHME.

Le guide CNIL « Developing and training an algorithm » couvre la phase technique : choix de l'architecture, entraînement, validation, tests. C'est la phase la plus technique du guide CNIL, mais elle reste accessible aux non-spécialistes parce qu'elle se concentre sur la GOUVERNANCE de la phase de développement, pas sur les détails algorithmiques.

SEPT CHANTIERS DE LA PHASE DE DÉVELOPPEMENT :

CHANTIER 1 — DOCUMENTER LES OBJECTIFS, CHOIX DE CONCEPTION, COMPROMIS.

Pour chaque modèle développé, la CNIL exige une documentation qui explicite :
A. L'OBJECTIF MÉTIER — qu'est-ce que le modèle DOIT faire?
B. L'OBJECTIF TECHNIQUE — comment le formaliser mathématiquement (classification, régression, génération)?
C. LES CHOIX DE CONCEPTION — quelle architecture? quels hyperparamètres? pourquoi?
D. LES COMPROMIS — précision globale vs équité par groupe; rapidité vs explicabilité; coût d'entraînement vs qualité.
E. LES LIMITES CONNUES — cas où le modèle est faible.

CHANTIER 2 — IMPLÉMENTER LA VALIDATION DU MODÈLE.

A. TESTS SUR ÉCHANTILLONS REPRÉSENTATIFS — pas seulement les données utilisées pour l'entraînement.
B. SURVEILLANCE DE LA DÉGRADATION DE PERFORMANCE dans le temps — c'est le « DRIFT ».
C. TESTS DE ROBUSTESSE face à des entrées atypiques (« out-of-distribution »).
D. COMPARAISON avec un baseline simple (modèle de règles, modèle linéaire) — l'IA est-elle vraiment meilleure?

CHANTIER 3 — ÉVALUER L'EXPLICABILITÉ.

Les décisions de l'algorithme peuvent-elles être expliquées de façon SIGNIFICATIVE à une personne affectée? Cinq techniques principales :
A. SHAP VALUES — attribution de l'importance de chaque variable.
B. LIME — explication locale autour d'une prédiction spécifique.
C. ATTENTION MAPS — pour les modèles avec mécanismes d'attention.
D. CONTREFACTUELS — quels changements minimaux dans l'entrée changeraient la prédiction?
E. MODEL CARDS — documentation publique du modèle et de ses limites.

POINT JURIDIQUE — l'article 12.1 de la Loi 25 et l'article 22 du RGPD exigent une explication SUFFISANTE pour permettre la contestation. La CNIL et la CAI ont indiqué qu'il faut être capable de fournir AU MOINS les CATÉGORIES de variables et leur PONDÉRATION RELATIVE.

CHANTIER 4 — TESTER LES BIAIS.

Évaluation de l'équité par sous-groupes (genre, origine ethnique, âge, situation socio-économique). Métriques principales :
A. DISPARATE IMPACT — taux de décisions favorables par groupe.
B. EQUALITY OF ODDS — taux d'erreurs (faux positifs, faux négatifs) par groupe.
C. DEMOGRAPHIC PARITY — distribution équilibrée des décisions favorables.
D. INDIVIDUAL FAIRNESS — des cas similaires reçoivent des décisions similaires.

POINT TECHNIQUE — ces définitions d'équité sont MUTUELLEMENT INCOMPATIBLES dans la plupart des cas. L'organisation doit CHOISIR explicitement laquelle viser, et JUSTIFIER ce choix.

CHANTIER 5 — METTRE EN PLACE LE SUIVI DE L'ENTRAÎNEMENT.

Pendant l'entraînement, surveiller :
A. CONVERGENCE — le modèle apprend-il correctement?
B. PATTERNS INATTENDUS — décisions surprenantes sur des cas de test.
C. SUR-AJUSTEMENT — performance excellente sur l'entraînement mais médiocre sur de nouvelles données.
D. LEAKAGE — fuite d'information (le modèle « voit » accidentellement les réponses pendant l'entraînement).

CHANTIER 6 — DOCUMENTER LES LIMITES.

Pour chaque modèle, lister :
A. CAS D'USAGE NON RECOMMANDÉS — où le modèle ne doit pas être utilisé.
B. CAS LIMITES — où le modèle est moins fiable (ex : sous-population peu représentée).
C. POPULATIONS POUR LESQUELLES LE MODÈLE A DES PERFORMANCES INFÉRIEURES.
D. PERFORMANCES MINIMALES GARANTIES — seuils sous lesquels le système ne devrait pas être déployé.

CHANTIER 7 — IMPLÉMENTER LA GESTION DE VERSIONS.

A. VERSION DU CODE — Git, MLflow ou équivalent.
B. VERSION DES DONNÉES — DVC, Weights & Biases ou équivalent.
C. VERSION DES PARAMÈTRES MODÈLE — sauvegarde des poids appris.
D. VERSION DE L'ENVIRONNEMENT — librairies, dépendances.

L'objectif : pouvoir REPRODUIRE EXACTEMENT n'importe quelle décision passée du système. C'est crucial pour répondre aux enquêtes (CAI, CNIL).

LIVRABLE TYPIQUE — MODEL CARD (« Model Card for Model Reporting » selon Mitchell et al., 2019). Sections : détails du modèle, utilisation prévue, facteurs, métriques, évaluation des données, données d'entraînement, analyses quantitatives, considérations éthiques, avertissements et recommandations.

POINT D'ATTENTION — la CNIL et la CAI ont les mêmes attentes sur cette phase, mais avec des seuils légaux différents : la CAI s'appuie sur la Loi 25 (ex : Art. 12.1 sur les facteurs et paramètres principaux); la CNIL s'appuie sur le RGPD (Art. 22 et 13-14).
        """.strip(),
    },

    "m7_c4_cnil_production": {
        "module": 7, "ordre": 4, "langue": "fr",
        "titre": "CNIL — déploiement en production",
        "prereqs": ["m7_c3_cnil_developpement_algorithme"],
        "texte": """
PHASE 4 — DÉPLOIEMENT EN PRODUCTION.

Le guide CNIL « Using an AI system in production » couvre les enjeux opérationnels APRÈS la mise en service. C'est la phase où la qualité de la gouvernance est mise à l'épreuve dans des conditions réelles.

CINQ DIMENSIONS À GÉRER :

DIMENSION 1 — STRUCTURE DE GOUVERNANCE OPÉRATIONNELLE.

A. PERSONNES RESPONSABLES NOMMÉES — pas seulement « le DG », mais une personne physique avec autorité décisionnelle. C'est le RPRP en contexte québécois (Loi 25 Art. 3.1).
B. AUTORITÉ DE DÉCISION pour les modifications du système (changement de version, ajout de fonctionnalités, étendue d'usage).
C. CHAÎNE D'ESCALADE en cas d'incident : qui appelle qui à 3 h du matin?

DIMENSION 2 — SUPERVISION HUMAINE PROPORTIONNÉE.

Le niveau de supervision humaine doit être PROPORTIONNEL à l'IMPACT des décisions :

A. DÉCISIONS À ENJEUX ÉLEVÉS (juridique, financier, médical, RH critique) → HUMAIN DANS LA BOUCLE (« human-in-the-loop »). Chaque décision est revue par un humain AVANT exécution.

B. DÉCISIONS À IMPACT MODÉRÉ → HUMAIN SUR LA BOUCLE (« human-on-the-loop »). L'humain examine les décisions a posteriori et peut les renverser.

C. DÉCISIONS À FAIBLE IMPACT (routine, réversibles) → HUMAIN AU-DESSUS DE LA BOUCLE (« human-over-the-loop »). Audit périodique du comportement, escalade seulement si anomalies détectées.

D. PLEINEMENT AUTONOME → seulement dans des contextes contrôlés et à faibles conséquences. Même là, monitoring continu obligatoire.

ATTENTION POUR L'ART. 12.1 LOI 25 — la « revue humaine perfunctoire » (humain qui valide en 5 secondes 200 décisions par jour) ne sort PAS du champ d'application de l'article. La CAI tient le même raisonnement que le RGPD Art. 22 : la revue doit être SUBSTANTIELLE.

DIMENSION 3 — MONITORING CONTINU.

A. PERFORMANCE — taux d'erreur, taux de revues humaines, taux de plaintes, temps de traitement.
B. DRIFT — la distribution des entrées change-t-elle dans le temps? Le modèle reste-t-il représentatif?
C. ÉQUITÉ — les écarts par sous-groupe restent-ils dans les bornes définies?
D. ATTAQUES — détection de données malicieuses (data poisoning), de prompts adversariaux, d'extraction de modèle.
E. DÉRIVE DE PURPOSE — le système est-il utilisé pour des finalités non prévues à la phase 1?

CRITÈRES DE DÉCLENCHEMENT D'UN RÉ-ENTRAÎNEMENT :
- Performance dégradée au-delà d'un seuil défini.
- Drift mesuré significatif.
- Plaintes croissantes des utilisateurs.
- Changement substantiel de la population d'entrées.

DIMENSION 4 — DOCUMENTATION DES DÉCISIONS.

Chaque décision du système doit être TRACÉE :
A. ENTRÉES (données utilisées).
B. SORTIE (décision prise).
C. DATE et HEURE.
D. UTILISATEUR (humain validateur si applicable).
E. JOURNAL D'ÉVÉNEMENTS (logs techniques).

DURÉE DE CONSERVATION — pour les systèmes à haut risque sous EU AI Act, AU MOINS 6 MOIS pour les déployeurs (Art. 26 al. 6). Pour la Loi 25, la durée doit permettre de répondre aux demandes des personnes — typiquement 1-3 ans selon la sensibilité.

DIMENSION 5 — MÉCANISMES DE FEEDBACK.

A. CANAL DE PLAINTE — accessible aux personnes affectées. Idéalement plusieurs canaux (web, courriel, téléphone).
B. CANAL DE SIGNALEMENT INTERNE — pour les employés qui détectent des anomalies (« whistleblowing »).
C. AUDITS INTERNES PÉRIODIQUES — au moins annuels, plus fréquents pour les systèmes à haut risque.
D. AUDITS EXTERNES — par un tiers indépendant pour les systèmes critiques.

INCIDENT RESPONSE — procédures pour :
A. DÉTECTER un incident (anomalie, plainte, fuite, attaque).
B. CONTENIR l'incident (couper l'accès, suspendre le système).
C. ÉVALUER la gravité et l'étendue.
D. NOTIFIER (CAI, personnes affectées, partenaires).
E. CORRIGER et redéployer.
F. POST-MORTEM organisationnel.

LIVRABLE TYPIQUE — SYSTEM CARD complète et tableau de bord opérationnel actualisé.

ARTICULATION AVEC L'EFVP / LA FRIA — l'EFVP (Loi 25) ou la FRIA (EU AI Act) doivent être MISES À JOUR à chaque modification substantielle du système et au minimum annuellement pour les systèmes en service.

POINT D'ATTENTION 2026 — la jurisprudence Zhang en C.-B. (cf. M3 c6) souligne que la production d'une décision fondée sur l'IA reste sous la RESPONSABILITÉ PERSONNELLE de celui qui l'utilise. Pour les avocats, médecins, comptables, ingénieurs : la documentation de leur usage de l'IA et de leur revue indépendante n'est plus optionnelle.
        """.strip(),
    },

    "m7_c5_cnil_droits_personnes": {
        "module": 7, "ordre": 5, "langue": "fr",
        "titre": "CNIL — droits des personnes face à un système d'IA",
        "prereqs": ["m7_c1_cnil_avant_deploiement"],
        "texte": """
PHASE 5 — GARANTIR L'EXERCICE DES DROITS DES PERSONNES.

Le guide CNIL « Ensuring individuals can exercise their rights » couvre la transparence et les droits des personnes affectées par le système d'IA. C'est l'opérationnalisation des droits subjectifs reconnus par le RGPD et la Loi 25.

LES SEPT DROITS À GARANTIR :

DROIT 1 — DROIT À L'INFORMATION.

Les personnes doivent être informées qu'elles font l'objet d'un traitement par un système d'IA. Information préalable, claire, intelligible, et au plus tard au moment de la prise de décision (Loi 25 Art. 12.1).

CONTENU DE L'INFORMATION OBLIGATOIRE :
A. Caractère automatisé du traitement.
B. Identité du responsable du traitement.
C. Finalités du traitement.
D. Durée de conservation des données.
E. Existence des droits (accès, rectification, opposition, etc.).
F. Coordonnées pour exercer ces droits (RPRP / DPO).

POUR LES TECHNOLOGIES D'IDENTIFICATION, LOCALISATION, PROFILAGE — Loi 25 Art. 8.1 impose une INFORMATION ACTIVE supplémentaire sur l'usage de la technologie ET des moyens d'activer/désactiver ses fonctions.

DROIT 2 — DROIT D'ACCÈS.

La personne peut demander :
A. Quels sont les RP la concernant qui sont traités par le système?
B. Quelles sont les SOURCES de ces données?
C. Quelle est la LOGIQUE GÉNÉRALE du traitement?
D. Quelles sont les CONSÉQUENCES PRÉVUES de ce traitement?

POUR L'IA — pour un modèle de scoring, cela inclut : les variables utilisées, l'importance relative de chaque variable, les seuils de décision.

DÉLAI — 30 jours sous la Loi 25, prolongeable de 30 jours en cas de complexité.

DROIT 3 — DROIT DE RECTIFICATION.

Correction des RP inexacts, incomplets ou équivoques. Pour l'IA, la rectification d'une donnée d'entrée peut imposer la mise à jour des prédictions ou recommandations dépendantes.

DROIT 4 — DROIT À L'EFFACEMENT (« droit à l'oubli »).

Suppression des RP sous certaines conditions :
A. Données plus nécessaires à la finalité.
B. Retrait du consentement et absence d'autre base légale.
C. Opposition au traitement.
D. Données traitées illégalement.

POUR LES MODÈLES GÉNÉRATIFS — DIFFICULTÉ TECHNIQUE MAJEURE. On ne peut pas « effacer » une donnée d'un modèle déjà entraîné. Solutions partielles :
A. Filtrage des sorties (output filtering) pour empêcher la réminiscence.
B. Ré-entraînement périodique avec exclusion des données effacées.
C. Documentation de la limite et information des personnes.

DROIT 5 — DROIT D'OPPOSITION.

La personne peut s'opposer à un traitement automatisé sous certaines conditions, notamment en présence de motifs légitimes liés à sa situation particulière.

DROIT 6 — DROIT DE RÉVISION HUMAINE D'UNE DÉCISION AUTOMATISÉE.

Pour les décisions exclusivement automatisées (Loi 25 Art. 12.1, RGPD Art. 22), la personne a le droit de demander une révision par un humain compétent. Cet humain doit avoir :
A. L'AUTORITÉ pour modifier ou renverser la décision.
B. L'INFORMATION nécessaire pour effectuer une revue substantielle.
C. LE TEMPS de mener cette revue (pas de validation perfunctoire).
D. UNE FORMATION sur le système et ses limites.

DROIT 7 — DROIT À UNE INFORMATION SIGNIFICATIVE.

L'information fournie ne doit pas se cacher dans des conditions générales d'utilisation impénétrables. Elle doit être :
A. ACCESSIBLE — visible, pas enterrée dans des CGU.
B. INTELLIGIBLE — langage simple, sans jargon.
C. COMPLÈTE — couvre tous les aspects pertinents.
D. ACTUALISÉE — reflète les changements du système.

CINQ MÉCANISMES PRATIQUES POUR FAIRE EXERCER LES DROITS :

A. INTERFACE WEB DÉDIÉE pour les demandes (formulaire, suivi du statut).
B. ADRESSE COURRIEL DU RPRP — surveillée et active.
C. PROCÉDURE INTERNE documentée (qui traite, dans quel délai).
D. FORMATION du personnel sur les obligations.
E. REGISTRE DES DEMANDES pour la traçabilité.

ERREUR FRÉQUENTE — créer un formulaire de demande mais ne pas avoir de PROCESSUS pour y répondre dans les 30 jours. Ce qui transforme la conformité formelle en non-conformité substantielle.

CAS PARTICULIER — IA GÉNÉRATIVE ET CONTENUS HALLUCINÉS SUR DES PERSONNES NOMMÉES. Si un modèle génératif produit du contenu inexact ou diffamatoire sur une personne, celle-ci a le droit de demander :
A. CESSATION DE LA DIFFUSION (Loi 25 Art. 28.1).
B. RECTIFICATION dans le système (techniquement, filtrage de sortie).
C. SI APPLICABLE, DÉSINDEXATION par les moteurs de recherche.

L'organisation doit prévoir un canal de retrait RAPIDE pour ces cas, sous peine d'engager sa responsabilité.

LIVRABLE TYPIQUE — POLITIQUE DE TRAITEMENT DES DEMANDES — document interne décrivant : les types de demandes, qui les reçoit, qui les traite, dans quels délais, avec quels gabarits de réponse.
        """.strip(),
    },

    "m7_c6_cnil_securite": {
        "module": 7, "ordre": 6, "langue": "fr",
        "titre": "CNIL — sécurité du traitement IA",
        "prereqs": ["m7_c3_cnil_developpement_algorithme"],
        "texte": """
PHASE 6 — SÉCURITÉ DU TRAITEMENT.

Le guide CNIL « Securing the processing » s'attaque aux risques cyber spécifiques aux systèmes d'IA. Les principes sont alignés avec ISO 27001 mais adaptés aux particularités de l'IA.

CINQ DIMENSIONS DE LA SÉCURITÉ IA :

DIMENSION 1 — CONFIDENTIALITÉ.

A. CONTRÔLE D'ACCÈS aux données d'entraînement, aux modèles, aux journaux.
B. CHIFFREMENT au repos (données stockées) et en transit (communications).
C. SÉPARATION DES ENVIRONNEMENTS (développement, test, production).
D. PSEUDONYMISATION des données d'entraînement quand possible.
E. PROTECTION CONTRE L'EXTRACTION DE MODÈLE — un attaquant qui peut interroger le modèle peut parfois reconstituer des données d'entraînement.
F. DIFFERENTIAL PRIVACY pour les modèles entraînés sur des données sensibles.

DIMENSION 2 — INTÉGRITÉ.

A. PROTECTION CONTRE LA MODIFICATION NON AUTORISÉE des données et modèles.
B. SIGNATURE NUMÉRIQUE des artefacts (modèles, datasets).
C. LOG INTÉGRITÉ (journal cryptographiquement vérifiable).
D. CONTRÔLE DES MISES À JOUR — qui peut modifier le modèle de production?

DIMENSION 3 — DISPONIBILITÉ.

A. REDONDANCE — multiples instances du modèle, multiple zones géographiques.
B. PROCÉDURES DE SAUVEGARDE et de restauration testées régulièrement.
C. PLAN DE CONTINUITÉ D'AFFAIRES en cas de défaillance.
D. SCALABILITÉ — capacité à absorber des pics de charge.

DIMENSION 4 — RÉSILIENCE FACE AUX ATTAQUES SPÉCIFIQUES À L'IA.

ATTAQUE 1 — DATA POISONING (empoisonnement des données). L'attaquant modifie les données d'entraînement pour faire dévier le modèle.
- Mitigation : validation des sources de données, détection statistique d'anomalies, tests sur datasets de référence.

ATTAQUE 2 — MODEL EVASION (fuite par perturbation). L'attaquant produit des entrées spécialement conçues pour faire mal classer le modèle.
- Mitigation : entraînement adversarial, tests de robustesse, monitoring des entrées suspectes.

ATTAQUE 3 — MODEL EXTRACTION (vol de modèle). L'attaquant interroge le modèle de façon répétée pour reconstituer ses paramètres.
- Mitigation : limitation du débit (rate limiting), détection des patterns d'interrogation suspects, watermarking.

ATTAQUE 4 — MODEL INVERSION (récupération de données d'entraînement). L'attaquant exploite les sorties pour reconstituer des données d'entraînement individuelles.
- Mitigation : differential privacy, filtrage des sorties, formation sur des données moins sensibles.

ATTAQUE 5 — PROMPT INJECTION (pour l'IA générative). L'attaquant inclut dans une entrée des instructions cachées qui font dévier le comportement du modèle.
- Mitigation : filtrage et validation des prompts, sandboxing, tests d'intrusion.

ATTAQUE 6 — JAILBREAK (pour l'IA générative). L'attaquant contourne les filtres de sécurité pour faire générer du contenu interdit.
- Mitigation : red teaming systématique, défenses en profondeur, monitoring des sorties.

DIMENSION 5 — GESTION DES INCIDENTS DE SÉCURITÉ.

A. DÉTECTION continue (SIEM, logs, alertes).
B. ANALYSE rapide (équipe de réponse à incident).
C. CONTAINMENT (isolation du système, suspension).
D. ÉRADICATION (correctif, mise à jour).
E. RECOVERY (restauration, validation).
F. LESSONS LEARNED (post-mortem, amélioration continue).

CHAÎNE D'APPROVISIONNEMENT IA — UN VECTEUR D'ATTAQUE CRITIQUE.

Beaucoup de systèmes d'IA reposent sur :
A. MODÈLES DE FONDATION TIERS (Claude, GPT, Llama).
B. COMPOSANTS OPEN-SOURCE.
C. DONNÉES D'ENTRAÎNEMENT EXTERNES.
D. INFRASTRUCTURES CLOUD.

Chaque maillon est un point d'attaque potentiel. Mesures :
- DUE DILIGENCE des fournisseurs (sécurité documentée, certifications, historique d'incidents).
- CONTRACTUALISATION CLAIRE des responsabilités (qui répond en cas d'incident?).
- VEILLE sur les vulnérabilités annoncées (CVE, disclosures).
- TESTS de validation des composants intégrés.

ARTICULATION AVEC LES NORMES :
A. ISO 27001 — couvre 80 % des contrôles de sécurité IA.
B. NIST CSF 2.0 — cadre cybersécurité général applicable.
C. NIST IR 8596 (Cyber AI Profile, draft Dec 2025) — adaptation spécifique au cyber-IA.
D. OWASP TOP 10 FOR LARGE LANGUAGE MODEL APPLICATIONS — vulnérabilités spécifiques aux LLM en production.
E. MITRE ATLAS — taxonomie des attaques sur les systèmes d'IA.

POINT JURIDIQUE — la Loi 25 oblige à prendre des « mesures de sécurité raisonnables eu égard à la sensibilité, à la finalité, à la quantité, à la répartition et au support des renseignements ». Pour un système d'IA traitant des RP, la conformité Loi 25 sur la sécurité passe par la mise en place des mesures décrites ici.

LIVRABLE TYPIQUE — POLITIQUE DE SÉCURITÉ IA — document combinant : analyse de risques, mesures techniques, procédures organisationnelles, plan de réponse aux incidents.
        """.strip(),
    },

    "m7_c7_cnil_conformite_incidents": {
        "module": 7, "ordre": 7, "langue": "fr",
        "titre": "CNIL — conformité globale et réponse aux incidents",
        "prereqs": ["m7_c1_cnil_avant_deploiement"],
        "texte": """
PHASE 7 — DÉMONTRER LA CONFORMITÉ ET RÉPONDRE AUX INCIDENTS.

Le guide CNIL « Achieving compliance » couvre la dimension finale : démontrer aux régulateurs et aux clients que le système est conforme, et savoir réagir lorsqu'un incident survient.

DEUX PILIERS :

PILIER 1 — DÉMONTRER LA CONFORMITÉ.

La conformité ne se déclare pas; elle se DÉMONTRE par des artefacts probants. Six livrables documentaires que la CNIL et la CAI examineront en cas d'enquête :

LIVRABLE 1 — ANALYSE D'IMPACT VIE PRIVÉE (DPIA / EFVP). Document central qui couvre :
- Description du traitement.
- Évaluation de la nécessité et proportionnalité.
- Évaluation des risques.
- Mesures de mitigation.
- Décision motivée.

LIVRABLE 2 — REGISTRE DES TRAITEMENTS — pour chaque traitement de RP : finalité, base légale, catégories de données, durées de conservation, destinataires.

LIVRABLE 3 — POLITIQUE DE CONFIDENTIALITÉ PUBLIQUE — accessible, claire, à jour.

LIVRABLE 4 — DOCUMENTATION TECHNIQUE — model card, data sheet, system card; logs de fonctionnement; rapports de tests.

LIVRABLE 5 — REGISTRE DES INCIDENTS — tous les incidents (notifiés ou non), avec mesures correctives et délais.

LIVRABLE 6 — PROCÉDURES INTERNES DOCUMENTÉES — politique IA, RACI, formation, veille réglementaire.

PRINCIPE DE RESPONSABILITÉ DOCUMENTAIRE (« accountability »). RGPD Art. 5(2) et Loi 25 — les organisations doivent être en mesure de DÉMONTRER leur conformité, pas seulement de l'affirmer. Cela signifie que la charge de la preuve repose sur l'organisation, pas sur l'autorité.

PILIER 2 — RÉPONSE AUX INCIDENTS.

Définition large : tout événement qui CAUSE OU CONTRIBUE À UN PRÉJUDICE pour une personne, ou qui PRÉSENTE UN RISQUE SÉRIEUX de préjudice. Inclut :
A. Fuites de données.
B. Décisions IA erronées causant un dommage.
C. Discrimination algorithmique avérée.
D. Sortie d'IA générative diffamatoire ou inexacte sur une personne nommée.
E. Compromission de sécurité.

PROCÉDURE EN SIX ÉTAPES :

ÉTAPE 1 — DÉTECTION.

Mécanismes :
A. Monitoring continu (M7 c4).
B. Plaintes des personnes affectées.
C. Signalements internes (whistleblowing).
D. Audits internes.
E. Alertes de fournisseurs ou tiers.

ÉTAPE 2 — ÉVALUATION.

Évaluer :
A. NATURE de l'incident — qu'est-ce qui s'est passé?
B. AMPLEUR — combien de personnes affectées?
C. SÉVÉRITÉ — quel niveau de préjudice?
D. DURÉE — combien de temps a duré l'incident?
E. CAUSE RACINE — pourquoi est-ce arrivé?

CRITÈRE LOI 25 — RISQUE SÉRIEUX DE PRÉJUDICE (RSP) :
- Sensibilité des RP touchés.
- Conséquences appréhendées.
- Probabilité d'utilisation préjudiciable.

ÉTAPE 3 — NOTIFICATION.

A. CAI / CNIL — si RSP, notification AVEC DILIGENCE (72 h en pratique).
B. PERSONNES AFFECTÉES — si RSP.
C. DIRECTION INTERNE et CONSEIL D'ADMINISTRATION pour les incidents majeurs.
D. PARTENAIRES contractuels si applicable.
E. ASSUREURS cyber.

CONTENU DE LA NOTIFICATION (Règlement de la CAI sur les incidents) :
- Description de l'incident, date, nature des RP touchés.
- Nombre de personnes touchées.
- Mesures prises pour atténuer le risque.
- Mesures que la personne peut prendre.
- Coordonnées du RPRP.

ÉTAPE 4 — DOCUMENTATION.

Tout incident — notifié ou non — doit être inscrit au REGISTRE DES INCIDENTS, conservé 5 ans (Loi 25 Art. 3.8).

ÉTAPE 5 — REMÉDIATION.

A. CONTAINMENT IMMÉDIAT (si pas encore fait).
B. CORRECTION TECHNIQUE (correctif, patch, ré-entraînement, retrait du modèle).
C. CORRECTION ORGANISATIONNELLE (procédures, formation, contrôles supplémentaires).
D. COMPENSATION ÉVENTUELLE des personnes affectées.

ÉTAPE 6 — TRANSPARENCE.

Pour les incidents PUBLICS d'envergure, communication publique sur :
- Ce qui s'est passé.
- Ce qui a été fait.
- Comment cela ne se reproduira pas.

La transparence renforce la confiance et contribue à la pédagogie sectorielle.

ARTICULATION AVEC LE PRINCIPE OECD DE DUE DILIGENCE GUIDANCE (février 2026) — la guidance OECD propose un cadre de DUE DILIGENCE en six étapes parfaitement alignée avec ces principes : intégrer, identifier, prévenir, suivre, communiquer, réparer.

CINQ PRINCIPES OPÉRATIONNELS DE LA CNIL — résumé pour démarrer :

1. PROTECTION DES DONNÉES PAR LA CONCEPTION (« privacy by design ») — intégrer vie privée et équité dès la conception, pas après.

2. RESPONSABILITÉ — désignation claire des responsabilités; documenter les décisions; être prêt à les justifier.

3. IA CENTRÉE SUR L'HUMAIN — les décisions automatisées soutiennent le jugement humain, ne le remplacent pas.

4. TRANSPARENCE POUR LA LÉGITIMITÉ — les personnes affectées méritent une information claire et compréhensible.

5. DISCIPLINE DE PROPORTIONNALITÉ — n'utilisez pas l'IA juste parce que c'est possible; utilisez-la quand c'est nécessaire et proportionné.

POSITIONNEMENT DE LA CNIL AU CANADA — bien que la CNIL soit l'autorité française, ses guides sont DIRECTEMENT TRANSPOSABLES dans un contexte canadien parce que :
A. La Loi 25 et le RGPD partagent l'esprit (transparence, consentement, droits, accountability).
B. Les pratiques techniques (chiffrement, anonymisation, monitoring) sont indépendantes de la juridiction.
C. La CAI cite régulièrement les positions de la CNIL et de l'EDPB dans ses propres décisions.

Pour Nord Paradigm, les guides CNIL constituent une SOURCE D'INSPIRATION OPÉRATIONNELLE pour structurer Brèche Pro et Prisme.
        """.strip(),
    },

})


# ══════════════════════════════════════════════════════════════════════════════
# MODULE 8 — SINGAPORE MODEL AI GOVERNANCE FRAMEWORK  (4 concepts, EN)
# ══════════════════════════════════════════════════════════════════════════════

CURRICULUM.update({

    "m8_c1_singapore_internal_governance": {
        "module": 8, "ordre": 1, "langue": "en",
        "titre": "Singapore MGF — internal governance structures",
        "prereqs": ["m1_c2_typologie_outils"],
        "texte": """
Singapore's Model AI Governance Framework (Model Framework, first released January 2019, second edition January 2020, dedicated agentic AI extension January 2026) is a practical, industry-focused framework for responsible AI deployment. Developed by Singapore's Infocomm Media Development Authority (IMDA) and Personal Data Protection Commission (PDPC) in partnership with the World Economic Forum Centre for the Fourth Industrial Revolution.

WHY STUDY THE SINGAPORE FRAMEWORK FROM CANADA:
A. Singapore is the WORLD-LEADING JURISDICTION on operational, industry-deployable AI governance frameworks. Its guidance is more PRACTICAL than NIST RMF (which is more conceptual) and more FLEXIBLE than EU AI Act (which is regulatory).
B. The framework is GROUND-TESTED — it has been adopted by hundreds of organizations across sectors (banking, healthcare, retail, public services).
C. It maps cleanly onto NIST AI RMF and ISO 42001 — a Quebec SME implementing one can borrow operational practices from the others.
D. Singapore positions its approach as a HUMAN-CENTRIC complement to risk-based regulation: balancing innovation with public trust.

DIMENSION 1 — INTERNAL GOVERNANCE STRUCTURES AND MEASURES.

The first dimension establishes the FOUNDATIONS for responsible AI within an organization. Seven elements:

ELEMENT 1 — AI GOVERNANCE STRUCTURES. Designate clear accountability:
A. BOARD-LEVEL OVERSIGHT — at least one director with explicit AI governance mandate. Becoming an enforcement expectation in 2026 (cf. IAPP Summit signals).
B. AI COMMITTEE — multidisciplinary (technical, legal, compliance, business); meets monthly or quarterly.
C. RESPONSIBLE PERSONS — named individuals for each AI system; accountable for outcomes.

ELEMENT 2 — RESOURCE ALLOCATION. Assign budget, personnel, and expertise. Common minimum: at least one full-time-equivalent role for AI governance, scaling with system complexity.

ELEMENT 3 — POLICIES AND PROCEDURES. Develop organizational AI ethics policies aligned with corporate values. Three layers typically:
A. AI ethics charter (corporate level, stable).
B. AI governance policy (management level, periodic update).
C. AI operating procedures (technical level, frequent update).

ELEMENT 4 — TRAINING AND COMPETENCY. Ensure workforce understands AI risks and governance responsibilities. Tiered approach:
A. ALL EMPLOYEES — awareness (1-2 hours yearly).
B. AI USERS — operational training (4-8 hours).
C. AI DEVELOPERS — technical training (16-40 hours).
D. AI GOVERNANCE LEADS — advanced certification (CIPP, CIPM, IAPP AIGP).

ELEMENT 5 — STAKEHOLDER ENGAGEMENT. Involve affected populations in governance decisions, including vulnerable groups. Mechanisms:
A. User research and design participation.
B. Stakeholder consultations.
C. Public reporting on AI deployments.

ELEMENT 6 — THIRD-PARTY MANAGEMENT. Establish requirements for AI vendors, data providers, infrastructure partners:
A. Security and privacy certifications.
B. Audit rights.
C. Incident notification commitments.
D. Termination conditions.

ELEMENT 7 — AUDIT AND MONITORING. Regular internal audits of AI systems for governance compliance. Frequency proportional to risk:
A. High-risk systems: at least annually.
B. Moderate-risk: every 18-24 months.
C. Low-risk: triennially.

KEY PRINCIPLE — Governance is not a compliance checklist but a CULTURAL COMMITMENT to responsible innovation. Organizations that treat governance as a paperwork exercise inevitably fail when scrutinized.

ALIGNMENT WITH NIST AI RMF — Dimension 1 of Singapore corresponds directly to the GOVERN function of NIST RMF. Both address: policies, accountability, training, stakeholder engagement, third-party management.

ALIGNMENT WITH ISO 42001 — Dimension 1 corresponds to ISO 42001 Domain A.2 (Policies) + A.3 (Internal Organization) + A.4 (Resources).

OPERATIONAL DOCUMENT — typically called « AI GOVERNANCE PROGRAM CHARTER ». A 5-15 page document covering:
- AI ethics principles.
- Governance structure (committee, roles, escalation).
- Policies and procedures inventory.
- Training program.
- Audit calendar.
- Reporting to executive and board.

FOR A QUEBEC SME — Dimension 1 corresponds in scope to what is required to comply with Loi 25 governance obligations (RPRP designation, EFVP processes, incident management) PLUS the broader AI-specific layer. A well-designed Loi 25 program is roughly 60-70 % of what Singapore Dimension 1 requires.

GAP TO ADDRESS BEYOND LOI 25:
A. AI-specific ethics policy (Loi 25 doesn't require it).
B. AI committee with technical expertise (Loi 25 mentions only the RPRP).
C. Tiered training program for AI roles.
D. Vendor governance specifically for AI providers.

POSITIONING FOR NORD PARADIGM — Dimension 1 of Singapore is what Brèche Pro should diagnose: does the client have the organizational structure to govern AI, beyond formal Loi 25 compliance?
        """.strip(),
    },

    "m8_c2_singapore_human_involvement": {
        "module": 8, "ordre": 2, "langue": "en",
        "titre": "Singapore MGF — levels of human involvement in decisions",
        "prereqs": ["m8_c1_singapore_internal_governance"],
        "texte": """
DIMENSION 2 — DETERMINING THE LEVEL OF HUMAN INVOLVEMENT IN AI-AUGMENTED DECISION-MAKING.

This dimension is Singapore's MOST DISTINCTIVE CONTRIBUTION to global AI governance. It provides a structured framework for deciding HOW MUCH HUMAN OVERSIGHT a given AI use case requires.

The framework distinguishes FOUR INVOLVEMENT LEVELS based on impact and reversibility of decisions:

LEVEL 1 — HUMAN-IN-THE-LOOP.
The AI RECOMMENDS, the human DECIDES. Each AI suggestion is reviewed by a human BEFORE execution. The human retains final decision authority and can override AI recommendations.

USED WHEN:
A. Decisions have SIGNIFICANT LEGAL consequences (e.g., loan denial, dismissal, insurance pricing).
B. Decisions have SIGNIFICANT FINANCIAL consequences for the affected party.
C. Decisions have SIGNIFICANT HEALTH consequences (e.g., diagnostic recommendations).
D. Decisions affect vulnerable populations (children, patients, employees).
E. Decisions are NOT EASILY REVERSIBLE.

EXAMPLE — a loan officer reviews each AI-generated credit-scoring recommendation before approving or denying the application. The officer has the data, the AI explanation, and the authority to override.

ALIGNMENT WITH LOI 25 — for « decisions based exclusively on automated processing » (Art. 12.1), human-in-the-loop with SUBSTANTIVE review (not rubber-stamping) is required to escape the article's transparency obligations. Without substantive review, the article applies and the organization must inform affected persons and provide explanation on request.

LEVEL 2 — HUMAN-ON-THE-LOOP.
The AI MAKES decisions; the human MONITORS and can intervene. The human reviews AI decisions AFTER THE FACT and can correct mistakes.

USED WHEN:
A. Decisions are REVERSIBLE.
B. Decisions have MODERATE CONSEQUENCES (operational efficiency, resource allocation).
C. The volume of decisions makes case-by-case review IMPRACTICAL.

EXAMPLE — an insurance claims processor lets the AI auto-approve simple claims under $500. A human reviews a sample of approved claims weekly and can revoke approvals.

LEVEL 3 — HUMAN-OVER-THE-LOOP.
The AI MAKES decisions; the human PROVIDES PERIODIC SUPERVISORY OVERSIGHT.

USED WHEN:
A. Decisions are LOW-IMPACT.
B. Decisions are REVERSIBLE.
C. The volume is HIGH (millions of decisions per day).

EXAMPLE — a recommendation engine suggests products to e-commerce users. Engineers periodically (weekly, monthly) audit the recommendation patterns to detect anomalies, drift, or unintended bias.

LEVEL 4 — FULLY AUTONOMOUS.
NO HUMAN INVOLVEMENT in individual decisions. Used only in SPECIFIC, LOW-RISK CONTEXTS. Even autonomous systems require GOVERNANCE OVERSIGHT (monitoring, audit, decommissioning authority).

USED WHEN:
A. Decisions have minimal individual impact.
B. Decisions are highly reversible.
C. Volume justifies pure automation.
D. Quality and risk thresholds are well-characterized.

EXAMPLE — automated content moderation that filters spam in a social network. Even fully autonomous, it requires: thresholds set by humans, periodic audits, kill-switches, and a human appeals process.

DETERMINING THE APPROPRIATE LEVEL — five factors:

FACTOR 1 — NATURE AND REVERSIBILITY OF HARM. High harm + low reversibility → more human involvement.

FACTOR 2 — IMPACT ON VULNERABLE POPULATIONS. Always pushes toward higher involvement.

FACTOR 3 — OPERATIONAL FEASIBILITY. Can the process scale with the proposed level of human review?

FACTOR 4 — REGULATORY REQUIREMENTS. Some sectors (medical diagnoses, judicial decisions) mandate human-in-the-loop by law.

FACTOR 5 — ORGANIZATIONAL RISK TOLERANCE. Conservative organizations choose more involvement; risk-tolerant ones less.

DECISION MATRIX (illustrative):

| Use case | Recommended level |
|---|---|
| Credit decision for individual | Human-in-the-loop |
| CV pre-screening (top 50 from 500) | Human-on-the-loop |
| Product recommendation | Human-over-the-loop |
| Spam filter | Fully autonomous |
| Medical diagnosis | Human-in-the-loop |
| Autonomous driving (highway) | Human-on-the-loop (current state) |
| Industrial robot in cage | Human-over-the-loop |

GOTCHAS — common mistakes:

MISTAKE 1 — Choosing the wrong level. Most organizations default to « human-on-the-loop » without thinking. This is too permissive for high-impact decisions and inefficient for low-impact ones.

MISTAKE 2 — Rubber-stamping at human-in-the-loop. The human is in the loop nominally but does not have the time, information, or authority to actually review. The CAI / CNIL and the EU AI Act treat this as functionally equivalent to fully autonomous.

MISTAKE 3 — Drift in the involvement level. Initially human-in-the-loop, but over months the human becomes a rubber stamp as workload grows. Solution: periodic audits of HUMAN OVERRIDE RATE — if the human always agrees with AI, they are no longer providing real oversight.

MISTAKE 4 — Insufficient training for human reviewers. The human must UNDERSTAND the system to provide meaningful oversight. Training is non-optional.

ALIGNMENT WITH OTHER FRAMEWORKS:
A. EU AI Act Art. 14 (human oversight for high-risk systems) — operationalized by Singapore's framework.
B. Loi 25 Art. 12.1 — Singapore's framework helps determine whether the « exclusively automated » threshold is crossed.
C. OECD Principle 1.5 (accountability) — Singapore makes the principle concrete.
D. NIST RMF GOVERN function — Singapore provides decision criteria.

ASSESSMENT TOOL — for each AI system in the inventory, document the involvement level and justify the choice. This should be part of the EFVP / AIA. Quarterly review of override rates and performance.

POSITIONING FOR NORD PARADIGM — the four-level framework is an EXCELLENT WORKSHOP TOOL. Have the client classify each of their AI systems on this scale, then discuss whether the classification matches the actual practice.
        """.strip(),
    },

    "m8_c3_singapore_operations": {
        "module": 8, "ordre": 3, "langue": "en",
        "titre": "Singapore MGF — operations management and AI Verify",
        "prereqs": ["m8_c1_singapore_internal_governance"],
        "texte": """
DIMENSION 3 — OPERATIONS MANAGEMENT.

The third dimension covers the OPERATIONAL LIFECYCLE of AI systems: from data preparation through model development, deployment, and ongoing maintenance. It is the DIMENSION RICHEST IN PRACTICAL TOOLS.

FIVE SUB-AREAS:

SUB-AREA 1 — DATA GOVERNANCE.
A. DATA QUALITY — accuracy, completeness, consistency, freshness, representativeness.
B. BIAS DETECTION AND MITIGATION in training data — testing for demographic, geographic, temporal biases.
C. DATA LINEAGE TRACKING — where does the data come from? How was it transformed?
D. FAIRNESS ASSESSMENT — does the system perform equally across population subgroups?

OVERLAP with NIST RMF MAP function and ISO 42001 Domain A.7.

SUB-AREA 2 — MODEL DEVELOPMENT AND TESTING.
A. MODEL ROBUSTNESS — performs consistently under expected conditions.
B. REPRODUCIBILITY — same data → same model with same results.
C. EXPLAINABILITY — stakeholders can understand decision-making.
D. ADVERSARIAL RESILIENCE — can the model be fooled or attacked?

SUB-AREA 3 — ALGORITHM AUDITS (ANNEX B of the framework).

Singapore distinguishes between TWO TYPES of audit:
A. ROUTINE AUDIT — periodic verification of compliance with governance policies.
B. FORENSIC AUDIT — detailed examination of system behaviour, typically triggered by an incident or regulatory request.

KEY PRINCIPLE — algorithm audits are conducted ONLY WHEN NECESSARY (not as routine), require SPECIALIZED TECHNICAL EXPERTISE, and produce documented findings actionable by the audited organization.

SUB-AREA 4 — PERFORMANCE MONITORING AND MAINTENANCE.
A. Track model performance over time for degradation or drift.
B. Monitor for bias emergence as data distributions shift.
C. Version control and change management for model updates.
D. Incident response procedures.

This is the operational equivalent of the NIST MEASURE function.

SUB-AREA 5 — TRANSPARENCY AND EXPLAINABILITY.
A. USER UNDERSTANDING — users must understand what the AI system does and its limitations.
B. DOCUMENTATION — clear descriptions of model objectives, capabilities, limitations.
C. EXPLAINABILITY METHODS — feature importance, decision trees, human-interpretable rules where feasible.
D. DISCLOSURE — inform affected populations that AI is being used in decisions affecting them.

THE AI VERIFY PROGRAM — Singapore's most distinctive operational asset.

AI VERIFY is a TESTING FRAMEWORK and TOOLKIT released by IMDA and Singapore's PDPC. It validates AI systems against 11 trustworthy AI principles aligned with international frameworks (OECD, EU AI Act, NIST RMF).

THE 11 PRINCIPLES validated by AI Verify:
1. Transparency
2. Explainability
3. Repeatability / reproducibility
4. Safety
5. Security
6. Robustness
7. Fairness
8. Data governance
9. Accountability
10. Human agency and oversight
11. Inclusive growth, societal and environmental wellbeing

THE TOOLKIT consists of:
A. PROCESS CHECKS — questionnaires that document organizational practices.
B. TECHNICAL TESTS — automated tests of model properties (fairness, robustness, explainability).
C. REPORT GENERATION — standardized reports for internal use, audits, customer disclosures.

The toolkit is OPEN-SOURCE and freely available. It runs locally to preserve confidentiality of models and data.

FOR A QUEBEC SME — AI Verify is one of the FEW FREE, INDUSTRY-GRADE TESTING TOOLS available. It can be used:
A. Internally — to systematically test AI systems before deployment.
B. With customers — to demonstrate trustworthiness through standardized reports.
C. As a pre-audit — to identify gaps before formal ISO 42001 or other certifications.

LLM STARTER KIT — Singapore additionally publishes a LLM STARTER KIT for organizations beginning to deploy large language models. Practical guidance on:
A. Use case selection.
B. Vendor evaluation.
C. Integration patterns.
D. Risk mitigation.
E. Operational monitoring.

ALIGNMENT WITH OTHER FRAMEWORKS:
A. NIST RMF MEASURE function — AI Verify operationalizes the measurement function.
B. EU AI Act Art. 9, 10, 15 — AI Verify provides evidence for conformity assessment.
C. ISO 42001 Domain A.5, A.6, A.7 — AI Verify supports impact assessment, lifecycle management, data governance.
D. CNIL Phase 4 (production) — AI Verify supports operational monitoring.

OPERATIONS MAINTENANCE — TYPICAL OUTPUTS:
A. MODEL CARDS for each model.
B. DATA SHEETS for each dataset.
C. AUDIT REPORTS (internal, periodic).
D. INCIDENT REPORTS.
E. TRENDED PERFORMANCE METRICS dashboards.

FOR NORD PARADIGM — operations management is where Brèche Pro provides the deepest diagnostic. Most clients have weak operations management even when their policies and EFVPs look good. The gap between « policy on paper » and « operational practice » is where most non-compliance hides.
        """.strip(),
    },

    "m8_c4_singapore_stakeholder": {
        "module": 8, "ordre": 4, "langue": "en",
        "titre": "Singapore MGF — stakeholder communication and use cases",
        "prereqs": ["m8_c1_singapore_internal_governance"],
        "texte": """
DIMENSION 4 — STAKEHOLDER INTERACTION AND COMMUNICATION.

The fourth dimension addresses HOW THE ORGANIZATION COMMUNICATES with the various parties affected by its AI systems. Singapore emphasizes that responsible AI is a SOCIO-TECHNICAL PRACTICE, not just a technical exercise.

INTERNAL STAKEHOLDERS:

STAKEHOLDER 1 — EXECUTIVE SPONSORS AND BOARD MEMBERS need governance oversight. They make resource decisions, approve high-impact deployments, and answer to shareholders / public. Communication: quarterly governance reports + escalation for major incidents or strategic shifts.

STAKEHOLDER 2 — SYSTEM DEVELOPERS need to understand ethical implications of their work. Communication: training, design reviews, ethics consultations during development.

STAKEHOLDER 3 — OPERATIONS TEAMS need to monitor performance and escalate issues. Communication: dashboards, alerts, incident response procedures, runbooks.

STAKEHOLDER 4 — HR AND COMPLIANCE TEAMS need to understand applicable regulations. Communication: compliance training, regulatory updates, audit findings.

EXTERNAL STAKEHOLDERS:

STAKEHOLDER 5 — END USERS of AI systems need to understand capabilities and limitations. Communication: product documentation, in-app disclosures, user education.

STAKEHOLDER 6 — AFFECTED INDIVIDUALS (those whose data is processed, whose lives are affected) deserve transparency. Communication: privacy notices, decision explanations on request, recourse mechanisms.

STAKEHOLDER 7 — REGULATORS need evidence of governance compliance. Communication: structured documentation (EFVPs, AIAs, model cards, audit reports), regulatory filings, incident notifications.

STAKEHOLDER 8 — GENERAL PUBLIC benefits from understanding how AI systems affect society. Communication: public reports, transparency initiatives, participation in industry forums.

COMMUNICATION APPROACH — FIVE PRINCIPLES:

PRINCIPLE 1 — TAILOR INFORMATION TO AUDIENCE. Highly technical for developers, accessible for users, structured for regulators. Avoid one-size-fits-all communications.

PRINCIPLE 2 — TIMING. Communicate EARLY (during design) — not only when problems arise. Engagement during development surfaces concerns when they're cheap to address.

PRINCIPLE 3 — MULTIPLE CHANNELS. Different stakeholders prefer different touchpoints. Web disclosures, training programs, direct meetings, regulatory filings, public reports — use them all where appropriate.

PRINCIPLE 4 — ACCOUNTABILITY. Communication must be TRANSPARENT, NOT MISLEADING MARKETING. The CAI, CNIL, and EU AI Office have all signaled they treat misleading transparency claims as more serious than honest disclosure of limitations.

PRINCIPLE 5 — TWO-WAY. Listen, not just broadcast. Stakeholder feedback drives system improvement.

THE COMPENDIUM OF USE CASES — Singapore's most operational deliverable.

The Singapore PDPC publishes a COMPENDIUM of use cases — real-world examples of organizations implementing AI governance practices aligned with the Model Framework. Two volumes published; periodically updated.

VOLUME 1 (2020) — covers initial use cases across banking, insurance, retail, healthcare.

VOLUME 2 — extends to additional sectors and addresses GenAI considerations.

VALUE OF THE COMPENDIUM:
A. CONCRETE EXAMPLES — abstract principles become actionable.
B. CROSS-SECTORAL LEARNING — practices that work in one sector transferable to others.
C. BENCHMARKING — organizations can compare their practices.
D. WORKSHOP MATERIAL — readymade case studies for team training.

DEDICATED AGENTIC AI EXTENSION (January 2026) — Singapore's MODEL AI GOVERNANCE FRAMEWORK FOR AGENTIC AI v1.0.

Published 22 January 2026. The FIRST GOVERNMENT FRAMEWORK DEDICATED TO AI AGENT GOVERNANCE worldwide.

FOUR CORE PRINCIPLES:
A. BOUND RISKS UPFRONT — define agent scope and limits before deployment.
B. HUMAN ACCOUNTABILITY — every agent has a responsible human; no diffused responsibility.
C. TECHNICAL CONTROLS — implement runtime safeguards (sandboxing, kill-switches, access scope).
D. END-USER RESPONSIBILITY — users must understand they are interacting with an autonomous agent.

This framework is covered in detail in Module 11.

IMPLEMENTATION AND SELF-ASSESSMENT GUIDE FOR ORGANISATIONS (ISAGO).

Singapore publishes a SELF-ASSESSMENT GUIDE that allows organizations to evaluate their alignment with the Model Framework. Sector-specific guidance for finance, healthcare, retail, government.

USAGE PATTERN — typical for a Quebec SME:
1. Conduct ISAGO self-assessment (1-2 days).
2. Identify gaps with current practices.
3. Prioritize remediation based on risk.
4. Use AI Verify for technical testing.
5. Document outcomes in policies and procedures.
6. Periodic re-assessment (annual minimum).

POSITIONING FOR NORD PARADIGM — the Singapore framework is an EXCELLENT BASELINE for Brèche Pro deliverables. Many of its components (ISAGO self-assessment, AI Verify testing, use case compendium) can be adapted as Nord Paradigm tools without licensing fees.

COMPARATIVE POSITIONING:
A. MORE OPERATIONAL than NIST RMF — NIST is risk-focused; Singapore is implementation-focused.
B. LESS PRESCRIPTIVE than EU AI Act — EU AI Act is regulatory; Singapore is voluntary guidance.
C. MORE STRUCTURED than OECD — OECD Principles are values-based; Singapore provides specific governance structures.
D. CROSS-SECTOR APPLICABLE — applies to any industry, any organization size.

KEY LESSON — Singapore's approach emphasizes that responsible AI is ACHIEVABLE across organizations of different maturity levels. It doesn't require perfect systems or perfect data; it requires HONEST ASSESSMENT, ONGOING MONITORING, and COMMITMENT TO IMPROVEMENT.

REGULATORY CONTEXT — Singapore operates:
A. Personal Data Protection Act (PDPA) — Singapore's data protection law (similar to GDPR in intent, simpler in scope).
B. Sectoral guidance (banking, healthcare, etc.).
C. AI governance strategy (2019 + updates).
D. International alignment with OECD AI principles and global trends.
        """.strip(),
    },

})


# ══════════════════════════════════════════════════════════════════════════════
# MODULE 9 — UK ICO and DATA (USE & ACCESS) ACT 2025  (3 concepts, EN)
# ══════════════════════════════════════════════════════════════════════════════

CURRICULUM.update({

    "m9_c1_uk_duaa_2025": {
        "module": 9, "ordre": 1, "langue": "en",
        "titre": "UK Data (Use & Access) Act 2025 — UK/EU regulatory divergence",
        "prereqs": ["m1_c3_approches_reglementaires"],
        "texte": """
The DATA (USE AND ACCESS) ACT 2025 (DUAA 2025) came into law in the United Kingdom on 19 JUNE 2025, with phased implementation through June 2026. It SIGNIFICANTLY CHANGES the UK's approach to automated decision-making compared to the EU and creates a notable regulatory split between UK and EU.

WHY STUDY THE UK FROM CANADA:
A. The UK is a major AI market and a competitor to the EU. Canadian companies often have UK operations or customers.
B. The UK's APPROACH (sectoral, lighter-touch) is closer to the United States and parts of the Canadian federal posture than to the EU.
C. The UK/EU DIVERGENCE on automated decision-making creates a STRATEGIC CHOICE for international organizations: where to operate, how to position.
D. The UK ICO has produced PRACTICAL TOOLS (cf. M9 c3) directly transposable to Canadian compliance work.

CONTEXT — POLICY DIRECTION.

The UK chose in 2023 a « PRO-INNOVATION APPROACH » — sectoral regulation rather than horizontal AI law. The DUAA 2025 is the legal embodiment of this approach. Three priorities:
A. SIMPLIFY GDPR-style obligations to reduce business burden.
B. ENABLE GROWTH in data-driven industries.
C. MAINTAIN ADEQUACY with EU GDPR (essential for UK-EU data flows post-Brexit).

KEY CHANGES IN AUTOMATED DECISION-MAKING:

THE OLD UK GDPR REGIME (pre-DUAA) — based on EU GDPR Article 22:
A. Decisions based « solely » on automated processing prohibited by default.
B. Three exceptions: contractual necessity, explicit consent, legal authorization.
C. Mandatory safeguards: human intervention, right to obtain explanation, right to contest.

THE NEW UK REGIME (post-DUAA):
A. RESTRICTIONS APPLY ONLY where significant decisions are based « entirely or partly » on the processing of SPECIAL CATEGORY DATA, unless certain conditions are met.
B. The default position is now PERMITTED (with safeguards), not prohibited.
C. Special category data still triggers stricter requirements.

UK/EU DIVERGENCE — concrete impact:

A SIMILAR USE CASE — automated CV pre-screening using non-sensitive data — is treated differently:
A. EU GDPR Art. 22 — restrictions APPLY by default; exception or explicit consent required.
B. UK DUAA 2025 — restrictions apply ONLY if special category data is involved. CV screening using only education/experience data faces MUCH LIGHTER restrictions.

This creates an OPERATIONAL CHOICE:
A. UK-only deployment — easier compliance, faster time to market.
B. EU deployment — heavier obligations.
C. Both UK and EU — most organizations align with the higher (EU) standard for simplicity.

OTHER DUAA 2025 PROVISIONS:

PROVISION 1 — STATUTORY CODE OF PRACTICE ON ADM/AI (expected autumn 2025, in development).

The DUAA mandates the ICO to produce a binding code of practice on automated decision-making and AI. The code will provide:
A. PRACTICAL GOOD PRACTICE GUIDANCE for AI development and deployment.
B. CLARIFICATION of when restrictions apply.
C. SAFE HARBOURS for organizations following the code.

This code, when finalized, becomes a DE FACTO STANDARD even for organizations not technically required to follow it.

PROVISION 2 — COPYRIGHT AND AI.

The DUAA does NOT create new copyright rules but mandates a STRUCTURED PROCESS for future reform. The government declined statutory transparency obligations (e.g., requiring AI providers to disclose training data) and rejected creating a new AI copyright regulator for now. This is a significant divergence from EU AI Act Art. 53 (which mandates copyright policy and training data summary).

PROVISION 3 — RESEARCH AND INNOVATION EXEMPTIONS.

DUAA expands exemptions for AI research, particularly when conducted in approved sandboxes or with academic partners.

PROVISION 4 — SUBJECT ACCESS REQUEST CHANGES.

DUAA modifies how organizations respond to subject access requests, including for AI-related processing. Some adjustments lighten the burden on organizations.

INTERNATIONAL COORDINATION.

In FEBRUARY 2026, the ICO co-signed a JOINT STATEMENT on AI-generated imagery with 61 data protection authorities globally, addressing risks of non-consensual AI-generated images and videos. This signals that despite domestic divergence on ADM, the ICO remains a coordinated player on cross-border AI risks.

POSITIONING FOR A QUEBEC SME:

SCENARIO 1 — UK CUSTOMERS, NO EU EXPOSURE. The DUAA 2025 light-touch regime applies. Easier to deploy ADM systems with non-sensitive data. Loi 25 obligations (RPRP, EFVP, Art. 12.1) still apply for Quebec residents.

SCENARIO 2 — UK + EU CUSTOMERS. Most organizations choose to comply with the HIGHER (EU) standard, applying it uniformly. The DUAA's lighter regime offers little operational benefit since EU compliance dominates.

SCENARIO 3 — DEVELOPMENT PARTNERSHIP WITH UK ENTITIES. UK research exemptions may enable joint R&D arrangements that would be more constrained under EU rules.

KEY MONITORING POINTS:
A. Publication of the ICO's STATUTORY CODE OF PRACTICE on ADM/AI.
B. ICO ENFORCEMENT ACTIONS interpreting the new regime.
C. UK COURT DECISIONS clarifying « significant » and « special category data » in the AI context.
D. POSSIBLE RECONVERGENCE if EU pressure leads UK to tighten rules.

POSITIONING FOR NORD PARADIGM — for clients with multi-jurisdictional operations, the UK/EU divergence is a strategic advisory opportunity. Most Canadian clients should adopt EU-level governance as baseline, but UK-only operations may benefit from a leaner approach.
        """.strip(),
    },

    "m9_c2_uk_ico_strategy": {
        "module": 9, "ordre": 2, "langue": "en",
        "titre": "UK ICO — strategy and foundation model engagement",
        "prereqs": ["m9_c1_uk_duaa_2025"],
        "texte": """
The UK INFORMATION COMMISSIONER'S OFFICE (ICO) is the UK's data protection authority. Like the CAI in Quebec or the CNIL in France, it enforces the country's privacy law (UK GDPR, modified by DUAA 2025) and increasingly oversees AI compliance. The ICO is among the WORLD'S MOST PROACTIVE regulators on AI engagement.

ICO'S AI AND BIOMETRICS STRATEGY UPDATE (March 2026).

The ICO published a strategic update in March 2026 outlining its AI and biometrics approach for the next 24-36 months. Three priorities:

PRIORITY 1 — DEVELOPMENT OF THE MANDATORY AI/ADM CODE OF PRACTICE (under DUAA 2025). The ICO is consulting with industry, civil society, and academic experts. Final code expected late 2025 or early 2026.

PRIORITY 2 — ENGAGEMENT WITH FOUNDATION MODEL DEVELOPERS. The ICO is currently engaging with 11 MAJOR AI FOUNDATION MODEL DEVELOPERS to:
A. Build EVIDENCE about their approaches to data protection compliance.
B. Seek ASSURANCES on steps to mitigate data protection harms.
C. UNDERSTAND the practical operations of large-scale model training.
D. INFORM future regulatory and code-of-practice development.

The list of 11 developers is not fully public, but credible reports suggest it includes OpenAI, Anthropic, Google, Microsoft, Meta, Cohere, Mistral, and major UK / European foundation model developers. This engagement DOES NOT presume non-compliance; it is an INFORMATION-GATHERING and STANDARDS-SETTING exercise.

PRIORITY 3 — BIOMETRIC TECHNOLOGIES. Particular focus on:
A. Facial recognition in retail and public spaces.
B. Biometric authentication in financial services.
C. Voice analysis tools.
D. Worker biometric monitoring.

ICO ACTION 1 — INVESTIGATIONS AND ENFORCEMENT.

The ICO uses a graduated approach:
A. GUIDANCE first — public guidance documents.
B. INFORMAL ENGAGEMENT — discussions with organizations.
C. FORMAL ENFORCEMENT — including monetary penalties (up to 4 % of worldwide turnover under UK GDPR; specific lower caps under DUAA for certain breaches).

PUBLIC ENFORCEMENT TRENDS visible in 2024-2026:
A. Multiple enforcement actions on facial recognition without proper basis.
B. Sanctions on automated decisions without transparency.
C. Investigations into chatbot deployments without consent or impact assessment.
D. Joint investigations with international counterparts on cross-border AI harms.

ICO ACTION 2 — REGULATORY SANDBOXES.

The ICO operates a REGULATORY SANDBOX program that allows companies to test AI products under the ICO's supervision. Benefits:
A. Reduced enforcement risk during testing.
B. Direct ICO feedback on compliance approaches.
C. Industry signaling of « ICO-approved » products.

The sandbox is OPEN TO INTERNATIONAL COMPANIES with UK operations. Quebec SMEs with UK customers can apply.

ICO ACTION 3 — COORDINATION WITH OTHER REGULATORS.

The ICO actively coordinates with:
A. Competition and Markets Authority (CMA) — for AI competition issues.
B. Financial Conduct Authority (FCA) — for AI in financial services.
C. Medicines and Healthcare Regulatory Agency (MHRA) — for medical AI.
D. International counterparts — CNIL, CAI, OPC, EDPB, etc.

This MULTI-REGULATOR APPROACH is distinctive. The UK does not have a single AI regulator; it has a NETWORK of regulators with overlapping authorities.

ICO PUBLICATIONS FOR PRACTITIONERS.

Beyond strategy documents, the ICO publishes a rich library of operational guidance:
A. AI AND DATA PROTECTION TOOLKIT (versions 1.0, 1.1; cf. M9 c3).
B. EXPLAINING DECISIONS MADE WITH AI — practical guidance for explainability.
C. DATA PROTECTION IMPACT ASSESSMENT GUIDANCE — for AI projects.
D. ANONYMISATION AND PSEUDONYMISATION CODE OF PRACTICE.
E. AGE APPROPRIATE DESIGN CODE — for AI products affecting children.
F. CHILDREN'S CODE assessment templates.

These documents are FREELY AVAILABLE and represent some of the BEST OPERATIONAL GUIDANCE worldwide on AI compliance.

DIFFERENCES BETWEEN ICO AND CNIL APPROACHES:

A. CNIL is more PHILOSOPHICAL / RIGHTS-BASED. ICO is more PRAGMATIC / BUSINESS-FOCUSED.
B. CNIL publishes lifecycle-stage guides. ICO publishes risk-based and practical-tool guides.
C. CNIL emphasizes consent and proportionality. ICO emphasizes risk management and accountability.
D. CNIL operates within the EU AI Act framework. ICO operates within the UK's lighter-touch framework.

For a Canadian organization, BOTH approaches are valuable to study. The CNIL provides depth; the ICO provides practical tools.

POSITIONING FOR A QUEBEC SME:

A. UK-FOCUSED OPERATIONS — engage with ICO guidance directly. Consider regulatory sandbox if developing novel AI products.

B. UK + EU OPERATIONS — use ICO toolkit (cf. M9 c3) as practical implementation guide; comply with the higher EU standard.

C. CANADIAN-FOCUSED OPERATIONS — use ICO toolkit AS A PRACTICAL TEMPLATE for Loi 25 / federal Canadian compliance work. The toolkit's structure transposes well to Canadian context.

D. SELLING AI TO UK GOVERNMENT — UK government has its own AI procurement standards (separate from ICO scope). Familiarity with ICO compliance posture is necessary but not sufficient.

POSITIONING FOR NORD PARADIGM — the ICO's TOOLS AND GUIDANCE are a TREASURE TROVE for client deliverables. The Risk Toolkit (covered in next concept) is particularly valuable.

KEY MONITORING POINTS for 2026-2027:
A. Publication of the mandatory AI/ADM Code of Practice.
B. Outcomes of foundation model engagement (publicly reported assessments).
C. New enforcement actions setting precedent.
D. Updates to the Risk Toolkit and related practical tools.
        """.strip(),
    },

    "m9_c3_uk_ico_risk_toolkit": {
        "module": 9, "ordre": 3, "langue": "en",
        "titre": "UK ICO AI and Data Protection Risk Toolkit v1.1",
        "prereqs": ["m9_c2_uk_ico_strategy"],
        "texte": """
The ICO AI AND DATA PROTECTION RISK TOOLKIT version 1.1 is a PRACTICAL EXCEL-BASED ASSESSMENT TOOL that maps data protection risks to UK GDPR obligations across four AI lifecycle stages. Released by the ICO and updated April 2026, it is one of the MOST OPERATIONAL TOOLS available globally for AI compliance work.

WHY THE TOOLKIT IS VALUABLE:

A. CONCRETE — 32 STRUCTURED RISK STATEMENTS rather than abstract principles.
B. FREE — released under open license; no proprietary tooling required.
C. EXCEL-BASED — accessible to any organization, no specialized software needed.
D. LIFECYCLE-ORGANIZED — risks mapped to specific development phases.
E. UK GDPR REFERENCED — each risk linked to specific GDPR articles.
F. TEAM-USABLE — designed for collaboration across functions (technical, legal, compliance, business).

STRUCTURE OF THE TOOLKIT.

Each risk statement includes:
A. RISK STATEMENT — clear description of the risk.
B. UK GDPR ARTICLE REFERENCE — which legal provision applies.
C. RISK ASSESSMENT SUMMARY column — for documenting findings.
D. RISK RATING — High / Medium / Low / N/A.
E. COMPLETION STATUS tracking.

THE FOUR LIFECYCLE STAGES (and their risks):

STAGE 1 — BUSINESS REQUIREMENTS AND DESIGN (Risks 1.1 — 1.8).

Covers planning and design phase. Eight risks:
1.1 ACCOUNTABILITY — clear identification of data controller, AI development responsibilities, governance structure.
1.2 PURPOSE LIMITATION — AI purposes well-defined and necessary; secondary use risks identified.
1.3 FAIRNESS — fairness considerations integrated from design.
1.4 TRANSPARENCY — affected individuals informed of AI use; explanations planned.
1.5 SECURITY — data and model security designed in (not bolted on).
1.6 DATA MINIMISATION — only necessary data planned for use.
1.7 INDIVIDUAL RIGHTS — design enables exercise of rights (access, rectification, opposition, etc.).
1.8 OTHER LEGAL OBLIGATIONS — compliance with sector-specific rules (financial, health, employment).

STAGE 2 — DATA ACQUISITION AND PREPARATION.

Covers obtaining and preparing training data. Major risks:
- DATA SOURCING legality and quality.
- CONSENT for personal data, especially special category data.
- ACCURACY of training data.
- BIAS in collected data.
- SPECIAL CATEGORY DATA additional safeguards.
- INTERNATIONAL TRANSFERS of training data.

STAGE 3 — TRAINING AND TESTING.

Covers model development. Major risks:
- MODEL VALIDATION methodology.
- BIAS TESTING across sub-populations.
- DOCUMENTATION of choices and trade-offs.
- PERFORMANCE MONITORING during training.
- DRIFT DETECTION.
- SECURITY of models in development.

STAGE 4 — DEPLOYMENT AND MONITORING.

Covers production operation. Major risks:
- ONGOING MONITORING and drift detection.
- INCIDENT RESPONSE procedures.
- HUMAN OVERSIGHT effectiveness.
- USER COMMUNICATIONS and explanations.
- DATA SUBJECT REQUEST handling.
- DECOMMISSIONING when system retired.

INTEGRATION WITH DPIA — the toolkit is designed to INTEGRATE WITH DPIA REQUIREMENTS UNDER ARTICLE 35 of UK GDPR. Many of the risks identified in the toolkit map directly to DPIA documentation sections.

CANADIAN APPLICABILITY — DIRECTLY TRANSPOSABLE.

The toolkit's risk categories MAP CLOSELY to Loi 25 and PIPEDA obligations. With minimal modification:
A. UK GDPR Art. 5 (lawfulness, fairness, transparency) → Loi 25 Art. 4-12 (consent and finalities).
B. UK GDPR Art. 22 (automated decision-making) → Loi 25 Art. 12.1.
C. UK GDPR Art. 35 (DPIA) → Loi 25 EFVP requirements.
D. UK GDPR Art. 32 (security) → Loi 25 Art. 10 (security measures).
E. UK GDPR Art. 33-34 (breach notification) → Loi 25 Art. 3.5 (incident notification).

For Nord Paradigm, the toolkit is a READY-TO-USE TEMPLATE for Brèche product governance gap identification. With approximately 20 % adaptation (terminology, legal references), it becomes a Canadian equivalent.

USING THE TOOLKIT IN PRACTICE:

STEP 1 — DOWNLOAD the latest version from the ICO website.

STEP 2 — ASSEMBLE THE TEAM. At minimum:
A. Project owner (business side).
B. Technical lead (data scientist, ML engineer).
C. Legal / compliance representative (DPO / RPRP).
D. Information security representative.

STEP 3 — WORK THROUGH STAGES SEQUENTIALLY. Discuss each risk; document the team's assessment; rate the residual risk (after mitigations).

STEP 4 — IDENTIFY GAPS. For each high-rated residual risk, define remediation actions with owner and deadline.

STEP 5 — DOCUMENT AND APPROVE. The completed toolkit serves as the PRIMARY EVIDENCE of due diligence in case of regulatory inquiry.

STEP 6 — REVISIT PERIODICALLY. Re-assess at major changes (new data sources, new use case, new model version) and at minimum annually.

LIMITATIONS — the toolkit is COMPREHENSIVE but generic. It does NOT replace:
A. Sector-specific regulatory requirements (FCA, MHRA, etc.).
B. Detailed technical risk assessments (e.g., adversarial robustness testing).
C. Regulatory engagement (sandbox application, ICO consultation).

But it provides a RIGOROUS BASELINE that demonstrates the organization has considered the relevant risks systematically.

FUTURE EVOLUTION — the toolkit is updated periodically as regulatory expectations evolve. Version 2.0 expected to incorporate:
A. Specific guidance on FOUNDATION MODELS.
B. AGENTIC AI risk additions.
C. Updated reference to the UK statutory CODE OF PRACTICE on AI/ADM (when published).
D. Alignment with EU AI Act for organizations operating in both jurisdictions.

POSITIONING FOR NORD PARADIGM — adopt the ICO toolkit as the BACKBONE TOOL for Brèche Pro engagements. Adapt the legal references to Loi 25 / PIPEDA / federal context. The Excel format makes it tangible for clients and easy to update collaboratively.
        """.strip(),
    },

})


# ══════════════════════════════════════════════════════════════════════════════
# MODULE 10 — MISE EN ŒUVRE PRATIQUE  (4 concepts, FR)
# ══════════════════════════════════════════════════════════════════════════════

CURRICULUM.update({

    "m10_c1_cartographie_systemes_ia": {
        "module": 10, "ordre": 1, "langue": "fr",
        "titre": "Cartographie et inventaire des systèmes d'IA",
        "prereqs": ["m5_c3_nist_rmf_govern_map_measure_manage"],
        "texte": """
La PREMIÈRE ACTION CONCRÈTE de tout programme de gouvernance d'IA est de SAVOIR ce qu'on a. Sans inventaire, aucun cadre (Loi 25, EU AI Act, NIST RMF, ISO 42001) n'est implémentable. La cartographie est l'étape préalable qui n'est jamais faite par défaut et qui révèle systématiquement plus de systèmes que l'organisation pensait avoir.

POURQUOI L'INVENTAIRE EST DIFFICILE — trois raisons :
A. SHADOW IA. Des employés utilisent ChatGPT, Claude, Copilot ou des outils SaaS dotés d'IA sans que la direction le sache.
B. IA INTÉGRÉE. De nombreux logiciels d'entreprise (CRM, ERP, outils RH, plateformes marketing) intègrent désormais des fonctionnalités d'IA en arrière-plan, sans que ce soit le motif principal d'achat.
C. FRONTIÈRE FLOUE. Quand un système devient-il « IA »? Un classificateur statistique simple? Un modèle de régression? Cette question mérite une définition opérationnelle.

DÉFINITION OPÉRATIONNELLE pour l'inventaire — adopter la définition de l'EU AI Act / OCDE : un système basé sur une machine, conçu pour fonctionner avec différents niveaux d'autonomie, qui peut faire preuve d'adaptabilité après son déploiement, et qui pour des objectifs explicites ou implicites, déduit, à partir des entrées qu'il reçoit, comment générer des sorties qui influencent des environnements physiques ou virtuels.

CRITÈRE PRATIQUE — tout système qui produit une sortie influençant une décision relative à une personne (employé, client, prospect) DOIT être dans l'inventaire, qu'il utilise du machine learning, des règles, ou un mélange.

CONTENU MINIMAL D'UNE FICHE D'INVENTAIRE (15 champs) :
1. NOM du système.
2. PROPRIÉTAIRE MÉTIER (qui paie? qui utilise?).
3. RESPONSABLE TECHNIQUE.
4. FOURNISSEUR / DÉVELOPPEUR (interne, fournisseur SaaS, modèle GPAI).
5. FINALITÉ DÉCLARÉE.
6. CAS D'USAGE COUVERTS.
7. CATÉGORIES DE PERSONNES AFFECTÉES.
8. DONNÉES D'ENTRÉE (catégories, sources, sensibilité).
9. DONNÉES UTILISÉES POUR L'ENTRAÎNEMENT (si applicable).
10. SORTIES (type de décision, automatisée ou aide à la décision).
11. NIVEAU DE CRITICITÉ (impact d'une défaillance).
12. CLASSIFICATION RÉGLEMENTAIRE (Annexe III EU AI Act? décision automatisée Loi 25? Directive AIA niveau I-IV?).
13. STATUT (en développement, en production, en retrait).
14. DATE DE DERNIÈRE ÉVALUATION.
15. RÉFÉRENCES (EFVP/DPIA, documentation technique, contrats).

OUTILS POUR CONSTRUIRE L'INVENTAIRE :
A. Tableur initial (Excel, Google Sheets) — suffisant pour une PME avec 10-30 systèmes.
B. Outils dédiés émergents — Credo AI, FairNow, Weights & Biases, Holistic AI, Monitaur. À considérer au-delà de 30-50 systèmes.
C. Intégration avec le CMDB (Configuration Management Database) — si l'organisation a une discipline IT mature.

PROCESSUS DE COLLECTE EN 4 ÉTAPES :
ÉTAPE 1 — RECENSEMENT TOP-DOWN. Lister les projets d'IA connus de la direction.
ÉTAPE 2 — RECENSEMENT BOTTOM-UP. Sondage / entretiens avec chaque équipe métier : « quels outils utilisez-vous qui produisent automatiquement des recommandations, des classements, des alertes, des contenus, des décisions? »
ÉTAPE 3 — RECENSEMENT FOURNISSEURS. Lister tous les contrats SaaS et identifier ceux qui annoncent des fonctionnalités d'IA.
ÉTAPE 4 — RECENSEMENT TECHNIQUE. Examen des pipelines de données et des appels API vers des modèles externes (OpenAI, Anthropic, Google, Hugging Face).

CLASSIFICATION DE CRITICITÉ — appliquer une matrice impact × probabilité :
A. CRITICITÉ ÉLEVÉE — système qui prend ou influence directement des décisions ayant un impact significatif sur une personne (embauche, crédit, traitement médical, sanction).
B. CRITICITÉ MODÉRÉE — système qui automatise des processus internes, des recommandations sans impact direct.
C. CRITICITÉ FAIBLE — IA d'assistance individuelle (rédaction de courriels, recherche, brouillon de code), sans externalisation de décision.

LIEN AVEC LE CHAMP RÉGLEMENTAIRE :
A. Critères Loi 25 — tout système traitant des RP entre dans le champ. Le caractère « décision exclusivement automatisée » (Art. 12.1) est le critère pivot.
B. Critères EU AI Act — l'Annexe III fournit la liste des cas d'usage à haut risque.
C. Critères Directive fédérale ADM — l'AIA produit un niveau I-IV; utilisable comme étalon même hors fédéral.
D. Critères ISO 42001 — pas de catégorie réglementaire mais une obligation d'évaluer les impacts (DOMAINE A.5).

GOUVERNANCE DE L'INVENTAIRE :
A. PROPRIÉTAIRE de l'inventaire — typiquement le RPRP, le DPO ou le pilote IA.
B. MISE À JOUR — revue trimestrielle minimum, déclenchée à chaque nouveau projet.
C. AUDIT — vérification annuelle par audit interne (cohérence, exhaustivité).
D. RAPPORT — bilan annuel au comité de direction et au conseil d'administration.

UTILITÉ AU-DELÀ DE LA CONFORMITÉ — un bon inventaire d'IA :
A. Aide à la décision d'investissement (identifier doublons, manques).
B. Permet la formation ciblée des utilisateurs.
C. Facilite la réponse rapide en cas d'incident (« quels systèmes utilisent ce modèle qui vient d'être désavoué? »).
D. Démontre la maturité aux auditeurs, clients, assureurs.

ERREURS FRÉQUENTES :
A. Limiter l'inventaire au « machine learning » — ce qui exclut beaucoup de systèmes décisionnels.
B. Confier l'inventaire à l'IT seul — manque de visibilité sur les usages métier.
C. Faire un inventaire ponctuel sans gouvernance de mise à jour.
D. Sous-estimer le shadow IA et les fonctionnalités émergentes des outils existants.

POUR UNE PME QUÉBÉCOISE — une cartographie initiale en 4-6 semaines révèle typiquement 15-50 systèmes là où l'organisation pensait en avoir 3-5. C'est ce premier moment de surprise qui légitime l'investissement dans la suite du programme.

POSITIONNEMENT NORD PARADIGM — la cartographie est le PREMIER LIVRABLE de Brèche (gratuit) et le PRÉREQUIS de Brèche Pro et Prisme. C'est aussi le service à plus haute valeur perçue : le client apprend en quelques semaines ce qu'il pensait savoir intuitivement.
        """.strip(),
    },

    "m10_c2_evaluation_incidence_integree": {
        "module": 10, "ordre": 2, "langue": "fr",
        "titre": "Évaluation d'incidence intégrée (EFVP / FRIA / AIA / DPIA)",
        "prereqs": ["m10_c1_cartographie_systemes_ia"],
        "texte": """
L'évaluation d'incidence est l'instrument central de plusieurs régimes : EFVP au Québec (Loi 25 Art. 3.3), DPIA au sens du RGPD (Art. 35), FRIA dans l'EU AI Act (Art. 27), Algorithmic Impact Assessment au Canada fédéral (Directive sur la prise de décisions automatisée du Conseil du Trésor depuis 2019). Toutes ces évaluations partagent une logique commune mais diffèrent dans leur étendue.

QUATRE FAMILLES D'ÉVALUATIONS :

A. EFVP — ÉVALUATION DES FACTEURS RELATIFS À LA VIE PRIVÉE (Loi 25, Québec). Centrée sur les renseignements personnels. Obligatoire pour tout projet impliquant la collecte, l'utilisation, la communication, la conservation ou la destruction de RP.

B. DPIA — DATA PROTECTION IMPACT ASSESSMENT (RGPD, Europe). Centré sur les données personnelles. Obligatoire si le traitement est susceptible d'engendrer un risque élevé pour les droits et libertés des personnes physiques.

C. FRIA — FUNDAMENTAL RIGHTS IMPACT ASSESSMENT (EU AI Act, Art. 27). Centré sur les droits fondamentaux. Obligatoire pour les déployeurs publics et certains déployeurs privés de systèmes à haut risque.

D. AIA — ALGORITHMIC IMPACT ASSESSMENT (Canada fédéral, Directive sur la prise de décisions automatisée). Centré sur les risques algorithmiques. Obligatoire pour les institutions fédérales (cf. M3 c2).

POURQUOI LES ARTICULER — un seul système d'IA qui traite des RP au Québec et est utilisé dans l'UE peut déclencher SIMULTANÉMENT EFVP + DPIA + FRIA. Plutôt que de produire trois documents séparés, l'organisation produit une ÉVALUATION INTÉGRÉE qui couvre les exigences de chacun.

STRUCTURE D'UNE ÉVALUATION INTÉGRÉE EN HUIT SECTIONS :

SECTION 1 — DESCRIPTION DU SYSTÈME ET DU PROJET.
A. Finalité, contexte, justification de la nécessité.
B. Description technique : architecture, type de modèle, sources de données.
C. Cycle de vie prévu, modifications anticipées.
D. Acteurs (fournisseur, opérateur, utilisateurs, personnes affectées).

SECTION 2 — CADRAGE LÉGAL ET RÉGLEMENTAIRE.
A. Régimes applicables (Loi 25, RGPD, EU AI Act, sectoriels, fédéral canadien).
B. Base légale du traitement (consentement, contrat, obligation légale, intérêt légitime).
C. Catégorisation du système selon chaque régime (haut risque EU AI Act? décision automatisée Loi 25? niveau AIA fédéral?).

SECTION 3 — CARTOGRAPHIE DES FLUX DE DONNÉES.
A. Données collectées (catégories, sources).
B. Données utilisées pour l'entraînement (provenance, licéité, consentement).
C. Sorties produites.
D. Destinataires (internes, sous-traitants, clients).
E. Localisation des traitements (cloud, juridiction).
F. Durée de conservation.

SECTION 4 — IDENTIFICATION DES RISQUES.
A. Risques pour la VIE PRIVÉE — accès non autorisé, fuite, ré-identification, profilage excessif.
B. Risques pour les DROITS FONDAMENTAUX — discrimination, atteinte à la dignité, atteinte à l'autonomie, déni de service.
C. Risques DE SÉCURITÉ — attaques sur le modèle ou les données.
D. Risques pour la SOCIÉTÉ — désinformation, manipulation, concentration de pouvoir.
E. Risques pour l'ENVIRONNEMENT — consommation énergétique, eau.

SECTION 5 — ANALYSE DES RISQUES.
Pour chaque risque identifié :
A. Probabilité d'occurrence (qualitative ou quantitative).
B. Gravité du préjudice (échelle de 1 à 5).
C. Niveau de risque résultant (matrice probabilité × gravité).
D. Justification.

SECTION 6 — MESURES D'ATTÉNUATION.
Pour les risques au-dessus du seuil d'acceptabilité :
A. Mesures techniques (anonymisation, chiffrement, filtrage, ré-entraînement, monitoring).
B. Mesures organisationnelles (formation, procédures, surveillance humaine).
C. Mesures contractuelles (clauses fournisseurs, restrictions d'usage).
D. Mesures d'information (transparence aux personnes affectées, droits offerts).

SECTION 7 — RISQUES RÉSIDUELS ET DÉCISION.
A. Niveau de risque APRÈS mitigation.
B. Acceptabilité du risque résiduel par l'autorité décisionnelle.
C. Décision : GO / NO-GO / GO conditionnel avec mesures additionnelles.
D. Conditions de revue (déclencheurs de re-évaluation).

SECTION 8 — DOCUMENTATION ET COMMUNICATION.
A. Conservation du document (recommandation : minimum 3 ans après la fin du système).
B. Approbations (RPRP, comité IA, conseil d'administration le cas échéant).
C. Communication aux parties intéressées (transparence).
D. Notification éventuelle aux autorités (selon les régimes).

QUAND DÉCLENCHER UNE ÉVALUATION :
A. AVANT mise en service (toujours).
B. À chaque modification SUBSTANTIELLE (nouveau modèle, nouvelle finalité, nouvelle source de données, nouvelle population affectée).
C. PÉRIODIQUEMENT (au moins annuellement pour les systèmes à haut risque).
D. À LA SUITE D'INCIDENT.

QUI PARTICIPE :
A. CHEF DE PROJET — pilote et rédige.
B. RPRP / DPO — supervise sur les aspects vie privée.
C. ÉQUIPE TECHNIQUE — fournit la description technique et les données factuelles.
D. JURIDIQUE — valide les bases légales et l'analyse réglementaire.
E. SÉCURITÉ — analyse les risques cyber.
F. MÉTIER — décrit la finalité, le contexte d'usage, les attentes.
G. PARTIES PRENANTES EXTERNES — selon le degré de risque, consultation d'experts indépendants ou de représentants des personnes affectées.

ERREURS FRÉQUENTES :
A. ÉVALUATION RÉTROACTIVE après le déploiement — viole l'esprit et la lettre de la loi.
B. ÉVALUATION FORMELLE qui se contente de cocher des cases — la CAI a explicitement déclaré que cela ne suffit pas.
C. ÉVALUATION SANS PARTICIPATION TECHNIQUE — l'analyse des risques techniques (biais, robustesse) doit être quantitative quand possible.
D. ÉVALUATION SANS REVUE PÉRIODIQUE — un système qui évolue sans nouvelle évaluation devient progressivement non conforme.
E. CONFUSION ENTRE EFVP et FRIA et DPIA — ces évaluations couvrent des dimensions partiellement distinctes; les ignorer mène à une couverture incomplète.

UTILISATION D'OUTILS — plusieurs cadres fournissent des templates :
A. CAI Québec — modèle d'EFVP publié.
B. EDPB — lignes directrices DPIA et templates.
C. Conseil du Trésor du Canada — outil d'AIA en ligne pour les institutions fédérales (open-source sur GitHub).
D. ICO UK — Risk Toolkit v1.1 (cf. M9 c3).
E. ISO/IEC 42005 (en développement) — guide d'évaluation des impacts d'IA.

DURÉE TYPIQUE — pour un système d'IA modéré, une évaluation rigoureuse demande 2 à 6 semaines de travail effectif (pas calendaire). Pour un système à haut risque déployé en Europe, 2 à 4 mois.

POSITIONNEMENT NORD PARADIGM — l'évaluation intégrée est le LIVRABLE PRINCIPAL de Brèche Pro. La capacité à produire UN seul document multi-juridiction, plutôt que trois documents séparés, est un avantage concurrentiel net pour le client.
        """.strip(),
    },

    "m10_c3_documentation_tracabilite": {
        "module": 10, "ordre": 3, "langue": "fr",
        "titre": "Documentation et traçabilité (data sheets, model cards, system cards)",
        "prereqs": ["m10_c1_cartographie_systemes_ia"],
        "texte": """
La documentation est la COLONNE VERTÉBRALE de la gouvernance d'IA. Sans documentation, on ne peut pas démontrer la conformité, on ne peut pas auditer, on ne peut pas répondre aux demandes des personnes, et on ne peut pas reproduire ou corriger un système. Trois artefacts standards émergent comme références : les data sheets, les model cards, les system cards.

DATA SHEETS FOR DATASETS — proposées dans l'article fondateur de Gebru et al. (2018, mis à jour 2021). Documentation structurée pour les jeux de données utilisés à l'entraînement.

CONTENU TYPIQUE D'UNE DATA SHEET (sept sections) :

SECTION 1 — MOTIVATION. Pourquoi le dataset a-t-il été créé? Pour qui? Quels biais inhérents au choix des sources?

SECTION 2 — COMPOSITION. De quoi se composent les instances? Quel est le volume? Y a-t-il des sous-populations identifiables? Quels labels?

SECTION 3 — PROCESSUS DE COLLECTE. Comment les données ont-elles été acquises? Avec consentement? Quelles méthodes d'échantillonnage?

SECTION 4 — PRÉTRAITEMENT, NETTOYAGE, ÉTIQUETAGE. Quelles transformations ont été appliquées? Qui a étiqueté?

SECTION 5 — UTILISATIONS PRÉVUES. Pour quoi le dataset est-il conçu? Quels usages non recommandés?

SECTION 6 — DISTRIBUTION. Qui peut accéder au dataset? Sous quelle licence?

SECTION 7 — MAINTENANCE. Qui maintient le dataset? Politique de mise à jour?

UTILITÉ — la data sheet permet à un utilisateur du dataset (équipe interne ou tiers) de comprendre la qualité, les biais et les limites avant de l'utiliser. Elle est exigée explicitement par l'EU AI Act (Art. 10) pour les systèmes à haut risque.

MODEL CARDS — proposées par Mitchell et al. (Google, 2019). Documentation structurée pour un modèle d'IA spécifique, indépendamment du système qui le déploie.

CONTENU TYPIQUE D'UNE MODEL CARD (neuf sections) :

SECTION 1 — DÉTAILS DU MODÈLE. Type, version, développeur, date, licence.
SECTION 2 — UTILISATION PRÉVUE. Cas d'usage primaires, hors champ, utilisateurs visés.
SECTION 3 — FACTEURS. Variables démographiques, environnementales, instrumentales pertinentes.
SECTION 4 — MÉTRIQUES. Métriques de performance, désagrégées par sous-groupe lorsque pertinent.
SECTION 5 — ÉVALUATION DES DONNÉES. Sur quels jeux de données les performances ont-elles été mesurées?
SECTION 6 — DONNÉES D'ENTRAÎNEMENT. Description (renvoie typiquement à une data sheet).
SECTION 7 — ANALYSES QUANTITATIVES. Performances ventilées (par sous-groupe, par sous-condition).
SECTION 8 — CONSIDÉRATIONS ÉTHIQUES. Risques identifiés, mitigations.
SECTION 9 — AVERTISSEMENTS et RECOMMANDATIONS.

EXEMPLES PUBLICS de model cards — Anthropic publie des « model cards » pour Claude (capacités, limites, évaluations). OpenAI publie des « system cards » pour GPT (plus détaillées). Google publie des model cards pour ses modèles open. Hugging Face exige une model card pour tout modèle hébergé sur sa plateforme.

SYSTEM CARDS — extension naturelle des model cards au niveau du SYSTÈME complet (modèle + données + interface + processus métier). Documentation pour l'ENSEMBLE qui produit la décision finale.

CONTENU TYPIQUE D'UNE SYSTEM CARD :
A. Description du système, de sa finalité, de son contexte de déploiement.
B. Architecture (incluant les modèles utilisés, leurs interactions).
C. Données d'entrée et de sortie.
D. Mécanismes de surveillance humaine.
E. Limites connues et risques résiduels.
F. Procédures opérationnelles, de maintenance, de retrait.

LA SYSTEM CARD est ce que les régulateurs (CAI, EU AI Office, ICO, CNIL) demanderont en cas d'enquête. Elle synthétise ce qu'une autorité doit savoir pour comprendre comment un système fonctionne et comment il a été gouverné.

EXIGENCES SPÉCIFIQUES IMPOSÉES PAR L'EU AI ACT (Annexe IV) :
A. Description générale du système.
B. Description détaillée des éléments du système et de son processus de développement.
C. Informations sur la surveillance, le fonctionnement et le contrôle.
D. Description des changements apportés au système au cours de son cycle de vie.
E. Liste des normes harmonisées appliquées.
F. Copie de la déclaration UE de conformité.
G. Description du système de gestion de la qualité.

JOURNALISATION ET TRAÇABILITÉ — au-delà de la documentation statique, les systèmes d'IA à haut risque doivent JOURNALISER leur fonctionnement (EU AI Act Art. 12) :
A. Type, durée, début et fin de chaque utilisation.
B. Données de référence en entrée.
C. Identification des personnes physiques qui ont vérifié les sorties (le cas échéant).
D. Pour les systèmes biométriques : journal complet des correspondances et non-correspondances.

DURÉE DE CONSERVATION — les déployeurs doivent conserver les journaux pendant au moins 6 mois (Art. 26 al. 6 EU AI Act). Pour des systèmes à enjeux supérieurs, durée plus longue recommandée.

EXIGENCES DE LA LOI 25 — la loi exige la traçabilité suffisante pour répondre aux demandes des personnes (renseignements utilisés, principaux facteurs et paramètres ayant mené à la décision, possibilité de rectifier). Cela impose techniquement la conservation des entrées et la capacité de reconstruire la décision a posteriori.

OUTILS PRATIQUES :
A. Hugging Face — model cards intégrées à la plateforme.
B. MLflow — suivi des expérimentations, des modèles, des versions.
C. Weights & Biases — monitoring des entraînements.
D. Outils de governance dédiés — Credo AI, Holistic AI, FairNow, Monitaur.

PRINCIPES DE BONNE DOCUMENTATION :
A. CONSISTANCE — formats standardisés à travers l'organisation.
B. ACCESSIBILITÉ — disponible aux équipes pertinentes (technique, juridique, métier).
C. VERSIONNAGE — chaque modification documentée.
D. RÉVISION RÉGULIÈRE — au moins annuelle pour les systèmes en service.
E. APPROPRIATION — chaque système a un PROPRIÉTAIRE responsable de sa documentation.

ERREURS FRÉQUENTES :
A. Documentation produite UNIQUEMENT pour l'audit, sans valeur opérationnelle.
B. Documentation NON MISE À JOUR après le déploiement initial.
C. Documentation EN SILO (isolée des outils MLOps).
D. Documentation TROP TECHNIQUE pour les non-spécialistes (limite la transparence vis-à-vis des affectés).
E. Absence de documentation des CHANGEMENTS et MAINTENANCE.

POUR UNE PME QUÉBÉCOISE — démarrer simplement : pour chaque système d'IA en service, produire une fiche d'une page reprenant les éléments essentiels (model card simplifiée + system card simplifiée). Cela suffit pour la majorité des audits initiaux et améliore la maturité graduellement.

POSITIONNEMENT NORD PARADIGM — la production de model cards et system cards CONFORMES AUX STANDARDS EXIGÉS PAR L'EU AI ACT est un livrable distinct et facturable. Les clients ne savent pas comment commencer; un gabarit prêt à l'emploi vaut beaucoup.
        """.strip(),
    },

    "m10_c4_gouvernance_organisationnelle_raci": {
        "module": 10, "ordre": 4, "langue": "fr",
        "titre": "Gouvernance organisationnelle (rôles, comités, formation, RACI)",
        "prereqs": ["m10_c1_cartographie_systemes_ia"],
        "texte": """
La gouvernance d'IA n'est pas un projet technique. C'est un dispositif ORGANISATIONNEL qui définit qui décide, qui exécute, qui contrôle. Sans architecture claire des rôles et responsabilités, les meilleures politiques restent lettre morte.

QUATRE NIVEAUX DE GOUVERNANCE :

NIVEAU 1 — STRATÉGIQUE (CONSEIL D'ADMINISTRATION). Approuve la politique d'IA de l'entreprise, alloue les ressources, supervise l'efficacité du programme. Reçoit un rapport annuel sur la gouvernance d'IA. Au moins un administrateur ayant une expertise IA ou avec un mandat explicite sur le sujet. TENDANCE 2026 — l'IAPP Summit a signalé que la SUPERVISION CONSEIL DE LA GOUVERNANCE IA devient une exigence d'application implicite (la California Privacy Protection Agency exige déjà la revue conseil pour les évaluations de risque vie privée).

NIVEAU 2 — TACTIQUE (DIRECTION GÉNÉRALE et COMITÉ IA). Définit les priorités, arbitre les décisions difficiles (déploiements à risque, conflits entre vitesse et conformité), valide les évaluations majeures. Le Comité IA se réunit typiquement mensuellement.

NIVEAU 3 — OPÉRATIONNEL (PILOTE IA / RPRP / DPO). Met en œuvre les politiques au quotidien. Coordonne les évaluations, gère les incidents, supervise la formation, prépare les rapports.

NIVEAU 4 — TERRAIN (ÉQUIPES PROJETS). Conçoivent, déploient, exploitent les systèmes d'IA en respectant les politiques.

RÔLES TYPIQUES dans une PME québécoise :

A. RPRP (RESPONSABLE DE LA PROTECTION DES RENSEIGNEMENTS PERSONNELS). Obligation Loi 25. Dans une PME, c'est souvent la même personne que le pilote IA — économies d'échelle.

B. PILOTE IA / AI LEAD. Coordonne le programme de gouvernance d'IA. Peut être un cadre dédié (dans les grandes PME) ou un rôle ajouté à une fonction existante (CTO, Directeur Conformité, Directeur Sécurité, RPRP).

C. PROPRIÉTAIRE D'UN SYSTÈME D'IA. Pour CHAQUE système, une personne nommément responsable (typiquement un cadre métier). Endosse les évaluations d'impact, valide la mise en service, est imputable des incidents.

D. RESPONSABLE TECHNIQUE D'UN SYSTÈME D'IA. Cadre technique chargé du développement, de la maintenance, du monitoring opérationnel.

E. AUDITEUR INTERNE IA. Réalise des audits indépendants, peut être un consultant externe pour les PME qui n'ont pas la masse critique.

F. CHAMPION SECTORIEL. Dans chaque équipe métier qui utilise de l'IA, une personne de référence pour les questions de gouvernance.

LE COMITÉ IA — composition recommandée :
A. Sponsor exécutif (DG ou COO).
B. Pilote IA (animateur).
C. RPRP / DPO.
D. Responsable juridique.
E. Responsable sécurité de l'information.
F. Représentant technique senior.
G. Représentants métier (RH, marketing, opérations, selon les enjeux).
H. Selon le sujet — éthicien, expert externe, représentant des personnes affectées.

MANDATS DU COMITÉ IA :
A. Approuver les déploiements à risque modéré ou élevé.
B. Arbitrer les évaluations d'impact qui soulèvent des questions sensibles.
C. Réviser les incidents et les leçons apprises.
D. Valider les politiques et procédures internes.
E. Suivre les indicateurs de gouvernance.
F. Préparer le rapport annuel au CA.

MATRICE RACI POUR UN PROJET D'IA TYPIQUE :

ACTION : Cartographie initiale.
R (responsible) : Pilote IA. A (accountable) : DG. C (consulted) : RPRP, métiers. I (informed) : CA.

ACTION : Évaluation d'impact (EFVP/FRIA).
R : Propriétaire métier. A : Pilote IA. C : RPRP, juridique, technique. I : Comité IA.

ACTION : Validation pré-déploiement.
R : Propriétaire métier. A : Comité IA (pour systèmes à haut risque). C : RPRP, juridique. I : DG.

ACTION : Monitoring opérationnel.
R : Responsable technique. A : Propriétaire métier. C : Pilote IA. I : Comité IA.

ACTION : Réponse à incident.
R : Responsable technique. A : Pilote IA. C : RPRP, juridique, communications. I : DG, CA si majeur, autorités si requis.

ACTION : Notification d'incident.
R : RPRP. A : Pilote IA. C : Juridique. I : DG, CA.

ACTION : Rapport annuel.
R : Pilote IA. A : DG. C : Comité IA. I : CA.

PROGRAMME DE FORMATION — quatre niveaux :

NIVEAU A — Sensibilisation pour TOUS les employés (1-2 heures par an). Comprendre la politique d'IA de l'entreprise, les usages autorisés et interdits, les obligations de signalement.

NIVEAU B — Formation pour les UTILISATEURS de systèmes d'IA en service (4-8 heures). Comprendre les capacités et limites, savoir interpréter les sorties, savoir quand intervenir, savoir signaler.

NIVEAU C — Formation pour les DÉVELOPPEURS et CHEFS DE PROJET d'IA (16-40 heures). Méthodologie d'évaluation d'impact, gestion des risques, documentation, monitoring, frameworks (NIST RMF, ISO 42001, Singapore MGF).

NIVEAU D — Formation AVANCÉE pour les rôles de gouvernance (Pilote IA, membres du Comité IA, auditeur interne) — typiquement par certifications externes (CIPP, CIPM, IAPP AIGP, certifications ISO).

INDICATEURS DE GOUVERNANCE à suivre :
A. Couverture de l'inventaire (% de systèmes formellement répertoriés).
B. Couverture des évaluations d'impact (% de systèmes avec évaluation à jour).
C. Délai moyen de réalisation des évaluations.
D. Nombre d'incidents (par classe de gravité).
E. Délai moyen de réponse aux demandes des personnes.
F. Couverture de la formation (% d'employés formés selon leur niveau).
G. Maturité ISO 42001 (% de contrôles implémentés).
H. Audits internes réalisés / planifiés.
I. NOUVEAU 2026 — Mesure de la VALEUR D'AFFAIRES de l'IA (Writer.com, ERP Today, Grant Thornton ont identifié ce manque comme la cause majeure du « AI ROI gap »). Métriques recommandées : utilisation effective, productivité gagnée, coût évité, qualité améliorée, risque réduit.

CULTURE — au-delà des structures, la gouvernance d'IA exige une CULTURE qui :
A. Récompense la transparence (signaler un problème ne doit pas pénaliser).
B. Tolère la lenteur quand elle protège (pas de précipitation imprudente).
C. Valorise les questions difficiles (un projet d'IA refusé n'est pas un échec).
D. Apprend des incidents (post-mortems systématiques, sans recherche de coupables).

POUR UNE TPE OU PME (< 50 employés) — version condensée :
A. Le DG est sponsor.
B. Une seule personne cumule RPRP + Pilote IA.
C. Pas de comité formel — décisions prises en réunion mensuelle de direction avec point IA fixe.
D. Auditeur interne externe (consultant) sur base annuelle.
E. Formation Niveau A pour tous, Niveau B pour utilisateurs, Niveau C pour 1-2 personnes.
F. Procédures simplifiées, mais NON ABSENTES.

POUR UNE PME (50-250 employés) — version standard :
A. Comité IA mensuel formel.
B. Pilote IA dédié 50-100 % temps.
C. RPRP distinct si volume de RP important.
D. Audit interne annuel par tiers.
E. Programme de formation structuré avec évaluations.
F. Reporting trimestriel à la direction, annuel au CA.

POSITIONNEMENT NORD PARADIGM — la conception de la gouvernance organisationnelle (RACI, comité, formation) est typiquement le LIVRABLE DE PRISME (audit interne ISO 42001). C'est l'aboutissement naturel d'un programme de gouvernance qui a démarré avec Brèche et Brèche Pro.
        """.strip(),
    },

})


# ══════════════════════════════════════════════════════════════════════════════
# MODULE 11 — AGENTIC AI GOVERNANCE  (4 concepts, EN)
# ══════════════════════════════════════════════════════════════════════════════

CURRICULUM.update({

    "m11_c1_agent_inventory_classification": {
        "module": 11, "ordre": 1, "langue": "en",
        "titre": "Agent inventory and classification",
        "prereqs": ["m10_c1_cartographie_systemes_ia"],
        "texte": """
AGENTIC AI is the FRONTIER of governance practice in 2026. Traditional AI governance frameworks assumed human-in-the-loop oversight. Agentic systems — AI that operates with minimal human supervision, makes decisions independently, accesses enterprise systems and data, and takes actions with business and security consequences — break this assumption. New risks emerge: uncontrolled access, emergent behaviours, unintended actions, inability to audit or reverse decisions in real-time.

WHY THIS MATTERS NOW:
A. ENTERPRISES ARE DEPLOYING AGENTS at scale (April 2026 signals: JPMorgan with hundreds of production AI use cases, OpenAI partnering with Customers Bank on agentic workflows, Microsoft Agent Framework 1.0.0 released April 2026).
B. INCIDENT DATA IS ALARMING — 80 % of organizations report unintended agent actions; 39 % involve agents accessing unauthorized systems; 35 % report inability to immediately stop a rogue agent.
C. GOVERNANCE FRAMEWORKS ARE EMERGING — Singapore Model AI Governance Framework for Agentic AI (January 2026), NIST AI Agent Standards Initiative (February 2026), Microsoft Agent Governance Toolkit (April 2026). These signal the field is moving from ad hoc to formal standardization.
D. LEGAL ACCOUNTABILITY remains an unsettled area. Fasken's March 2026 analysis notes that legal liability for agent actions has no binding Canadian framework. Organizations must build their own governance.

THE FIRST STEP — AGENT INVENTORY AND CLASSIFICATION.

You cannot govern what you cannot see. The first action of agentic AI governance is to know what agents exist in your environment. Many organizations have « SHADOW AGENTS » running untracked: an employee built a Zapier flow with an LLM step; another created a Microsoft Power Automate task with Copilot; a third deployed an Auto-GPT instance for a one-off project. Each is an agent, with access to corporate data, that no one is monitoring.

CLASSIFICATION FRAMEWORK — the SailPoint and Singapore frameworks converge on FIVE AGENT TYPES, each with distinct governance levels:

TYPE 1 — PACKAGED AGENTS.
Examples: Microsoft 365 Copilot, Google Workspace Duet AI, Anthropic Claude in Sheets/Slides integrations.
GOVERNANCE LEVEL: LOW. Vendor manages security; flexibility is limited; risks are bounded by the vendor's controls.
KEY CONCERN: data exposure to vendor's infrastructure; vendor's terms of service.

TYPE 2 — LOW-CODE / NO-CODE AGENTS.
Examples: N8N Agents, Microsoft Copilot Studio, Zapier with AI actions.
GOVERNANCE LEVEL: MEDIUM. Risk varies with system access; scalability issues; often built by non-developers without security training.
KEY CONCERN: privilege creep; lack of monitoring; integration sprawl.

TYPE 3 — PROFESSIONAL CODED AGENTS.
Examples: Custom chatbots using OpenAI / Anthropic APIs; enterprise supply-chain agents.
GOVERNANCE LEVEL: HIGH. Development errors, maintenance burden, vulnerabilities; codebase complexity.
KEY CONCERN: code quality; supply chain (libraries); secrets management.

TYPE 4 — AUTONOMOUS AGENTS.
Examples: Auto-GPT, Boston Dynamics Spot, autonomous trading agents.
GOVERNANCE LEVEL: VERY HIGH. Unintended actions, ethical concerns, safety requirements.
KEY CONCERN: emergent behaviour; insufficient human oversight; physical or financial harm.

TYPE 5 — MULTI-AGENT SYSTEMS.
Examples: CrewAI, gaming simulations, financial trading platforms with multiple coordinating agents.
GOVERNANCE LEVEL: VERY HIGH. Complexity, coordination failures, emergent behaviours not predicted from individual agent design.
KEY CONCERN: system-level behaviours; conflicts between agents; cascade failures.

Each category requires TAILORED GOVERNANCE; applying uniform governance to all agents wastes resources and misses real risks.

INVENTORY METHODOLOGY:

STEP 1 — TOP-DOWN ENUMERATION. List agent projects known to leadership.

STEP 2 — BOTTOM-UP DISCOVERY. Survey each business team: « What automated tools take actions on your behalf without your approval per action? Which ones can access systems beyond their immediate task? »

STEP 3 — VENDOR / PLATFORM DISCOVERY. List all SaaS products with AI agent features:
A. Microsoft 365 Copilot — agent count varies by team usage.
B. Google Workspace agents.
C. ServiceNow / Salesforce agentic features.
D. Zapier, Make, n8n with AI steps.
E. Custom-built agents via OpenAI / Anthropic / Google APIs.

STEP 4 — TECHNICAL DISCOVERY. For technical environments:
A. Examine API call logs for outbound LLM calls.
B. Audit IAM permissions for service accounts that may be agent identities.
C. Review function-as-a-service / serverless deployments.
D. Check task schedulers (cron, Power Automate, Workflow).

INVENTORY FIELDS — additions beyond standard AI inventory:
A. AGENT TYPE (1-5 above).
B. SCOPE OF ACCESS (which systems and data the agent can interact with).
C. TRIGGER MECHANISM (what causes the agent to act?).
D. ACTION SET (what can the agent actually do?).
E. HUMAN OVERSIGHT LEVEL (in-the-loop, on-the-loop, over-the-loop, fully autonomous).
F. KILL-SWITCH MECHANISM (how to stop the agent immediately).
G. AUDIT TRAIL (what is logged, where, for how long).

GOVERNANCE LEVEL DECISION — based on:
A. Type of agent.
B. Scope of access (broader = higher level).
C. Reversibility of actions.
D. Affected populations.
E. Regulatory exposure (Loi 25, EU AI Act).

POSITIONING FOR NORD PARADIGM — agent inventory is a NEW DIAGNOSTIC service. Most organizations have no idea what agents they have. A 4-6 week engagement that produces a full inventory is high-value and unique in the market.

LIMITS OF CLASSIFICATION — boundaries between types blur. A « low-code agent » that gains broader access via plugins effectively becomes a « professional coded agent. » Classification must be REVIEWED PERIODICALLY.
        """.strip(),
    },

    "m11_c2_agent_iam_governance": {
        "module": 11, "ordre": 2, "langue": "en",
        "titre": "Identity and Access Management as agent governance foundation",
        "prereqs": ["m11_c1_agent_inventory_classification"],
        "texte": """
The Singapore framework for agentic AI and SailPoint's « Governed Agent » approach CONVERGE ON IDENTITY MANAGEMENT as the linchpin of agent governance. Without identity, you cannot enforce least privilege. Without least privilege, agents inevitably accumulate access and become compliance and security risks.

THE PRINCIPLE — every agent must have a DEFINED IDENTITY, just as every human user has an account. Without this, you cannot:
A. AUDIT what the agent did.
B. REVOKE access if the agent misbehaves.
C. SCOPE permissions to what the agent actually needs.
D. ATTRIBUTE actions to a responsible human.
E. COMPLY with privacy and security obligations that require traceable access.

SIX IAM PRACTICES FOR AGENT GOVERNANCE:

PRACTICE 1 — AGENT DISCOVERY.

Identify all agents in the environment. Many organizations have « shadow agents » running untracked. Discovery techniques:
A. Inventory all service accounts in IAM systems.
B. Examine outbound API call logs (LLM provider endpoints, automation platforms).
C. Survey teams for tools that take actions automatically.
D. Audit no-code / low-code platforms for AI-enabled flows.

PRACTICE 2 — AGENT IDENTITIES.

Assign UNIQUE IDENTITIES to agents:
A. Distinct service account per agent (not shared).
B. Identity tied to a RESPONSIBLE HUMAN (so accountability is preserved).
C. Strong authentication (certificates, short-lived tokens, not passwords).
D. Visible in IAM dashboards alongside human users.

PRACTICE 3 — LEAST PRIVILEGE.

Grant agents the MINIMUM PERMISSIONS needed for their intended function:
A. EXPLICIT ALLOW LIST (not « can do anything except… »).
B. SCOPED to specific resources (which buckets, which databases, which APIs).
C. SCOPED to specific actions (read-only when possible, no DELETE without approval).
D. TIME-BOUNDED if appropriate (permissions valid only during a project).

PRACTICE 4 — ENTITLEMENT REVIEWS.

Periodically AUDIT what access each agent actually has versus what it should have:
A. QUARTERLY review of high-risk agents.
B. ANNUAL review of low-risk agents.
C. AUTOMATED detection of permission drift.
D. CERTIFICATIONS by responsible humans.

PRACTICE 5 — ACCESS MONITORING.

Log all agent access to data and systems:
A. WHO (which agent identity).
B. WHAT (resource accessed, action taken).
C. WHEN (timestamp).
D. CONTEXT (originating user, business purpose if known).
E. ANOMALY DETECTION — alert when an agent accesses unusual resources or acts outside its profile.

PRACTICE 6 — REVOCATION CAPABILITY.

The ability to IMMEDIATELY REVOKE agent access:
A. KILL-SWITCH for individual agents (disable identity, revoke tokens).
B. SYSTEM-LEVEL kill-switch for agent classes.
C. EMERGENCY PROCEDURE for multi-agent system shutdown.
D. TESTING of kill-switches periodically (a kill-switch never tested is unreliable).

CRITICAL DATA POINT — only 65 % of organizations have an effective kill-switch capability for autonomous agents (April 2026 surveys). This is a MAJOR governance gap.

THE GOVERNED AGENT MODEL — SailPoint's framework.

The « Governed Agent » concept treats agents as FIRST-CLASS IAM ENTITIES. Key elements:

ELEMENT 1 — AGENT LIFECYCLE TIED TO IAM. Agent creation triggers IAM provisioning; agent retirement triggers IAM deprovisioning. No agents exist outside IAM.

ELEMENT 2 — POLICY-BASED ACCESS. Agents inherit access policies from defined roles (« data analyst agent », « customer service agent », « monitoring agent »), not ad hoc.

ELEMENT 3 — CONTINUOUS COMPLIANCE. IAM continuously evaluates whether each agent's access matches its assigned role.

ELEMENT 4 — RUNTIME ENFORCEMENT. Beyond initial provisioning, runtime systems enforce policies on each action (Microsoft Agent Governance Toolkit, April 2026, is an example).

INTEGRATION WITH BROADER IAM:

A. EXISTING IDP (Identity Provider) — Okta, Azure AD, Auth0 — extended to support agent identities.
B. PRIVILEGED ACCESS MANAGEMENT (PAM) for high-privilege agents.
C. SIEM (Security Information and Event Management) ingesting agent logs.
D. CASB (Cloud Access Security Broker) for agents in cloud environments.

CHALLENGES:

CHALLENGE 1 — LEGACY SYSTEMS. Many enterprise systems weren't designed for agent identities. Workarounds: API gateways, adapter layers, manual provisioning.

CHALLENGE 2 — DYNAMIC PERMISSIONS. Some agents need TEMPORARY elevated access (e.g., to perform a one-time task). Solution: just-in-time access with automatic revocation.

CHALLENGE 3 — MULTI-AGENT SYSTEMS. When agents talk to each other, who has what access? Solution: explicit agent-to-agent authorization protocols.

CHALLENGE 4 — VENDOR AGENTS. Microsoft Copilot, Salesforce Einstein, etc. — these run on vendor infrastructure with vendor-defined permissions. Limited visibility for the customer organization.

ARTICULATION WITH BROADER GOVERNANCE:

A. PRIVACY (LOI 25) — agent identity enables auditing of who accessed which personal data.
B. SECURITY (ISO 27001) — agent IAM is part of access control (Annex A.5).
C. COMPLIANCE (EU AI ACT) — Art. 12 logging and Art. 14 oversight require agent identity.
D. INCIDENT RESPONSE — without agent identity, root cause analysis is impossible.

POSITIONING FOR NORD PARADIGM — agent IAM is a TECHNICAL DELIVERABLE that may require partnership with cyber security firms or IAM platform vendors. But the governance design (which agent should have which permissions) is firmly in Nord Paradigm's expertise.
        """.strip(),
    },

    "m11_c3_agent_lifecycle_governance": {
        "module": 11, "ordre": 3, "langue": "en",
        "titre": "Agent governance lifecycle (design to decommissioning)",
        "prereqs": ["m11_c1_agent_inventory_classification"],
        "texte": """
Agent governance is not a one-time event; it is a CONTINUOUS LIFECYCLE from design through decommissioning. The Singapore Model AI Governance Framework for Agentic AI (January 2026) and SailPoint's Governed Agent approach define five lifecycle phases.

PHASE 1 — DESIGN: INTENTIONAL SCOPE DEFINITION.

Before any code is written, define:

A. INTENDED USE — what should the agent do? Explicit purpose statement.
B. ACCESSIBLE SYSTEMS — explicit ALLOW LIST (not block list) of systems the agent can interact with.
C. PROCESSABLE DATA — what data the agent can read and write.
D. HUMAN OVERSIGHT CHECKPOINTS — where must a human approve before the agent proceeds? Critical for autonomous agents.
E. AGENT OBJECTIVES AND LIMITATIONS — what the agent IS and IS NOT meant to do.

DESIGN DOCUMENT TEMPLATE:
- Agent name and unique ID.
- Responsible human (named).
- Purpose and use cases.
- Inputs (what triggers it; what data it reads).
- Outputs (what it produces; what actions it can take).
- Boundaries (what it cannot do).
- Oversight mechanisms.
- Performance metrics.
- Termination conditions.

PHASE 2 — DEPLOYMENT: CONTROLLED ACTIVATION.

Move from concept to production carefully:
A. PILOT in controlled environment first (sandbox, limited user group).
B. ASSIGN IDENTITY and initial least-privilege permissions.
C. SET UP MONITORING and alerting from day one.
D. ESTABLISH ESCALATION PROCEDURES for unintended actions.
E. TRAIN USERS on agent capabilities and limitations.
F. DOCUMENT in agent inventory.

DEPLOYMENT GATES — for high-risk agents, require explicit approvals:
A. Technical sign-off (security, IT operations).
B. Business sign-off (responsible human, data owner).
C. Compliance sign-off (RPRP / DPO for personal data agents).
D. Executive sign-off for high-stakes deployments.

PHASE 3 — OPERATIONS: CONTINUOUS MONITORING.

Day-to-day operation requires:

A. BEHAVIOUR MONITORING — is the agent acting within expected parameters? Drift detection.
B. ACCESS PATTERN AUDITING — is the agent accessing resources it shouldn't? Anomaly alerts.
C. DECISION QUALITY TRACKING — are the agent's recommendations or decisions good?
D. ANOMALY DETECTION — sudden changes in behaviour, access patterns, or outputs.
E. AGENT LOGS — comprehensive audit trail of decisions and actions.

KEY METRICS:
A. Volume of actions per period.
B. Error rate (where measurable).
C. Human override rate (for human-on-the-loop and human-over-the-loop).
D. Resource consumption (cost, time).
E. User satisfaction (if applicable).

PHASE 4 — INCIDENT: DETECTION AND RESPONSE.

When something goes wrong:

DETECTION mechanisms:
A. Alerts from monitoring (anomaly detected, threshold exceeded).
B. User reports (customer complains about an agent decision).
C. Audit findings (periodic review uncovers issue).
D. External notifications (regulator, partner, media).

RESPONSE STEPS:
A. IMMEDIATE CONTAINMENT — revoke agent permissions, isolate, prevent further damage.
B. INVESTIGATION — what happened, why, what's the scope?
C. REMEDIATION — fix the agent, update permissions, prevent recurrence.
D. COMMUNICATION — inform affected stakeholders, regulators if required.
E. POST-MORTEM — lessons learned, process improvements.

CONTAINMENT IS CRITICAL — the difference between a contained incident and a runaway disaster is often measured in minutes. Kill-switches must be functional and personnel must be trained to use them.

PHASE 5 — DECOMMISSIONING: CONTROLLED RETIREMENT.

When an agent is no longer needed:

A. SYSTEMATIC DECOMMISSION — not just « stop running it » but full retirement.
B. REVOKE ALL PERMISSIONS — IAM cleanup.
C. DELETE OR ARCHIVE agent models, configurations, logs.
D. NOTIFY users and dependent systems.
E. UPDATE INVENTORY (mark as retired).
F. DOCUMENT LESSONS LEARNED.
G. RETAIN AUDIT LOGS per regulatory requirements (often 6 months minimum, longer for high-risk systems).

HUMAN OVERSIGHT FOR AUTONOMOUS AGENTS — APPROPRIATE LEVELS.

The Singapore framework for agentic AI extends human involvement guidance:

HIGH-STAKES DECISIONS (legal, financial, health consequences) → human-in-the-loop. Human reviews EVERY agent action before execution.

MODERATE-IMPACT DECISIONS (operational efficiency, resource allocation) → human-on-the-loop. Human reviews decisions retrospectively and can reverse them.

LOW-IMPACT DECISIONS (routine tasks, easily reversible) → human-over-the-loop. Periodic audits of agent behaviour, escalation only if anomalies detected.

FULLY AUTONOMOUS (extremely rare and high-risk) → only in controlled, low-consequence contexts. Even then, require continuous monitoring.

OVERRIDE AND ESCALATION:
A. ALL agents must be STOPPABLE BY HUMANS (kill switch).
B. HIGH-RISK AGENT ACTIONS must be ESCALATED to authorized humans for approval.
C. ESCALATION procedures must be CLEAR, FAST, and PRACTICED REGULARLY.
D. RESPONSIBILITY for agent actions must be assigned to a NATURAL PERSON (not diffused across a team).

ACCOUNTABILITY ASSIGNMENT — A NAMED INDIVIDUAL is responsible for each agent (accountable to executive leadership). Incident responsibility is clear, not diffused. Performance metrics are transparent.

POSITIONING FOR NORD PARADIGM — agent lifecycle governance is a SEPARATE DELIVERABLE from traditional AI governance. Many organizations need help BOTH at the policy level (« what should our agent governance program look like? ») and at the operational level (« here is our agent, design its governance »). Both are billable.
        """.strip(),
    },

    "m11_c4_multi_agent_systems": {
        "module": 11, "ordre": 4, "langue": "en",
        "titre": "Multi-agent systems and emerging tooling",
        "prereqs": ["m11_c3_agent_lifecycle_governance"],
        "texte": """
Multi-agent systems exhibit BEHAVIOURS NOT PREDICTABLE from individual agent design. When agents communicate, coordinate, and possibly compete with each other, system-level outcomes can surprise everyone. This is the FRONTIER of AI governance, and the area where formal frameworks are still emerging.

EMERGENT BEHAVIOUR — some examples:

EXAMPLE 1 — TWO TRADING AGENTS, both designed conservatively, can produce a feedback loop that crashes prices in a flash crash. Neither agent does anything « wrong »; the interaction does.

EXAMPLE 2 — A CUSTOMER SERVICE AGENT and a SALES AGENT may reach contradictory conclusions about a customer's eligibility for a refund, creating customer confusion and brand damage.

EXAMPLE 3 — IN A GAMING SIMULATION, agents tasked with maximizing different metrics may sabotage each other in unexpected ways.

EXAMPLE 4 — AUTONOMOUS DEVOPS AGENTS may unintentionally cascade infrastructure changes that take down a service.

ADDRESSING EMERGENT BEHAVIOUR — six practices:

PRACTICE 1 — TESTING IN SIMULATION. Test agent interactions in simulated environments before production. Tools: simulators, replay infrastructures, agent-based modelling platforms.

PRACTICE 2 — STAGED ROLLOUT. Deploy gradually:
A. Start with one agent type, single instance.
B. Add multiple instances of same type.
C. Add second agent type interacting with first.
D. Scale up volume and complexity.
E. Monitor at each stage for unexpected behaviours.

PRACTICE 3 — AGENT COMMUNICATION PROTOCOLS. Establish clear rules for how agents communicate and coordinate:
A. STANDARDIZED MESSAGE FORMATS.
B. AUTHENTICATION between agents.
C. PRIORITY AND ARBITRATION rules.
D. TIMEOUT AND FALLBACK behaviours.

PRACTICE 4 — CONFLICT RESOLUTION. Define how agents handle disagreements or competing goals:
A. ARBITRATION RULES (e.g., one agent designated as authoritative).
B. ESCALATION TO HUMAN if conflict cannot be resolved.
C. LOGGING of conflicts for analysis.

PRACTICE 5 — GLOBAL MONITORING. Monitor SYSTEM-LEVEL behaviour, not just individual agents:
A. Aggregate metrics (total volume, total resource use, total errors).
B. Pattern detection across agents.
C. Cascade detection (one agent's actions triggering others).

PRACTICE 6 — KILL SWITCH. Ability to STOP ALL AGENTS if system-level behaviour is unexpected. Tested and documented procedure. Cascading rollback if needed.

EMERGING TOOLING — APRIL 2026 LANDSCAPE.

Multiple major vendors and open-source projects released agentic AI governance tooling in early 2026:

TOOL 1 — MICROSOFT AGENT GOVERNANCE TOOLKIT (April 2026). MIT-licensed open-source project bringing RUNTIME SECURITY GOVERNANCE to autonomous AI agents. Enforces security policies across LangChain, AutoGen, and other agent frameworks. Critical capability given that 35 % of organizations report inability to immediately stop a rogue agent.

TOOL 2 — MICROSOFT AGENT FRAMEWORK 1.0.0 (April 2026). Major consolidation point combining prior AutoGen and Semantic Kernel patterns into governed orchestration. Signals shift from experimental agent scripts toward enterprise-ready agentic infrastructure. Creates consulting opening around agent policies, permissions, logging, and human-in-the-loop controls.

TOOL 3 — LANGCHAIN / LANGRAPH GOVERNANCE EXTENSIONS. The popular open-source frameworks have added governance hooks for tracing, logging, and policy enforcement.

TOOL 4 — CREDO AI, FAIRNOW, HOLISTIC AI — vendor governance platforms with agent-specific modules.

TOOL 5 — SAILPOINT GOVERNED AGENT. Enterprise-grade agent identity and access management.

TOOL 6 — ANTHROPIC, OPENAI, GOOGLE platform-level agent governance (built into their respective developer platforms).

TOOL 7 — SECURITY VENDORS (Palo Alto, CrowdStrike, etc.) adding agent-aware monitoring.

CHOOSING TOOLING — for a Quebec SME:
A. SMALL DEPLOYMENT (1-5 agents) — manual governance via spreadsheet inventory + IAM controls + monitoring.
B. MEDIUM DEPLOYMENT (5-20 agents) — open-source toolkit (LangChain governance, Microsoft Agent Toolkit) + extended IAM.
C. LARGE DEPLOYMENT (20+ agents) — vendor governance platform (Credo AI, FairNow, etc.) + enterprise IAM (SailPoint).

KEY GOVERNANCE STANDARDS FOR AGENTIC AI:

A. SINGAPORE MODEL AI GOVERNANCE FRAMEWORK FOR AGENTIC AI v1.0 (January 22, 2026) — first official framework guidance.
B. NIST AI AGENT STANDARDS INITIATIVE (February 2026) — NIST announced an initiative to establish standards for interoperable and secure AI agent systems. Will produce formal standards over the coming 12-24 months.
C. NIST AI RMF 1.0 + GenAI Profile — applicable to agentic systems; emphasizes risk management.
D. ISO/IEC 42001 — applicable to agentic systems via the AI Management System scope.
E. EU AI ACT — will regulate high-risk agentic systems (Annex III applies if the agent operates in domains like recruitment, credit, etc.).

NO SINGLE MATURE STANDARD YET EXISTS, but the NIST initiative marks the beginning of formal standardization. Organizations are implementing DE FACTO GOVERNANCE based on identity, access, and monitoring.

GOVERNANCE GAP — FROM PILOT TO PRODUCTION.

The « pilot-to-production » challenge: organizations succeed in small, controlled, well-monitored pilots, but fail to scale governance to production environments (large-scale, distributed, harder to monitor). This creates « shadow agents » and uncontrolled access.

Bridging the gap requires:
A. Extending IAM to ALL agents (not just production-ready).
B. Automated discovery and monitoring (manual tracking doesn't scale).
C. Integration with existing security/compliance infrastructure.
D. Building governance INTO development tools, not adding it after.

LEGAL SIGNAL — Fasken Martineau Dumoulin LLP notes in its March 2026 technology sector trends analysis that AGENTIC AI WILL CONTINUE EXPANDING AUTOMATION, and organizations must balance innovation with rigorous legal, governance, and operational controls. Legal liability for agent actions remains an unsettled area with no binding Canadian framework in place. Fasken also notes a trend toward MULTI-JURISDICTIONAL HARMONIZATION: organizations adopting the highest applicable standard (typically EU AI Act) as a baseline for all jurisdictions, including Canada.

POSITIONING FOR NORD PARADIGM — agentic AI governance is the FUTURE-FACING SERVICE. Most clients today don't need it; they will in 12-24 months. Building expertise NOW — through case studies, framework adoption, tooling familiarity — positions Nord Paradigm as a thought leader as the market matures.

SECTOR-SPECIFIC APPLICATIONS:
A. FINANCE — trading agents must have bounded trading authority (portfolio limits, risk limits). Decision agents must maintain audit trails for regulatory compliance. Agents cannot override human risk controls.
B. HEALTHCARE — diagnostic agents cannot make final diagnoses autonomously; they recommend to physicians. Clinical decision support agents must be validated for safety and efficacy.
C. SUPPLY CHAIN — logistics agents can operate more autonomously (decisions are reversible, lower stakes). Procurement agents must respect budget and vendor policies. Agents cannot commit to contracts without human approval.
D. CUSTOMER SERVICE — chatbots can handle routine queries autonomously. Escalation to humans for complex or high-consequence issues. Agents must be transparent about when they involve humans.
        """.strip(),
    },

})


# ══════════════════════════════════════════════════════════════════════════════
# MODULE 12 — AI GOVERNANCE PROFESSION (IAPP AIGP)  (3 concepts, EN)
# ══════════════════════════════════════════════════════════════════════════════

CURRICULUM.update({

    "m12_c1_aigp_body_of_knowledge": {
        "module": 12, "ordre": 1, "langue": "en",
        "titre": "IAPP AI Governance Professional (AIGP) Body of Knowledge",
        "prereqs": ["m1_c2_typologie_outils"],
        "texte": """
The AI GOVERNANCE PROFESSION is an EMERGING FIELD defined by the IAPP (International Association of Privacy Professionals) through its AIGP (AI Governance Professional) certification program. The AIGP Body of Knowledge (BoK), released April 2, 2026, defines six core competency areas for professionals guiding organizational AI implementation while managing risk and ensuring safety and trust.

WHY THIS MATTERS:

A. AI GOVERNANCE IS BECOMING A DEDICATED PROFESSION, not just a side responsibility of DPOs, compliance officers, or risk managers. Just as the privacy field professionalized in the 2000s with CIPP / CIPM certifications, AI governance is following the same path.

B. CERTIFICATION VALIDATES EXPERTISE. Clients, employers, and regulators increasingly look for credentialed AI governance professionals, especially as enforcement intensifies.

C. IAPP RESEARCH FINDING — only 31 % of organizations are STRONGLY CONFIDENT in their ability to comply with applicable digital law and policy initiatives. This gap creates demand for professionals.

D. FOR DOMINIC AND NORD PARADIGM, the AIGP certification represents BOTH a learning objective (what should I master?) and a credential to differentiate the firm in the Quebec / Canadian market.

THE SIX CORE COMPETENCY AREAS of the AIGP Body of Knowledge:

DOMAIN 1 — UNDERSTANDING AI RISK MANAGEMENT.
A. Identifying AI risks (technical, ethical, legal, business).
B. Assessing impact and probability.
C. Implementing risk treatment strategies.
D. Continuous monitoring.
E. Documentation and evidence.

DOMAIN 2 — UNDERSTANDING AI GOVERNANCE FRAMEWORKS.
A. Knowledge of major frameworks: NIST AI RMF, EU AI Act, ISO/IEC 42001, OECD Principles, Singapore Model AI Governance Framework, sectoral frameworks.
B. Selecting appropriate frameworks for organizational context.
C. Mapping between frameworks (NIST ↔ ISO ↔ EU AI Act crosswalks).
D. Implementing frameworks in practice.

DOMAIN 3 — UNDERSTANDING AI USE CASES AND IMPLEMENTATION.
A. Common AI use cases across industries.
B. Implementation patterns (centralized vs decentralized, build vs buy).
C. Integration with existing IT and business systems.
D. Vendor management.
E. Sectoral considerations (finance, health, retail, public sector).

DOMAIN 4 — UNDERSTANDING AI POLICY AND REGULATION.
A. Major regulatory frameworks: EU AI Act, Loi 25 / federal Canadian regulation (evolving), GDPR, sectoral US regulations, UK approach.
B. Compliance obligations by jurisdiction.
C. Cross-border considerations.
D. Emerging regulation trends.
E. Industry codes of practice.

DOMAIN 5 — UNDERSTANDING AI ETHICS AND TRUST.
A. Ethical principles (fairness, transparency, accountability, privacy).
B. Bias detection and mitigation.
C. Stakeholder engagement.
D. Trust-building practices.
E. Cultural and societal considerations.

DOMAIN 6 — UNDERSTANDING AI GOVERNANCE OPERATIONS.
A. Building and managing AI governance programs.
B. Governance structures (committees, roles, responsibilities).
C. Documentation and reporting.
D. Training and culture change.
E. Continuous improvement.

WHAT THE AIGP CERTIFICATION VALIDATES:

The certification is designed for professionals who:
A. GUIDE ORGANIZATIONAL AI IMPLEMENTATION — strategy, policy, decisions.
B. MANAGE AI RISK throughout the lifecycle.
C. ENSURE SAFETY AND TRUST in AI systems.
D. NAVIGATE REGULATORY AND ETHICAL COMPLEXITY.
E. BRIDGE TECHNICAL AND BUSINESS perspectives.

It IS NOT a technical certification (it doesn't test ability to build models). It IS a governance, risk, compliance, and strategy certification.

WHO BENEFITS:
A. PRIVACY PROFESSIONALS expanding into AI (most common path).
B. COMPLIANCE OFFICERS adding AI to their portfolio.
C. RISK MANAGERS incorporating AI risk.
D. CONSULTANTS advising clients on AI governance.
E. EXECUTIVES needing structured knowledge.

CERTIFICATION TIMELINE:
A. AIGP exam launched 2024.
B. Body of Knowledge officially published April 2026.
C. Continuous updates as the field evolves (likely annual revisions).
D. Recertification required (typical IAPP cadence: every 2 years).

PREPARATION RESOURCES:
A. IAPP official training (4-day course).
B. Self-study guide based on BoK.
C. Practice exams.
D. Community of certified professionals.

OTHER RELEVANT IAPP CERTIFICATIONS for AI governance professionals:
A. CIPP/E (Europe-focused privacy) — useful for EU AI Act + GDPR work.
B. CIPP/C (Canada-focused privacy) — directly relevant for Loi 25 / federal Canadian work.
C. CIPM (privacy program management) — operational complement to AIGP.

POSITIONING FOR NORD PARADIGM — for Dominic, the AIGP certification validates expertise to current and prospective clients. Combined with CIPP/C (Canadian privacy), it forms a recognized credential package. Cost: AIGP exam ~$550 USD, CIPP/C exam ~$550 USD, recertification fees ~$250/year. Investment recoupable in 2-3 small client engagements.

KEY OBSERVATION — the IAPP positions AIGP as the CIPP / CIPM EQUIVALENT FOR AI GOVERNANCE. Privacy professionals rapidly adopted CIPP / CIPM in the 2010s; AIGP is following the same trajectory in 2024-2026. Early adopters benefit from market positioning before the certification becomes table stakes.

ALTERNATIVE / COMPLEMENTARY CERTIFICATIONS:
A. ISACA CDPSE (Certified Data Privacy Solutions Engineer) — more technical.
B. Certifications from cloud providers (AWS, Azure, Google Cloud) on responsible AI.
C. Academic micro-credentials from universities (ULaval, McGill, etc. starting to offer).
D. ISO 42001 lead auditor / lead implementer certifications (TÜV SÜD, BSI, etc.).

NORD PARADIGM RECOMMENDATION — pursue AIGP + CIPP/C as core. Add ISO 42001 lead auditor if the practice extends to certification audits. Stay aware of academic offerings as they may shape the next generation of professionals.
        """.strip(),
    },

    "m12_c2_enforcement_shift_2026": {
        "module": 12, "ordre": 2, "langue": "en",
        "titre": "AI governance enforcement shift — IAPP Summit 2026 signals",
        "prereqs": ["m12_c1_aigp_body_of_knowledge"],
        "texte": """
The 2026 IAPP GLOBAL SUMMIT (Washington D.C., March 30 — April 2, 2026) delivered a CONSISTENT REGULATORY MESSAGE across privacy, AI, and cybersecurity: PAPER COMPLIANCE IS NO LONGER SUFFICIENT. The signals from regulators and senior practitioners reflect a structural shift in how AI governance will be assessed and enforced.

This concept synthesizes the SIX MAJOR ENFORCEMENT SIGNALS observable in 2026 and what they mean for governance practice.

SIGNAL 1 — OUTCOMES-BASED ENFORCEMENT.

Regulators are signaling a shift from DOCUMENT-FIRST assessment to OPERATIONAL-EXECUTION-FIRST assessment. Governance programs that exist only on paper will face increasing scrutiny.

CONCRETE IMPLICATION:
A. A well-written EFVP that doesn't reflect actual practice → non-compliance.
B. A documented incident response procedure that's never been tested → non-compliance.
C. A governance committee that meets formally but doesn't actually decide → non-compliance.

WHAT REGULATORS LOOK FOR:
A. EVIDENCE that procedures are FOLLOWED, not just exist.
B. RECORDS of committee decisions and dissent.
C. INCIDENT post-mortems demonstrating learning.
D. METRICS showing year-over-year improvement.

SIGNAL 2 — BOARD AND C-SUITE ACCOUNTABILITY.

The California Privacy Protection Agency now REQUIRES BOARD-LEVEL OVERSIGHT of privacy risk assessments. Multiple regulators indicated mandated board review for AI governance is a likely expansion. For AI governance professionals, this means accountability chains must extend to the EXECUTIVE LEVEL.

CONCRETE IMPLICATION:
A. AI governance must be a regular BOARD AGENDA ITEM.
B. The CEO / DG personally bears accountability — not just the privacy officer.
C. Annual reports to the board on AI governance maturity become expected practice.
D. Board members need TRAINING on AI governance basics.

WHAT THIS MEANS for Nord Paradigm — Brèche Pro and Prisme should produce executive summaries SUITABLE FOR BOARD CONSUMPTION. The technical detail goes in appendices; the governance maturity assessment goes in the main report.

SIGNAL 3 — UNIFIED GOVERNANCE MODEL.

Regulators emphasized that AI governance CANNOT BE SEPARATED from privacy and security compliance, given AI's dependence on personal data processing. Organizations are expected to INTEGRATE these functions rather than maintain siloed programs.

CONCRETE IMPLICATION:
A. PRIVACY OFFICER, SECURITY OFFICER, and AI LEAD should coordinate or be the same person.
B. INTEGRATED documentation (one set of policies covering privacy + security + AI).
C. INTEGRATED training across functions.
D. INTEGRATED risk register.

POSITIONING — for a Quebec SME, this means the RPRP / DPO and the AI Lead should be ONE PERSON or operate as a TIGHTLY-COORDINATED TEAM. Separate functions with separate documentation is increasingly viewed as inefficient and ineffective.

SIGNAL 4 — TRANSPARENCY REQUIREMENTS.

INCREASING REGULATORY EXPECTATION for transparency around AI inputs, logic, and outputs. Explainability is shifting from a BEST PRACTICE to an ENFORCEMENT TARGET.

CONCRETE IMPLICATION:
A. Organizations must be able to explain AI decisions — not just claim explainability.
B. Affected individuals' demands for explanation must be RESPONDED TO TIMELY (30 days under Loi 25).
C. Public-facing transparency reports on AI use are increasingly common (and increasingly expected).
D. Hidden AI use (« stealth deployment ») is becoming a violation in itself.

NEW ARTIFACT TYPE — TRANSPARENCY REPORTS, similar to corporate sustainability reports, becoming standard for organizations using AI substantially.

SIGNAL 5 — VENDOR LANDSCAPE MATURATION.

The IAPP AI GOVERNANCE VENDOR REPORT 2026 (released at Summit, available via aigl.blog) is a landscape report on AI governance tooling vendors. It indicates a MATURING VENDOR ECOSYSTEM for governance platforms. Major players: Credo AI, FairNow, Holistic AI, Monitaur. Plus integrations with established platforms (ServiceNow, Workday, Salesforce).

CONCRETE IMPLICATION:
A. Manual governance approaches (Excel spreadsheets) sufficient for SMEs.
B. Mid-market organizations increasingly adopting vendor platforms.
C. Enterprises demanding integrated governance across compliance, security, AI.

POSITIONING — Nord Paradigm should know the vendor landscape but remain VENDOR-AGNOSTIC. Recommend tools based on client size and needs, not vendor relationships. Most Quebec SMEs are best served by manual / spreadsheet approaches initially, graduating to platforms as scale increases.

SIGNAL 6 — INTERNATIONAL COORDINATION.

Regulators demonstrated growing coordination:
A. The OPC and 60 international counterparts joint statement on AI-generated content (February 2026).
B. The ICO foundation model engagement.
C. The CAI participating in international working groups.
D. Cross-border investigations becoming more common.

CONCRETE IMPLICATION — a violation in one jurisdiction is increasingly likely to draw scrutiny from others. Multi-jurisdictional organizations cannot rely on « we're only big in Quebec » reasoning to limit exposure.

WHAT IT MEANS FOR THE PROFESSION:

The IAPP Summit 2026 signals that AI GOVERNANCE PROFESSIONALS will need to:
A. THINK OPERATIONALLY, not just legally — execution matters more than documentation.
B. INTERFACE WITH EXECUTIVES — communication skills as important as technical knowledge.
C. INTEGRATE FUNCTIONS — privacy, security, AI all converge.
D. DEMONSTRATE METRICS — quantitative impact of governance on the business.
E. MAINTAIN INTERNATIONAL AWARENESS — even local practices have global implications.

NEW SKILLS THAT MATTER:
A. Risk quantification (not just qualitative risk matrices).
B. Executive communication and storytelling.
C. Cross-functional facilitation.
D. Vendor evaluation and procurement.
E. Public reporting and stakeholder engagement.

POSITIONING FOR DOMINIC — the AF9000+ background is RELEVANT. Quality auditing trained the discipline of evidence-based assessment, which is exactly what outcomes-based enforcement requires. Nord Paradigm can frame its services as « AF9000+ rigour applied to AI governance » — a unique market positioning.

KEY MONITORING POINTS:
A. First major enforcement actions citing « failed paper compliance ».
B. Board-level requirements becoming explicit in regulations.
C. Vendor consolidation in governance platform space.
D. Maturation of metrics and benchmarks.
E. Evolution of AIGP Body of Knowledge.
        """.strip(),
    },

    "m12_c3_ai_roi_measurement": {
        "module": 12, "ordre": 3, "langue": "en",
        "titre": "AI ROI measurement and value scorecard demand",
        "prereqs": ["m12_c1_aigp_body_of_knowledge"],
        "texte": """
A SECOND MAJOR THEME of 2026 — alongside enforcement intensification — is the GROWING GAP between AI adoption and provable business value. ERP Today and Grant Thornton both report (April 2026) that the issue is not whether teams can run pilots; it is whether LEADERS CAN CONNECT AI USAGE TO PRODUCTIVITY, COST, QUALITY, AND RISK OUTCOMES. This creates direct demand for SIMPLE AI VALUE SCORECARDS, USE-CASE PRIORITIZATION FRAMEWORKS, and GOVERNANCE METRICS that non-technical executives can understand.

THE STARK DATA — April 2026 surveys:

WRITER.COM SURVEY: 75 % of executives admit their AI strategy is « MORE FOR SHOW » than operational guidance.

KPMG GLOBAL AI PULSE SURVEY: only a small group of « AI leaders » capture real business value from agentic deployments.

FORRESTER PREDICTION: enterprises will defer 25 % of planned 2026 AI spend into 2027 due to inability to demonstrate value.

CFIB 2026 RESEARCH (Canadian Federation of Independent Business): Canadian businesses are moving into AI, but EMPLOYEE ENABLEMENT remains uneven. Adoption without training creates low utilization, weak ROI, employee resistance.

STATISTICS CANADA APRIL 2026 STUDY: confirmed adoption-productivity gap; AI investment not yet translating to GDP-level productivity gains.

THE CORE PROBLEM — AI projects often:
A. Start with TECHNICAL EXCITEMENT but no clear business case.
B. Lack OUTCOME METRICS (« we deployed AI » is not an outcome).
C. Don't account for CHANGE MANAGEMENT and training costs.
D. Underinvest in GOVERNANCE, leading to incidents that erode value.
E. Overpromise on TIMELINES to executive sponsors.

THE VALUE PROPOSITION SHIFT — for AI governance professionals:

The governance profession's value proposition shifts from « COMPLIANCE DOCUMENTATION » to « MEASURABLE BUSINESS IMPACT DEMONSTRATION ». Three concrete deliverables in demand:

DELIVERABLE 1 — AI VALUE SCORECARD.

A simple, executive-readable artifact that for each AI initiative captures:
A. INTENDED OUTCOMES — productivity, cost reduction, quality, customer experience, risk reduction.
B. BASELINE METRICS — current state before AI.
C. TARGET METRICS — expected after AI deployment.
D. ACTUAL METRICS — measured after deployment, periodically updated.
E. GOVERNANCE STATUS — compliance, incidents, audit results.

The scorecard makes ROI VISIBLE and DEFENSIBLE. It also surfaces GOVERNANCE FAILURES (a system meeting business metrics but causing privacy or fairness issues).

DELIVERABLE 2 — USE-CASE PRIORITIZATION FRAMEWORK.

A structured method for choosing WHICH AI USE CASES to pursue:
A. EXPECTED VALUE (cost, productivity, quality benefits).
B. EXPECTED COST (development, integration, training, governance).
C. RISK PROFILE (privacy, fairness, security, regulatory).
D. CHANGE MANAGEMENT REQUIREMENTS.
E. STRATEGIC FIT.

Output: a PRIORITIZED PORTFOLIO. Avoid the « we're doing AI! » mode where every department launches its own pilot without coordination.

DELIVERABLE 3 — GOVERNANCE METRICS DASHBOARD.

Quantitative metrics on the governance program itself:
A. INVENTORY COVERAGE (% systems formally inventoried).
B. ASSESSMENT COVERAGE (% systems with current EFVP / AIA).
C. INCIDENT COUNT (by severity, trend).
D. RESPONSE TIMES (to data subject requests, to incidents).
E. TRAINING COVERAGE (% personnel trained at appropriate level).
F. AUDIT FINDINGS (open / closed / overdue).
G. ROI METRICS (productivity, cost reduction, quality improvements per system).

POSITIONING FOR NORD PARADIGM — these three deliverables are HIGH-VALUE and SCARCE. Most consulting firms either focus on technical implementation (deploying models) or pure compliance (writing EFVPs). Few translate AI governance into BUSINESS-EXECUTIVE language.

OPPORTUNITIES:

A. Add AI VALUE SCORECARD as a standard deliverable in Brèche Pro engagements.
B. Offer USE-CASE PRIORITIZATION WORKSHOPS as a service for clients with multiple AI ambitions.
C. Build a GOVERNANCE METRICS DASHBOARD template for Prisme certifications.

THE QUEBEC ANGLE — Statistics Canada's data is available; CFIB's research is available; many SMEs have done pilots. The OPPORTUNITY for Nord Paradigm is to help clients TRANSLATE PILOT PROOFS-OF-CONCEPT INTO PRODUCTION VALUE — a specific transition where most organizations stumble.

THE BROADER MESSAGE — AI governance is not a COST CENTER. It is a VALUE-PROTECTION FUNCTION that prevents:
A. Regulatory fines.
B. Reputational damage.
C. Customer churn from privacy violations.
D. Failed deployments (« shelfware »).
E. Insurance premium increases.

Quantifying this prevention is the next professional skill.

EXAMPLE QUANTIFIED CASE — a hypothetical but realistic scenario:

A Quebec SME deploys an AI recruitment tool without an EFVP. The CAI investigates following a complaint. Outcome: CAI finds violations of Loi 25 Art. 12.1 and 3.3.
A. SAP imposed: $200,000 (modest, given small company).
B. Reputational impact: 18 months of public scrutiny.
C. Two key clients leave.
D. Insurance renewal cost increases.
E. Internal remediation: 3 months of work, $150,000.
TOTAL VISIBLE COST: ~$2-4 million over 24 months for a modest violation.

PREVENTION COST — full Brèche Pro engagement for this client: $50,000-$100,000. Expected value of prevention: 20-40x.

This kind of QUANTIFIED VALUE STORY is what executives respond to. AI governance professionals must be able to TELL IT.

POSITIONING FOR THE NORD PARADIGM PORTFOLIO:
A. BRÈCHE (free) — initial cartography. Demonstrates SCALE OF EXPOSURE.
B. BRÈCHE PRO — full assessment with VALUE SCORECARD and risk-quantified action plan.
C. PRISME — ISO 42001 audit producing GOVERNANCE METRICS DASHBOARD and CERTIFICATION-READY documentation.

Each tier creates increasing demonstrable value, justifying premium pricing on the high end.
        """.strip(),
    },

})


# ══════════════════════════════════════════════════════════════════════════════
# MODULE 13 — SYNTHÈSE STRATÉGIQUE POUR PME QUÉBÉCOISE  (2 concepts, FR)
# ══════════════════════════════════════════════════════════════════════════════

CURRICULUM.update({

    "m13_c1_comparaison_transversale": {
        "module": 13, "ordre": 1, "langue": "fr",
        "titre": "Comparaison transversale des cadres",
        "prereqs": [
            "m2_c1_loi25_vue_ensemble",
            "m3_c1_canada_paysage_federal",
            "m4_c1_eu_ai_act_overview",
            "m5_c1_nist_rmf_origin_structure",
            "m6_c1_iso42001_norme_certifiable",
            "m1_c4_principes_ocde",
        ],
        "texte": """
Une vue comparative est essentielle pour comprendre où chaque cadre apporte une valeur unique et où ils se chevauchent. Cette comparaison se fait selon SIX DIMENSIONS : nature juridique, champ d'application, approche, exigences, sanctions, calendrier.

DIMENSION 1 — NATURE JURIDIQUE.

LOI 25 (Québec) : Hard law. Loi provinciale. En vigueur.
RÉGULATION FÉDÉRALE CANADIENNE : En cours d'élaboration. Pas adoptée au 25 avril 2026.
DIRECTIVE FÉDÉRALE ADM : Politique du Conseil du Trésor, contraignante pour le secteur public fédéral.
CODE VOLONTAIRE CANADIEN : Soft law. Engagement public.
EU AI ACT : Hard law. Règlement européen directement applicable. En vigueur, application phasée.
RGPD : Hard law. Règlement européen. En vigueur depuis 2018.
UK DUAA 2025 : Hard law. Loi britannique. En vigueur.
NIST AI RMF : Cadre opérationnel volontaire.
ISO/IEC 42001 : Norme volontaire certifiable.
CNIL — guides opérationnels : soft law / lignes directrices d'autorité.
SINGAPORE MGF : Cadre volontaire industrie-friendly.
PRINCIPES OCDE : Soft law. Recommandation intergouvernementale.
UNESCO ETHIQUE : Soft law mondiale.
IAPP AIGP : Cadre professionnel volontaire.

DIMENSION 2 — CHAMP D'APPLICATION.

LOI 25 : Tout traitement de RP de Québécois, où que soit l'organisation.
DIRECTIVE FÉDÉRALE : Institutions fédérales canadiennes.
EU AI ACT : Tout système d'IA mis sur le marché ou ayant des sorties utilisées dans l'UE.
UK DUAA 2025 : Organismes opérant au Royaume-Uni; ADM avec données catégories spéciales.
NIST RMF : Adoption volontaire mondiale.
ISO 42001 : Adoption volontaire mondiale.
CNIL : Organisations sous juridiction française (RGPD).
SINGAPORE : Adoption volontaire mondiale, avec présence forte en Asie-Pacifique.
PRINCIPES OCDE / UNESCO : Soft law mondiale.

DIMENSION 3 — APPROCHE RÉGLEMENTAIRE.

LOI 25 : Fondée sur les principes (transparence, consentement, minimisation), focalisée sur les RP.
DIRECTIVE FÉDÉRALE ADM : Fondée sur les niveaux d'impact (I-IV) avec AIA en outil pivot.
EU AI ACT : Fondée sur les risques (4 niveaux + GPAI).
UK DUAA 2025 : Sectoriel avec assouplissements ADM.
NIST RMF : Fondée sur les fonctions (GOVERN, MAP, MEASURE, MANAGE).
ISO 42001 : Fondée sur le management (PDCA, AIMS).
CNIL : Fondée sur le cycle de vie (7 phases).
SINGAPORE MGF : Fondée sur 4 dimensions opérationnelles.
PRINCIPES OCDE : Fondée sur les valeurs (5 principes + 5 recommandations + Due Diligence 6 étapes).
UNESCO : Fondée sur les droits humains (4 valeurs + 10 principes).

DIMENSION 4 — EXIGENCES PRINCIPALES.

LOI 25 : RPRP, EFVP, consentement renforcé, droits des personnes (incluant Art. 8.1 et 12.1), notification d'incidents, registres.

DIRECTIVE FÉDÉRALE ADM : AIA, niveaux d'impact, transparence, intervention humaine proportionnelle, recours, AI Register.

EU AI ACT : Pour les systèmes à haut risque, neuf exigences techniques (gestion des risques, données, documentation, journalisation, transparence, surveillance humaine, exactitude/robustesse/cybersécurité, gestion qualité, surveillance post-commercialisation), plus enregistrement, marquage CE, et FRIA.

UK DUAA 2025 : Code statutaire ADM/AI à venir; engagement avec fournisseurs de modèles de fondation; toolkit ICO de risques.

NIST RMF : 19 catégories d'actions opérationnelles, 70+ sous-catégories, à appliquer selon le contexte. Profils sectoriels (GenAI, Critical Infrastructure, Agents).

ISO 42001 : 38 contrôles répartis en 9 domaines, plus la conformité aux 10 chapitres HLS.

CNIL : 7 phases du cycle de vie, chacune avec ses chantiers détaillés.

SINGAPORE : 4 dimensions × multiples sous-éléments + outils (AI Verify, ISAGO, Compendium, GenAI Starter Kit, framework agentique).

OCDE : Application via le travail réglementaire des États adhérents + Due Diligence Guidance (6 étapes).

DIMENSION 5 — SANCTIONS.

LOI 25 : SAP jusqu'à 10 M$ ou 2 % CA. Pénales jusqu'à 25 M$ ou 4 %.

DIRECTIVE FÉDÉRALE ADM : Politique interne; pas de SAP directe pour le secteur public.

EU AI ACT : Pratiques interdites (Art. 5) jusqu'à 35 M€ ou 7 %. Manquements haut risque/GPAI jusqu'à 15 M€ ou 3 %. Information trompeuse jusqu'à 7,5 M€ ou 1 %. PME : moins élevé des deux.

UK DUAA 2025 : Sanctions UK GDPR (jusqu'à 4 % CA mondial pour les violations majeures); sanctions spécifiques DUAA à préciser.

NIST RMF : Aucune sanction directe. Risque réputationnel et exposition civile.

ISO 42001 : Aucune sanction directe. Perte de la certification.

CNIL : Sanctions RGPD (jusqu'à 4 % CA mondial).

SINGAPORE : Sanctions PDPA (jusqu'à 10 % chiffre d'affaires depuis 2022).

PRINCIPES OCDE / UNESCO : Aucune sanction.

DIMENSION 6 — CALENDRIER.

LOI 25 : Toutes les phases en vigueur (sept 2024).

RÉGULATION FÉDÉRALE CANADIENNE : Non adoptée au 25 avril 2026.

DIRECTIVE FÉDÉRALE ADM : Mise à jour effective 24 juin 2025; conformité requise 24 juin 2026 pour systèmes existants.

EU AI ACT : Entrée 1 août 2024. Pratiques interdites 2 février 2025. GPAI 2 août 2025. Haut risque (Annexe III) 2 août 2026. Plein 2 août 2027. STATUT OMNIBUS (mai 2026) : trilogue 13 mai 2026 sans accord; deadline ferme 2 août 2026 si non adopté.

UK DUAA 2025 : Loi en vigueur juin 2025; implémentation phasée jusqu'à juin 2026; code statutaire AI/ADM attendu.

NIST RMF : Disponible depuis 26 janvier 2023. GAI Profile 26 juillet 2024. Critical Infrastructure Profile en développement (avril 2026). Agent Standards Initiative (février 2026).

ISO 42001 : Publiée 18 décembre 2023. Certifiable immédiatement.

CNIL : Guides actifs depuis 2023-2024.

SINGAPORE : MGF depuis 2019; édition 2 depuis 2020; framework agentique depuis 22 janvier 2026; AI Verify maintenu en continu.

OCDE : Principes 22 mai 2019, mis à jour 3 mai 2024. Due Diligence Guidance 19 février 2026.

UNESCO : Adoptée novembre 2021.

CHEVAUCHEMENTS et COMPLÉMENTARITÉS :

ZONE A — RP traités par IA. Loi 25 + RGPD + EU AI Act + ISO 27701 + CNIL guides + NIST RMF (vie privée).

ZONE B — Système d'IA à haut risque déployé en Europe. EU AI Act + RGPD + ISO 42001 + NIST RMF + Code OECD Due Diligence.

ZONE C — Système d'IA déployé au Québec sans clientèle européenne. Loi 25 + Code volontaire canadien + Directive fédérale (référence) + NIST RMF + Singapore MGF (référence opérationnelle).

ZONE D — Modèle GPAI. EU AI Act (Art. 51-55) + GPAI Code of Practice + NIST AI 600-1.

ZONE E — Système agentique. Singapore MGF for Agentic AI + NIST Agent Standards + Microsoft Agent Governance Toolkit.

ZONE F — Système à haut risque dans l'infrastructure critique. NIST Critical Infrastructure Profile + secteur réglementaire applicable.

DIVERGENCES NOTABLES :

A. LOI 25 vs RGPD — la Loi 25 PERMET les décisions automatisées moyennant transparence; le RGPD les INTERDIT par défaut sauf exceptions.

B. EU AI ACT vs UK DUAA 2025 — divergence sur l'ADM. UK est plus permissif que UE.

C. EU AI ACT vs NIST RMF — EU AI Act est PRESCRIPTIF (obligations énumérées); NIST RMF est ADAPTATIF (méthode à appliquer selon le contexte).

D. ISO 42001 vs NIST RMF — ISO impose une structure auditée et certifiable; NIST laisse la liberté d'implémentation.

CONVERGENCES STRUCTURELLES :

A. TOUS les cadres exigent une forme d'ÉVALUATION D'IMPACT préalable.
B. TOUS les cadres exigent une forme de GOUVERNANCE INTERNE (rôles, responsabilités).
C. TOUS les cadres exigent une forme de TRANSPARENCE pour les personnes affectées.
D. TOUS les cadres exigent une forme de SURVEILLANCE HUMAINE et de capacité à corriger.
E. TOUS les cadres exigent une forme de DOCUMENTATION TRAÇABLE.

CONCLUSION ANALYTIQUE — bien que les cadres divergent en force juridique et en détail, ils convergent fortement sur les FONCTIONS organisationnelles attendues. Une organisation qui implémente sérieusement le NIST AI RMF couvre simultanément 70-90 % des exigences de fond de tous les autres cadres. Ce qui change, c'est la FORME (documentation, certification, notification) et les SANCTIONS.

POUR LE LECTEUR — exercice utile : prendre votre système d'IA et identifier dans cette matrice les zones applicables. La somme des zones définit votre programme de conformité minimal.
        """.strip(),
    },

    "m13_c2_strategie_pme_quebecoise": {
        "module": 13, "ordre": 2, "langue": "fr",
        "titre": "Stratégie de conformité IA pour PME québécoise — feuille de route 24 mois",
        "prereqs": ["m13_c1_comparaison_transversale", "m10_c4_gouvernance_organisationnelle_raci"],
        "texte": """
Synthèse opérationnelle — comment une PME québécoise structure pratiquement son programme de gouvernance d'IA en tenant compte de tous les cadres étudiés. Cette stratégie repose sur QUATRE PRINCIPES, SEPT ÉTAPES, et tient compte des SIGNAUX D'APPLICATION 2026.

LES QUATRE PRINCIPES STRATÉGIQUES :

PRINCIPE 1 — PROPORTIONNALITÉ. Le programme doit être proportionnel à l'exposition réelle. Une PME avec un chatbot interne ne doit pas appliquer le même dispositif qu'une PME qui vend de l'IA à des hôpitaux européens.

PRINCIPE 2 — PRIMAUTÉ DU DROIT DUR. Les obligations LÉGALES (Loi 25) priment sur les normes volontaires (ISO, NIST). Une certification ISO 42001 sans conformité Loi 25 expose à des sanctions; l'inverse expose à perdre des contrats mais pas à des amendes immédiates.

PRINCIPE 3 — INVESTIR DANS L'INFRASTRUCTURE COMMUNE. Plus de 70 % des exigences se chevauchent entre les cadres. Construire une infrastructure de gouvernance unique (politique, comité, inventaire, évaluations, formation) qui sert simultanément plusieurs cadres maximise l'effet de chaque dollar.

PRINCIPE 4 — HARMONISER VERS LE STANDARD LE PLUS ÉLEVÉ. Tendance observée par Fasken et l'IAPP en 2026 : les organisations multinationales harmonisent leur gouvernance interne sur le STANDARD APPLICABLE LE PLUS STRICT (typiquement l'EU AI Act). Plus économique sur 3-5 ans qu'une approche multi-juridiction fragmentée.

LES SEPT ÉTAPES — feuille de route 24 mois :

ÉTAPE 1 — DIAGNOSTIC INITIAL (semaines 1-4).
A. Cartographier les SYSTÈMES D'IA en service ou en projet (concept M10 c1).
B. Identifier les CLIENTS SOUMIS À DES RÉGIMES (européens? sectoriels? gouvernementaux?).
C. Identifier les DONNÉES traitées (RP de Québécois? d'Européens? de mineurs? sensibles?).
D. Évaluer la MATURITÉ ACTUELLE en gouvernance.
E. Produire un RAPPORT DE DIAGNOSTIC qui identifie les écarts et chiffre l'effort.

CORRESPOND À — Brèche (gratuit) chez Nord Paradigm.

ÉTAPE 2 — CONFORMITÉ LOI 25 (mois 1-6).
A. Désigner et FORMALISER le RPRP. Publier les coordonnées.
B. Adopter une POLITIQUE DE CONFIDENTIALITÉ conforme et accessible.
C. Mettre en place le PROCESSUS D'EFVP — pour les nouveaux projets ET, rétroactivement, pour les systèmes en service.
D. Mettre en place les REGISTRES (incidents, communications hors Québec).
E. Adapter les CONSENTEMENTS pour qu'ils soient manifestes, libres, éclairés, à des fins spécifiques.
F. Pour les décisions exclusivement automatisées : préparer le mécanisme de notification (Art. 12.1) et de révision humaine.
G. Former le PERSONNEL au minimum sur les bases.

ÉTAPE 3 — ADOPTION DU NIST AI RMF (mois 4-12, en parallèle).
A. POLITIQUE D'IA d'entreprise (1 page) approuvée par la direction.
B. COMITÉ IA mensuel constitué.
C. PILOTE IA désigné (peut être le RPRP).
D. INVENTAIRE D'IA finalisé et mis sous gouvernance.
E. ÉVALUATIONS D'IMPACT (MAP) sur les 3-5 systèmes les plus critiques.
F. MESURES (MEASURE) opérationnelles : monitoring, tests de biais, journaux.
G. PLAN DE TRAITEMENT (MANAGE) des risques identifiés.
H. RAPPORT TRIMESTRIEL à la direction.

CORRESPOND À — Brèche Pro chez Nord Paradigm.

ÉTAPE 4 — CODE VOLONTAIRE et COMMUNICATION (mois 6-12).
A. Évaluer si la signature du Code de conduite volontaire canadien apporte une valeur (signal client, alignement stratégique).
B. Si oui : signer et publier l'engagement.
C. Communiquer la POLITIQUE D'IA aux clients, partenaires, employés.
D. Mettre à jour le SITE WEB avec la politique de confidentialité, les coordonnées du RPRP, les principes IA suivis.

ÉTAPE 5 — ADAPTATION EU AI ACT (mois 9-18, si exposition européenne).
A. CARTOGRAPHIER les systèmes selon les niveaux de risque (Annexe III, GPAI, transparence, minimal).
B. Pour systèmes à HAUT RISQUE : projet de mise en conformité distinct (gestion des risques, qualité des données, documentation Annexe IV, surveillance humaine, marquage CE).
C. Pour systèmes intégrant des modèles GPAI : conserver les attestations des fournisseurs, intégrer dans la documentation système.
D. Désigner un REPRÉSENTANT AUTORISÉ dans l'UE si fournisseur hors UE.
E. ENREGISTRER les systèmes à haut risque dans la base européenne.
F. ANTICIPER l'application aux systèmes à haut risque le 2 août 2026 (deadline ferme malgré le statut Omnibus).

ÉTAPE 6 — CERTIFICATION ISO 42001 (mois 12-24, si justifiée).
A. Faire un GAP ANALYSIS contre les 38 contrôles (utiliser l'infrastructure NIST RMF déjà en place).
B. Combler les écarts.
C. Faire un AUDIT INTERNE.
D. Sélectionner un ORGANISME CERTIFICATEUR.
E. Audit Stage 1 (documentation), Audit Stage 2 (terrain).
F. Obtenir et communiquer la certification.

CORRESPOND À — Prisme chez Nord Paradigm.

ÉTAPE 7 — VEILLE et AMÉLIORATION CONTINUE (mois 18+).
A. SURVEILLER l'évolution de la régulation fédérale canadienne, les actes délégués de l'EU AI Act, les nouveaux profils NIST (Critical Infrastructure, Agents), les développements UK.
B. METTRE À JOUR les évaluations d'impact.
C. AUDITER chaque année.
D. RÉVISER la politique d'IA aux changements majeurs (nouveau modèle, nouveau marché, nouvelle clientèle).
E. FORMER en continu (nouveautés réglementaires, nouveaux risques).
F. SUIVRE les indicateurs de VALEUR D'AFFAIRES (cf. M12 c3) — ne pas laisser le programme dériver vers une simple conformité.

BUDGETS INDICATIFS pour une PME (50-250 employés, 5-15 systèmes d'IA) :

POSTE A — Conformité Loi 25 + NIST RMF + Code volontaire :
A. Effort interne : 0,3-0,7 ETP × 12 mois.
B. Conseil externe ponctuel : 30 000 $ - 80 000 $.
C. Formation : 5 000 $ - 20 000 $.
D. Outils : 10 000 $ - 30 000 $ par an.
TOTAL Année 1 : 100 000 $ - 250 000 $. Récurrent : 50 000 $ - 100 000 $/an.

POSTE B — Conformité EU AI Act (si exposition) :
A. Effort interne additionnel : 0,3-0,5 ETP × 12 mois.
B. Conseil juridique européen : 30 000 $ - 100 000 $.
C. Documentation et contrôles techniques : 50 000 $ - 200 000 $.
D. Représentant autorisé UE : 5 000 $ - 20 000 $/an.
TOTAL incrémental : 100 000 $ - 350 000 $.

POSTE C — Certification ISO 42001 :
A. Gap analysis et conseil : 30 000 $ - 80 000 $.
B. Audit Stage 1+2 : 15 000 $ - 40 000 $.
C. Surveillance annuelle : 8 000 $ - 20 000 $.
TOTAL : 50 000 $ - 140 000 $ d'entrée; 8 000 $ - 20 000 $/an récurrent.

GRILLE DE PRIORITÉS — où investir d'abord :
A. PME locale, sans IA décisionnelle : Loi 25 + politique d'IA simple.
B. PME avec IA décisionnelle au Québec : Loi 25 (incluant Art. 8.1, 12.1) + NIST RMF.
C. PME avec exposition européenne : ajouter EU AI Act.
D. PME B2B avec exigences clients : ajouter ISO 42001.
E. PME développant des GPAI : ajouter régime GPAI EU AI Act + profil NIST GAI.
F. PME déployant des agents : ajouter Singapore MGF for Agentic AI + Microsoft Agent Governance Toolkit.
G. PME en infrastructure critique (énergie, santé) : ajouter NIST Critical Infrastructure Profile.

ERREURS STRATÉGIQUES À ÉVITER :

A. ATTENDRE QU'UNE LOI FÉDÉRALE SOIT ADOPTÉE pour démarrer — la Loi 25 est déjà en vigueur et l'EU AI Act aussi.

B. PRENDRE UNE POSITION RÉACTIVE — répondre aux audits clients un par un est plus coûteux que mettre en place un programme structuré.

C. CHERCHER LA CERTIFICATION AVANT LA MATURITÉ — un échec d'audit ISO est coûteux et publiquement embarrassant.

D. CONFIER UNIQUEMENT À LA TECHNIQUE — la gouvernance d'IA n'est pas un projet IT, c'est un projet d'entreprise.

E. NÉGLIGER LA FORMATION — une politique non comprise par les équipes ne sera pas appliquée.

F. SOUS-ESTIMER LE TEMPS — les programmes mûrs prennent 24-36 mois à se mettre en place.

G. PAPER COMPLIANCE — l'IAPP Summit 2026 a explicitement signalé que les programmes documentés mais non exécutés sont la prochaine cible des régulateurs.

CONCLUSION DU CURRICULUM — la gouvernance d'IA n'est plus un sujet académique. Au 25 avril 2026, la Loi 25 est exécutoire au Québec, l'EU AI Act commence à s'appliquer aux systèmes à haut risque (deadline ferme 2 août 2026), la Directive fédérale ADM est entrée dans sa phase de pleine conformité, et les attentes contractuelles entre entreprises se durcissent. Une PME qui démarre maintenant un programme structuré aura, dans 24 mois, un avantage compétitif important sur les concurrents qui auront tardé.

LA GOUVERNANCE BIEN FAITE N'EST PAS UN COÛT; C'EST UN INVESTISSEMENT DANS LA CONFIANCE — la ressource la plus rare dans un marché où l'IA s'industrialise plus vite que la confiance qu'elle inspire.

POUR DOMINIC ET NORD PARADIGM — la séquence Brèche → Brèche Pro → Prisme correspond DIRECTEMENT à la trajectoire d'apprentissage stratégique d'une PME québécoise. Chaque étape produit de la valeur incrémentale, et chaque étape construit l'infrastructure nécessaire à la suivante. C'est le contrat implicite que Nord Paradigm noue avec ses clients : non pas un audit ponctuel, mais un parcours de maturation sur 24 mois.
        """.strip(),
    },

})


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
    for p in prereqs:
        if p not in progression:
            return False
        if progression[p].get("statut") not in ("en_cours", "maitrise"):
            return False
    return True


def lister_curriculum() -> None:
    for m in ORDRE_AFFICHAGE_MODULES:
        nom = NOMS_MODULES.get(m)
        concepts = get_concepts_par_module(m)
        if not concepts:
            continue
        print(f"\n  Module {m} — {nom}")
        for k in concepts:
            source = CURRICULUM[k].get("source", "")
            tag = f"  [{source}]" if source else ""
            print(f"    • {CURRICULUM[k]['titre']}{tag}")


# ══════════════════════════════════════════════════════════════════════════════
# Métadonnées des modules
# ══════════════════════════════════════════════════════════════════════════════

NOMS_MODULES = {
    1:  "Fondations de la gouvernance d'IA",
    2:  "Loi 25 et la CAI",
    3:  "Cadre fédéral canadien et provinces",
    4:  "EU AI Act",
    5:  "NIST AI Risk Management Framework",
    6:  "ISO/IEC 42001 — système de management de l'IA",
    7:  "CNIL — guide opérationnel",
    8:  "Singapore Model AI Governance Framework",
    9:  "UK ICO and Data (Use & Access) Act 2025",
    10: "Mise en œuvre pratique",
    11: "Agentic AI Governance",
    12: "AI Governance Profession (IAPP AIGP)",
    13: "Synthèse stratégique pour PME québécoise",
    99: "Documents ingérés",
}

# Ordre d'affichage dans l'UI : suit l'ordre logique d'apprentissage,
# le bucket d'ingestion (99) à la fin.
ORDRE_AFFICHAGE_MODULES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 99]

# Langue principale du module : "fr" ou "en".
LANGUE_MODULES = {
    1:  "fr",
    2:  "fr",
    3:  "fr",
    4:  "en",
    5:  "en",
    6:  "fr",
    7:  "fr",
    8:  "en",
    9:  "en",
    10: "fr",
    11: "en",
    12: "en",
    13: "fr",
    99: "fr",
}

DOMAINES_MODULES = {
    1:  "gouvernance_ia",
    2:  "gouvernance_ia",
    3:  "gouvernance_ia",
    4:  "gouvernance_ia",
    5:  "gouvernance_ia",
    6:  "gouvernance_ia",
    7:  "gouvernance_ia",
    8:  "gouvernance_ia",
    9:  "gouvernance_ia",
    10: "gouvernance_ia",
    11: "gouvernance_ia",
    12: "gouvernance_ia",
    13: "gouvernance_ia",
    99: "gouvernance_ia",
}

# Sous-groupes pour segmenter les modules longs (M2, M4, M5, M7).
SOUS_GROUPES: dict[int, list[dict]] = {
    2: [
        {"titre": "Vue d'ensemble et calendrier", "min": 1, "max": 1},
        {"titre": "Gouvernance interne (RPRP, EFVP)", "min": 2, "max": 2},
        {"titre": "Consentement et droits", "min": 3, "max": 3},
        {"titre": "Décisions automatisées (8.1, 12.1)", "min": 4, "max": 4},
        {"titre": "Incidents et sanctions", "min": 5, "max": 5},
        {"titre": "Principes IA générative CAI", "min": 6, "max": 6},
        {"titre": "Tendances d'application 2026", "min": 7, "max": 7},
    ],
    4: [
        {"titre": "Overview & extraterritoriality", "min": 1, "max": 1},
        {"titre": "Prohibited practices (Art. 5)", "min": 2, "max": 2},
        {"titre": "High-risk: typology", "min": 3, "max": 3},
        {"titre": "High-risk: obligations", "min": 4, "max": 4},
        {"titre": "GPAI regime + Code of Practice", "min": 5, "max": 5},
        {"titre": "Sanctions, calendar, Omnibus", "min": 6, "max": 6},
    ],
    7: [
        {"titre": "Avant le déploiement",            "min": 1, "max": 1},
        {"titre": "Collecte et qualification",       "min": 2, "max": 2},
        {"titre": "Développement de l'algorithme",   "min": 3, "max": 3},
        {"titre": "Déploiement en production",       "min": 4, "max": 4},
        {"titre": "Droits des personnes",            "min": 5, "max": 5},
        {"titre": "Sécurité du traitement",          "min": 6, "max": 6},
        {"titre": "Conformité et incidents",         "min": 7, "max": 7},
    ],
}

PARCOURS_CONSEILLES: dict[int, dict] = {
    1:  {"module": 2,  "label": "Continuer avec la Loi 25 et la CAI →"},
    2:  {"module": 3,  "label": "Continuer avec le cadre fédéral canadien →"},
    3:  {"module": 4,  "label": "Continuer avec le EU AI Act →"},
    4:  {"module": 5,  "label": "Continuer avec NIST AI RMF →"},
    5:  {"module": 6,  "label": "Continuer avec ISO/IEC 42001 →"},
    6:  {"module": 7,  "label": "Continuer avec le guide CNIL →"},
    7:  {"module": 8,  "label": "Continuer avec Singapore Model Framework →"},
    8:  {"module": 9,  "label": "Continuer avec UK ICO + DUAA 2025 →"},
    9:  {"module": 10, "label": "Continuer avec la mise en œuvre pratique →"},
    10: {"module": 11, "label": "Continuer avec Agentic AI Governance →"},
    11: {"module": 12, "label": "Continuer avec la profession AIGP →"},
    12: {"module": 13, "label": "Conclure avec la synthèse stratégique PME →"},
}


# ══════════════════════════════════════════════════════════════════════════════
# Chargement des concepts dynamiques (ingérés via ingestion.py)
# ══════════════════════════════════════════════════════════════════════════════

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
