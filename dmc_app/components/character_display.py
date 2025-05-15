import streamlit as st
from PIL import Image

def display_character_info(character):
    st.markdown(f"<h2 class='character-name'{character['name']}</h2>", unsafe_allow_html=True)
    try:
        try:
            image = Image.open(character['image'])
        except FileNotFoundError:
            image = Image.open("../dmc-images/" + character["image"].split('/')[-1])
        st.image(image, width=300, use_container_width=False, output_format="JPEG", )
    except FileNotFoundError:
        st.warning(f"Image not found: {character['image']}")
    st.write(character["bio"])
    st.write(f"**Style:** {character['style']}")
