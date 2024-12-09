import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from sklearn.preprocessing import StandardScaler

# This file contains the trained machine learning model
survival_model = pickle.load(open('survival_prediction_model.sav', 'rb'))
#This file contains the scaled data
scaler = pickle.load(open('scaler.sav', 'rb'))  

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Survival Prediction System',
                           ['Survival Prediction'],
                           icons=['activity'],
                           default_index=0)

# Survival Prediction Page
if (selected == 'Survival Prediction'):
    # Page title
    st.title('Survival Prediction using ML')

    # Getting the input data from the user
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        Pclass = st.selectbox('Ticket class', ['1', '2', '3'])
        
    with col2:
        Sex = st.selectbox('Sex', ['male', 'female'])
        
    with col3:
        Age = st.text_input('Age')
        
    with col4:
        Fare = st.text_input('Ticket Price in $')

    # Convert input values to appropriate data types when button is clicked
    if st.button('Survival Test Result'):
        try:
            # Convert Pclass to integer
            Pclass = int(Pclass)  

            # Convert Age to float (if the input is empty or invalid, set it to 0)
            Age = float(Age) if Age and Age.replace('.', '', 1).isdigit() else 0

            # Convert Fare to float 
            Fare = float(Fare) if Fare and Fare.replace('.', '', 1).isdigit() else 0

            # Convert Sex to numeric (1 for male, 0 for female)
            Sex = 1 if Sex == 'male' else 0

            # Prepare the input data for prediction
            input_data = [[Pclass, Sex, Age, Fare]]

            # Scale the input data using the same scaler((ensure the model receives scaled data))
            input_data_scaled = scaler.transform(input_data)
            
            # Make prediction with the model
            survival_prediction = survival_model.predict(input_data_scaled)

            # Display the result based on the prediction
            if survival_prediction[0] == 1:
                survival_diagnosis = 'The person survived'
            else:
                survival_diagnosis = 'The person did not survive'

            st.success(survival_diagnosis)

        except Exception as e:
            st.error(f"Error: {e}")
