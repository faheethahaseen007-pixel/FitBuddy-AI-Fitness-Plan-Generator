import streamlit as st

# Set page configuration
st.set_page_config(page_title="Fit Buddy", page_icon="🏋️")

# App Title & Description
st.title("🏋️ Fit Buddy - AI Fitness Plan Generator")
st.write("Welcome to Fit Buddy! Get your personalized workout plan below.")

# User Input Form
st.header("Enter Your Details")
age = st.number_input("Age", min_value=10, max_value=100, value=25)
goal = st.selectbox("Fitness Goal", ["Weight Loss", "Muscle Gain", "Endurance"])
intensity = st.select_slider("Workout Intensity", options=["Low", "Medium", "High"])

# Action Button
if st.button("Generate Workout Plan"):
    st.success(f"Generated a {intensity} intensity {goal} plan for a {age}-year-old!")
