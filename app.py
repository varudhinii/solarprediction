import streamlit as st
import joblib
import numpy as np
import pandas as pd
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium

# Load the trained model
model = joblib.load("solar_model_compatible.pkl")

# App title
st.title("☀️ Solar Potential Prediction")

# Create tabs
tab1, tab2 = st.tabs(["🔢 Prediction", "🗺️ Heatmap"])

# -----------------------------
# TAB 1: Prediction
# -----------------------------
with tab1:
    st.header("Predict Solar Potential")

    # Input fields
    temperature = st.number_input("Temperature (°C)", value=25.0)
    humidity = st.number_input("Humidity (%)", value=50.0)
    clearness_index = st.number_input("Clearness Index", value=0.7)

    # Predict button
    if st.button("Predict"):
        X_input = np.array([[temperature, humidity, clearness_index]])
        prediction = model.predict(X_input)
        st.success(f"🌞 Predicted Solar Potential: **{prediction[0]:.2f}**")

# -----------------------------
# TAB 2: Heatmap
# -----------------------------
with tab2:
    st.header("India Solar Irradiance Heatmap")

    try:
        # Load dataset
        grid_df = pd.read_csv("grid_data.csv")

        # Create map
        m = folium.Map(location=[16, 79], zoom_start=6, tiles='CartoDB positron')

        # Prepare heat data
        heat_data = [[row['Latitude'], row['Longitude'], row['Predicted_Irradiance']]
                     for _, row in grid_df.iterrows()]

        # Add heatmap
        HeatMap(heat_data, radius=12, blur=15, max_zoom=6).add_to(m)

        # Display map
        st_folium(m, width=700, height=500)

    except FileNotFoundError:
        st.error("⚠️ 'grid_data.csv' not found. Please make sure it's in the same folder as app.py.")