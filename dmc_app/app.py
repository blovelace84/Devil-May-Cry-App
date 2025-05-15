import streamlit as st
from PIL import Image
from components import character_display, weapon_display, enemy_display, utils
from data import character_data, weapon_data, enemy_data # Import the data
# --- 1. Basic Setup ---
st.set_page_config(
    page_title="Devil May Cry App",
    page_icon="⚔️",
    layout="wide",
)
# --- 2. Custom CSS ---
st.markdown(utils.load_custom_css(), unsafe_allow_html=True)  # Load CSS from utils
# --- 4. App Content ---
# Use a container for the main content
with st.container(border=True):
    st.markdown('<h1 class="title">Devil May Cry</h1>', unsafe_allow_html=True)
    try:
        dante_image = Image.open("../dmc-images/dante_image.jpeg")
        st.image(dante_image, width=400, use_container_width=False, output_format="JPEG")
    except FileNotFoundError:
        st.warning("Dante image not found.  Please make sure you have dante.jpg in the dmc-images directory")
    if st.button("Enter"):
        st.write("Welcome to the world of Devil May Cry!")
with st.container(border=True):
    st.markdown("<h2 class='header'>Character Profiles</h2>", unsafe_allow_html=True)
    #characters = { ... } # Remove this
    character_selection = st.selectbox("Select a Character", list(character_data.characters.keys())) # Use character_data
    character_display.display_character_info(character_data.characters[character_selection])
with st.container(border=True):
    st.markdown("<h2 class='header'>Weapon Showcase</h2>", unsafe_allow_html=True)
    #weapons = { ... } # Remove this
    weapon_selection = st.selectbox("Select a Weapon", list(weapon_data.weapons.keys())) # Use weapon_data
    weapon_display.display_weapon_info(weapon_data.weapons[weapon_selection])
with st.container(border=True):
    st.markdown("<h2 class='header'>Enemy Database</h2>", unsafe_allow_html=True)
    #enemies = { ... } # Remove this
    enemy_selection = st.selectbox("Select an Enemy", list(enemy_data.enemies.keys())) # Use enemy_data
    enemy_display.display_enemy_info(enemy_data.enemies[enemy_selection])
with st.container(border=True):
    st.markdown("<h2 class='header'>Lore</h2>", unsafe_allow_html=True)
    lore_sections = {
        "Mythology": "The story of Sparda, the legendary dark knight, and his rebellion against the demon world.",
        "History": "Important events in the Devil May Cry timeline, including the battles between Dante and Vergil.",
        "Characters": "Backstories of the main characters and their motivations.",
        "Devil Arms": "Powerful weapons forged from the remains of defeated demons"
    }
    lore_selection = st.selectbox("Select a Lore Section", list(lore_sections.keys()))
    st.markdown(f"<h3 class='lore-title'>{lore_selection}</h3>", unsafe_allow_html=True)
    st.write(lore_sections[lore_selection])
with st.container(border=True):
    st.markdown("<h2 class='header'>Style Meter</h2>", unsafe_allow_html=True)
    st.write("The Style Meter reflects the player's combat performance, ranging from 'D' (Dismal) to 'SSS' (Stylish).")
    style_level = st.slider("Simulate Style Level", 0, 100, 50)
    style_levels = ["D", "C", "B", "A", "S", "SS", "SSS"]
    level_index = min(style_level // 15, 6)
    st.write(f"**Current Style:** {style_levels[level_index]}")