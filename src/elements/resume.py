import streamlit as st
import streamlit.components.v1 as components

def overwrite_css(file_name):
    with open((file_name), "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

if __name__ == "__main__":
    overwrite_css("style.css")
    st.markdown("<h1 style='text-align: center;'>Lea Yeh's Resume</h1>", unsafe_allow_html=True)
    components.html("""
        <iframe id='myIframe' src='https://registry.jsonresume.org/LeaYeh' width='100%' height='1200px' frameborder='0'></iframe>
    """, height=1200)
