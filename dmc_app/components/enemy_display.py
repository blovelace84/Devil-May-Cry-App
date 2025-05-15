import streamlit as st

def display_enemy_info(enemy):
    st.markdown(f"<h3 class='enemy-name'>{enemy['name']}</h3>", unsafe_allow_html=True)
    st.write(enemy["description"])
    st.write(f"**Weakness:** {enemy['weakness']}")
    st.write(f"**Attacks:** {enemy['attacks']}")