import streamlit as st
from PIL import Image

def display_enemy_info(enemy):
    st.markdown(f"<h2 class='enemy-name'>{enemy['name']}</h2>", unsafe_allow_html=True)
    image_path = enemy["image"]
    print(f"Debug: Trying to open image at: {image_path}")  # Print the path
    try:
        try:
            image = Image.open(image_path)
        except FileNotFoundError:
            image = Image.open("../enemy_images/" + enemy["image"].split('/')[-1])
        st.image(image, width=300, use_container_width=False, output_format="JPEG")  # Updated line
    except FileNotFoundError:
        st.warning(f"Image not found: {enemy['image']}")
    st.write(enemy["description"])
    st.write(f"**Weakness:** {enemy['weakness']}")
    st.write(f"**Attacks:** {enemy['attacks']}")
