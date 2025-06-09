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

#Hymenolepsis nana-------------------------------------------------------------------------------------------------------------------------------------------------------------------
  st.header("2.Hymenolepis nana")
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
  st.image("https://www.cdc.gov/dpdx/hymenolepiasis/modules/H_nana_LifeCycle.gif?_=01675")
  st.markdown("""
  - **Mode of Transmission:** Ingestion of infective eggs from contaminated food or water.
  - **Route of Infection:** Fecal-oral route.
  - **Laboratory Diagnosis:** Detection of eggs in stool samples; ELISA for antigen detection. 
  - **Treatment:** Praziquantel, albendazole, or mebendazole
  - **Prevention and Control:** Improved sanitation, rodent control, and personal hygiene.
  """)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#diminuta-----------------------------------------------------------------------------------------------------------------------------------------------------------
  st.header("3..Hymenolepis diminuta")
  st.subheader("Geographical Distribution")
  st.write("""
  Hymenolepis diminuta, while less frequent, has been reported from various areas of the world.
  """)
  st.subheader("Morphology")
  st.image("http://www.medical-labs.net/wp-content/uploads/2014/06/H.diminuta-OVA.jpg")
  st.subheader("Life cycle")
  st.markdown("""
  1. ggs are passed in the feces of infected rodents or humans Gravid proglottids disintegrate in the intestine, releasing eggs that are excreted in feces.
  2. Eggs are ingested by arthropod intermediate hosts (e.g., beetles, fleas) ,Common hosts include Tribolium species (flour beetles).
  3. Oncospheres hatch and penetrate the intestinal wall of the arthropod ,They develop into cysticercoid larvae inside the insect's body.
  4. Humans or rodents become infected by ingesting infected arthropods,Often through contaminated food (e.g., cereals) or environmental exposure.
  5. Cysticercoid larvae are released in the stomach and evert their scolex,The scolex attaches to the intestinal wall using suckers.
  6. Adult worms mature in about 20 days and produce eggs,Adults can grow up to 30 cm; eggs are again released in feces, continuing the cycle.
  """)
  st.image("https://www.cdc.gov/dpdx/hymenolepiasis/modules/H_diminuta_LifeCycle.gif?_=01676")
  st.markdown("""
  - **Mode of Transmission:** Ingestion of infected intermediate hosts.
  - **Route of Infection:** Ingestion of infected arthropods.
  - **Laboratory Diagnosis:** Detection of eggs in stool samples.
  - **Treatment:** Praziquantel or niclosamide
  - **Prevention and Control:** Rodent control and proper food handling.
  """)

#--------------------------------------------------------------------------------------------------------------------------------------------------

#tenia-----------------------------------------------------------------------------------------------------------------------------------------------
  st.header("4.enia spp.")
  st.subheader("Geographical Distribution")
  st.write("""
  Taenia saginata and T. solium are worldwide in distribution. Taenia solium is more prevalent in poorer communities where humans live in close contact with pigs and eat undercooked pork. Taenia asiatica is limited to Asia and is seen mostly in the Republic of Korea, China, Taiwan, Indonesia, and Thailand.
  """)
  st.subheader("Morphology")
  st.image("https://www.cdc.gov/dpdx/taeniasis/images/1/Taenia_egg.jpg?_=96649")
  st.subheader("Life cycle")
  st.markdown("""
  1. Eggs or gravid proglottids are passed in human feces ,These can survive in the environment for days to months.
  2. Cattle or pigs ingest eggs or proglottids from contaminated vegetation,T. saginata infects cattle; T. solium and T. asiatica infect pigs.
  3. Oncospheres hatch in the animal’s intestine and migrate to striated muscles ,They develop into cysticerci, which can survive in tissue for years.
  4. Humans become infected by eating raw or undercooked infected meat ,Ingested cysticerci mature into adult tapeworms in the human intestine.
  5. Adult tapeworms attach to the small intestine via the scolex ,Development into a fully mature worm takes around 2 months.
  6. Gravid proglottids are passed in feces, releasing thousands of eggs ,T. saginata may produce up to 100,000 eggs per proglottid, T. solium about 50,000.
  """)
  st.image("https://www.cdc.gov/dpdx/taeniasis/modules/Taenia_LifeCycle.gif?_=96656")
  st.markdown("""
  - **Mode of Transmission:** Ingestion of undercooked or raw infected meat.
  - **Route of Infection:** Ingestion of cysticerci in meat.
  - **Laboratory Diagnosis:** Detection of eggs or proglottids in stool samples; identification of scolex morphology.
  - **Treatment:** Praziquantel or niclosamide. 
  - **Prevention and Control:** Proper cooking of meat, sanitation, and meat inspection.
  """)

#---------------------------------------------------------------------------------------------------------------------------------------------

#Trichuris trichiura---------------------------------------------------------------------------------------------------------------------------------------------------------
  st.header("5.Trichuris trichiura")
  st.subheader("Geographical Distribution")
  st.write("""
  The third most common round worm of humans. Worldwide, with infections more frequent in areas with tropical weather and poor sanitation practices, and among children. It is estimated that 800 million people are infected worldwide. Trichuriasis occurs in the southern United States.
  """)
  st.subheader("Morphology")
  st.image("https://www.cdc.gov/dpdx/trichuriasis/images/1/Trichuris_trichiura_egg1.jpg?_=01207")
  st.subheader("Life cycle")
  st.markdown("""
  1. Unembryonated eggs are passed in the stool ,Eggs are released by adult females in the large intestine and excreted in feces.
  2. Eggs develop in soil through multiple stages to become infective ,They pass through a 2-cell stage, advanced cleavage, and embryonate in 15–30 days.
  3. Humans become infected by ingesting embryonated eggs ,Via contaminated hands, food, or soil.
  4. Eggs hatch in the small intestine, releasing larvae ,Larvae migrate to the large intestine.
  5. Larvae mature into adult worms in the cecum and colon ,Adults thread their anterior ends into the mucosa and remain fixed.
  6. Females begin egg production 60–70 days post-infection ,They lay 3,000–20,000 eggs per day; adult worms can live up to 1 year.
  """)
  st.image("https://www.cdc.gov/dpdx/trichuriasis/modules/Trichuris_LifeCycle.gif?_=01176")
  st.markdown("""
  - **Mode of Transmission:** Fecal-oral route via ingestion of embryonated eggs from contaminated food or water.
  - **Route of Infection:** Ingestion of infective eggs.
  - **Laboratory Diagnosis:** Detection of characteristic lemon-shaped eggs in stool samples.
  - **Treatment:** Mebendazole, albendazole, or ivermectin.
  - **Prevention and Control:** Improved sanitation, clean water, proper hygiene, and mass deworming programs.
  """)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Hookworm---------------------------------------------------------------------------------------------------------------------------------------------------------------------
  
  
  





  
  
              


   







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



