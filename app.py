import streamlit as st
import joblib

# Loading the trained ML model
model = joblib.load("aqi_prediction_model.pkl")

# App title
st.title("AQI Prediction App")
st.write("Enter the following parameters to predict AQI:")

# User input fields
pm25 = st.number_input("PM2.5 (10 - 100)", min_value=0.0)
pm10 = st.number_input("PM10 (20 - 200)", min_value=0.0)
no2 = st.number_input("NO2 (0.1 - 10)", min_value=0.0)
so2 = st.number_input("SO2 (1 - 50)", min_value=0.0)
co = st.number_input("CO (0.1 - 5.0)", min_value=0.0)
o3 = st.number_input("O3 (10 - 100)", min_value=0.0)

# Prediction button
if st.button("Predict AQI"):
    input_data = [[pm25, pm10, no2, so2, co, o3]]
    prediction = model.predict(input_data)
    
    st.success(f"Estimated AQI: {prediction[0]:,.2f}")