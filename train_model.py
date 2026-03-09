import streamlit as st
import numpy as np
import pickle

st.title("PulseGuard AI")
st.write("Hypertension Prediction System")

# load model
model = pickle.load(open("model.pkl", "rb"))

age = st.number_input("Age", 1, 100)
bmi = st.number_input("BMI", 10.0, 50.0)
cholesterol = st.selectbox("High Cholesterol", [0,1])
smoker = st.selectbox("Smoker", [0,1])
exercise = st.selectbox("Exercise", [0,1])

if st.button("Predict"):
    
    data = np.array([[age,bmi,cholesterol,smoker,exercise]])
    
    prediction = model.predict(data)
    
    if prediction == 1:
        st.error("High Risk of Hypertension")
    else:
        st.success("Low Risk of Hypertension")