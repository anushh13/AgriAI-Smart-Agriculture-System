import streamlit as st
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AgriAI", page_icon="🌱", layout="wide")

# ---------------- PATHS ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))   # app folder
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

logo_path = os.path.join(ASSETS_DIR, "logo.png")
hero_img = os.path.join(ASSETS_DIR, "hero_main.png")
overview_img = os.path.join(ASSETS_DIR, "system_overview.png")

# ---------------- CSS ----------------
st.markdown("""
<style>
.stApp {
    background:
        radial-gradient(circle at top left, rgba(116,245,159,0.10), transparent 24%),
        radial-gradient(circle at top right, rgba(78,225,184,0.10), transparent 22%),
        linear-gradient(135deg, #06121c 0%, #0b2232 100%);
    color: white;
}

.block-container {
    max-width: 1420px;
    padding-top: 2.3rem;
    padding-bottom: 0rem !important;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #091520 0%, #102739 100%);
    border-right: 1px solid rgba(255,255,255,0.08);
}

footer {
    visibility: hidden;
}

html, body {
    overflow-x: hidden;
}

@keyframes fadeUp {
    from {
        opacity: 0;
        transform: translateY(18px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes floatSlow {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-8px); }
    100% { transform: translateY(0px); }
}

.hero-shell {
    margin-bottom: 1.4rem;
    animation: fadeUp 0.7s ease-out;
}

.hero-card {
    padding: 34px;
    border-radius: 28px;
    background: linear-gradient(135deg, rgba(255,255,255,0.07), rgba(255,255,255,0.03));
    border: 1px solid rgba(255,255,255,0.10);
    box-shadow: 0 18px 40px rgba(0,0,0,0.28);
    backdrop-filter: blur(10px);
    min-height: 100%;
}

.hero-badge {
    display: inline-block;
    padding: 9px 16px;
    border-radius: 999px;
    background: rgba(116,245,159,0.14);
    border: 1px solid rgba(116,245,159,0.18);
    color: #bff8d1;
    font-size: 0.92rem;
    font-weight: 700;
    margin-bottom: 1rem;
}

.hero-title {
    font-size: 3.5rem;
    line-height: 1.05;
    font-weight: 800;
    color: #8ef7b8;
    margin-bottom: 0.5rem;
}

.hero-subtitle {
    font-size: 1.15rem;
    font-weight: 600;
    color: #d9f7e7;
    margin-bottom: 1rem;
}

.hero-text {
    color: #dce7ef;
    font-size: 1rem;
    line-height: 1.8;
}

.image-card {
    padding: 10px;
    border-radius: 28px;
    background: linear-gradient(135deg, rgba(255,255,255,0.06), rgba(255,255,255,0.03));
    border: 1px solid rgba(255,255,255,0.10);
    box-shadow: 0 18px 40px rgba(0,0,0,0.26);
    backdrop-filter: blur(8px);
    animation: floatSlow 4.8s ease-in-out infinite;
}

.section-card {
    padding: 26px;
    border-radius: 24px;
    background: linear-gradient(135deg, rgba(255,255,255,0.06), rgba(255,255,255,0.03));
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 12px 28px rgba(0,0,0,0.20);
    margin-bottom: 1.4rem;
    backdrop-filter: blur(8px);
    animation: fadeUp 0.8s ease-out;
}

.feature-card {
    padding: 24px;
    border-radius: 22px;
    background: linear-gradient(135deg, rgba(255,255,255,0.06), rgba(255,255,255,0.03));
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 10px 24px rgba(0,0,0,0.18);
    min-height: 100%;
    transition: transform 0.25s ease, box-shadow 0.25s ease;
}

.feature-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 16px 32px rgba(0,0,0,0.22);
}

.metric-card {
    padding: 22px 18px;
    border-radius: 22px;
    background: linear-gradient(135deg, rgba(255,255,255,0.07), rgba(255,255,255,0.03));
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 10px 24px rgba(0,0,0,0.18);
    text-align: center;
    min-height: 100%;
}

.metric-label {
    color: #cde5da;
    font-size: 0.95rem;
    margin-bottom: 0.45rem;
    font-weight: 600;
}

.metric-value {
    color: #8ef7b8;
    font-size: 1.7rem;
    font-weight: 800;
    line-height: 1.1;
}

.metric-sub {
    color: #d7e5ec;
    font-size: 0.85rem;
    margin-top: 0.3rem;
}

.section-title {
    font-size: 1.7rem;
    font-weight: 760;
    margin-bottom: 0.9rem;
    color: #ffffff;
}

.soft-text {
    color: #dbe8ef;
    line-height: 1.8;
    font-size: 0.98rem;
}

.team-card {
    padding: 22px;
    border-radius: 22px;
    background: linear-gradient(135deg, rgba(255,255,255,0.06), rgba(255,255,255,0.03));
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 10px 24px rgba(0,0,0,0.18);
    text-align: center;
    min-height: 100%;
}

.team-name {
    color: #8ef7b8;
    font-size: 1.2rem;
    font-weight: 700;
    margin-bottom: 0.25rem;
}

.team-role {
    color: #d9f7e7;
    font-size: 0.95rem;
    margin-bottom: 0.5rem;
}

.side-title {
    color: white;
    font-size: 1.15rem;
    font-weight: 700;
    margin-top: 0.5rem;
}

.side-text {
    color: #d2e6ef;
    font-size: 0.94rem;
    line-height: 1.7;
}

img {
    border-radius: 20px;
}

div.stButton > button {
    width: 100%;
    border: none;
    border-radius: 16px;
    padding: 0.95rem 1rem;
    font-weight: 800;
    font-size: 1rem;
    background: linear-gradient(90deg, #74f59f, #4ee1b8);
    color: #041923;
    box-shadow: 0 10px 20px rgba(78,225,184,0.18);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

div.stButton > button:hover {
    background: linear-gradient(90deg, #8ef7b8, #66f0c8);
    color: #041923;
    transform: translateY(-2px);
    box-shadow: 0 14px 24px rgba(78,225,184,0.22);
}
</style>
""", unsafe_allow_html=True)

