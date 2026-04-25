# Scientia

**Apprentissage espacé adaptatif pour lire la recherche scientifique.**
Quiz générés et évalués par Claude · Algorithme FSRS-4.5 · Curriculum
multi-domaines (statistiques, biologie, sciences politiques, histoire,
informatique, gouvernance de l'IA, ...).

L'application existe en deux saveurs :

| | Cible | Lance avec |
|---|---|---|
| **`streamlit_app.py`** *(recommandé)* | Bureau **et mobile** (web responsive) | `streamlit run streamlit_app.py` |
| `scientia.py` *(legacy)* | Terminal | `python scientia.py` |

---

## Démarrage rapide

### 1. Cloner et installer

```bash
git clone https://github.com/DA-Leclerc/Scientia.git
cd Scientia
pip install -r requirements.txt
```

### 2. Configurer la clé API Anthropic

Récupère une clé sur https://console.anthropic.com/keys

**Option A — Fichier `.env` (local)** :
```
ANTHROPIC_API_KEY=sk-ant-...
```

**Option B — Variable d'environnement (shell)** :
```bash
# macOS/Linux
export ANTHROPIC_API_KEY="sk-ant-..."

# Windows PowerShell
$env:ANTHROPIC_API_KEY = "sk-ant-..."
```

**Option C — `.streamlit/secrets.toml`** (recommandé pour Streamlit Cloud) :
```toml
ANTHROPIC_API_KEY = "sk-ant-..."
```
Voir [`.streamlit/secrets.toml.example`](.streamlit/secrets.toml.example).

### 3. Lancer

```bash
streamlit run streamlit_app.py
```

L'application s'ouvre sur http://localhost:8501

---

## Utilisation sur mobile

Trois chemins, du plus simple au plus robuste.

### Chemin A — Streamlit Community Cloud (gratuit, accessible partout)

1. Pousse ton fork sur GitHub.
2. Va sur https://share.streamlit.io/ et connecte ton compte GitHub.
3. Sélectionne le repo `DA-Leclerc/Scientia` et `streamlit_app.py`
   comme entry point.
4. Dans **Settings → Secrets**, ajoute :
   ```toml
   ANTHROPIC_API_KEY = "sk-ant-..."
   ```
5. Déploie. Tu obtiens une URL `https://...streamlit.app`
   que tu ouvres sur ton iPhone/Android.
6. Dans Safari/Chrome mobile, ajoute la page à l'écran d'accueil
   (Partager → « Sur l'écran d'accueil ») — ça l'installe comme
   une app native.

### Chemin B — Réseau local (rapide, sans déploiement)

Sur ton ordinateur :
```bash
streamlit run streamlit_app.py --server.address=0.0.0.0 --server.port=8501
```

Sur ton mobile, connecté au même WiFi, ouvre `http://<IP-ordi>:8501`.
Pour trouver l'IP :
```bash
ipconfig            # Windows  → cherche IPv4 Address
ifconfig            # macOS/Linux  → cherche inet 192.168.x.x
```

### Chemin C — Railway / Render / Fly.io (production)

1. Push sur GitHub.
2. Sur Railway, **New project → Deploy from GitHub** → Scientia.
3. Définis les variables :
   - `ANTHROPIC_API_KEY=sk-ant-...`
   - `DATA_DIR=/data` (et monte un Volume sur `/data` pour
     persister `scientia.db`)
4. **Start command** :
   ```
   streamlit run streamlit_app.py --server.port=$PORT --server.address=0.0.0.0
   ```

---

## Structure du projet

```
Scientia/
├── streamlit_app.py        # Application web (mobile + bureau)
├── scientia.py             # CLI terminal historique
├── curriculum.py           # 22 modules · 100+ concepts statiques
├── generator.py            # Génération de questions (Claude)
├── ingestion.py            # Ingestion de PDF/MD/TXT en concepts
├── db.py                   # Persistance SQLite + algo FSRS-4.5
├── requirements.txt
├── .streamlit/
│   ├── config.toml         # Thème + serveur
│   └── secrets.toml.example
├── docs/                   # PDFs et notes à ingérer (gitignore)
└── scientia.db             # Base SQLite locale (gitignore)
```

---

## Modules du curriculum

| # | Module | Domaine |
|---:|---|---|
| 1 | Fondations (statistiques) | Statistiques |
| 2 | Inférence statistique | Statistiques |
| 3 | Relations entre variables | Statistiques |
| 4 | Psychométrie et génétique | Statistiques |
| 5 | Documents personnels (ingestion) | — |
| 6 | Biologie | Biologie |
| 7 | Sciences politiques | Sciences politiques |
| 8 | Informatique | Informatique |
| 9 | Finances | Finances |
| 10 | Histoire — Historionomie | Histoire |
| 11 | Antiquité — Grèce & Rome | Histoire |
| 12 | Apprentissage moteur | Apprentissage moteur |
| 13 | Mécanique et leviers | Mécanique |
| 14 | Historiographie de la Shoah | Histoire |
| 15 | Architecture Railway | Informatique |
| 16 | Bitcoin & Cryptomonnaies | Finances |
| 17 | JSON pour non-programmeurs | Informatique |
| 18 | Lire une erreur d'agent | Informatique |
| 19 | Anatomie d'un workflow Claude | Informatique |
| 20 | Concevoir un workflow multi-agents | Informatique |
| 21 | Bash et terminal — l'essentiel | Informatique |
| **22** | **Gouvernance de l'IA** *(nouveau)* | Gouvernance IA |

### Module 22 — Gouvernance de l'IA (7 concepts)

1. Loi 25 — Québec (vie privée et IA)
2. AIDA — Canada (projet de loi C-27)
3. ISO/IEC 42001 — Management de l'IA
4. NIST AI RMF — Cadre américain
5. EU AI Act — Règlement européen
6. Principes de l'OCDE sur l'IA
7. Synthèse — Quel cadre pour quelle situation

---

## Algorithme FSRS-4.5

Scientia planifie les révisions avec
[FSRS-4.5](https://github.com/open-spaced-repetition/fsrs4anki/wiki/The-Algorithm)
(Free Spaced Repetition Scheduler), entraîné sur des millions de
révisions Anki/SuperMemo. Chaque carte conserve une `stabilité` (jours
avant que la rétention tombe à 90%) et une `difficulté` (1-10). La
date de prochaine révision est calculée pour cibler 90% de rétention.

---

## Licence

Privé — Dominic Leclerc.
