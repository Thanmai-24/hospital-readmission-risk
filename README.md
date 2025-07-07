# 🧠 Hospital Readmission Risk Predictor

A web-based machine learning application that predicts whether a patient is likely to be readmitted to a hospital within 30 days of discharge — based on their discharge details and medical information.

> 💡 Built with a clean ML pipeline and a glowing UI for professional presentation.

---

## 📌 Problem Statement

Create a model that predicts likelihood of hospital readmission within 30 days using patient data such as:

- Demographics (age, gender)
- Diagnosis codes
- Length of stay
- Number of procedures

---

## 🛠️ Technologies Used

- **Python**
- **Flask**
- **Pandas**
- **Scikit-learn**
- **HTML + CSS (glow UI)**

---

## 💡 Key Features

- ✅ Real-time web prediction tool
- ✅ Random Forest model with balanced class weighting
- ✅ Feature engineering: age groups, diagnosis grouping
- ✅ One-hot encoding for categorical codes
- ✅ Modular code (each task in its own file)
- ✅ Handles unknown diagnosis inputs gracefully
- ✅ Animated, responsive frontend UI

---

## 🧠 Skills Demonstrated

| Skill Area         | Demonstrated By                                 |
|--------------------|--------------------------------------------------|
| **AI/ML**          | Model trained on medical diagnosis + stay data   |
| **Critical Thinking** | Risk factors like age/stay/meds weighted in model |
| **Problem Solving** | Categorical encoding + class imbalance handled  |
| **Modular Design** | `preprocess.py`, `feature_engineering.py`, etc. |
| **Architecture**   | Clear pipeline from input → prediction → frontend |
| **User Experience**| Interactive frontend with polished design        |

---

## 🏗️ Project Structure

hospital-readmission-risk/
│
├── data/
│ └── hospital_data.csv # 25-row sample data
├── processed/
│ └── cleaned.csv # After preprocessing
├── features/
│ └── final.csv # After one-hot encoding
├── models/
│ └── model.pkl # Trained RandomForestClassifier
├── templates/
│ └── index.html # Frontend form (glow UI)
│
├── preprocess.py # Cleans and encodes data
├── feature_engineering.py # Age group binning, one-hot
├── train.py # Trains and saves model
├── app.py # Flask backend for predictions
└── README.md

1. 🔧 Install required packages:

```bash
pip install pandas scikit-learn flask
🔄 Run the ML pipeline:

bash
Copy
Edit
python preprocess.py
python feature_engineering.py
python train.py
🌐 Start the web app:

bash
Copy
Edit
python app.py
🖥 Open your browser and go to:

cpp
Copy
Edit
http://127.0.0.1:5000


✅ Try These Example Inputs
🟥 High Risk Example:
Field	Value
Age	85
Length of Stay	14
Gender	1 (Male)
Procedures	4
Diagnosis	E11 (Diabetes)

📈 Output: Readmission Risk: High

🟩 Low Risk Example:
Field	Value
Age	25
Length of Stay	2
Gender	0 (Female)
Procedures	1
Diagnosis	J20 (Bronchitis)

📉 Output: Readmission Risk: Low


