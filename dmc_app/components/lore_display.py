import streamlit as st
from PIL import Image

def display_lore_info(lore_section):
    st.markdown(f"<h2 class='lore-title'>{lore_section['title']}</h2>", unsafe_allow_html=True)
    try:
        image = Image.open(lore_section['image'])
        st.image(image, width=400, use_container_width=False, output_format="JPEG")
    except FileNotFoundError:
       st.warning(f"Image not found: {lore_section['image']}")
    st.write(lore_section["content"], unsafe_allow_html=True)