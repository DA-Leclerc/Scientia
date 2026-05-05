# Scientia — Démarrage rapide

**Apprentissage espacé pour la pratique de gouvernance d'IA chez Nord Paradigm.**

13 modules, 59 concepts, alternant français et anglais selon la langue native du cadre étudié.

## Installation (une fois)

```bash
pip install -r requirements.txt
```

## Configuration de la clé API

Va sur https://console.anthropic.com/keys récupérer ta clé.

**Option recommandée — fichier `.env`** :
```
ANTHROPIC_API_KEY=sk-ant-...
```

**Ou via PowerShell** :
```powershell
$env:ANTHROPIC_API_KEY = "sk-ant-..."
```

## Lancer

```bash
streamlit run streamlit_app.py
```

L'app s'ouvre sur http://localhost:8501

## Les 13 modules

| # | Titre | Lang |
|---:|---|:---:|
| 1 | Fondations de la gouvernance d'IA | 🇫🇷 |
| 2 | Loi 25 et la CAI | 🇫🇷 |
| 3 | Cadre fédéral canadien et provinces | 🇫🇷 |
| 4 | EU AI Act | 🇬🇧 |
| 5 | NIST AI Risk Management Framework | 🇬🇧 |
| 6 | ISO/IEC 42001 | 🇫🇷 |
| 7 | CNIL — guide opérationnel | 🇫🇷 |
| 8 | Singapore Model AI Governance Framework | 🇬🇧 |
| 9 | UK ICO et Data (Use & Access) Act 2025 | 🇬🇧 |
| 10 | Mise en œuvre pratique | 🇫🇷 |
| 11 | Agentic AI Governance | 🇬🇧 |
| 12 | AI Governance Profession (AIGP) | 🇬🇧 |
| 13 | Synthèse stratégique PME québécoise | 🇫🇷 |
| 99 | Documents ingérés (dynamique) | — |

## Comment utiliser

1. Choisis un concept dans un module.
2. Claude génère 5 questions adaptées (intuition, application, contre-exemple, connexion, erreur fréquente).
3. Tu réponds en texte libre. Le texte source reste visible (open-book).
4. Claude évalue avec une grille indulgente sur la forme, exigeante sur le fond.
5. Tes scores sont sauvegardés. FSRS-4.5 planifie tes prochaines révisions pour cibler 90 % de rétention.

## Ingérer un document

Glisse un PDF, Markdown ou TXT dans `docs/`. Dans l'app, choisis « Ingérer un document » : Claude extrait 1-5 concepts. Ils apparaissent dans le module 99.

## Tuteur socratique

Bouton « Discuter avec Claude » sous chaque question : aide à décortiquer la question sans révéler la réponse, ou à explorer le concept en dialogue.
