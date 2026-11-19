import streamlit as st

st.title("Sim App")
st.write("Hello Dennis! This is your first app.")

name = st.text_input("What is your name?")
if name:
    st.success(f"Welcome, {name}!")
