import streamlit as st
from PIL import Image
import os

def home_page():
  st.write("this is home page")
  st.markdown('<h2 style="text-align:center;">Platform for parasitic egg detection</h2>',unsafe_allow_html=True)
def home_page():
    st.title(" Parasite Egg Identification & Quiz Platform")
    
    st.image("https://example.com/parasite_eggs_banner.jpg", use_column_width=True)  # Optional banner image

    st.markdown("""
    ##  Purpose
    This web application is designed to assist students, medical technologists, and professionals 
    in the identification and understanding of **parasitic eggs** through visual references, 
    morphological features, and interactive quizzes.

    ##  What You’ll Learn
    - Morphological characteristics of different parasite eggs
    - Routes and modes of transmission
    - Key differences between similar parasites
    - Diagnostic features and clinical relevance

    ##  Features
    - **Egg Reference Gallery** – High-quality images and descriptions of parasite eggs
    - **Interactive Quiz** – Test your knowledge with multiple-choice questions
    - **Learning Resources** – Educational material and transmission life cycles

    ## Target Parasites Covered
    - *Ascaris lumbricoides*
    - *Hymenolepis nana*
    - *Hymenolepis diminuta*
    - *Taenia spp.*
    - *Trichuris trichiura*
    - *Hookworm*
    - *Opisthorchis viverrini*
    - *Minute intestinal flukes*
    - ... and more

    ## How to Use
    1. Navigate through the sidebar menu to access pages.
    2. Review reference materials or start the quiz.
    3. Check your score and review correct answers.

    ---
    🔄 **This platform is best viewed on desktop for image clarity and usability.**
    """)

    st.info("👉 Use the sidebar to get started with the reference section or the quiz.")

  

