import streamlit as st
import helper

st.title("Car Model Selector")

# Input fields for car type and get models button
car_type = st.sidebar.radio("Select Car Type", ("Two Wheeler", "Four Wheeler"))
get_models_button = st.sidebar.button("Get Car Models")

# Dropdown for car company name
car_company_name = st.sidebar.selectbox("Select Car Company Name", (
    "Toyota", "Honda", "Ford", "Chevrolet", "BMW", "Mercedes", "Volkswagen", "Audi", "Nissan", "Hyundai", "Tesla"
))

if get_models_button:
    response = helper.get_car_models_and_colors(car_company_name, car_type)
    car_models = response["car_models"].strip().split(",")
    
    st.header(f"Top 10 {car_type} Models for {car_company_name}")
    
    if not car_models:
        st.write("No cars available for the selected criteria. Please try again.\n")
    else:
        st.header("Car Models")
        for model in car_models:
            st.write("", model)
        print("\n")
