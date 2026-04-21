import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("models/lr.save")
scaler = joblib.load("models/sc.save")

st.title("Big Mart Sales Prediction")

item_weight = st.number_input("Item Weight")

item_fat_content = st.selectbox(
    "Item Fat Content",
    [("Low Fat",1),("Regular",2),("High Fat",0)],
    format_func=lambda x: x[0]
)[1]

item_visibility = st.number_input("Item Visibility")

item_type = st.selectbox(
    "Item Type",
    [
        ("Baking Goods",0),("Breads",1),("Breakfast",2),
        ("Canned",3),("Dairy",4),("Frozen Foods",5),
        ("Fruits and Vegetables",6),("Hard Drinks",7),
        ("Health and Hygiene",8),("Household",9),
        ("Meat",10),("Others",11),("Seafood",12),
        ("Snack Foods",13),("Soft Drinks",14),("Starchy Foods",15)
    ],
    format_func=lambda x: x[0]
)[1]

item_mrp = st.number_input("Item MRP")
outlet_year = st.number_input("Outlet Establishment Year")

outlet_size = st.selectbox(
    "Outlet Size",
    [("High",0),("Medium",1),("Small",2)],
    format_func=lambda x: x[0]
)[1]

outlet_location_type = st.selectbox(
    "Outlet Location Type",
    [("Tier 1",0),("Tier 2",1),("Tier 3",2)],
    format_func=lambda x: x[0]
)[1]

outlet_type = st.selectbox(
    "Outlet Type",
    [
        ("Grocery Store",0),
        ("Supermarket Type1",1),
        ("Supermarket Type2",2),
        ("Supermarket Type3",3)
    ],
    format_func=lambda x: x[0]
)[1]

if st.button("Predict"):

    X = np.array([[item_weight,item_fat_content,item_visibility,
                   item_type,item_mrp,outlet_year,
                   outlet_size,outlet_location_type,outlet_type]])

    X_scaled = scaler.transform(X)
    pred = model.predict(X_scaled)

    st.success(f"Predicted Sales: {pred[0]:.2f}")