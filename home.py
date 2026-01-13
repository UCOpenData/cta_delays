import streamlit as st
from sidebar import init_sidebar

st.set_page_config(page_title="CTA Delays Analysis App", layout="wide")

st.title("Welcome to our CTA delays analysis app!")
st.write("Use the sidebar to navigate to different pages.")

init_sidebar()