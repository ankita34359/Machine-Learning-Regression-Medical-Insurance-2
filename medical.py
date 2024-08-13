import pandas as pd
import numpy as np
import joblib
import streamlit as st

medical_insurance_model_pkl = r'C:\Users\Lenovo\OneDrive\Desktop\Juypter_projects\medical_insurance_model.pkl'
loaded_model = joblib.load(medical_insurance_model_pkl)

st.header("Medical Insurance Application")

age=st.number_input("Enter the Age ")/75

sex=st.selectbox("Enter the Sex ", ("male", "female"))
sex_dict={"male":0, "female":1}
sex=sex_dict[sex]

bmi=st.number_input("Enter the BMI ")

smoker=st.selectbox("Enter the Smoker ", ("no", "yes"))
smoker_dict={"no":0, "yes":1}
smoker=smoker_dict[smoker]

region=st.selectbox("Enter the Region ", ("southwest", "southeast", "northwest", "northeast"))
region_dict = {
    "southwest": 0,
    "southeast": 1,
    "northwest": 2,
    "northeast": 3,
    
}

region=region_dict[region]


X_new = np.array([[age, sex, bmi, smoker, region]])

button = st.button("Submit")

if button:

    result = loaded_model.predict(X_new)
    result=np.round(result[0])

    st.info("Total charges of medical insurance : " + str(result))