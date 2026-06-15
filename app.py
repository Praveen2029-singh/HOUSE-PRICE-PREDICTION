import streamlit as st
import pickle
import numpy as np

# Load model
with open('../Model/house_price_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.set_page_config(page_title="House Price Prediction", page_icon="🏠")
st.title("🏠 House Price Prediction System")
st.write("Enter the property details below to estimate the house price.")

col1, col2 = st.columns(2)

with col1:
    area = st.number_input("Area (sq ft)", min_value=100, value=2000)
    bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3)
    bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)
    stories = st.number_input("Stories", min_value=1, max_value=5, value=2)
    parking = st.number_input("Parking Spaces", min_value=0, max_value=5, value=1)
    furnishingstatus = st.selectbox(
        "Furnishing Status", ["Unfurnished", "Semi-Furnished", "Furnished"]
    )

with col2:
    mainroad = st.selectbox("Main Road Access", ["Yes", "No"])
    guestroom = st.selectbox("Guest Room", ["Yes", "No"])
    basement = st.selectbox("Basement", ["Yes", "No"])
    hotwaterheating = st.selectbox("Hot Water Heating", ["Yes", "No"])
    airconditioning = st.selectbox("Air Conditioning", ["Yes", "No"])
    prefarea = st.selectbox("Preferred Area", ["Yes", "No"])

def encode_yn(val):
    return 1 if val == "Yes" else 0

furnish_map = {"Unfurnished": 0, "Semi-Furnished": 1, "Furnished": 2}

if st.button("🔍 Predict Price"):
    total_rooms = bedrooms + bathrooms

    # Order must EXACTLY match the X columns used in training (Cell 10):
    # area, bedrooms, bathrooms, stories, mainroad, guestroom, basement,
    # hotwaterheating, airconditioning, parking, prefarea, furnishingstatus, total_rooms
    features = np.array([[
        area, bedrooms, bathrooms, stories,
        encode_yn(mainroad), encode_yn(guestroom), encode_yn(basement),
        encode_yn(hotwaterheating), encode_yn(airconditioning), parking,
        encode_yn(prefarea), furnish_map[furnishingstatus], total_rooms
    ]])

    prediction = model.predict(features)[0]
    st.success(f"🏷️ Estimated House Price: ₹ {prediction:,.2f}")