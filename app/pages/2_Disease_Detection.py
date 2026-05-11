import streamlit as st
import os
import json
import numpy as np
import pandas as pd
from PIL import Image
import tensorflow as tf
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Disease Detection", page_icon="🌿", layout="wide")

# ---------------- PATHS ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))   # pages folder
APP_DIR = os.path.dirname(BASE_DIR)                     # app folder
PROJECT_DIR = os.path.dirname(APP_DIR)                  # project root

ASSETS_DIR = os.path.join(APP_DIR, "assets")
MODELS_DIR = os.path.join(PROJECT_DIR, "models")

disease_banner = os.path.join(ASSETS_DIR, "disease_banner.png")
model_keras_path = os.path.join(MODELS_DIR, "disease_model.keras")
model_h5_path = os.path.join(MODELS_DIR, "disease_model.h5")
class_names_path = os.path.join(MODELS_DIR, "disease_class_names.json")

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_disease_model():
    if os.path.exists(model_keras_path):
        return tf.keras.models.load_model(model_keras_path)
    elif os.path.exists(model_h5_path):
        return tf.keras.models.load_model(model_h5_path)
    else:
        raise FileNotFoundError("Disease model file not found. Keep disease_model.keras or disease_model.h5 in the models folder.")

model = load_disease_model()

# ---------------- LOAD CLASS NAMES ----------------
def load_class_names():
    if os.path.exists(class_names_path):
        with open(class_names_path, "r") as f:
            return json.load(f)
    else:
        # fallback list; replace with your exact classes if needed
        return [
            "Pepper__bell___Bacterial_spot",
            "Pepper__bell___healthy",
            "Potato___Early_blight",
            "Potato___Late_blight",
            "Potato___healthy",
            "Tomato_Bacterial_spot",
            "Tomato_Early_blight",
            "Tomato_Late_blight",
            "Tomato_Leaf_Mold",
            "Tomato_Septoria_leaf_spot",
            "Tomato_Spider_mites_Two_spotted_spider_mite",
            "Tomato__Target_Spot",
            "Tomato__Tomato_YellowLeaf__Curl_Virus",
            "Tomato__Tomato_mosaic_virus",
            "Tomato_healthy"
        ]

class_names = load_class_names()

# ---------------- SESSION STATE FOR HISTORY ----------------
if "disease_history" not in st.session_state:
    st.session_state["disease_history"] = []

# ---------------- DISEASE INFO ----------------
disease_info = {
    "Pepper__bell___Bacterial_spot": "Use disease-free seeds, remove infected leaves, and apply copper-based bactericides.",
    "Pepper__bell___healthy": "The plant appears healthy. Continue proper irrigation and nutrient management.",
    "Potato___Early_blight": "Remove infected leaves, rotate crops, and apply fungicide if required.",
    "Potato___Late_blight": "Avoid excess moisture, remove infected parts, and apply a recommended fungicide immediately.",
    "Potato___healthy": "The plant appears healthy. Maintain regular crop monitoring.",
    "Tomato_Bacterial_spot": "Use certified seeds, avoid overhead watering, and remove infected foliage.",
    "Tomato_Early_blight": "Prune lower leaves, improve air circulation, and use fungicide if necessary.",
    "Tomato_Late_blight": "Remove infected plants quickly, reduce leaf wetness, and apply fungicide.",
    "Tomato_Leaf_Mold": "Reduce humidity, improve ventilation, and remove affected leaves.",
    "Tomato_Septoria_leaf_spot": "Remove infected leaves and avoid splashing water on foliage.",
    "Tomato_Spider_mites_Two_spotted_spider_mite": "Use neem oil or miticides and inspect nearby plants regularly.",
    "Tomato__Target_Spot": "Remove affected leaves and improve plant spacing and airflow.",
    "Tomato__Tomato_YellowLeaf__Curl_Virus": "Control whiteflies, remove infected plants, and use resistant varieties.",
    "Tomato__Tomato_mosaic_virus": "Remove infected plants and disinfect tools to prevent spread.",
    "Tomato_healthy": "The plant appears healthy. Continue good crop care practices."
}

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
    max-width: 1380px;
    padding-top: 2.8rem;
    padding-bottom: 2rem;
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

@keyframes glowPulse {
    0% {
        box-shadow: 0 0 0 rgba(116,245,159,0.15);
        transform: scale(1);
    }
    50% {
        box-shadow: 0 0 22px rgba(116,245,159,0.20);
        transform: scale(1.02);
    }
    100% {
        box-shadow: 0 0 0 rgba(116,245,159,0.15);
        transform: scale(1);
    }
}

.hero-shell {
    margin-bottom: 1.6rem;
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
    animation: glowPulse 2.8s ease-in-out infinite;
}

.hero-title {
    font-size: 3.2rem;
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
    animation: floatSlow 4.5s ease-in-out infinite;
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

.result-card {
    padding: 26px;
    border-radius: 24px;
    background: linear-gradient(135deg, rgba(116,245,159,0.18), rgba(78,225,184,0.08));
    border: 1px solid rgba(116,245,159,0.24);
    box-shadow: 0 14px 34px rgba(0,0,0,0.22);
    margin-bottom: 1.2rem;
}

.metric-card {
    padding: 22px 18px;
    border-radius: 22px;
    background: linear-gradient(135deg, rgba(255,255,255,0.07), rgba(255,255,255,0.03));
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 10px 24px rgba(0,0,0,0.18);
    text-align: center;
    height: 100%;
    transition: transform 0.25s ease, box-shadow 0.25s ease;
}

.metric-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 16px 32px rgba(0,0,0,0.22);
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
    font-size: 1.5rem;
    font-weight: 750;
    margin-bottom: 0.9rem;
    color: #ffffff;
}

