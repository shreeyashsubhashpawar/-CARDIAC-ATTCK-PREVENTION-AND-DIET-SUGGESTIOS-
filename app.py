import streamlit as st
import pandas as pd
import joblib
import os
import datetime
import requests


from streamlit_extras.add_vertical_space import add_vertical_space

# Load Models and Encoders
heart_model = joblib.load('C:/Users/LENOVO/Downloads/peti/model/heart_attack_model.pkl')
diet_model = joblib.load('C:/Users/LENOVO/Downloads/peti/model/diet_model.pkl')
label_encoders = joblib.load('C:/Users/LENOVO/Downloads/peti/model/label_encoders.pkl')

# API Endpoint for Slope and Peak
API_URL = "http://192.168.139.116:5000/get_latest_data"

def get_slope_and_peak():
    try:
        response = requests.get(API_URL, timeout=3)
        if response.status_code == 200:
            data = response.json()
            return data['slope'], data['peak']
        else:
            return 2, 4  # Default values in case of error
    except:
        return 2, 4

# Streamlit App Design
st.markdown(
    """
    <style>
    body {background: linear-gradient(135deg, #ff9a9e, #fad0c4);}
    .stButton>button {background: #ff5733; color: white; font-size: 18px; padding: 10px 24px; border-radius: 8px;}
    .stButton>button:hover {background: #c70039;}
    .title {color: #fff; text-align: center; font-size: 40px; font-weight: bold;}
    .result {background: #ffffff; padding: 30px; border-radius: 10px; text-align: center;}
    .result h3 {color: #d9534f; font-size: 28px;}
    .result p {color: #2c3e50; font-size: 20px; font-weight: bold;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h1 class='title'>❤️ Heart Attack Risk & Diet Plan</h1>", unsafe_allow_html=True)

# User Input
name = st.text_input("Name")
age = st.number_input("Age", min_value=1, max_value=120, step=1)
gender = st.selectbox("Gender", ["Male", "Female"])
chestpain = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
restingBP = st.number_input("Resting Blood Pressure (mm Hg)", min_value=50, max_value=250)
serumcholestrol = st.number_input("Serum Cholestrol (mg/dL)", min_value=50, max_value=600)
fastingbloodsugar = st.selectbox("Fasting Blood Sugar > 120 mg/dL", [0, 1])
restingrelectro = st.selectbox("Resting Electrocardiographic Results", [0, 1, 2])
maxheartrate = st.number_input("Maximum Heart Rate Achieved", min_value=50, max_value=220)
exerciseangia = st.selectbox("Exercise Induced Angina", [0, 1])
oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=10.0, step=0.1)

# Fetch Real-time Slope & Peak Values
slope, peak = get_slope_and_peak()
st.write(f"✅ Auto-Fetched Slope: {slope}, Peak: {peak}")

noofmajorvessels = st.selectbox("Number of Major Vessels (0-3)", [0, 1, 2, 3])

# Prediction Button
if st.button("Predict Heart Attack Risk and Diet Plan"):
    input_data = [[age, 1 if gender == "Male" else 0, chestpain, restingBP, serumcholestrol, fastingbloodsugar,
                   restingrelectro, maxheartrate, exerciseangia, oldpeak, slope, noofmajorvessels]]
    input_df = pd.DataFrame(input_data, columns=["age", "gender", "chestpain", "restingBP", "serumcholestrol", "fastingbloodsugar", 
                                                  "restingrelectro", "maxheartrate", "exerciseangia", "oldpeak", "slope", "noofmajorvessels"])
    heart_prediction = heart_model.predict(input_df)
    heart_prob = heart_model.predict_proba(input_df)[0][1] * 100
    risk = "High" if heart_prediction[0] == 1 else "Low"

    diet_input = [[age, serumcholestrol, restingBP, slope, oldpeak, chestpain]]
    diet_prediction = diet_model.predict(diet_input)
    diet_plan = label_encoders['Diet Plan'].inverse_transform([diet_prediction[0][0]])[0]
    foods_include = label_encoders['Foods to Include'].inverse_transform([diet_prediction[0][1]])[0]
    foods_avoid = label_encoders['Foods to Avoid'].inverse_transform([diet_prediction[0][2]])[0]

    # Display Result
    st.markdown(
        f"""
        <div class='result'>
            <h3>Predicted Heart Attack Risk: {risk} ({heart_prob:.2f}%)</h3>
            <p>🍽 Recommended Diet Plan: {diet_plan}</p>
            <p>✅ Foods to Include: {foods_include}</p>
            <p>❌ Foods to Avoid: {foods_avoid}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Save Data to CSV
    data = {
        'Name': [name], 'Age': [age], 'Gender': [gender], 'Chest Pain Type': [chestpain],
        'Resting BP': [restingBP], 'Serum Cholesterol': [serumcholestrol], 'Fasting Blood Sugar': [fastingbloodsugar],
        'Resting ECG': [restingrelectro], 'Max Heart Rate': [maxheartrate], 'Exercise Angina': [exerciseangia],
        'Oldpeak': [oldpeak], 'Slope': [slope], 'Major Vessels': [noofmajorvessels],
        'Heart Attack Risk': [risk], 'Probability (%)': [heart_prob], 'Diet Plan': [diet_plan],
        'Foods to Include': [foods_include], 'Foods to Avoid': [foods_avoid],
        'Timestamp': [datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
    }
    df = pd.DataFrame(data)
    df.to_csv("prediction_details.csv", mode='a', header=not os.path.exists("prediction_details.csv"), index=False)
    st.success("✅ Prediction details saved successfully!")
