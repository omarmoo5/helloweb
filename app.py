import streamlit as st

def run_python_code():
    # Your Python code goes here
    st.write("Hello, Streamlit!")

st.button("Run Python Code", on_click=run_python_code)
