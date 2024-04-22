import streamlit as st

def create_sidebar():
    with st.sidebar:
        st.title("Configuration")
        add_radio = st.radio(
            "Choose a shipping method",
            ("Standard (5-15 days)", "Express (2-5 days)")
        )
    return add_radio  # You can return values to use in the main script if needed