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
#----------------------------------------------------------------------------------------------------------------------------------------
  
#ascaris---------------------------------------------------------------------------------------------------------------------------------
  st.header("1.Ascaris lumbricoides")
  st.subheader("Geographical Distribution")
  st.write("""
  Ascaris lumbricoides, a common human roundworm, is found globally but is most prevalent in tropical and subtropical regions.
  """)
  st.subheader("Morphology")
  st.image('https://upload.wikimedia.org/wikipedia/commons/a/a9/Ascaris_lumbricoides4.jpg')
  st.image('https://laboratorytests.org/wp-content/uploads/2019/03/Fertilized-and-Unfertilized-Eggs-of-Ascaris-Lumbricoides.jpg')
  st.markdown("""
  - **Fertilized eggs:** The fertilized eggs are laid by females after inseminated by mating with a male. These are embryonated and develop into the infective eggs.
  - **Unfertilized Eggs:** he unfertilized eggs are laid by uninseminated female. Thes are non-embryonated and cannot become infective.
  """)
  st.subheader("Life cycle")
  st.markdown("""
  1. Adult worms live in the small intestine of people. There, females (the larger worm in the image) may produce approximately 200,000 eggs per day. The eggs are excreted with stool.
  2. In the small intestine, females may produce approximately 200,000 eggs per day. The eggs are excreted with stool (feces). Only fertilized eggs cause infection.
  3. The fertilized eggs develop in the soil. The eggs develop best in moist, warm, shaded soil.
  4. People become infected when they swallow Ascaris eggs, often in food that came in contact with soil contaminated with human stool containing fertilized Ascaris eggs.
  5. The eggs hatch and release larvae in the intestine.
  6. The larvae penetrate the wall of the small intestine and travel through the lymphatic vessels (tubes that carry a fluid called lymph through the body) and bloodstream to the lungs.
  7. Once inside the lungs, larvae pass into air sacs (alveoli) in the lungs, move up the respiratory tract and into the throat, and are swallowed. When the larvae reach the small intestine, they develop into adult worms.
  """)
  st.image("https://edge.sitecorecloud.io/mmanual-ssq1ci05/media/home/images/a/s/c/ascaris-lumbricoides-lifecycle-lg-cdc-sized.jpg?sc_lang=en&mw=2048")
  st.markdown("""
  - **Mode of Transmission:** Ingestion of infective eggs from contaminated food or water. 
  - **Route of Infection:** Ingestion of infective eggs.
  - **Laboratory Diagnosis:** Detection of characteristic eggs in stool samples. 
  - **Treatment:** Albendazole, mebendazole, or ivermectin.
  - **Prevention and Control:** Improved sanitation, clean water, proper hygiene, and mass deworming programs. 
  """)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Hymenolepsis-------------------------------------------------------------------------------------------------------------------------------------------------------------------
  st.header("2.Hymenolepsis nana")
  st.subheader("Geographical Distribution")
  st.write("""
  Hymenolepis nana is the most common cause of all cestode infections, and is encountered worldwide. In temperate areas its incidence is higher in children and institutionalized groups.
  """)
  st.subheader("Morphology")
  st.image("https://www.cdc.gov/dpdx/hymenolepiasis/images/2/H_nana_egg_wtmt2.jpg?_=01693")
  st.subheader("Life cycle")
  st.markdown("""
  1. Eggs passed in stool are immediately infective ,Eggs released in feces can infect instantly and survive up to 10 days outside the host.
  2. Direct ingestion of eggs by humans causes infection ,Through contaminated food, water, or hands → eggs hatch in the intestine.
  3. Oncospheres penetrate intestinal villi and develop into cysticercoid larvae ,Larvae mature inside the villi before returning to the intestinal lumen.
  4. Cysticercoids evaginate scoleces and attach to intestinal mucosa ,They develop into adult worms in the ileum (part of the small intestine).
  5. Adults release eggs through gravid proglottids ,Eggs are excreted or may cause autoinfection inside the same host.
  6. Autoinfection allows the parasite to persist for years,Eggs hatch internally, restarting the cycle without leaving the body.
  """)
   







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



