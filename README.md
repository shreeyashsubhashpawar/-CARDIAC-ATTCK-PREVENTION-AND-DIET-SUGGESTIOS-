# 💓 Heart Disease Prediction & Personalized Diet Recommendation

This project is a smart healthcare system that leverages machine learning and embedded hardware to predict heart attack risk and provide real-time, personalized dietary recommendations. It integrates physiological signal processing from ECG sensors with data-driven ML models for comprehensive cardiovascular health monitoring.

---

## 🚀 Features

- **Heart Disease Prediction** using Random Forest with 98% accuracy.
- **Real-Time ECG Signal Processing** via ESP32 and AD8232 sensor.
- **Automatic Slope & Peak Extraction** from ECG for enhanced predictions.
- **Personalized Diet Recommendations** based on risk levels (e.g., DASH diet).
- **Interactive Streamlit Dashboard** for user input and result visualization.
- **Flask Backend API** for real-time data communication.

---

## 🛠 Tech Stack

| Component       | Technology Used                |
|----------------|----------------------------------|
| Frontend       | Streamlit                       |
| Backend        | Flask, Python                   |
| Machine Learning | Scikit-learn, Pandas, NumPy     |
| ECG Processing | ESP32, AD8232 ECG Sensor        |
| Data Visualization | Matplotlib, Seaborn           |

---

## 📊 Input Parameters
- Age
- Gender
- Chest Pain Type
- Resting Blood Pressure
- Serum Cholesterol
- Fasting Blood Sugar
- Resting ECG Results
- Maximum Heart Rate
- Exercise-Induced Angina
- ST Depression (Oldpeak)
- **Slope** and **Peak** (from ECG hardware)
- Number of Major Vessels

---

## 📁 Project Structure
```
├── model/
│   ├── heart_attack_model.pkl
│   ├── diet_model.pkl
│   └── label_encoders.pkl
├── app.py
├── backend/
│   └── flask_api.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
```

---

## ⚙️ Setup Instructions
1. Clone the repository.
2. Install dependencies:
   ```bash
   ALREADY IN CODE
   ```
  
3. Run the Flask API:
   ```bash
   python backend/flask_api.py (IF ALSO USING HARDWARE)
   ```
4. Launch the Streamlit interface:
   ```bash
   streamlit run app.py
   ```

---

## 📌 Author
**Shreeyash Pawar**  
Department of Electronics & Electrical Engineering, MIT-WPU  
Email: shreeyashpawar0903@gmail.com

---

## 🏁 Future Enhancements
- Add multi-diet plan recommendations using user preferences.
- Integrate mobile app for real-time alerts.
- Extend to monitor more cardiac anomalies via ECG.

---


