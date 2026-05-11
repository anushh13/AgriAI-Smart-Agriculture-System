# 🌱 AgriAI – Smart Crop Recommendation and Plant Disease Detection System

AgriAI is an AI-powered smart agriculture platform that helps farmers make intelligent farming decisions using Machine Learning and Deep Learning techniques.

The system integrates:

- 🌾 Crop Recommendation based on soil and environmental conditions
- 🌿 Plant Disease Detection using leaf image classification

This project aims to improve agricultural productivity, reduce crop loss, and support smart farming through data-driven insights.

---

# 🚀 Features

## 🌾 Crop Recommendation Module
- Predicts the most suitable crop
- Uses soil and environmental parameters
- Displays Top 3 crop recommendations
- Shows confidence/suitability score
- Generates PDF reports
- Provides charts and analytics

---

## 🌿 Plant Disease Detection Module
- Detects plant diseases from leaf images
- Uses CNN-based Deep Learning model
- Displays disease confidence score
- Supports image upload
- Maintains prediction history
- Real-time disease prediction

---

# 🧠 Technologies Used

| Component | Technology |
|---|---|
| Frontend | Streamlit |
| Backend | Python |
| Machine Learning | Random Forest |
| Deep Learning | CNN (MobileNetV2) |
| Libraries | TensorFlow, Scikit-learn, Pandas, NumPy |
| Visualization | Matplotlib |
| Dataset | Crop Dataset + PlantVillage Dataset |

---

# 📊 Dataset Information

## 🌾 Crop Recommendation Dataset
The crop recommendation dataset contains:
- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- pH
- Rainfall
- Crop Label

### Dataset Type
- Structured tabular dataset
- Supervised learning dataset

---

## 🌿 Plant Disease Detection Dataset
Dataset Used:
- PlantVillage Dataset

### Dataset Contains
- Healthy leaf images
- Diseased leaf images
- Multiple crop disease classes

### Dataset Type
- Image classification dataset
- Multi-class classification

---

# 🤖 Models Used

## 🌾 Crop Recommendation Model
### Algorithm:
- Random Forest Classifier

### Why Random Forest?
- High accuracy
- Handles non-linear data
- Reduces overfitting
- Efficient for agricultural prediction

---

## 🌿 Disease Detection Model
### Model:
- CNN (Convolutional Neural Network)

### Transfer Learning:
- MobileNetV2

### Why MobileNetV2?
- Lightweight architecture
- Faster processing
- Better image classification accuracy
- Suitable for real-time prediction

---

# 📈 Results

| Module | Accuracy |
|---|---|
| Crop Recommendation | ~99% |
| Disease Detection | ~89.5% |

---

# 🌟 Project Novelty

- Combines ML + DL in one system
- Integrates crop recommendation and disease detection
- Provides real-time predictions
- Includes charts, reports, and analytics
- User-friendly Streamlit dashboard

---

# 📁 Project Structure

```text
AgriAI/
│
├── app/
│   ├── main_app.py
│   ├── assets/
│   └── pages/
│       ├── 1_Crop_Recommendation.py
│       └── 2_Disease_Detection.py
│
├── models/
│   ├── crop_model.pkl
│   ├── label_encoder.pkl
│   └── disease_model.keras
│
├── notebooks/
│   ├── 01_crop_recommendation.ipynb
│   └── 02_disease_detection.ipynb
│
├── data/
├── requirements.txt
└── README.md
```

---

# ▶️ How to Run the Project

## Step 1: Clone the Repository

```bash
git clone https://github.com/anushh13/AgriAI-Smart-Agriculture-System.git
```

---

## Step 2: Navigate to the Project Directory

```bash
cd AgriAI-Smart-Agriculture-System
```

---

## Step 3: Create a Conda Environment

```bash
conda create -n agriai39 python=3.9
```

---

## Step 4: Activate the Environment

```bash
conda activate agriai39
```

---

## Step 5: Install Required Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 6: Run the Streamlit Application

```bash
streamlit run app/main_app.py
```

---

## Step 7: Open in Browser

```text
http://localhost:8501
```

The AgriAI dashboard will open successfully.

---

# 📄 PDF Report Generation

The system supports:
- Crop prediction reports
- Confidence scores
- Input summary
- Visual analytics
- Downloadable PDF export

---

# 🚀 Future Scope

- Mobile application development
- IoT sensor integration
- Voice-based assistance
- Multilingual support
- Cloud deployment
- Real-time weather API integration
- Smart irrigation recommendation

---

# 💼 Business Scope

The project can be extended as:
- Smart Farming Platform
- SaaS Agriculture Tool
- Mobile Agriculture Assistant
- Government Agriculture Support System

---

# 🎓 Academic Information

Final Year Major Project  
Department of Computer Science & Engineering  
Pimpri Chinchwad University

---


# ✅ Conclusion

AgriAI is an intelligent smart agriculture system that combines Machine Learning and Deep Learning for crop recommendation and plant disease detection.

The project demonstrates how Artificial Intelligence can improve farming decisions, reduce crop loss, and support modern smart agriculture practices.
