import streamlit as st
import requests

st.title("Student Performance Predictor")

hours = st.number_input("Hours Studied", 0.0, 24.0, 5.0)
prev_scores = st.number_input("Previous Scores", 0.0, 100.0, 70.0)
extracurricular = st.selectbox("Extracurricular Activities", ["Yes", "No"])
sleep_hours = st.number_input("Sleep Hours", 0.0, 24.0, 7.0)
sample_papers = st.number_input("Sample Question Papers Practiced", 0, 50, 3)

if st.button("Predict"):
    data = {
        "Hours_Studied": hours,
        "Previous_Scores": prev_scores,
        "Extracurricular_Activities": extracurricular,
        "Sleep_Hours": sleep_hours,
        "Sample_Question_Papers_Practiced": sample_papers
    }

    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=data)
        response.raise_for_status()
        st.success(f"Predicted Performance Index: {response.json()['Performance Index']}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")