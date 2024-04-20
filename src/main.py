import requests
import streamlit as st
import streamlit.components.v1 as components


# Custom CSS to adjust iframe borders, etc.
st.markdown(
    """
    <style>
    iframe {
        border: 0px solid #f0f2f6;
        border-radius: 0px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Embedding the website
components.html(
    f"<iframe src='https://registry.jsonresume.org/LeaYeh' width='100%' height='800'></iframe>",
    height=800
)
