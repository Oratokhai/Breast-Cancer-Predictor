import streamlit as st
import joblib
import numpy as np

model = joblib.load("best_model.pkl")

st.title(" Breast Cancer Prediction System")
st.write("Enter the following features to predict if the tumor is malignant or benign.")

features = [
    "mean radius", "mean texture", "mean smoothness", "worst radius", "worst smoothness"
]

user_inputs = []

for feature in features:
    val = st.number_input(f"{feature}", min_value=0.0, format="%.5f")
    user_inputs.append(val)

if st.button("Predict"):
    data = np.array([user_inputs])
    prediction = model.predict(data)
    if prediction[0] == 0:
        st.success(" The tumor is **Benign** (Not cancerous).")
    else:
        st.error(" The tumor is **Malignant** (Cancerous).")
