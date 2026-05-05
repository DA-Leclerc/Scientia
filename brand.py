"""
Nord Paradigm — système de design pour Scientia.

Centralise :
  - palette de couleurs
  - polices Google (Sora + DM Sans)
  - bloc CSS global injecté dans Streamlit
  - helpers HTML pour les composants brandés (hero, cartes, badges)

Source : brand-theme-kit.jsx du site Nord Paradigm.
"""
from __future__ import annotations


COLORS = {
    # Backgrounds — du plus profond au plus élevé
    "abyss":    "#0a0f1e",
    "deep":     "#0d1a2d",
    "navy":     "#112240",
    "slate":    "#1a3050",
    "steel":    "#2a4a6b",
    # Texte
    "mist":     "#8ba3be",
    "cloud":    "#c4d5e8",
    "white":    "#eaf2f8",
    # Accents
    "gold":     "#d4a853",
    "amber":    "#f0c060",
    "honey":    "#ffd98040",
    "teal":     "#1abc9c",
    "cyan":     "#00bcd4",
    "mint":     "#2dd4a830",
    "electric": "#4fc3f7",
}

GRADIENTS = {
    "hero":      f"linear-gradient(135deg, {COLORS['abyss']} 0%, {COLORS['deep']} 40%, {COLORS['navy']} 100%)",
    "cta":       f"linear-gradient(135deg, {COLORS['gold']}, {COLORS['amber']})",
    "accent":    f"linear-gradient(180deg, {COLORS['gold']}, {COLORS['teal']})",
    "card":      f"linear-gradient(160deg, {COLORS['navy']}cc, {COLORS['deep']}cc)",
    "header":    f"linear-gradient(135deg, {COLORS['abyss']}, {COLORS['navy']})",
}


def global_css() -> str:
    """
    Bloc CSS global injecté en début d'app via st.markdown(unsafe_allow_html=True).

    Imports : Sora (display) + DM Sans (body) depuis Google Fonts.
    Override : tous les composants Streamlit pour respecter la palette
    Nord Paradigm.
    """
    c = COLORS
    return f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700&family=DM+Sans:wght@300;400;500;700&display=swap');

/* ── Document & corps ──────────────────────────────────────── */
html, body, [class*="css"], .stApp {{
    font-family: 'DM Sans', sans-serif !important;
    background: {c['abyss']} !important;
    color: {c['white']};
}}

.stApp {{
    background: linear-gradient(180deg, {c['abyss']} 0%, {c['deep']} 100%);
}}

/* ── Headings ──────────────────────────────────────────────── */
h1, h2, h3, h4, h5, h6,
.stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {{
    font-family: 'Sora', sans-serif !important;
    color: {c['white']} !important;
    letter-spacing: -0.025em !important;
    font-weight: 700 !important;
}}
h1 {{ letter-spacing: -0.03em !important; }}
h4, h5, h6 {{ font-weight: 600 !important; }}

/* ── Paragraphes & captions ────────────────────────────────── */
p, .stMarkdown p, .stMarkdown li, .stCaption, [data-testid="stCaptionContainer"] {{
    font-family: 'DM Sans', sans-serif !important;
    color: {c['cloud']} !important;
    line-height: 1.65 !important;
}}
small, .stCaption, [data-testid="stCaptionContainer"] {{
    color: {c['mist']} !important;
}}

