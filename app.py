import streamlit as st
import pandas as pd
import sys
import os

# Get the absolute path to the parent directory (works for Streamlit too)
app_dir = os.path.dirname(os.path.abspath(__file__)) if "__file__" in globals() else os.getcwd()
sys.path.append(os.path.abspath(os.path.join(app_dir, '..')))
import joblib
from scripts.utils_optimize import solve_best_route

st.set_page_config("Smart Route Planner", layout="wide")

st.title(" Smart Route Planner Dashboard")

menu = st.sidebar.radio("Navigation", ["Overview", "Predict Delay", "Route Optimization"])


if menu == "Overview":
    st.subheader(" Data Overview")
    df = pd.read_csv("data/orders.csv")
    

    # Create route column if missing
    
    df["route"] = df["Origin"] + " → " + df["Destination"]

    st.dataframe(df.head())
    st.metric("Total Orders", len(df))

    st.dataframe(df.head())
    st.metric("Total Orders", len(df))
    st.metric("Unique Routes", df['route'].nunique())

elif menu == "Predict Delay":
    st.subheader("Predict Delivery Delay")
    model = joblib.load("models/delay_predictor.pkl")

    distance = st.number_input("Distance (km)", 0.0)
    toll = st.number_input("Toll Charge (₹)", 0.0)
    traffic = st.slider("Traffic Delay (minutes)", 0, 120)
    weather = st.slider("Weather Impact (0-10)", 0, 10)
    priority = st.selectbox("Priority", ["Express", "Standard", "Economy"])

    input_data = pd.DataFrame([{
        "distance_km": distance,
        "toll_charge": toll,
        "traffic_delay": traffic,
        "weather_impact": weather,
        "priority": priority
    }])
    prediction = model.predict(input_data)[0]
    st.success("✅ On-time Delivery Expected" if prediction == 0 else "⚠️ Delay Expected")

elif menu == "Route Optimization":
    st.subheader(" Optimize Routes")
    if st.button("Find Optimal Route"):
        route, total = solve_best_route()
        st.write("Best Route:", route)
        st.metric("Total Distance", f"{total} km")