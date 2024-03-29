import streamlit as st
import pickle
import pandas as pd
import numpy as np


# Load the model and data (replace 'pipe.pkl' and 'home.pkl' with your actual file names)
pipe = pickle.load(open('pipe.pkl', 'rb'))
home = pd.read_pickle('home.pkl')

st.title('HomeValueXpert')

# City
city = st.selectbox('City', home['City'].unique())

# Address
#location = st.selectbox('Address', home['Address'].unique())

# Area
area = st.number_input('Area', min_value=2.5)

# Floor
floors = st.number_input('No. of Floors', min_value=1.0)

# Bedroom
bedroom = st.number_input('No. of Bedrooms', min_value=1)

# Bathroom
bathroom = st.number_input('No. of Bathrooms', min_value=1)

if st.button('Predict Price'):

    # Prepare the input data for prediction
    input_data = {
        'City': city,
        #'Address': location,
        'Area': area,
        'Floors': floors,
        'Bedroom': bedroom,
        'Bathroom': bathroom
    }
# Transform the input data (you may need to apply preprocessing)
    input_features = pd.DataFrame(input_data, index=[0])

    # Make a prediction using the loaded model
    predicted_price = pipe.predict(input_features)

    st.write(f'Predicted Price:{predicted_price[0]:,.2f} Cr')