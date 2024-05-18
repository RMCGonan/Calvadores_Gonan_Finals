import streamlit as st
import numpy as np
import tensorflow as tf

@st.cache_resource
def load_model(filepath):
    model = tf.keras.models.load_model(filepath)
    return model

st.title("Water Quality Prediction")

model = load_model('model (1).h5')

col1, col2, col3 = st.columns(3)

with col1:
    aluminium = st.slider("Aluminium", min_value=0.0, max_value=5.0, step=0.01, format="%.5f")
    arsenic = st.slider("Arsenic", min_value=0.0, max_value=35.0, step=0.01, format="%.5f")
    barium = st.slider("Barium", min_value=0.0, max_value=3.0, step=0.01, format="%.5f")
    cadmium = st.slider("Cadmium", min_value=0.0, max_value=2.0, step=0.01, format="%.5f")

with col2:
    chloramine = st.slider("Chloramine", min_value=0.0, max_value=5.0, step=0.01, format="%.5f")
    chromium = st.slider("Chromium", min_value=0.0, max_value=1.0, step=0.01, format="%.5f")
    viruses = st.slider("Viruses", min_value=0.0, max_value=1.0, step=0.01, format="%.5f")
    nitrates = st.slider("Nitrates", min_value=0.0, max_value=15.0, step=0.01, format="%.5f")

with col3:
    perchlorate = st.slider("Perchlorate", min_value=0.0, max_value=60.0, step=0.01, format="%.5f")
    radium = st.slider("Radium", min_value=0.0, max_value=10.0, step=0.01, format="%.5f")
    silver = st.slider("Silver", min_value=0.0, max_value=1.0, step=0.01, format="%.5f")
    uranium = st.slider("Uranium", min_value=0.0, max_value=1.0, step=0.01, format="%.5f")

if st.button("Predict"):
    features = np.array([[aluminium, arsenic, barium, cadmium, chloramine, chromium, viruses, nitrates, perchlorate, radium, silver, uranium]])
    prediction = model.predict(features)
    if prediction[0] > 0.5:  
        st.success("The water is safe.")
    else:
        st.error("The water is not safe.")

page_bg = '''
<style>
[data-testid="stAppViewContainer"] {
    background: rgba(0, 0, 0, 0) url("https://images.pexels.com/photos/1533720/pexels-photo-1533720.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    color: black;
}
[data-testid="stHeader"] {
    background: rgba(0, 0, 0, 0);
}
</style>
'''

st.markdown(page_bg, unsafe_allow_html=True)
