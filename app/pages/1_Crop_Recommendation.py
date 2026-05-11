import streamlit as st
import pandas as pd
import joblib
import numpy as np
from datetime import datetime
from fpdf import FPDF
import tempfile
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Crop Recommendation", page_icon="🌾", layout="wide")

# ---------------- PATHS ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))   # pages folder
APP_DIR = os.path.dirname(BASE_DIR)                     # app folder
PROJECT_DIR = os.path.dirname(APP_DIR)                  # Agri AI folder

ASSETS_DIR = os.path.join(APP_DIR, "assets")
MODELS_DIR = os.path.join(PROJECT_DIR, "models")

crop_banner = os.path.join(ASSETS_DIR, "crop_banner.png")
model_path = os.path.join(MODELS_DIR, "crop_model.pkl")
label_encoder_path = os.path.join(MODELS_DIR, "label_encoder.pkl")

# ---------------- LOAD MODEL ----------------
model = joblib.load(model_path)
label_encoder = joblib.load(label_encoder_path)

# ---------------- CSS ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #06121c 0%, #0b2232 100%);
    color: #ffffff;
}

.block-container {
    padding-top: 3.2rem;
    max-width: 1400px;
}

/* Hero */
.hero-wrap {
    margin-bottom: 1.4rem;
}

.hero-card {
    padding: 30px;
    border-radius: 26px;
    background: linear-gradient(135deg, rgba(116,245,159,0.10), rgba(78,225,184,0.05));
    border: 1px solid rgba(116,245,159,0.16);
    box-shadow: 0 14px 30px rgba(0,0,0,0.22);
    min-height: 100%;
}

.hero-title {
    font-size: 3rem;
    font-weight: 800;
    color: #8ef7b8;
    line-height: 1.1;
    margin-bottom: 0.4rem;
    white-space: nowrap;
}

.hero-subtitle {
    font-size: 1.12rem;
    font-weight: 600;
    color: #d4f5e9;
    margin-bottom: 1rem;
}

.hero-text {
    color: #d8e7ef;
    font-size: 1rem;
    line-height: 1.75;
}

.hero-badge {
    display: inline-block;
    padding: 8px 14px;
    border-radius: 999px;
    background: rgba(116,245,159,0.14);
    border: 1px solid rgba(116,245,159,0.20);
    color: #baf7d0;
    font-size: 0.9rem;
    font-weight: 600;
    margin-bottom: 1rem;
}

.hero-image {
    border-radius: 24px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 14px 30px rgba(0,0,0,0.28);
    background: rgba(255,255,255,0.03);
    padding: 8px;
}

/* Cards */
.section-card {
    padding: 24px;
    border-radius: 20px;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    margin-bottom: 20px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.18);
}

.result-card {
    padding: 24px;
    border-radius: 20px;
    background: linear-gradient(135deg, rgba(116,245,159,0.16), rgba(78,225,184,0.08));
    border: 1px solid rgba(116,245,159,0.25);
    margin-bottom: 20px;
    box-shadow: 0 10px 28px rgba(0,0,0,0.22);
}

.metric-card {
    padding: 20px;
    border-radius: 18px;
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.08);
    text-align: center;
    box-shadow: 0 8px 20px rgba(0,0,0,0.18);
}

.metric-title {
    font-size: 0.95rem;
    color: #cfe8db;
    margin-bottom: 0.4rem;
}

.metric-value {
    font-size: 1.8rem;
    font-weight: 800;
    color: #8ef7b8;
}

.section-title {
    font-size: 1.9rem;
    font-weight: 750;
    color: #ffffff;
    margin-bottom: 0.8rem;
}

.small-text {
    color: #d8e7ef;
    font-size: 0.98rem;
    line-height: 1.7;
}

img {
    border-radius: 18px;
}