.soft-text {
    color: #dbe8ef;
    line-height: 1.75;
    font-size: 0.98rem;
}

img {
    border-radius: 20px;
}

div.stButton > button {
    width: 100%;
    border: none;
    border-radius: 16px;
    padding: 0.9rem 1rem;
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

[data-testid="stDataFrame"] {
    border-radius: 18px;
    overflow: hidden;
}

thead tr th {
    background-color: rgba(255,255,255,0.08) !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------- PREPROCESS IMAGE ----------------
def preprocess_image(image):
    image = image.convert("RGB")
    image = image.resize((224, 224))
    img_array = np.array(image).astype("float32")
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# ---------------- HERO SECTION ----------------
st.markdown('<div class="hero-shell">', unsafe_allow_html=True)
left, right = st.columns([1.18, 1], gap="large")

with left:
    st.markdown('<div class="hero-card">', unsafe_allow_html=True)
    st.markdown('<div class="hero-badge">🌿 AI-powered leaf disease intelligence</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-title">Plant Disease Detection</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">Deep Learning Based Plant Health Analysis</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="hero-text">
    Upload a plant leaf image to detect disease conditions using a trained deep learning model.
    This module provides prediction confidence, top alternative diagnoses, treatment guidance,
    and exportable prediction history.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    if os.path.exists(disease_banner):
        st.markdown('<div class="image-card">', unsafe_allow_html=True)
        st.image(disease_banner, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("disease_banner.png not found in app/assets")
st.markdown('</div>', unsafe_allow_html=True)

# ---------------- UPLOAD SECTION ----------------
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Upload Leaf Image</div>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("Choose a plant leaf image", type=["jpg", "jpeg", "png"])

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- PREDICTION SECTION ----------------
if uploaded_file is not None:
    image = Image.open(uploaded_file)

    c1, c2 = st.columns([1, 1], gap="large")

    with c1:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Uploaded Image</div>', unsafe_allow_html=True)
        st.image(image, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    processed_image = preprocess_image(image)
    predictions = model.predict(processed_image, verbose=0)[0]

    predicted_index = int(np.argmax(predictions))
    confidence = float(np.max(predictions) * 100)
    predicted_class = class_names[predicted_index]

    top3_idx = np.argsort(predictions)[-3:][::-1]
    top3_data = []
    for idx in top3_idx:
        top3_data.append({
            "Prediction": class_names[idx].replace("___", " - ").replace("_", " "),
            "Confidence (%)": float(predictions[idx] * 100)
        })

    top3_df = pd.DataFrame(top3_data)

    clean_name = predicted_class.replace("___", " - ").replace("_", " ")
    recommendation = disease_info.get(predicted_class, "Monitor the plant regularly and consult an agricultural expert if symptoms increase.")

    with c2:
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown(f"## ✅ Detected Result: **{clean_name}**")
        st.markdown(f"""
        <div class="soft-text">
        The uploaded image has been analyzed by the deep learning model. Based on the detected leaf patterns,
        the most likely condition is <b>{clean_name}</b>.
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        m1, m2, m3 = st.columns(3)
        with m1:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Top Prediction</div>
                <div class="metric-value">{clean_name[:14]}{"..." if len(clean_name) > 14 else ""}</div>
                <div class="metric-sub">Primary result</div>
            </div>
            """, unsafe_allow_html=True)
        with m2:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Confidence</div>
                <div class="metric-value">{confidence:.2f}%</div>
                <div class="metric-sub">Model certainty</div>
            </div>
            """, unsafe_allow_html=True)
        with m3:
            st.markdown("""
            <div class="metric-card">
                <div class="metric-label">Alternatives</div>
                <div class="metric-value">3</div>
                <div class="metric-sub">Compared classes</div>
            </div>
            """, unsafe_allow_html=True)

    # Top 3 + Recommendation
    t1, t2 = st.columns(2, gap="large")

    with t1:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">🌿 Top 3 Predictions</div>', unsafe_allow_html=True)
        st.dataframe(top3_df, use_container_width=True, hide_index=True)
        st.bar_chart(top3_df.set_index("Prediction"))
        st.markdown('</div>', unsafe_allow_html=True)

    with t2:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">💡 Recommendation / Treatment Guidance</div>', unsafe_allow_html=True)
        st.markdown(f"""
        <div class="soft-text">
        {recommendation}
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Save history
    history_record = {
        "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "File Name": uploaded_file.name,
        "Detected Result": clean_name,
        "Confidence (%)": round(confidence, 2)
    }
    st.session_state["disease_history"].append(history_record)

# ---------------- HISTORY SECTION ----------------
if len(st.session_state["disease_history"]) > 0:
    history_df = pd.DataFrame(st.session_state["disease_history"])

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📜 Prediction History</div>', unsafe_allow_html=True)
    st.dataframe(history_df, use_container_width=True, hide_index=True)

    d1, d2 = st.columns(2)
    with d1:
        st.download_button(
            label="📥 Download History CSV",
            data=history_df.to_csv(index=False),
            file_name="disease_prediction_history.csv",
            mime="text/csv"
        )

    with d2:
        if st.button("🗑 Clear History"):
            st.session_state["disease_history"] = []
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)