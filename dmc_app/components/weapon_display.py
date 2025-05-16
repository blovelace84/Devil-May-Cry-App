import streamlit as st
from PIL import Image

def display_weapon_info(weapon):
    st.markdown(f"<h3 class='weapon-name'>{weapon['name']}</h3>", unsafe_allow_html=True)
    image_path = weapon["image"]  # Get the image path
    try:
        image = Image.open(image_path)
        st.image(image, width=300, use_container_width=False, output_format="JPEG")
    except FileNotFoundError:
        st.warning(f"Image not found: {image_path}")
    st.write(weapon["description"])
    st.write(f"**Type:** {weapon['type']}")
    st.write(f"**Damage:** {weapon['damage']}")
