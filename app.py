import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


try:
    model = pickle.load(open('model.pkl', 'rb'))
    scaler = pickle.load(open('scaler.pkl', 'rb'))
except FileNotFoundError:
    st.error("Error: model.pkl or scaler.pkl not found. Please make sure these files are in the same directory.")
    st.stop()


st.title("Flight Price Prediction")

st.write("""
This application predicts the price of a flight based on various features.
Please enter the flight details below:
""")

# Create input fields for the features
total_stops = st.selectbox("Total Stops", [0, 1, 2, 3, 4], format_func=lambda x: {0: 'non-stop', 1: '1 stop', 2: '2 stops', 3: '3 stops', 4: '4 stops'}.get(x))
journey_day = st.slider("Journey Day", 1, 31, 1)
journey_month = st.slider("Journey Month", 1, 12, 1)
dep_hour = st.slider("Departure Hour", 0, 23, 0)
dep_min = st.slider("Departure Minute", 0, 59, 0)
arrival_hour = st.slider("Arrival Hour", 0, 23, 0)
arrival_min = st.slider("Arrival Minute", 0, 59, 0)
duration_hours = st.slider("Duration Hours", min_value=0, value=0)
duration_mins = st.slider("Duration Minutes", min_value=0, value=0)
airline = st.selectbox("Airline", ['IndiGo', 'Air India', 'Jet Airways', 'SpiceJet', 'Multiple carriers', 'GoAir', 'Vistara', 'Air Asia', 'Vistara Premium economy', 'Jet Airways Business', 'Multiple carriers Premium economy', 'Trujet'])
source = st.selectbox("Source", ['Banglore', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai'])
destination = st.selectbox("Destination", ['New Delhi', 'Banglore', 'Cochin', 'Kolkata', 'Delhi', 'Hyderabad'])


if st.button("Predict Price"):
  
    input_data = pd.DataFrame({
        'Total_Stops': [total_stops],
        'Journy_Day': [journey_day],
        'Journy_Month': [journey_month],
        'Dep_hour': [dep_hour],
        'Dep_min': [dep_min],
        'Arrival_hour': [arrival_hour],
        'Arrival_min': [arrival_min],
        'Duration_hours': [duration_hours],
        'Duration_mins': [duration_mins],
        'Airline': [airline],
        'Source': [source],
        'Destination': [destination]
    })

    airline_encoded = pd.get_dummies(input_data['Airline'], prefix='Airline', drop_first=True)
    source_encoded = pd.get_dummies(input_data['Source'], prefix='Source', drop_first=True)
    destination_encoded = pd.get_dummies(input_data['Destination'], prefix='Destination', drop_first=True)

    input_data_processed = pd.concat([
        input_data[['Total_Stops', 'Journy_Day', 'Journy_Month', 'Dep_hour', 'Dep_min', 'Arrival_hour', 'Arrival_min', 'Duration_hours', 'Duration_mins']],
        airline_encoded,
        source_encoded,
        destination_encoded
    ], axis=1)

    expected_columns = ['Total_Stops', 'Journy_Day', 'Journy_Month', 'Dep_hour', 'Dep_min', 'Arrival_hour',
                      'Duration_hours', 'Duration_mins', 'Airline_Air India', 'Airline_GoAir', 'Airline_IndiGo',
                      'Airline_Jet Airways', 'Airline_Jet Airways Business', 'Airline_Multiple carriers',
                      'Airline_Multiple carriers Premium economy', 'Airline_SpiceJet', 'Airline_Trujet',
                      'Airline_Vistara', 'Airline_Vistara Premium economy', 'Source_Chennai', 'Source_Delhi', 'Source_Kolkata',
                      'Source_Mumbai', 'Destination_Cochin', 'Destination_Delhi', 'Destination_Hyderabad', 'Destination_Kolkata',
                      'Destination_New Delhi']

    for col in expected_columns:
        if col not in input_data_processed.columns:
            input_data_processed[col] = 0

    # Reorder columns to match training data
    input_data_processed = input_data_processed[expected_columns]

    # Scale the input data
    input_data_scaled = scaler.transform(input_data_processed)

    # Predict the price
    predicted_price = model.predict(input_data_scaled)
    st.write(f"Predicted Flight Price: ₹ {predicted_price[0]:.2f}")