import streamlit as st
import pickle
import os

# Streamlit Page Configuration
st.set_page_config(page_title="Kidney Disease Prediction", layout="wide", page_icon="🩺")

st.title("Kidney Disease Prediction using Machine Learning")

# Load Model with Error Handling
model_path = "Kidney.pkl"

if not os.path.exists(model_path):
    st.error("Model file not found! Please check 'Kidney.pkl' in your directory.")
    st.stop()

with open(model_path, 'rb') as f:
    kidney_disease_model = pickle.load(f)

# UI Input Form
st.markdown("### Enter Patient Details:")

col1, col2, col3, col4, col5 = st.columns(5)

def get_float_input(label, col):
    """ Helper function to get float input and handle errors """
    value = col.text_input(label)
    try:
        return float(value) if value.strip() else None
    except ValueError:
        return None  # Invalid input

with col1:
    age = get_float_input('Age', col1)
    red_blood_cells = st.selectbox('Red Blood Cells (0: Abnormal, 1: Normal)', [0, 1])  
    blood_urea = get_float_input('Blood Urea', col1)
    packed_cell_volume = get_float_input('Packed Cell Volume', col1)
    coronary_artery_disease = st.selectbox('Coronary Artery Disease', [0, 1]) 

with col2:
    blood_pressure = get_float_input('Blood Pressure', col2)
    pus_cell = st.selectbox('Pus Cell (0: Abnormal, 1: Normal)', [0, 1])  
    serum_creatinine = get_float_input('Serum Creatinine', col2)
    white_blood_cell_count = get_float_input('White Blood Cell Count', col2)
    appetite = st.selectbox('Appetite (0: Poor, 1: Good)', [0, 1])  

with col3:
    specific_gravity = get_float_input('Specific Gravity', col3)
    pus_cell_clumps = st.selectbox('Pus Cell Clumps (0: Not Present, 1: Present)', [0, 1])  
    sodium = get_float_input('Sodium', col3)
    red_blood_cell_count = get_float_input('Red Blood Cell Count', col3)
    peda_edema = st.selectbox('Peda Edema (0: No, 1: Yes)', [0, 1])  

with col4:
    albumin = get_float_input('Albumin', col4)
    bacteria = st.selectbox('Bacteria (0: Not Present, 1: Present)', [0, 1])  
    potassium = get_float_input('Potassium', col4)
    hypertension = st.selectbox('Hypertension (0: No, 1: Yes)', [0, 1])  
    anemia = st.selectbox('Anemia (0: No, 1: Yes)', [0, 1])  

with col5:
    sugar = get_float_input('Sugar', col5)
    blood_glucose_random = get_float_input('Blood Glucose Random', col5)
    haemoglobin = get_float_input('Haemoglobin', col5)
    diabetes_mellitus = st.selectbox('Diabetes Mellitus (0: No, 1: Yes)', [0, 1])  

# Prediction Section
st.markdown("### 🔎 Kidney Disease Test Result")
kidney_diagnosis = ""

if st.button("🔍 Predict"):
    user_input = [
        age, blood_pressure, specific_gravity, albumin, sugar,
        red_blood_cells, pus_cell, pus_cell_clumps, bacteria,
        blood_glucose_random, blood_urea, serum_creatinine, sodium,
        potassium, haemoglobin, packed_cell_volume,
        white_blood_cell_count, red_blood_cell_count, hypertension,
        diabetes_mellitus, coronary_artery_disease, appetite,
        peda_edema, anemia
    ]

    # Check for Missing Inputs
    if None in user_input:
        st.error("⚠️ Please enter **all required fields** before predicting!")
    else:
        with st.spinner("🔍 Analyzing data... Please wait!"):
            prediction = kidney_disease_model.predict([user_input])
        
        # Fix Prediction Output Based on Correct CKD Mapping
        if prediction[0] == 0:
            kidney_diagnosis = "⚠️ The person **has Kidney Disease!**"
        else:
            kidney_diagnosis = "✅ The person does **not** have Kidney Disease."
        
        st.success(kidney_diagnosis)
