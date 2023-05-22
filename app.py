import streamlit as st
import flwr as fl

def run_python_code():
    st.write(fl.server.strategy.__all__)
    # Your Python code goes here
    st.write("Hello, Streamlit!")

st.button("Run Python Code", on_click=run_python_code)
