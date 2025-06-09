import streamlit as st
from PIL import Image
import os

def home_page():
  st.write("this is home page")
  st.markdown('<h2 style="text-align:center;">Platform for parasitic egg detection</h2>',unsafe_allow_html=True)
  

def parasite_detail_page():
  
  st.write("this is page detail")
  st.sidebar.title("Table of Content")
  st.sidebar.markdown("""
  - [Ascaris lumbricoides](#ascaris-lumbricoides)
  - [Hymenolepsis nana](#hymenolepsis-nana)
  - [Hymenolepsis diminuta](#hymenolepsis-diminuta)
  - [Tenia spp.](#tenia-spp.)
  - [Trichuris trichiura](#trichuris-trichiura)
  - [Hookworm](#hookworm)
  - [Opisthorchis viverrini](#opisthorchis-viverrini)
  - [Minute intestinal flukes](#minute-intestinal-flukes)
""")
  
  
  st.header("Ascaris lumbricoides")
  st.subheader("Geographical Distribution")
  st.write("""
  Ascaris lumbricoides, a common human roundworm, is found globally but is most prevalent in tropical and subtropical regions.
  """)
  st.header("Morphology")
  
# row1
item1,item2 = st.columns(2)

with item1:
    item1.markdown('<h4 style="text-align:center;">Fertilized eggs</h4',unsafe_allow_html=True)
    item1.write("The fertilized eggs are laid by females after inseminated by mating with a male. These are embryonated and develop into the infective eggs.")

with item2:
    item2.markdown('<h4 style="text-align:center;">Unfertilized Eggs</h4',unsafe_allow_html=True)
    item2.write("The unfertilized eggs are laid by uninseminated female. Thes are non-embryonated and cannot become infective.")

  

  
  


 


def ai_detector_page():
  st.write("this is page ai detector")

def quiz_page():
  st.write("this is page quiz")


st.sidebar.markdown("<div class='sidebar-title'>Platform Navigation</div>", unsafe_allow_html=True)
    
pages = {
    "Home": home_page,
    "Parasite egg Detail": parasite_detail_page,
    "Ai Detector": ai_detector_page,
    "Quiz": quiz_page,
    }

selected_page = st.sidebar.selectbox("Select a page", list(pages.keys()))
pages[selected_page]()