# ---------------- TOP LEFT LOGO ABOVE PAGE NAV ----------------
if os.path.exists(logo_path):
    st.logo(logo_path, size="large")

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("##  AgriAI")
    st.caption("AI-Powered Precision Farming")
    st.markdown("---")

    st.markdown('<div class="side-title">About</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="side-text">
    AgriAI is an intelligent agriculture platform that combines machine learning and deep learning
    to support crop recommendation and plant disease detection.
    </div>
    """, unsafe_allow_html=True)

# ---------------- HERO SECTION ----------------
st.markdown('<div class="hero-shell">', unsafe_allow_html=True)
left, right = st.columns([1.18, 1], gap="large")

with left:
    st.markdown('<div class="hero-card">', unsafe_allow_html=True)
    st.markdown('<div class="hero-badge"> Smart agriculture powered by AI</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-title">AgriAI</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">Precision farming for smarter crop and disease decisions</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="hero-text">
    AgriAI is a multi-module smart farming platform that helps users make better agricultural decisions.
    It combines crop recommendation based on soil and climate parameters with plant disease detection from
    leaf images, supported by visual analytics, prediction confidence, and downloadable reports.
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    b1, b2 = st.columns(2)
    with b1:
        if st.button("🌾 Open Crop Recommendation"):
            st.switch_page("pages/1_Crop_Recommendation.py")
    with b2:
        if st.button("🌿 Open Disease Detection"):
            st.switch_page("pages/2_Disease_Detection.py")

    st.markdown('</div>', unsafe_allow_html=True)

with right:
    if os.path.exists(hero_img):
        st.markdown('<div class="image-card">', unsafe_allow_html=True)
        st.image(hero_img, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("hero_main.png not found in app/assets")
st.markdown('</div>', unsafe_allow_html=True)

# ---------------- MODULES + TECHNOLOGY STACK BELOW HERO IMAGE ----------------
mod_col, tech_col = st.columns(2, gap="large")

with mod_col:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Modules</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="soft-text">
    <b>Crop Recommendation</b><br>
    Predicts the most suitable crop based on soil nutrients and environmental parameters.
    <br><br>
    <b>Disease Detection</b><br>
    Detects plant diseases from uploaded leaf images using deep learning.
    <br><br>
    <b>Reports & Insights</b><br>
    Provides confidence scores, analytics, charts, and downloadable reports.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with tech_col:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Technology Stack</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="soft-text">
    • <b>Scikit-learn</b> for crop recommendation models<br>
    • <b>TensorFlow / Keras</b> for disease detection models<br>
    • <b>Streamlit</b> for interactive web interface<br>
    • <b>Python</b> for end-to-end implementation<br>
    • <b>Pandas / NumPy</b> for preprocessing and data handling
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- LIVE AI INSIGHTS ----------------
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title"> Live AI Insights</div>', unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label"> Recommended Crop</div>
        <div class="metric-value">Rice</div>
        <div class="metric-sub">Based on latest inputs</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Confidence</div>
        <div class="metric-value">92%</div>
        <div class="metric-sub">Prediction accuracy</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Disease Detection</div>
        <div class="metric-value">Healthy</div>
        <div class="metric-sub">Latest scan result</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">System Status</div>
        <div class="metric-value">Active</div>
        <div class="metric-sub">All models running</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- HIGHLIGHTS / METRICS ----------------
m1, m2, m3 = st.columns(3)
with m1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Crop Module Accuracy</div>
        <div class="metric-value">99.5%</div>
        <div class="metric-sub">Random Forest based recommendation</div>
    </div>
    """, unsafe_allow_html=True)
