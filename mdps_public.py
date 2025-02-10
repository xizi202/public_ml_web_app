import os
import pickle 
import streamlit as st 
from streamlit_option_menu import option_menu 

st.set_page_config(
    page_title="Prediction of Disease Outbreaks System",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)
working_dir = os.path.dirname(os.path.abspath(__file__))

diabetes_model=pickle.load(open(r"C:\Users\geeky\OneDrive\Documents\MDP Project\Trained Models\diabetes_model.sav",'rb'))
heart_model=pickle.load(open(r"C:\Users\geeky\OneDrive\Documents\MDP Project\Trained Models\heart_model.sav",'rb'))
parkinsons_model=pickle.load(open(r"C:\Users\geeky\OneDrive\Documents\MDP Project\Trained Models\parkinsons_model.sav",'rb'))

with st.sidebar:
    selected= option_menu('Prediction of disease outbreak system',
                          ['Diabetes Prediction','Heart Disease Prediction','Parkinsons Prediction'],
                          menu_icon='hospital-fill',icons=['activity','heart','person'],default_index=0)

if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction Using Ml')
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('No. of Preganancies')
    with col2:
        Glucose = st.text_input('Glucose level')
    with col3:
        Bloodpressure = st.text_input('B.P value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('(DPF) Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the person')

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
          user_input = [Pregnancies, Glucose, Bloodpressure, SkinThickness, Insulin, 
                  BMI, DiabetesPedigreeFunction, Age]
          user_input = [float(x) for x in user_input]
          diab_prediction = diabetes_model.predict([user_input])
          if diab_prediction[0]==1:
              diab_diagnosis = 'The person is diabetic'
          else:
             diab_diagnosis = 'The person is not diabetic'
    st.success(diab_diagnosis)

if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction Using Ml')
    col1,col2,col3 = st.columns(3)
    with col1:
        Age = st.text_input('Age of the person')
    with col2:
        Sex = st.text_input('Sex of the person')
    with col3:
        cp = st.text_input('cp of the Patient')
    with col1:
        trestbps = st.text_input('Trestbps')
    with col2:
        chol = st.text_input('(chol) Cholestoral ')
    with col3:
        fbs = st.text_input('Fbs')   
    with col1:
        restecg = st.selectbox('Restecg Value', [0, 1, 2]) 
    with col2:
        thalach = st.text_input('Thalach')
    with col3:
        exang = st.text_input('Exang Value')  

    with col1:
        oldpeak = st.text_input('oldpeak')
    with col2:
        slope = st.text_input('Value of Slope')  
    with col3:
        ca = st.text_input('Ca Value')  

    with col1:
        thal = st.text_input('Thal Value')
    
    
    heart_diagnosis = ''

    if st.button('HeartDisease Test Result'):
        user_input = [Age,Sex,cp,trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca,thal]
        user_input = [float(x) for x in user_input]
        heart_prediction = heart_model.predict([user_input])
        if heart_prediction[0]==1:
            heart_diagnosis = 'The person has heart disease'
        else:
            heart_diagnosis = 'The person does not have heart disease'
    st.success(heart_diagnosis)

if selected == 'Parkinsons Prediction':
    st.title('Parkinsons Disease Prediction Using ML')
    col1, col2, col3 = st.columns(3)
    
    with col1:
        MDVP_Fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        MDVP_Fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        MDVP_Flo = st.text_input('MDVP:Flo(Hz)')
    with col1:
        MDVP_Jitter = st.text_input('MDVP:Jitter(%)')
    with col2:
        MDVP_Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col3:
        MDVP_RAP = st.text_input('MDVP:RAP')
    with col1:
        MDVP_PPQ = st.text_input('MDVP:PPQ')
    with col2:
        Jitter_DDP = st.text_input('Jitter:DDP')
    with col3:
        MDVP_Shim = st.text_input('MDVP:Shimmer')
    with col1:
        Shimmer_db = st.text_input('MDVP:Shimmer(db)')
    with col2:
        Shimmer_APQ3 = st.text_input('Shimmer:APQ3')
    with col3:
        Shimmer_APQ5 = st.text_input('Shimmer:APQ5')
    with col1:
        MDVP_APQ = st.text_input('MDVP:APQ5')
    with col2:
        Shimmer_DDA = st.text_input('Shimmer:DDA')
    with col3:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col1:
        spread1 = st.text_input('spread1')
    with col2:
        spread2 = st.text_input('spread2')
    with col3:
        D2 = st.text_input('D2')
    with col1:
        PPE = st.text_input('PPE')
    Parkinsons_diagnosis = ''
    if st.button('Parkinsons Test Result'):
        user_input = [MDVP_Fo, MDVP_Fhi, MDVP_Flo,MDVP_Jitter,MDVP_Jitter_Abs,MDVP_RAP,MDVP_PPQ,
                  Jitter_DDP,MDVP_Shim,Shimmer_db,Shimmer_APQ3,Shimmer_APQ5,MDVP_APQ,Shimmer_DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]
        user_input = [float(x) for x in user_input]
        Parkinsons_prediction = parkinsons_model.predict([user_input])
        if Parkinsons_prediction[0]==1:
            Parkinsons_diagnosis = 'The person has Parkinsons disease'
        else:
            Parkinsons_diagnosis = 'The person does not have Parkinsons disease'
    st.success(Parkinsons_diagnosis)