/* ── Sidebar ───────────────────────────────────────────────── */
[data-testid="stSidebar"] {{
    background: {c['deep']} !important;
    border-right: 1px solid {c['steel']}30;
}}
[data-testid="stSidebar"] * {{ color: {c['cloud']} !important; }}
[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {{
    color: {c['white']} !important;
}}

/* ── Boutons (primary = gold, secondary = ghost) ──────────── */
.stButton button {{
    font-family: 'Sora', sans-serif !important;
    font-weight: 500 !important;
    border-radius: 10px !important;
    border: 1px solid {c['steel']} !important;
    background: transparent !important;
    color: {c['cloud']} !important;
    transition: all 0.2s ease !important;
    letter-spacing: -0.01em !important;
}}
.stButton button:hover {{
    border-color: {c['gold']}80 !important;
    color: {c['white']} !important;
    transform: translateY(-1px);
}}

/* Primary button — gold gradient with FORCED dark text on children */
.stButton button[kind="primary"],
.stButton button[data-testid="baseButton-primary"],
button[kind="primary"],
[data-testid="stBaseButton-primary"] {{
    background: linear-gradient(135deg, {c['gold']}, {c['amber']}) !important;
    color: {c['abyss']} !important;
    border: none !important;
    font-weight: 600 !important;
    box-shadow: 0 4px 20px {c['gold']}30 !important;
}}
/* Override the global `p { color: cloud }` rule for every descendant
   of a primary button — including <p>, <div>, <span>, icon SVGs. */
.stButton button[kind="primary"] *,
.stButton button[data-testid="baseButton-primary"] *,
button[kind="primary"] *,
[data-testid="stBaseButton-primary"] *,
.stButton button[kind="primary"] p,
.stButton button[kind="primary"] div,
.stButton button[kind="primary"] span {{
    color: {c['abyss']} !important;
    fill: {c['abyss']} !important;
}}
.stButton button[kind="primary"]:hover,
.stButton button[data-testid="baseButton-primary"]:hover {{
    box-shadow: 0 6px 28px {c['gold']}50 !important;
    transform: translateY(-2px);
}}
/* Download button (st.download_button) — same gold treatment */
.stDownloadButton button {{
    background: linear-gradient(135deg, {c['gold']}, {c['amber']}) !important;
    color: {c['abyss']} !important;
    border: none !important;
    font-weight: 600 !important;
    box-shadow: 0 4px 20px {c['gold']}30 !important;
}}
.stDownloadButton button * {{
    color: {c['abyss']} !important;
    fill: {c['abyss']} !important;
}}

/* ── Métriques ─────────────────────────────────────────────── */
[data-testid="stMetric"] {{
    background: {c['navy']}80;
    border: 1px solid {c['steel']}30;
    border-radius: 12px;
    padding: 16px;
    backdrop-filter: blur(8px);
}}
[data-testid="stMetricLabel"] {{
    color: {c['mist']} !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 12px !important;
    text-transform: uppercase;
    letter-spacing: 0.04em;
}}
[data-testid="stMetricValue"] {{
    color: {c['gold']} !important;
    font-family: 'Sora', sans-serif !important;
    font-weight: 700 !important;
    letter-spacing: -0.02em;
}}

/* ── Container avec border ────────────────────────────────── */
[data-testid="stVerticalBlockBorderWrapper"] > div {{
    border-radius: 14px !important;
}}
div[data-testid="stVerticalBlock"] > div[style*="border"] {{
    border: 1px solid {c['steel']}40 !important;
    background: {c['navy']}66 !important;
    backdrop-filter: blur(8px);
    border-radius: 14px !important;
}}

/* ── Inputs ───────────────────────────────────────────────── */
.stTextArea textarea, .stTextInput input, .stSelectbox > div > div,
.stRadio > div, .stSlider > div {{
    background: {c['deep']} !important;
    color: {c['white']} !important;
    border: 1px solid {c['steel']}50 !important;
    border-radius: 10px !important;
    font-family: 'DM Sans', sans-serif !important;
}}
.stTextArea textarea:focus, .stTextInput input:focus {{
    border-color: {c['gold']} !important;
    box-shadow: 0 0 0 1px {c['gold']}40 !important;
}}

/* ── Selectbox dropdown ───────────────────────────────────── */
[data-baseweb="select"] > div {{
    background: {c['deep']} !important;
    border: 1px solid {c['steel']}50 !important;
}}
[data-baseweb="popover"] {{
    background: {c['navy']} !important;
    border: 1px solid {c['steel']} !important;
}}
[data-baseweb="popover"] li {{
    color: {c['cloud']} !important;
    font-family: 'DM Sans', sans-serif !important;
}}
[data-baseweb="popover"] li:hover {{
    background: {c['slate']} !important;
}}

/* ── Progress bars ────────────────────────────────────────── */
.stProgress > div > div > div > div {{
    background: linear-gradient(90deg, {c['gold']}, {c['teal']}) !important;
}}
.stProgress > div > div > div {{
    background: {c['steel']}30 !important;
}}

/* ── Expander ─────────────────────────────────────────────── */
.streamlit-expanderHeader, [data-testid="stExpander"] summary {{
    background: {c['navy']}80 !important;
    border: 1px solid {c['steel']}30 !important;
    border-radius: 10px !important;
    color: {c['cloud']} !important;
    font-family: 'Sora', sans-serif !important;
    font-weight: 500 !important;
}}
.streamlit-expanderContent, [data-testid="stExpander"] [data-testid="stExpanderDetails"] {{
    background: {c['deep']} !important;
    border: 1px solid {c['steel']}30 !important;
    border-top: none !important;
    border-radius: 0 0 10px 10px !important;
}}

/* ── Alertes (info / success / warning / error) ───────────── */
[data-testid="stAlert"] {{
    border-radius: 12px !important;
    backdrop-filter: blur(8px);
    border: 1px solid;
}}
.stAlert[data-baseweb="notification"][data-kind="info"],
[data-testid="stAlert"][kind="info"] {{
    background: {c['cyan']}15 !important;
    border-color: {c['cyan']}40 !important;
    color: {c['cloud']} !important;
}}
[data-testid="stAlert"][kind="success"] {{
    background: {c['teal']}15 !important;
    border-color: {c['teal']}40 !important;
    color: {c['white']} !important;
}}
[data-testid="stAlert"][kind="warning"] {{
    background: {c['amber']} !important;
    border-color: {c['gold']} !important;
    color: {c['abyss']} !important;
}}
[data-testid="stAlert"][kind="warning"] *,
[data-testid="stAlert"][kind="warning"] p,
[data-testid="stAlert"][kind="warning"] div,
[data-testid="stAlert"][kind="warning"] span,
[data-testid="stAlert"][kind="warning"] svg {{
    color: {c['abyss']} !important;
    fill: {c['abyss']} !important;
}}
[data-testid="stAlert"][kind="error"] {{
    background: #f4433615 !important;
    border-color: #f4433640 !important;
    color: {c['cloud']} !important;
}}

/* ── Chat bubbles ─────────────────────────────────────────── */
[data-testid="stChatMessage"] {{
    background: {c['navy']}66 !important;
    border: 1px solid {c['steel']}30 !important;
    border-radius: 12px !important;
}}
[data-testid="stChatInput"] textarea {{
    background: {c['deep']} !important;
    color: {c['white']} !important;
    border: 1px solid {c['steel']}50 !important;
}}

/* ── Tabs ─────────────────────────────────────────────────── */
.stTabs [data-baseweb="tab-list"] {{
    background: transparent !important;
    border-bottom: 1px solid {c['steel']}30 !important;
}}
.stTabs [data-baseweb="tab"] {{
    color: {c['mist']} !important;
    font-family: 'Sora', sans-serif !important;
}}
.stTabs [aria-selected="true"] {{
    color: {c['gold']} !important;
    border-bottom-color: {c['gold']} !important;
}}

/* ── File uploader ────────────────────────────────────────── */
[data-testid="stFileUploaderDropzone"] {{
    background: {c['deep']} !important;
    border: 2px dashed {c['steel']} !important;
    border-radius: 12px !important;
    color: {c['cloud']} !important;
}}

/* ── Code & inline code ───────────────────────────────────── */
code, pre {{
    font-family: 'JetBrains Mono', 'Fira Code', monospace !important;
    background: {c['deep']} !important;
    color: {c['amber']} !important;
    border-radius: 6px !important;
    padding: 2px 6px !important;
    font-size: 0.9em !important;
}}

/* ── Scrollbar ────────────────────────────────────────────── */
::-webkit-scrollbar {{ width: 8px; height: 8px; }}
::-webkit-scrollbar-track {{ background: {c['abyss']}; }}
::-webkit-scrollbar-thumb {{ background: {c['steel']}; border-radius: 4px; }}
::-webkit-scrollbar-thumb:hover {{ background: {c['gold']}; }}

/* ── Cacher le « Made with Streamlit » et le menu hamburger
       en mode déploiement ───────────────────────────────────── */
#MainMenu {{ visibility: hidden; }}
footer {{ visibility: hidden; }}
header[data-testid="stHeader"] {{
    background: {c['abyss']} !important;
    border-bottom: 1px solid {c['steel']}30;
}}

/* ── Composants brandés (préfixe .np-) ────────────────────── */

.np-hero {{
    position: relative;
    border-radius: 16px;
    overflow: hidden;
    background: {GRADIENTS['hero']};
    padding: 48px 40px;
    margin-bottom: 24px;
    border: 1px solid {c['steel']}30;
}}
.np-hero::before {{
    content: '';
    position: absolute; inset: 0; opacity: 0.04;
    background-image:
      linear-gradient({c['cyan']} 1px, transparent 1px),
      linear-gradient(90deg, {c['cyan']} 1px, transparent 1px);
    background-size: 60px 60px;
    pointer-events: none;
}}
.np-hero::after {{
    content: '';
    position: absolute; top: -80px; right: -80px;
    width: 300px; height: 300px; border-radius: 50%;
    background: radial-gradient(circle, {c['teal']}15, transparent 70%);
    pointer-events: none;
}}
.np-hero-inner {{ position: relative; z-index: 1; max-width: 640px; }}
.np-hero-tag {{
    display: inline-flex; align-items: center; gap: 8px;
    padding: 6px 16px; border-radius: 100px;
    border: 1px solid {c['gold']}40; background: {c['gold']}08;
    margin-bottom: 20px;
}}
.np-hero-tag-dot {{
    width: 6px; height: 6px; border-radius: 50%;
    background: {c['gold']}; box-shadow: 0 0 8px {c['gold']};
}}
.np-hero-tag-text {{
    font-family: 'DM Sans', sans-serif;
    font-size: 12px; color: {c['gold']};
    font-weight: 500; letter-spacing: 0.04em;
    text-transform: uppercase;
}}
.np-hero h1 {{
    font-family: 'Sora', sans-serif;
    font-size: 38px; font-weight: 700;
    color: {c['white']}; line-height: 1.15;
    margin: 0 0 16px; letter-spacing: -0.03em;
}}
.np-hero h1 .accent {{
    background: linear-gradient(90deg, {c['gold']}, {c['amber']});
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}}
.np-hero p {{
    font-family: 'DM Sans', sans-serif;
    font-size: 16px; color: {c['mist']};
    line-height: 1.7; margin: 0; max-width: 520px;
}}

/* Logo mark — petit losange or/sarcelle */
.np-logo-mark {{
    width: 32px; height: 32px; border-radius: 8px;
    background: linear-gradient(135deg, {c['gold']}, {c['teal']});
    display: inline-flex; align-items: center; justify-content: center;
}}

/* Carte brandée générique */
.np-card {{
    border-radius: 14px; padding: 24px;
    background: {c['navy']}99;
    border: 1px solid {c['steel']}40;
    backdrop-filter: blur(8px);
    margin-bottom: 16px;
}}
.np-card-title {{
    font-family: 'Sora', sans-serif;
    font-size: 16px; font-weight: 600;
    color: {c['white']};
    margin: 0 0 6px;
    letter-spacing: -0.01em;
}}
.np-card-meta {{
    font-family: 'DM Sans', sans-serif;
    font-size: 13px; color: {c['mist']};
    margin: 0;
}}

/* Bandeau de reprise — sombre + accent or */
.np-resume {{
    border-radius: 14px;
    padding: 22px 26px;
    background: linear-gradient(135deg, {c['navy']}, {c['slate']});
    border: 1px solid {c['gold']}40;
    box-shadow: 0 4px 24px {c['gold']}10;
    margin-bottom: 20px;
}}
.np-resume-label {{
    font-family: 'DM Sans', sans-serif;
    font-size: 11px; font-weight: 500;
    color: {c['gold']};
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 8px;
}}
.np-resume-title {{
    font-family: 'Sora', sans-serif;
    font-size: 18px; font-weight: 600;
    color: {c['white']};
    margin: 0 0 6px;
    letter-spacing: -0.015em;
}}
.np-resume-meta {{
    font-family: 'DM Sans', sans-serif;
    font-size: 13px; color: {c['cloud']};
    margin: 0;
}}

/* Reco card */
.np-reco {{
    border-radius: 14px; padding: 22px 26px;
    background: linear-gradient(135deg, {c['deep']}, {c['navy']});
    border: 1px solid {c['teal']}40;
    box-shadow: 0 4px 24px {c['teal']}10;
    margin-bottom: 20px;
}}
.np-reco-label {{
    font-family: 'DM Sans', sans-serif;
    font-size: 11px; font-weight: 500;
    color: {c['teal']};
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 8px;
}}
.np-reco-title {{
    font-family: 'Sora', sans-serif;
    font-size: 18px; font-weight: 600;
    color: {c['white']};
    margin: 0 0 6px;
    letter-spacing: -0.015em;
}}
.np-reco-meta {{
    font-family: 'DM Sans', sans-serif;
    font-size: 13px; color: {c['mist']};
    margin: 0;
}}

/* Footer */
.np-footer {{
    margin-top: 48px;
    padding: 24px;
    border-top: 1px solid {c['steel']}20;
    text-align: center;
    font-family: 'DM Sans', sans-serif;
    font-size: 12px;
    color: {c['mist']}80;
}}
.np-footer-brand {{
    color: {c['gold']};
    font-weight: 600;
    font-family: 'Sora', sans-serif;
    letter-spacing: -0.01em;
}}

/* Sidebar brand block */
.np-sidebar-brand {{
    display: flex; align-items: center; gap: 12px;
    padding: 8px 0 16px;
    border-bottom: 1px solid {c['steel']}30;
    margin-bottom: 16px;
}}
.np-sidebar-brand-text {{
    font-family: 'Sora', sans-serif;
    font-size: 17px; font-weight: 700;
    color: {c['white']}; letter-spacing: -0.02em;
}}
.np-sidebar-brand-sub {{
    font-family: 'DM Sans', sans-serif;
    font-size: 11px; color: {c['gold']};
    text-transform: uppercase; letter-spacing: 0.06em;
    margin-top: -2px;
}}
</style>
"""


def hero_html(title_main: str, title_accent: str, subtitle: str,
              tag_text: str = "Nord Paradigm | AI Governance Training") -> str:
    """Bloc hero brandé pour l'accueil."""
    return f"""
<div class="np-hero">
  <div class="np-hero-inner">
    <div class="np-hero-tag">
      <span class="np-hero-tag-dot"></span>
      <span class="np-hero-tag-text">{tag_text}</span>
    </div>
    <h1>{title_main}<br/><span class="accent">{title_accent}</span></h1>
    <p>{subtitle}</p>
  </div>
</div>
"""


def resume_card_html(label: str, title: str, meta: str) -> str:
    """Bandeau de reprise."""
    return f"""
<div class="np-resume">
  <div class="np-resume-label">{label}</div>
  <div class="np-resume-title">{title}</div>
  <div class="np-resume-meta">{meta}</div>
</div>
"""


def reco_card_html(label: str, title: str, meta: str) -> str:
    """Carte de recommandation."""
    return f"""
<div class="np-reco">
  <div class="np-reco-label">{label}</div>
  <div class="np-reco-title">{title}</div>
  <div class="np-reco-meta">{meta}</div>
</div>
"""


def sidebar_brand_html() -> str:
    """Bloc de marque en haut de la sidebar."""
    g = COLORS
    return f"""
<div class="np-sidebar-brand">
  <div class="np-logo-mark">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none"
         stroke="{g['abyss']}" stroke-width="2.5"
         stroke-linecap="round" stroke-linejoin="round">
      <path d="M12 2L2 7l10 5 10-5-10-5z"/>
      <path d="M2 17l10 5 10-5"/>
      <path d="M2 12l10 5 10-5"/>
    </svg>
  </div>
  <div>
    <div class="np-sidebar-brand-text">Scientia</div>
    <div class="np-sidebar-brand-sub">Nord Paradigm</div>
  </div>
</div>
"""


def footer_html() -> str:
    return """
<div class="np-footer">
  <span class="np-footer-brand">Nord Paradigm · Scientia</span><br/>
  Apprentissage espacé FSRS-4.5 · Évaluation Claude · v0.4
  <br/><span style="opacity: 0.7;">© 2026 Dominic-André Leclerc — Military-grade discipline. AI governance that works.</span>
</div>
"""
