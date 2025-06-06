import streamlit as st
from PIL import Image
import os

def home_page():
  st.write("this is home page")

def parasite_detail_page():
  st.write("this is page detail")


def ai_detector_page():
  st.write("this is page ai detector")

st.sidebar.markdown("<div class='sidebar-title'>Platform Navigation</div>", unsafe_allow_html=True)
    
pages = {
    "Home": home_page,
    "Parasite egg Detail": parasite_detail_page,
    "Ai Detector": ai_detector_page,
    }

selected_page = st.sidebar.selectbox("Select a page", list(pages.keys()))
pages[selected_page]()



