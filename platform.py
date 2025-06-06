import streamlit as st
from PIL import Image
import os

def home_page():
  st.write("this is home page")

def pinworm_detail_page():
  st.write("this is page detail")

st.sidebar.image(image, use_container_width=True)
st.sidebar.markdown("<div class='sidebar-title'>Platform Navigation</div>", unsafe_allow_html=True)
    
pages = {
    "Home": home_page,
    "Pinworm Detail": pinworm_detail_page,
    }

selected_page = st.sidebar.selectbox("Select a page", list(pages.keys()))
pages[selected_page]()



