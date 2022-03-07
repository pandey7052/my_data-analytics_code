import streamlit as st

st.title("My Streamlit App")
st.header("This is a Header")
st.subheader("a subheader")
st.text("small text")

name =st.text_input("enter your name")
agree =st.checkbox("DO you Agree?")
btn =st.button("Click to fly!!")

sidebar =st.sidebar

sidebar.title("sidebar title")
age = sidebar.text_input("Enter your age:")
btn2 = sidebar.button("its magic")

if btn2:
    st.balloons()