div.stButton > button {
    width: 100%;
    border-radius: 14px;
    padding: 12px;
    font-weight: 700;
    background: linear-gradient(90deg, #74f59f, #4ee1b8);
    color: black;
    border: none;
}

div.stButton > button:hover {
    background: linear-gradient(90deg, #8ef7b8, #64f0c6);
    color: black;
}

thead tr th {
    background-color: rgba(255,255,255,0.08) !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------- PDF REPORT ----------------
def create_pdf_report(summary_df, predicted_crop, confidence, top3_df):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "AgriAI Crop Recommendation Report", ln=True, align="C")

    pdf.ln(5)
    pdf.set_font("Arial", "", 11)
    pdf.cell(0, 8, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)

    pdf.ln(4)
    pdf.set_font("Arial", "B", 13)
    pdf.cell(0, 8, "Prediction Result", ln=True)

    pdf.set_font("Arial", "", 11)
    pdf.cell(0, 8, f"Recommended Crop: {predicted_crop}", ln=True)
    pdf.cell(0, 8, f"Confidence: {confidence:.2f}%", ln=True)

    pdf.ln(4)
    pdf.set_font("Arial", "B", 13)
    pdf.cell(0, 8, "Input Summary", ln=True)

    pdf.set_font("Arial", "", 11)
    for _, row in summary_df.iterrows():
        pdf.cell(0, 8, f"{row['Parameter']}: {row['Value']}", ln=True)

    pdf.ln(4)
    pdf.set_font("Arial", "B", 13)
    pdf.cell(0, 8, "Top 3 Crop Suggestions", ln=True)

    pdf.set_font("Arial", "", 11)
    for i, row in top3_df.iterrows():
        pdf.cell(0, 8, f"{i+1}. {row['Crop']} - {row['Confidence (%)']:.2f}%", ln=True)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        pdf.output(tmp_file.name)
        with open(tmp_file.name, "rb") as f:
            return f.read()

# ---------------- HERO SECTION ----------------
st.markdown('<div class="hero-wrap">', unsafe_allow_html=True)
left, right = st.columns([1.2, 1], gap="large")

with left:
    st.markdown('<div class="hero-card">', unsafe_allow_html=True)
    st.markdown('<div class="hero-badge">🌾 AI-powered soil intelligence</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-title">Crop Recommendation</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">AI-Based Smart Crop Recommendation System</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="hero-text">
    Analyze soil nutrients and environmental conditions to identify the most suitable crop.
    This module provides recommendation confidence, top alternatives, visual analytics, and downloadable reports.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    if os.path.exists(crop_banner):
        st.markdown('<div class="hero-image">', unsafe_allow_html=True)
        st.image(crop_banner, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("crop_banner.png not found in app/assets")
st.markdown('</div>', unsafe_allow_html=True)

# ---------------- INPUT SECTION ----------------
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Enter Soil & Environmental Parameters</div>', unsafe_allow_html=True)

if st.button("Use Sample Rice Values"):
    st.session_state["N"] = 90.0
    st.session_state["P"] = 42.0
    st.session_state["K"] = 43.0
    st.session_state["temperature"] = 20.0
    st.session_state["humidity"] = 82.0
    st.session_state["ph"] = 6.5
    st.session_state["rainfall"] = 200.0

c1, c2 = st.columns(2)

with c1:
    N = st.number_input("Nitrogen (N)", min_value=0.0, max_value=200.0, value=st.session_state.get("N", 90.0), step=1.0)
    P = st.number_input("Phosphorus (P)", min_value=0.0, max_value=200.0, value=st.session_state.get("P", 42.0), step=1.0)
    K = st.number_input("Potassium (K)", min_value=0.0, max_value=200.0, value=st.session_state.get("K", 43.0), step=1.0)
    temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, value=st.session_state.get("temperature", 20.0), step=0.1)

with c2:
    humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=st.session_state.get("humidity", 82.0), step=0.1)
    ph = st.number_input("pH Value", min_value=0.0, max_value=14.0, value=st.session_state.get("ph", 6.5), step=0.1)
    rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=500.0, value=st.session_state.get("rainfall", 200.0), step=0.1)

recommend_clicked = st.button("🌾 Generate Recommendation")
st.markdown('</div>', unsafe_allow_html=True)

# ---------------- RESULT SECTION ----------------
if recommend_clicked:
    input_df = pd.DataFrame([{
        "N": N,
        "P": P,
        "K": K,
        "temperature": temperature,
        "humidity": humidity,
        "ph": ph,
        "rainfall": rainfall
    }])

    prediction = model.predict(input_df)
    probabilities = model.predict_proba(input_df)[0]

    predicted_crop = label_encoder.inverse_transform(prediction)[0]
    confidence = float(np.max(probabilities) * 100)

    top3_idx = np.argsort(probabilities)[-3:][::-1]
    top3_crops = label_encoder.inverse_transform(top3_idx)
    top3_scores = probabilities[top3_idx] * 100

    top3_df = pd.DataFrame({
        "Crop": top3_crops,
        "Confidence (%)": top3_scores
    })

    summary_df = pd.DataFrame({
        "Parameter": [
            "Nitrogen (N)",
            "Phosphorus (P)",
            "Potassium (K)",
            "Temperature (°C)",
            "Humidity (%)",
            "pH",
            "Rainfall (mm)"
        ],
        "Value": [N, P, K, temperature, humidity, ph, rainfall]
    })

    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    st.markdown(f"## Recommended Crop: **{predicted_crop.upper()}**")
    st.markdown("### Decision Summary")
    st.markdown(f"""
    <div class="small-text">
    Based on the provided soil and climate parameters, the model predicts that
    <b>{predicted_crop.upper()}</b> is the most suitable crop for cultivation.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Top Crop</div>
            <div class="metric-value">{predicted_crop.upper()}</div>
        </div>
        """, unsafe_allow_html=True)
    with m2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Confidence</div>
            <div class="metric-value">{confidence:.2f}%</div>
        </div>
        """, unsafe_allow_html=True)
    with m3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Alternatives</div>
            <div class="metric-value">3</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    t1, t2 = st.columns(2)
    with t1:
        st.markdown("## 🌾 Top 3 Crop Suggestions")
        st.dataframe(top3_df, use_container_width=True, hide_index=True)

    with t2:
        st.markdown("## 📋 Input Summary")
        st.dataframe(summary_df, use_container_width=True, hide_index=True)

    st.write("")

    ch1, ch2 = st.columns(2)
    with ch1:
        st.markdown("### 📊 Soil Parameter Analysis")
        st.bar_chart(summary_df.set_index("Parameter"))

    with ch2:
        st.markdown("### 📉 Crop Confidence Comparison")
        st.bar_chart(top3_df.set_index("Crop"))

    st.write("")

    pdf_data = create_pdf_report(summary_df, predicted_crop, confidence, top3_df)

    d1, d2 = st.columns(2)
    with d1:
        st.download_button(
            label="📄 Download PDF Report",
            data=pdf_data,
            file_name="crop_recommendation_report.pdf",
            mime="application/pdf"
        )
    with d2:
        st.download_button(
            label="📥 Download CSV Summary",
            data=summary_df.to_csv(index=False),
            file_name="crop_input_summary.csv",
            mime="text/csv"
        )