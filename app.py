import streamlit as st
import helper

st.title("Restaurant Menu Generator")

user_cuisine = st.sidebar.selectbox("Select Cuisine ", ("Indian", "Chinese", "Italian", "Mexican", "Thai",
                                         "Japanese","French","Caribbean","Russian","Spanish"))

if user_cuisine:
    response = helper.get_restaurant_name_and_menu_items(user_cuisine)
    st.header(response["restaurant_name"].strip())
    menu_items = response["menu_items"].strip().split(",")
    st.write("Menu Items")
    for items in menu_items:
        st.write("-",items)