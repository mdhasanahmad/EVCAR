# -*- coding: utf-8 -*-
"""
Created on Thu May 23 19:21:11 2024

@author: DCL
"""


import numpy as np
import pickle
import streamlit as st


# Load the model
loaded_model = pickle.load(open('D:/New folder/Evcar_acceptance.sav', 'rb'))

# creating a function for Prediction

def EVCAR_PREDICTION(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return ' PEOPLE WILL BUY EVCAR'
    else:
      return 'PEOPLE WILL BUY GASOLINE CAR'
  
    
  
def main():
    
    
    # giving a title
    st.title('EVcar_acceptance_prediction_by_2035')
    
    
    # getting the input data from the user
    
    
    Gender = st.text_input('Gender Type')
    Country = st.text_input('Country you live in')
    profession= st.text_input(' What is your profession?')
    Age = st.text_input('How old are you?')
    sustainable = st.text_input('How do you perceive sustainable mobility, particularly in relation to Electric Vehicles (EVs)?')
    factors = st.text_input('What factors influence your perception of eco-friendly transportation, with a focus on electric vehicles?')
    aware = st.text_input('Are you aware of the environmental impact of electric vehicles compared to traditional gasoline-powered cars?')
    perceive = st.text_input('What do you perceive as the potential environmental effects of a large-scale adoption of electric vehicles?')
    switching = st.text_input('How do you think switching to environmentally friendly transport methods, such as electric vehicles, would impact your personal finances?How do you think switching to environmentally friendly transport methods, such as electric vehicles, would impact your personal finances?')
    laws = st.text_input('Do you believe government laws and incentives play a significant role in encouraging the adoption of electric vehicles?')
    purchasing = st.text_input('How likely are you to consider purchasing an electric vehicle for your next vehicle?')
    influence = st.text_input('What factors would most influence your decision to purchase an electric vehicle?What factors would most influence your decision to purchase an electric vehicle?')
    prefer = st.text_input('Would you prefer to use Electric Cars, if roadside charging infrastructures are available in the road?')
    price= st.text_input('Do you think gasoline price will impact on using EV cars by 2035?')
    
    
    
    # code for Prediction
    acceptance = ''
    
    # creating a button for Prediction
    
    if st.button('ACCEPTANCE Test Result'):
        acceptance = EVCAR_PREDICTION([Gender, Country, profession, Age, sustainable,factors, aware, perceive,switching,laws,purchasing,influence,prefer,price])
        
        
    st.success(acceptance)
    
    
    
    
    
if __name__ == '__main__':
    main()
    