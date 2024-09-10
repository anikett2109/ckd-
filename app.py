import streamlit as st
import pickle
import numpy as np

# Load the trained model
model_path = 'Chronic_kidney_disease.pkl'
try:
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error(f"Model file '{model_path}' not found.")
    st.stop()

# Define the Streamlit app layout
st.title('Chronic Kidney Disease Prediction')

# Input fields for user data
age = st.number_input('Age', min_value=0, max_value=150, value=50, step=1)
bp = st.number_input('Blood Pressure', min_value=0, max_value=300, value=80, step=1)
sg = st.selectbox('Specific Gravity', options=['1.010', '1.020', '1.030'])
al = st.selectbox('Albumin', options=['0', '1', '2', '3', '4'])
su = st.selectbox('Sugar', options=['0', '1', '2', '3'])
rbc = st.selectbox('Red Blood Cells', options=['normal', 'abnormal'])
pc = st.selectbox('Pus Cell', options=['normal', 'abnormal'])
pcc = st.selectbox('Pus Cell Clumps', options=['notpresent', 'present'])
ba = st.selectbox('Bacteria', options=['notpresent', 'present'])
bgr = st.number_input('Blood Glucose Random', min_value=0, max_value=500, value=121, step=1)
bu = st.number_input('Blood Urea', min_value=0, max_value=500, value=36, step=1)
sc = st.number_input('Serum Creatinine', min_value=0.0, max_value=10.0, value=1.2, step=0.1)
sod = st.number_input('Sodium', min_value=0, max_value=200, value=140, step=1)
pot = st.number_input('Potassium', min_value=0.0, max_value=20.0, value=4.0, step=0.1)
hemo = st.number_input('Hemoglobin', min_value=0.0, max_value=20.0, value=15.4, step=0.1)
pcv = st.number_input('Packed Cell Volume', min_value=0, max_value=100, value=44, step=1)
wbcc = st.number_input('White Blood Cell Count', min_value=0, max_value=100000, value=7800, step=1)
rbcc = st.number_input('Red Blood Cell Count', min_value=0.0, max_value=10.0, value=5.2, step=0.1)
htn = st.selectbox('Hypertension', options=['yes', 'no'])
dm = st.selectbox('Diabetes Mellitus', options=['yes', 'no'])
cad = st.selectbox('Coronary Artery Disease', options=['yes', 'no'])
appet = st.selectbox('Appetite', options=['good', 'poor'])
pe = st.selectbox('Pedal Edema', options=['yes', 'no'])
ane = st.selectbox('Anemia', options=['yes', 'no'])

# Convert categorical and binary variables to numerical format
def convert_to_numerical(value, options):
    return options.index(value) if value in options else -1

def convert_binary(value):
    return 1 if value == 'yes' else 0

# Prepare the feature vector
features = np.array([
    age,
    bp,
    float(sg),
    float(al),
    float(su),
    convert_binary(rbc),
    convert_binary(pc),
    convert_binary(pcc),
    convert_binary(ba),
    bgr,
    bu,
    sc,
    sod,
    pot,
    hemo,
    pcv,
    wbcc,
    rbcc,
    convert_binary(htn),
    convert_binary(dm),
    convert_binary(cad),
    convert_binary(appet),
    convert_binary(pe),
    convert_binary(ane)
]).reshape(1, -1)

# Make prediction
if st.button('Predict'):
    prediction = model.predict(features)
    result = 'CKD' if prediction[0] == 1 else 'Not CKD'
    st.write(f'Prediction: {result}')
