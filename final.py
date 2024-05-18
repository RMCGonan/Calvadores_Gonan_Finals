import streamlit as st
import numpy as np
import tensorflow as tf

# Load the trained model
def load_model():
    model = tf.keras.models.load_model('C:/Users/robvi/Downloads/streamlit/model.h5')
    return model

# Title of the Streamlit app
st.title("Water Quality Prediction")

# Description
st.write("Enter the values for the following parameters to predict if the water is safe:")

# Load the model
model = load_model()

# Input fields for the parameters
aluminium = st.number_input("Aluminium", min_value=0.0, format="%.5f")
arsenic = st.number_input("Arsenic", min_value=0.0, format="%.5f")
barium = st.number_input("Barium", min_value=0.0, format="%.5f")
cadmium = st.number_input("Cadmium", min_value=0.0, format="%.5f")
chloramine = st.number_input("Chloramine", min_value=0.0, format="%.5f")
chromium = st.number_input("Chromium", min_value=0.0, format="%.5f")
viruses = st.number_input("Viruses", min_value=0.0, format="%.5f")
nitrates = st.number_input("Nitrates", min_value=0.0, format="%.5f")
perchlorate = st.number_input("Perchlorate", min_value=0.0, format="%.5f")
radium = st.number_input("Radium", min_value=0.0, format="%.5f")
silver = st.number_input("Silver", min_value=0.0, format="%.5f")
uranium = st.number_input("Uranium", min_value=0.0, format="%.5f")

# Predict button
if st.button("Predict"):
    # Prepare the feature vector
    features = np.array([[aluminium, arsenic, barium, cadmium, chloramine, chromium, viruses, nitrates, perchlorate, radium, silver, uranium]])
    
    # Predict
    prediction = model.predict(features)
    
    # Display the result
    if prediction[0] == 1:
        st.success("The water is safe.")
    else:
        st.error("The water is not safe.")
