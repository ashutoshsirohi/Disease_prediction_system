import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# set page configuration 
st.set_page_config(page_title="Health Guard",layout="wide")

#path of working directory
working_dir = os.path.dirname(os.path.abspath(__file__))

#loading of the saved models
diabete_model = pickle.load(open('diabete_model.sav','rb'))
heart_model = pickle.load(open('heart_disease_model.sav','rb'))

#sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',['Diabetes Prediction','Heart Disease Prediction'],menu_icon='hospital-fill',icons=['activity','heart','person'],default_index=0)

#Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    #page title
    st.title("Diabetes Prediction User Interface Using ML")     

    #getting ipnut data from the user
    col1,col2,col3=st.columns(3)

    with col1:
        pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        glucose= st.text_input('Glucose Level')

    with col3:
        bloodpressure = st.text_input('Blood Pressure Value') 
        
    with col1:
        skinthickness = st.text_input('Skin Thickness Value')
    
    with col2:
        insuline= st.text_input('Insulin Level')

    with col3:
        bmi = st.text_input('BMI Value')

    with col1:
        dfv= st.text_input('Diabetes Prediction Function Value')

    with col2:
        age = st.text_input('Age of the Person') 

    # backend logic
    diab_diagnosis = ''

    #creation of a button
    if st.button('Diabeties Test Result'):

        input=[pregnancies,glucose,bloodpressure,skinthickness,insuline,bmi,dfv,age]

        input=[float(x) for x in input]

        diab_prediction = diabete_model.predict([input])

        if diab_prediction[0] ==1:
            diab_diagnosis= 'The person is diabetic'
        else:
            diab_diagnosis= 'The person is not diabetic'

    st.success(diab_diagnosis)




#Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    #page title
    st.title("Heart Disease Prediction User Interface Using ML")     

    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        age = col1.slider('Age', 0, 100, 50)

    with col2:
        sex = col2.radio('Sex', ['Male', 'Female'])

    with col3:
        cp = col3.selectbox('Chest Pain types', ['Type 1', 'Type 2', 'Type 3', 'Type 4'])

    with col1:
        trestbps = col1.slider('Resting Blood Pressure', 0, 200, 120)

    with col2:
        chol = col2.slider('Serum Cholestoral in mg/dl', 100, 600, 200)

    with col3:
        fbs = col3.radio('Fasting Blood Sugar > 120 mg/dl', ['Yes', 'No'])

    with col1:
        restecg = col1.radio('Resting Electrocardiographic results', ['Normal', 'Abnormal'])

    with col2:
        thalach = col2.slider('Maximum Heart Rate achieved', 50, 220, 150)

    with col3:
        exang = col3.radio('Exercise Induced Angina', ['Yes', 'No'])

    with col1:
        oldpeak = col1.slider('ST depression induced by exercise', 0.0, 10.0, 1.0)

    with col2:
        slope = col2.selectbox('Slope of the peak exercise ST segment', ['Upsloping', 'Flat', 'Downsloping'])

    with col3:
        ca = col3.slider('Major vessels colored by fluoroscopy', 0, 4, 0)

    with col1:
        thal = col1.selectbox('Thalassemia', ['Normal', 'Fixed Defect', 'Reversable Defect'])

    # Convert categorical variables to numeric values
    sex_numeric = 1 if sex == 'Male' else 0
    fbs_numeric = 1 if fbs == 'Yes' else 0
    exang_numeric = 1 if exang == 'Yes' else 0
    restecg_numeric = 1 if restecg == 'Abnormal' else 0
    slope_numeric = {'Upsloping': 1, 'Flat': 2, 'Downsloping': 3}.get(slope, 0)
    thal_numeric = {'Normal': 1, 'Fixed Defect': 2, 'Reversable Defect': 3}.get(thal, 0)
    cp_numeric = {'Type 1': 1, 'Type 2': 2, 'Type 3': 3, 'Type 4': 4}.get(cp, 0)  # Added conversion for cp

    # Backend logics
    Heart_diagnosis = ''

    # Creation of a button
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex_numeric, cp_numeric, trestbps, chol, fbs_numeric, restecg_numeric, thalach, exang_numeric, oldpeak, slope_numeric, ca, thal_numeric]
        Heart_Prediction = heart_model.predict([user_input])
        Heart_diagnosis = 'The person is having Heart disease' if Heart_Prediction[0] == 1 else 'The person does not have any heart disease'
        st.success(Heart_diagnosis)


                


