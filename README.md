# ☀️ Solar Potential Prediction & Analytics Dashboard

## Overview
This project predicts solar energy potential using a machine learning model and presents the results through an interactive Streamlit dashboard. It demonstrates how data-driven approaches can support renewable energy planning and decision-making.

The application allows users to:
- Input environmental parameters
- Predict solar potential values
- Visualize solar irradiance across regions in India using a heatmap

---

## Key Features
- Machine learning–based solar potential prediction
- Interactive Streamlit web interface
- Dynamic input controls for temperature, humidity, and clearness index
- Geospatial heatmap visualization of solar irradiance in India
- Pre-trained model integration using a `.pkl` file

---

## Tech Stack
- Programming Language: Python  
- Libraries & Tools:
  - Pandas
  - NumPy
  - Scikit-learn
  - Streamlit
  - Joblib
  - Folium
- Visualization: Interactive heatmaps & UI components
- Model Type: Pre-trained regression model

---


---

## How the System Works
1. User inputs environmental parameters such as temperature, humidity, and clearness index.
2. The trained machine learning model processes the inputs.
3. The application predicts solar potential values.
4. A heatmap visualizes solar irradiance distribution across selected regions in India.

---

## How to Run the Application Locally

### Install Dependencies
```bash
pip install -r requirements.txt
