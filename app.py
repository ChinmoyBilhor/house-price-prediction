import streamlit as st
import pandas as pd
import joblib


# Load model
model = joblib.load("model.pkl")


# Page settings
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠"
)


# Title
st.title("🏠 House Price Predictor")
st.write("Enter house details to predict the estimated price.")


# Inputs
area = st.number_input(
    "Area (sq ft)",
    min_value=300,
    max_value=5000,
    value=1500,
    step=100
)

bedrooms = st.number_input(
    "Number of Bedrooms",
    min_value=1,
    max_value=10,
    value=3,
    step=1
)

bathrooms = st.number_input(
    "Number of Bathrooms",
    min_value=1,
    max_value=10,
    value=2,
    step=1
)

age = st.number_input(
    "House Age (years)",
    min_value=0,
    max_value=100,
    value=5,
    step=1
)


# Prediction
if st.button("Predict Price"):

    input_data = pd.DataFrame({
        "area": [area],
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms],
        "age": [age]
    })

    prediction = model.predict(input_data)[0]

    st.success(
        f"🏠 Estimated Price: ₹{prediction:.2f} Lakhs"
    )


st.divider()

st.caption(
    "This application is for demonstration and educational purposes."
)