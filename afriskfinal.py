import pandas as pd
import os
import streamlit as st
import streamlit as st
import pandas as pd
import requests
from streamlit_lottie import st_lottie
def loti(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    else:
        return r.json()

class Home:
    def __init__(self):
        self.file_path = "patient_data.xlsx"

    def save_data_to_excel(self, data):
        if os.path.exists(self.file_path):
            existing_data = pd.read_excel(self.file_path)
            updated_data = existing_data.append(data, ignore_index=True)
        else:
            updated_data = data

        updated_data.to_excel(self.file_path, index=False)

# Placeholder for storing chat history
chat_history = []

def display_analysis_image(image_path, analysis_type):
    if os.path.exists(image_path):
        st.image(image_path, caption=f"{analysis_type} Analysis")
    else:
        st.warning(f"The model failed to analyze the image/data accurately for {analysis_type}.")

def main():
      # Title and sidebar
    st.title("Patient Management System")
    lottie_url_1 = "https://assets6.lottiefiles.com/packages/lf20_olluraqu.json"
    lottie_url_patient = "https://assets6.lottiefiles.com/packages/lf20_vPnn3K.json"
    lott1 = loti(lottie_url_1)
    lotipatient = loti(lottie_url_patient)

    menu = ["Home", "Add Patient Record", "Show Patient Records", "Search and Edit Patient", "Delete Patient Record"]
    options = st.sidebar.radio("Select an Option", menu)

    if options == "Home":
        st.subheader("Welcome to Hospital Management System")
        st.write("Navigate from sidebar to access features")
        st_lottie(lott1, height=500)

    elif options == "Add Patient Record":
        st.subheader("Add New Patient Record")
        st_lottie(lotipatient, height=200)
        # Example form to add patient data (not functional without a database)
        with st.form(key='patient_form'):
            name = st.text_input("Name")
            age = st.number_input("Age", min_value=0, max_value=120)
            contact = st.text_input("Contact Number")
            email = st.text_input("Email")
            address = st.text_input("Address")
            submit_button = st.form_submit_button("Submit")

    elif options == "Show Patient Records":
        st.subheader("Patient Records")
        # Static or placeholder data for demonstration
         # Imaginary patient data for demonstration
        data = {
            "Name": ["John Doe", "Jane Smith", "Michael Johnson"],
            "Age": [42, 35, 50],
            "Gender": ["Male", "Female", "Male"],
            "BMI": [28.5, 24.9, 31.2],
            "Hypertension": ["Present", "Absent", "Present"],
            "Diabetes": ["Absent", "Present", "Absent"],
            "Cholesterol": [195, 220, 240],
            "Triglyceride": [150, 180, 160],
            "Hemogram": [13.2, 12.5, 14.1],
            "Iron": [70, 80, 65],
            "Creatinine": [1.0, 1.2, 0.9],
            "TSH": [2.5, 3.1, 2.0],
            "LV Hypertrophy": ["No", "Yes", "No"],
            "LA Dilatation": ["No", "No", "Yes"],
            "Valve Problem": ["No", "Yes", "No"],
            "RA Dilatation": ["Yes", "No", "No"],
            "PA Pressure": ["No", "Yes", "No"],
            "Ejection Fraction": ["Preserved", "Reduced", "Middle"],
        }
        df = pd.DataFrame(data)
        st.dataframe(df)
    home = Home()
    st.title("AF Risk and Health Parameters")

    # Patient Information Section
    st.header("Patient Information")
    email = st.text_input("Email")
    name = st.text_input("Firstname")
    surname = st.text_input("Lastname")
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    gender_options = ['Male', 'Female', 'Other']
    gender = st.selectbox("Gender", gender_options)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("AF Risk Parameters")
        bmi = st.number_input("Body Mass Index", min_value=0.0, max_value=100.0, step=0.1, key='bmi')
        hypertension = st.radio("Hypertension", ('Present', 'Absent'), key='hypertension')
        diabetes = st.radio("Diabetes", ('Present', 'Absent'), key='diabetes')

    with col2:
        st.subheader("Blood Parameters")
        cholesterol = st.number_input("Cholesterol", key='cholesterol')
        triglyceride = st.number_input("Triglyceride", key='triglyceride')
        hemogram = st.number_input("Hemogram", key='hemogram')
        iron = st.number_input("Iron", key='iron')
        creatinine = st.number_input("Creatinine", key='creatinine')
        tsh = st.number_input("TSH", key='tsh')

    with col3:
        st.subheader("Echo Parameters")
        lv_hypertrophy = st.radio("Left Ventricular Hypertrophy", ('Yes', 'No'), key='lv_hypertrophy')
        la_dilatation = st.radio("Left Atrial Dilatation", ('Yes', 'No'), key='la_dilatation')
        valve_problem = st.radio("Valve Problem", ('Yes', 'No'), key='valve_problem')
        ra_dilatation = st.radio("Right Atrial Dilatation", ('Yes', 'No'), key='ra_dilatation')
        pa_pressure = st.radio("Pulmonary Artery Pressure", ('Yes', 'No'), key='pa_pressure')
        ejection_fraction = st.selectbox("Ejection Fraction", ('Reduced', 'Middle', 'Preserved'), key='ejection_fraction')

    if st.button("Submit"):
        data = pd.DataFrame({
            "Email": [email], 
            "Firstname": [name],
            "Lastname": [surname],
            "Age": [age],
            "Gender": [gender],
            "BMI": [bmi],
            "Hypertension": [hypertension],
            "Diabetes": [diabetes],
            "Cholesterol": [cholesterol],
            "Triglyceride": [triglyceride],
            "Hemogram": [hemogram],
            "Iron": [iron],
            "Creatinine": [creatinine],
            "TSH": [tsh],
            "LV Hypertrophy": [lv_hypertrophy],
            "LA Dilatation": [la_dilatation],
            "Valve Problem": [valve_problem],
            "RA Dilatation": [ra_dilatation],
            "PA Pressure": [pa_pressure],
            "Ejection Fraction": [ejection_fraction]
        })
        home.save_data_to_excel(data)
        st.success("Data saved successfully!")

        # ECG Data Upload and Analysis
    st.subheader("ECG Data Upload and Analysis")
    data_type = st.radio("Select data type:", ["CSV", "Image"])

    if data_type == "CSV":
        ecg_data = st.file_uploader("Upload ECG Data (CSV)", type=['csv'])
        if ecg_data is not None:
            df_ecg = pd.read_csv(ecg_data)
            st.write(df_ecg)
    elif data_type == "Image":
        ecg_image = st.file_uploader("Upload ECG Image", type=['jpg', 'png', 'jpeg'])
        if ecg_image is not None:
            # Process and display the image here
            st.image(ecg_image, caption="Uploaded ECG Image")


    # ECG Data Analysis and Interpretation Section
    st.header("ECG Data Analysis and Interpretation")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("LIME"):
            st.write("LIME Analysis Results")
            display_analysis_image("path_to_lime_image.jpg", "LIME")

    with col2:
        if st.button("SHAP"):
            st.write("SHAP Analysis Results")
            display_analysis_image("path_to_shap_image.jpg", "SHAP")


    # Doctor-GPT Chatbot Interaction
    st.header("Doctor-AI Conversation")
    chat_input = st.text_input("Doctor: Hi, can you tell me why the model thinks the patient is at a high risk of developing AF disease?")
    if st.button("Send"):
        response = "AI: Well, based on the results and the model interpretation using LIME, it shows that the patient has several risk factors such as high BMI, hypertension, and diabetes. These factors contribute to the increased risk of AF disease."
        chat_history.append("Doctor: " + chat_input)
        chat_history.append("AI: " + response)
        for chat in chat_history:
            st.text(chat)

            # Feedback Form
    feedback = st.text_area("Feedback", "Please provide your feedback here")
    if st.button("Submit Feedback"):
        st.success("Thank you for your feedback!")


if __name__ == "__main__":
    main()
