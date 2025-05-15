import streamlit as st

def display_weapon_info(weapon):
    st.markdown(f"<h3 class='weapon-name'>{weapon['name']}</h3>", unsafe_allow_html=True)
    st.write(weapon["description"])
    st.write(f"**Type:** {weapon['type']}")
    st.write(f"**Damage:** {weapon['damage']}")