def parasite_detail_page():
  
  st.write("this is page detail")
  st.sidebar.title("Table of Content")
  st.sidebar.markdown("""
  - [Ascaris lumbricoides](#ascaris-lumbricoides)
  - [Hymenolepsis nana](#hymenolepsis-nana)
  - [Hymenolepsis diminuta](#hymenolepsis-diminuta)
  - [Taenia spp.](#taenia-spp.)
  - [Trichuris trichiura](#trichuris-trichiura)
  - [Hookworm](#hookworm)
  - [Opisthorchis viverrini](#opisthorchis-viverrini)
  - [Minute intestinal flukes](#minute-intestinal-flukes)
  - [Reference] (#reference)
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
  st.image('https://ars.els-cdn.com/content/image/3-s2.0-B9780128187319001075-f00107-14-9780128187319.jpg')
  st.image('https://learnzoology.wordpress.com/wp-content/uploads/2014/04/ascaris-male-female.jpg?w=640')
  st.subheader("Adult")
  st.write("""
  Adult worms are characterized by their large size, cylindrical, unsegmented bodies, and distinct sexual dimorphism. Females are typically 20-35 cm long, while males are slightly smaller, ranging from 15-30 cm. Both sexes have three "lips" at the anterior end of the body. 
  """)
  st.subheader("Life cycle")
  st.markdown("""
  The life cycle of *Ascaris* worms begins when adult worms reside in the small intestine of humans. In this environment, female worms—which are generally larger than males—can produce approximately 200,000 eggs per day. These eggs are passed out of the body through the stool. Only fertilized eggs are capable of causing infection. Once excreted, the fertilized eggs require specific environmental conditions to develop; they mature best in moist, warm, and shaded soil.
  People typically become infected by accidentally ingesting these eggs, often through food that has been in contact with soil contaminated by human feces containing fertilized *Ascaris* eggs. After ingestion, the eggs hatch in the small intestine, releasing larvae. These larvae then penetrate the intestinal wall and travel via the lymphatic system and bloodstream to the lungs. Within the lungs, the larvae enter the air sacs (alveoli), migrate up the respiratory tract to the throat, and are subsequently swallowed. Once back in the small intestine, the larvae mature into adult worms, completing the life cycle.
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
  The life cycle of the parasite begins when eggs are passed in the stool of an infected individual. These eggs are immediately infective and can survive in the external environment for up to 10 days. Humans become infected primarily through the accidental ingestion of these eggs, often via contaminated food, water, or hands. Once ingested, the eggs hatch in the small intestine, releasing oncospheres. These oncospheres penetrate the intestinal villi and develop into cysticercoid larvae within the tissue.
  As the larvae mature, they return to the intestinal lumen, where they evaginate their scoleces and attach themselves to the intestinal mucosa, particularly in the ileum, a section of the small intestine. There, they develop into adult worms. The adult worms release eggs through gravid proglottids, which are either excreted in the stool or may cause autoinfection within the same host. In cases of autoinfection, the eggs hatch internally, allowing the parasite to complete its life cycle without leaving the host’s body. This mechanism enables the infection to persist for extended periods, sometimes lasting for years.
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
  st.header("3.Hymenolepis diminuta")
  st.subheader("Geographical Distribution")
  st.write("""
  Hymenolepis diminuta, while less frequent, has been reported from various areas of the world.
  """)
  st.subheader("Morphology")
  st.image("http://www.medical-labs.net/wp-content/uploads/2014/06/H.diminuta-OVA.jpg")
  st.subheader("Life cycle")
  st.markdown("""
  The life cycle of this parasite begins when eggs are passed in the feces of infected rodents or humans. Gravid proglottids, segments of the adult worm containing eggs, disintegrate within the host’s intestine, releasing eggs that are subsequently excreted in the stool. These eggs are then ingested by arthropod intermediate hosts, such as beetles or fleas, with Tribolium species (flour beetles) being particularly common carriers. Once inside the arthropod, the eggs hatch, and the resulting oncospheres penetrate the intestinal wall, developing into cysticercoid larvae within the insect’s body.
  Humans or rodents may become infected by accidentally ingesting these infected arthropods, often through contaminated food—such as improperly stored cereals—or by exposure in infested environments. When ingested, the cysticercoid larvae are released in the stomach, where they evert their scolex (head) and attach to the intestinal wall using suckers. The worms mature into adults within approximately 20 days. Adult worms, which can grow up to 30 centimeters in length, begin producing eggs that are once again released through the feces, thereby continuing the cycle.
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

#taenia-----------------------------------------------------------------------------------------------------------------------------------------------
  st.header("4.Taenia spp.")
  st.subheader("Geographical Distribution")
  st.write("""
  Taenia saginata and T. solium are worldwide in distribution. Taenia solium is more prevalent in poorer communities where humans live in close contact with pigs and eat undercooked pork. Taenia asiatica is limited to Asia and is seen mostly in the Republic of Korea, China, Taiwan, Indonesia, and Thailand.
  """)
  st.subheader("Morphology")
  st.image("https://www.cdc.gov/dpdx/taeniasis/images/1/Taenia_egg.jpg?_=96649")
  st.subheader("Life cycle")
  st.markdown("""
  The life cycle of Taenia tapeworms begins when eggs or gravid proglottids are passed in human feces, which can remain viable in the environment for days to months. These are ingested by cattle or pigs through contaminated vegetation—T. saginata infects cattle, while T. solium and T. asiatica infect pigs. Inside the animal, the eggs hatch into oncospheres that migrate to muscle tissue and develop into cysticerci, which can survive for years.Humans become infected by consuming raw or undercooked infected meat. The cysticerci then mature into adult tapeworms in the intestine, a process that takes about two months. The adult worms attach to the small intestine and begin producing proglottids, which are released in feces, each containing tens of thousands of eggs, thus continuing the cycle..
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
  The life cycle begins when unembryonated eggs are passed in human stool, having been released by adult female worms in the large intestine. In the soil, these eggs develop through several stages and become infective within 15 to 30 days. Humans acquire the infection by ingesting embryonated eggs through contaminated hands, food, or soil.
  Once ingested, the eggs hatch in the small intestine, and the larvae migrate to the large intestine. There, they mature into adult worms, which attach to the mucosal lining of the cecum and colon. About 60 to 70 days after infection, females begin producing 3,000 to 20,000 eggs daily. Adult worms can survive in the host for up to one year.
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
  st.header("6.Hookworm")
  st.subheader("Geographical Distribution")
  st.write("""
  Hookworm species have a worldwide distribution, mostly in areas with moist, warm climates where larvae can survive in the environment. Both Necator americanus and Ancylostoma duodenale are found in Africa, Asia, Australia and the Americas. Only N. americanus is found in south India and predominates in the Americas, while only A. duodenale is found in the Middle East, North Africa, and northern India.
  """)
  st.subheader("Morphology")
  st.image("https://www.cdc.gov/dpdx/hookworm/images/1/Hookworm_2x2_B.jpg?_=02464")
  st.subheader("Life cycle")
  st.markdown("""
  The life cycle begins when eggs are passed in the stool and hatch into rhabditiform larvae within 1–2 days under warm, moist, and shaded conditions. These larvae develop into infective filariform (L3) larvae within 5–10 days and can survive in soil for several weeks.
  Infective larvae penetrate human skin—often through bare feet—enter the bloodstream, and travel to the lungs. From there, they migrate up the bronchial tree, are swallowed, and reach the small intestine.
  In the jejunum, the larvae mature into adult worms that attach to the intestinal wall and feed on the host's blood. Some larvae may enter a dormant state (hypobiosis). Notably, Ancylostoma duodenale can also infect via oral or transmammary routes, unlike Necator americanus.
  """)
  st.image("https://www.cdc.gov/dpdx/hookworm/modules/Hookworm_LifeCycle_19.jpg?_=81699")
  st.markdown("""
  - **Mode of Transmission:** Transmitted via skin penetration by infective larvae from contaminated soil.
  - **Route of Infection:** Larvae enter through skin → lungs → swallowed → mature in small intestine.
  - **Laboratory Diagnosis:** Stool exam reveals characteristic hookworm eggs under microscope.
  - **Treatment:** Albendazole or mebendazole is effective; iron supplements for anemia.
  - **Prevention and Control:** Wear shoes, improve sanitation, and implement deworming programs.
  """)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Opisthorchis viverrini ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  st.header("7.Opisthorchis viverrini")
  st.subheader("Geographical Distribution")
  st.write("""
  Opisthorchis viverrini is found mainly in northeast Thailand, Laos, Cambodia, and central and southern Vietnam. Opisthorchis felineus is found mainly in Italy, Germany, Belarus, Russia, Kazakhstan, and Ukraine.
  """)
  st.subheader("Morphology")
  st.image("https://www.cdc.gov/dpdx/opisthorchiasis/images/1/O_viverrini_egg_wtmt_BAM3.jpg?_=00772")
  st.subheader("Life cycle")
  st.markdown("""
  The life cycle begins when fully developed eggs are passed in the feces of humans or animals. These eggs are ingested by freshwater snails, the first intermediate host, where they hatch into miracidia and develop through several stages—sporocysts, rediae, and then cercariae.
  The cercariae are released from the snails and penetrate freshwater fish, the second intermediate host. Inside the fish, they encyst as metacercariae within the muscles or beneath the scales.
  Humans or other mammals become infected by consuming undercooked or raw fish containing metacercariae. Once ingested, the parasites excyst in the duodenum, migrate to the bile ducts, and mature into adult flukes, beginning egg production within 3 to 4 weeks.
  """)
  st.image("https://www.cdc.gov/dpdx/opisthorchiasis/modules/Opisthorchis_LifeCycle.gif?_=00785")
  st.markdown("""
  - **Mode of Transmission:** Ingestion of undercooked or raw infected fish
  - **Route of Infection:** Ingestion of metacercariae in fish.
  - **Laboratory Diagnosis:** Detection of eggs in stool samples; serological tests for antibodies.
  - **Treatment:**  Praziquantel , albendazole.
  - **Prevention and Control:** Avoid eating raw or undercooked freshwater fish ,Cook fish thoroughly to kill metacercariae ,Mass deworming programs – in high-risk communities to reduce transmission.
  """)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Minute------------------------------------------------------------------------------------------------------------------------------------------------------------
  st.header("8.Minute intestinal fluke ")
  st.subheader("Geographical Distribution")
  st.write("""
  Egypt, the Middle East, and Far East.
  """)
  st.subheader("Morphology")
  st.image("https://www.troccap.com/wp-content/uploads/2018/09/intestinal-fluke-fig1.jpg")
  st.subheader("Life cycle")
  st.markdown("""
  The life cycle begins when embryonated eggs, containing fully developed miracidia, are passed in the feces of infected hosts. These eggs are ingested by specific snails such as Cerithidia or Pironella, where the miracidia hatch and develop through sporocyst, redia, and cercaria stages.
  The cercariae are then released from the snails and encyst as metacercariae in freshwater or brackish fish. Humans and other animals become infected by consuming undercooked or salted fish that contain these metacercariae.
  After ingestion, the metacercariae excyst in the small intestine, attach to the intestinal mucosa, and develop into adult flukes. Definitive hosts include humans, cats, dogs, and fish-eating birds.
  """)
  st.image("https://www.cdc.gov/dpdx/heterophyiasis/modules/Heterophyes_LifeCycle.gif?_=01559")
  st.markdown("""
  - **Mode of Transmission:** Transmitted by ingestion of metacercariae in raw or undercooked freshwater fish.
  - **Route of Infection:** After ingestion, metacercariae excyst in the small intestine and attach to the mucosa.
  - **Laboratory Diagnosis:** Detection of small, operculated eggs in stool via microscopy.
  - **Treatment:** Praziquantel 75 mg/kg/day in 3 divided doses for 1 day.
  - **Prevention and Control:** Avoid eating raw fish, ensure proper cooking, and improve sanitation.
  """)
#-----------------------------------------------------------------------------------------------------------------------
#reference_page----------------------------------------------------------------------------------------------------------------------- 
  st.header("9.Reference ")
  st.markdown("""
  1. Centers for Disease Control and Prevention. (2019, July 19). DPDx - Ascariasis.https://www.cdc.gov/dpdx/ascariasis/index.html
  2. Centers for Disease Control and Prevention. (n.d.). DPDx - Hymenolepiasis.https://www.cdc.gov/dpdx/hymenolepiasis/index.html
  3. Centers for Disease Control and Prevention. (n.d.). DPDx - Hymenolepiasis.https://www.cdc.gov/dpdx/hymenolepiasis/index.html
  4. Centers for Disease Control and Prevention. (n.d.). DPDx - Taeniasis.https://www.cdc.gov/dpdx/taeniasis/index.html
  5. Centers for Disease Control and Prevention. (n.d.). DPDx - Trichuriasis.https://www.cdc.gov/dpdx/trichuriasis/index.html
  6. Centers for Disease Control and Prevention. (n.d.). DPDx - Hookworm.https://www.cdc.gov/dpdx/hookworm/index.html
  7. Centers for Disease Control and Prevention. (n.d.). DPDx - Opisthorchiasis.https://www.cdc.gov/dpdx/opisthorchiasis/index.html
  8. Centers for Disease Control and Prevention. (n.d.). DPDx - Heterophyiasis.https://www.cdc.gov/dpdx/heterophyiasis/index.html
  """)
#ai detection----------------------------------------------------------------------------------------------------------------------
import cv2
import numpy as np
import tensorflow as tf


def ai_detector_page():
  st.title("Parasit Egg Detector")

#----------------------------------------------------------------------------------------------
  model_path = "model/tong.keras"

  model = tf.keras.models.load_model(model_path, custom_objects={'mse': tf.keras.losses.MeanSquaredError()})

  def boxlocation(img_c, box_size):
    non_zero_points = np.argwhere(img_c > 0)
    if non_zero_points.size == 0:
        return None

    y_min, x_min = np.min(non_zero_points, axis=0)
    y_max, x_max = np.max(non_zero_points, axis=0)

    return [y_min - box_size, y_max + box_size, x_min - box_size, x_max + box_size]

  def drawbox(img, label, a, b, c, d, box_size):
    image = cv2.rectangle(img, (c, a), (d, b), (0, 255, 0), 2)
    image = cv2.putText(image, label, (c + box_size, a - 10), cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 0, 255), 1)
    return image

  def objectdet(img):
    img = cv2.resize(img, (img.shape[1] // 1, img.shape[0] // 1), interpolation=cv2.INTER_AREA)
    
    box_size_y, box_size_x = 370, 370
    step_size = 50
    img_output = np.array(img)
    img_cont = np.zeros((img_output.shape[0], img_output.shape[1]), dtype=np.uint8)
    result = 0

    for i in range(0, img_output.shape[0] - box_size_y, step_size):
        for j in range(0, img_output.shape[1] - box_size_x, step_size):
            img_patch = img_output[i:i + box_size_y, j:j + box_size_x]
            img_patch = cv2.resize(img_patch, (64, 64), interpolation=cv2.INTER_AREA)
            img_patch = np.expand_dims(img_patch, axis=0)

            y_outp = model.predict(img_patch, verbose=0)

            if result < y_outp[0][1] and y_outp[0][1] > 0.95:
                result = y_outp[0][1]
                img_cont[i + (box_size_y // 2), j + (box_size_x // 2)] = int(y_outp[0][1] * 255)

    if result != 0:
        label = f"ev: {result:.2f}"
        boxlocat = boxlocation(img_cont, box_size_x // 2)
        if boxlocat:
            img_output = drawbox(img, label, *boxlocat, box_size_x // 2)

    return img_output
#----------------------------------------------------------------------------------------------

uploaded_file = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg", "tif"])
if uploaded_file is not None:
    try:
        image = np.array(Image.open(uploaded_file))
        if image.ndim == 2:
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

        st.image(image, caption="Uploaded Image")

        output_img = objectdet(image)
        st.image(output_img, caption="Processed Image")

    except Exception as e:
        st.error(f"Error loading image: {e}")
  
#--------------------------------------------------------------------------------------------------------
def quiz_page():
  st.write("this is page quiz")

import streamlit as st
import random

# List of quiz questions
quiz_questions = [
    {
        "question": "Which parasite egg has a characteristic barrel shape with bipolar plugs?",
        "options": ["Ascaris lumbricoides", "Trichuris trichiura", "Hookworm", "Tenia spp."],
        "answer": "Trichuris trichiura"
    },
    {
        "question": "Which parasite is transmitted by ingestion of undercooked freshwater fish?",
        "options": ["Hymenolepis nana", "Opisthorchis viverrini", "Hookworm", "Minute intestinal flukes"],
        "answer": "Opisthorchis viverrini"
    },
    {
        "question": "Which parasite’s egg has a thick mammillated shell?",
        "options": ["Ascaris lumbricoides", "Hookworm", "Tenia spp.", "Trichuris trichiura"],
        "answer": "Ascaris lumbricoides"
    },
    {
        "question": "Minute intestinal flukes are typically transmitted via which route?",
        "options": ["Skin penetration", "Ingestion of metacercaria in fish", "Fecal-oral", "Vector bite"],
        "answer": "Ingestion of metacercaria in fish"
    },
    {
        "question": "Which parasite can auto-infect the host?",
        "options": ["Hymenolepis nana", "Ascaris lumbricoides", "Tenia spp.", "Hookworm"],
        "answer": "Hymenolepis nana"
    },
    {
        "question": "Which parasite has an operculated egg visible under the microscope?",
        "options": ["Hookworm", "Opisthorchis viverrini", "Ascaris lumbricoides", "Trichuris trichiura"],
        "answer": "Opisthorchis viverrini"
    },
    {
        "question": "Which of these parasites infects humans through skin penetration?",
        "options": ["Hookworm", "Trichuris trichiura", "Tenia spp.", "Minute intestinal flukes"],
        "answer": "Hookworm"
    },
    {
        "question": "Which parasite is transmitted by ingestion of contaminated cereal or insects?",
        "options": ["Hymenolepis diminuta", "Tenia spp.", "Ascaris lumbricoides", "Hookworm"],
        "answer": "Hymenolepis diminuta"
    },
    {
        "question": "Tenia spp. eggs are typically transmitted through what source?",
        "options": ["Contaminated vegetables", "Infected pork or beef", "Skin penetration", "Drinking water"],
        "answer": "Infected pork or beef"
    },
    {
        "question": "Which egg is oval with a thin shell and visible larva inside?",
        "options": ["Hymenolepis nana", "Ascaris lumbricoides", "Hookworm", "Tenia spp."],
        "answer": "Hookworm"
    }
]



def quiz_page():
    st.title("Parasite Egg Morphology and Transmission Quiz 🦠")
    st.write("Answer the following questions about various parasitic eggs and their characteristics.")

    # เก็บลำดับคำถามไว้ใน session_state
    if "question_order" not in st.session_state:
        st.session_state.question_order = random.sample(quiz_questions, len(quiz_questions))

    score = 0

    for idx, q in enumerate(st.session_state.question_order):
        st.markdown(f"**Q{idx+1}: {q['question']}**")
        user_answer = st.radio("Choose one:", q["options"], key=f"q_{idx}")
        if user_answer == q["answer"]:
            st.success("✅ Correct!")
            score += 1
        else:
            st.error(f"❌ Incorrect. Correct answer: {q['answer']}")
        st.write("---")

    st.markdown(f"## Your final score: {score} / {len(st.session_state.question_order)}")

    # ปุ่ม reset เพื่อเริ่มใหม่
    if st.button("🔁 Restart Quiz"):
        del st.session_state.question_order
        for idx in range(len(quiz_questions)):
            st.session_state.pop(f"q_{idx}", None)
        st.experimental_rerun()

def reference_page():
  st.write("this is page ai reference")
  




    

st.sidebar.markdown("<div class='sidebar-title'>Platform Navigation</div>", unsafe_allow_html=True)
    
pages = {
    "Home": home_page,
    "Parasite egg Detail": parasite_detail_page,
    "Ai Detector": ai_detector_page,
    "Quiz": quiz_page,
    "Reference": reference_page,
    }

selected_page = st.sidebar.selectbox("Select a page", list(pages.keys()))
pages[selected_page]()



