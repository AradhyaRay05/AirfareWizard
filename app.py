import streamlit as st
import pandas as pd
import numpy as np
import catboost
import pickle 
try:
    with open('model.pkl', 'rb') as f:
        catboost_model = pickle.load(f)
except FileNotFoundError:
    st.error("Error: model.pkl not found.")
except Exception as e:
    st.error(f"Error loading the model: {e}")
st.title("Flight Price Prediction")
st.write("Enter the flight details to predict the price.")
airline = st.selectbox("Airline", ['IndiGo', 'Air India', 'Jet Airways', 'SpiceJet',
       'Multiple carriers', 'GoAir', 'Vistara', 'Air Asia',
       'Vistara Premium economy', 'Jet Airways Business',
       'Multiple carriers Premium economy', 'Trujet'])
date_of_journey = st.date_input("Date of Journey")
source = st.selectbox("Source", ['Banglore', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai'])
destination = st.selectbox("Destination", ['New Delhi', 'Banglore', 'Cochin', 'Kolkata', 'Delhi', 'Hyderabad'])
dep_hour = st.slider("Departure Hour", 0, 23, 0)
dep_min = st.slider("Departure Minute", 0, 59, 0)
arrival_hour = st.slider("Arrival Hour", 0, 23, 0)
arrival_min = st.slider("Arrival Minute", 0, 59, 0)
duration_hours = st.slider("Duration Hours", min_value=0, value=0) 
duration_mins = st.slider("Duration Minutes", min_value=0, value=0)


total_stops = st.selectbox("Total Stops", ['non-stop', '1 stop', '2 stops', '3 stops', '4 stops'])
additional_info = st.selectbox("Additional Info", ['No info', 'In-flight meal not included', 'No check-in baggage included',
       '1 Short layover', '1 Long layover', 'Change of airports',
       'Business class', 'Red-eye flight', '2 Long layover'])
if st.button("Predict Price"):
    try:
        journey_day = date_of_journey.day
        journey_month = date_of_journey.month
        input_data = {
            'Total_Stops': 0,
            'Journy_Day': journey_day,
            'Journy_Month': journey_month,
            'Dep_hour': dep_hour,
            'Dep_min': dep_min,
            'Arrival_hour': arrival_hour,
            'Arrival_min': arrival_min,
            'Duration_hours': duration_hours,
            'Duration_mins': duration_mins,
            'Airline_Air India': 0, 'Airline_GoAir': 0, 'Airline_IndiGo': 0,
            'Airline_Jet Airways': 0, 'Airline_Jet Airways Business': 0,
            'Airline_Multiple carriers': 0, 'Airline_Multiple carriers Premium economy': 0,
            'Airline_SpiceJet': 0, 'Airline_Trujet': 0, 'Airline_Vistara': 0,
            'Airline_Vistara Premium economy': 0, 'Source_Chennai': 0, 'Source_Delhi': 0,
            'Source_Kolkata': 0, 'Source_Mumbai': 0, 'Destination_Cochin': 0,
            'Destination_Delhi': 0, 'Destination_Hyderabad': 0, 'Destination_Kolkata': 0,
            'Destination_New Delhi': 0
        }
        if f'Airline_{airline}' in input_data:
            input_data[f'Airline_{airline}'] = 1
        if f'Source_{source}' in input_data:
            input_data[f'Source_{source}'] = 1
        if destination == 'New Delhi':
             input_data['Destination_New Delhi'] = 1
        elif f'Destination_{destination}' in input_data:
            input_data[f'Destination_{destination}'] = 1

        stop_mapping = {"non-stop": 0, "1 stop": 1, "2 stops": 2, "3 stops": 3, "4 stops": 4}
        input_data['Total_Stops'] = stop_mapping.get(total_stops, 0)
        input_df = pd.DataFrame([input_data])
        train_cols = ['Total_Stops', 'Journy_Day', 'Journy_Month', 'Dep_hour', 'Dep_min',
                      'Arrival_hour', 'Arrival_min', 'Duration_hours', 'Duration_mins',
                      'Airline_Air India', 'Airline_GoAir', 'Airline_IndiGo',
                      'Airline_Jet Airways', 'Airline_Jet Airways Business',
                      'Airline_Multiple carriers', 'Airline_Multiple carriers Premium economy',
                      'Airline_SpiceJet', 'Airline_Trujet', 'Airline_Vistara',
                      'Airline_Vistara Premium economy', 'Source_Chennai', 'Source_Delhi',
                      'Source_Kolkata', 'Source_Mumbai', 'Destination_Cochin',
                      'Destination_Delhi', 'Destination_Hyderabad', 'Destination_Kolkata',
                      'Destination_New Delhi']
        input_df = input_df.reindex(columns=train_cols, fill_value=0)
        prediction = catboost_model.predict(input_df)
        st.success(f"Predicted Flight Price: ₹{prediction[0]:.2f}")
    except ValueError as ve:
        st.error(f"Input Error: {ve}")
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")