with m2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Disease Module Accuracy</div>
        <div class="metric-value">89.5%</div>
        <div class="metric-sub">Deep learning validation accuracy</div>
    </div>
    """, unsafe_allow_html=True)
with m3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Core AI Modules</div>
        <div class="metric-value">2</div>
        <div class="metric-sub">Integrated in one platform</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ---------------- FEATURES SECTION ----------------
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Platform Features</div>', unsafe_allow_html=True)

f1, f2, f3 = st.columns(3)
with f1:
    st.markdown("""
    <div class="feature-card">
        <h3> Crop Recommendation</h3>
        <p class="soft-text">
        Predict the most suitable crop using nitrogen, phosphorus, potassium, temperature,
        humidity, pH, and rainfall.
        </p>
    </div>
    """, unsafe_allow_html=True)

with f2:
    st.markdown("""
    <div class="feature-card">
        <h3> Disease Detection</h3>
        <p class="soft-text">
        Detect disease classes from plant leaf images using a trained deep learning model
        and get confidence-based results.
        </p>
    </div>
    """, unsafe_allow_html=True)

with f3:
    st.markdown("""
    <div class="feature-card">
        <h3>Smart Analytics</h3>
        <p class="soft-text">
        View charts, top predictions, downloadable reports, and prediction history
        in a clean decision-support dashboard.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- ABOUT SECTION ----------------
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">About AgriAI</div>', unsafe_allow_html=True)
st.markdown("""
<div class="soft-text">
AgriAI was designed as a smart agriculture support system to improve farming decisions through artificial intelligence.
The platform combines two practical modules:
<br><br>
<b>1. Crop Recommendation:</b> Recommends the most suitable crop based on soil nutrients and environmental conditions.
<br>
<b>2. Plant Disease Detection:</b> Detects disease conditions from uploaded leaf images using deep learning.
<br><br>
The goal of the project is to support productivity, reduce loss, and make agriculture more data-driven and intelligent.
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---------------- SYSTEM OVERVIEW ----------------
if os.path.exists(overview_img):
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">System Overview</div>', unsafe_allow_html=True)
    st.image(overview_img, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- TEAM SECTION ----------------
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Team</div>', unsafe_allow_html=True)

t1, t2, t3 = st.columns(3)

with t1:
    st.markdown("""
    <div class="team-card">
        <div class="team-name">Anushka Sadegaonkar</div>
        <div class="team-role">Project Developer</div>
        <div class="soft-text">
        Worked on ML models, UI design, system integration, analytics, and system implementation.
        </div>
    </div>
    """, unsafe_allow_html=True)

with t2:
    st.markdown("""
    <div class="team-card">
        <div class="team-name">Vaishnavi Konduru</div>
        <div class="team-role">Team Member</div>
        <div class="soft-text">
        Contributed to development, testing, and implementation support.
        </div>
    </div>
    """, unsafe_allow_html=True)

with t3:
    st.markdown("""
    <div class="team-card">
        <div class="team-name">Viraj Awate</div>
        <div class="team-role">Team Member</div>
        <div class="soft-text">
        Assisted in system design, integration, and project support activities.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

st.markdown("""
<div class="team-card" style="text-align:center;">
    <div class="team-name">Dr. Satpal Singh Rajput</div>
    <div class="team-role">Project Mentor</div>
    <div class="soft-text">
    Guided the project architecture, research methodology, and implementation strategy.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("""
<div style="
    text-align:center;
    padding: 14px;
    margin-top: 10px;
    color: #bcd6e4;
    font-size: 0.9rem;
    border-top: 1px solid rgba(255,255,255,0.08);
">
    AgriAI • Final Year Project • Pimpri Chinchwad University
</div>
""", unsafe_allow_html=True)