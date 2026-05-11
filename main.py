import streamlit as st
import pandas as pd

st.title("My First Streamlit App")
st.write("Hello World! This is running from VS Code.")

# Add a simple slider
number = st.slider("Select a number", 0, 100, 20)
st.write(f"You selected: {number}")

