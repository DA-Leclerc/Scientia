# Scientia

**Spaced-repetition learning for AI governance practice.**

Scientia is the personal training and reference platform for **Dominic-André Leclerc** at [Nord Paradigm](https://nordparadigm.ca), a Quebec-based AI governance consultancy. It serves as the back-end knowledge spine for the firm's three offerings: **Brèche** (free AI risk diagnostic), **Brèche Pro** (RADAR governance assessment), and **Prisme** (ISO/IEC 42001 internal audit).

The 13 modules cover all major AI governance frameworks relevant to Canadian and international practice, with a deliberate French/English split that follows the native language of each framework's source material.

| Module | Title | Lang | Concepts |
|---:|---|:---:|:---:|
| 1 | Fondations de la gouvernance d'IA | 🇫🇷 | 5 |
| 2 | Loi 25 et la CAI | 🇫🇷 | 7 |
| 3 | Cadre fédéral canadien et provinces | 🇫🇷 | 6 |
| 4 | EU AI Act | 🇬🇧 | 6 |
| 5 | NIST AI Risk Management Framework | 🇬🇧 | 5 |
| 6 | ISO/IEC 42001 — système de management de l'IA | 🇫🇷 | 3 |
| 7 | CNIL — guide opérationnel | 🇫🇷 | 7 |
| 8 | Singapore Model AI Governance Framework | 🇬🇧 | 4 |
| 9 | UK ICO and Data (Use & Access) Act 2025 | 🇬🇧 | 3 |
| 10 | Mise en œuvre pratique | 🇫🇷 | 4 |
| 11 | Agentic AI Governance | 🇬🇧 | 4 |
| 12 | AI Governance Profession (IAPP AIGP) | 🇬🇧 | 3 |
| 13 | Synthèse stratégique pour PME québécoise | 🇫🇷 | 2 |
| 99 | Documents ingérés (dynamique) | — | — |

**Total: 59 concepts. Distribution: 34 FR / 25 EN.**

The content covers Loi 25 (Quebec), CAI guidance including the principles on generative AI, the Canadian federal landscape (Directive on ADM, voluntary code, ISED National Sprint, provincial fragmentation, Zhang case), the EU AI Act including the 2026 GPAI Code of Practice and Omnibus trilogue status, NIST AI RMF including the GenAI profile and 2026 Critical Infrastructure / Agent Standards extensions, ISO/IEC 42001 with its 38 controls, CNIL's seven-stage operational guide, the Singapore Model Framework including the January 2026 agentic AI extension and AI Verify, the UK ICO and DUAA 2025, agentic AI governance with Microsoft tooling, the IAPP AIGP Body of Knowledge, and a synthesis for Quebec SMEs.

---

## Architecture

```
Scientia/
├── streamlit_app.py        # Web app (mobile + desktop)
├── curriculum.py           # 13 modules, 59 concepts
├── generator.py            # Question generation + lenient evaluator (Claude)
├── ingestion.py            # PDF/MD/TXT → dynamic concepts (module 99)
├── db.py                   # SQLite + FSRS-4.5 spaced repetition
├── requirements.txt
├── .streamlit/
│   ├── config.toml
│   └── secrets.toml.example
├── docs/                   # Drop PDFs here for ingestion (gitignored)
└── scientia.db             # Local SQLite (gitignored)
```

---

## Quick start

### 1. Install

```bash
git clone https://github.com/DA-Leclerc/Scientia.git
cd Scientia
pip install -r requirements.txt
```

### 2. Set the API key

Get a key from https://console.anthropic.com/keys

**Local `.env`** (recommended):
```
ANTHROPIC_API_KEY=sk-ant-...
```

**Or shell variable**:
```bash
# Windows PowerShell
$env:ANTHROPIC_API_KEY = "sk-ant-..."

# macOS/Linux
export ANTHROPIC_API_KEY="sk-ant-..."
```

**Or `.streamlit/secrets.toml`** (for Streamlit Cloud):
```toml
ANTHROPIC_API_KEY = "sk-ant-..."
```

### 3. Run

```bash
streamlit run streamlit_app.py
```

Opens at http://localhost:8501

---

## Mobile usage

### Streamlit Community Cloud (free, recommended)

1. Push your fork to GitHub.
2. Go to https://share.streamlit.io/ and connect your GitHub.
3. Select the repo and `streamlit_app.py` as entry point.
4. In **Settings → Secrets**:
   ```toml
   ANTHROPIC_API_KEY = "sk-ant-..."
   ```
5. Deploy. You get a `https://...streamlit.app` URL.
6. On mobile (Safari/Chrome), add to home screen.

### Local network

```bash
streamlit run streamlit_app.py --server.address=0.0.0.0 --server.port=8501
```

Open `http://<computer-IP>:8501` on the mobile device on the same Wi-Fi.

### Production (Railway, Render, Fly.io)

Set environment variables:
- `ANTHROPIC_API_KEY=sk-ant-...`
- `DATA_DIR=/data` (and mount a volume on `/data` to persist `scientia.db`)

Start command:
```
streamlit run streamlit_app.py --server.port=$PORT --server.address=0.0.0.0
```

---

## Ingesting your own documents

Drop a PDF, Markdown, or TXT file into `docs/`, then in the app:

1. Open **Ingest a document**.
2. Select the file — Claude extracts 1-5 atomic concepts.
3. Concepts land in **Module 99 (Documents ingérés)** and become quiz-ready.

Sources to ingest in priority order: CAI decisions and guidance documents, EU AI Office publications, ICO guidance, CNIL lifecycle guides, NIST profiles, ISO standards (excerpts), and case law (e.g., the BC Zhang decision).

---

## FSRS-4.5 spaced repetition

Scientia schedules reviews with [FSRS-4.5](https://github.com/open-spaced-repetition/fsrs4anki/wiki/The-Algorithm) (Free Spaced Repetition Scheduler), trained on millions of Anki/SuperMemo reviews. Each card carries a `stability` (days before retention drops to 90%) and a `difficulty` (1-10). Next review date targets 90% retention.

The evaluator (in `generator.py`) is calibrated for **substance over form**: it rewards correct understanding even when the formulation differs from the reference answer. Penalizes only factual errors (wrong article cited, wrong threshold, wrong jurisdiction), missing core ideas, and concept confusion.

---

## License

Private — Dominic-André Leclerc / Nord Paradigm.
