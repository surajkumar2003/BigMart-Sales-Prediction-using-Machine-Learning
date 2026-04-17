import streamlit as st
import requests

st.title("Big Mart Sales Prediction")

item_weight = st.number_input("Enter Item Weight")

item_fat_content = st.selectbox(
    "Item Fat Content",
    options=[("Low Fat", 1), ("Regular", 2), ("High Fat", 0)],
    format_func=lambda x: x[0]
)[1]

item_visibility = st.number_input("Enter Item Visibility")

item_type = st.selectbox(
    "Item Type",
    options=[
        ("Baking Goods",0),("Breads",1),("Breakfast",2),("Canned",3),
        ("Dairy",4),("Frozen Foods",5),("Fruits and Vegetables",6),
        ("Hard Drinks",7),("Health and Hygiene",8),("Household",9),
        ("Meat",10),("Others",11),("Seafood",12),
        ("Snack Foods",13),("Soft Drinks",14),("Starchy Foods",15)
    ],
    format_func=lambda x: x[0]
)[1]

item_mrp = st.number_input("Enter Item MRP")

outlet_year = st.number_input("Outlet Establishment Year")

outlet_size = st.selectbox(
    "Outlet Size",
    options=[("High",0),("Medium",1),("Small",2)],
    format_func=lambda x: x[0]
)[1]

outlet_location_type = st.selectbox(
    "Outlet Location Type",
    options=[("Tier 1",0),("Tier 2",1),("Tier 3",2)],
    format_func=lambda x: x[0]
)[1]

outlet_type = st.selectbox(
    "Outlet Type",
    options=[
        ("Grocery Store",0),
        ("Supermarket Type1",1),
        ("Supermarket Type2",2),
        ("Supermarket Type3",3)
    ],
    format_func=lambda x: x[0]
)[1]

if st.button("Predict"):

    data = {
        "item_weight": item_weight,
        "item_fat_content": item_fat_content,
        "item_visibility": item_visibility,
        "item_type": item_type,
        "item_mrp": item_mrp,
        "outlet_establishment_year": outlet_year,
        "outlet_size": outlet_size,
        "outlet_location_type": outlet_location_type,
        "outlet_type": outlet_type
    }

    response = requests.post("http://127.0.0.1:5000/predict", json=data)

    result = response.json()

    st.success(f"Prediction: {result['prediction']}")