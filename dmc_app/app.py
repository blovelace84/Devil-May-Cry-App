import streamlit as st
from components import character_display, weapon_display, enemy_display, utils
from PIL import Image

# --- 1. Basic Setup ---
st.set_page_config(
    page_title="Devil May Cry App",
    page_icon="😈⚔️",
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
        st.warning("Dante image not found.  Please make sure you have dante.jpg in the same directory")

    if st.button("Enter"):
        st.write("Welcome to the world of Devil May Cry!")

with st.container(border=True):
    st.markdown("<h2 class='header'>Character Profiles</h2>", unsafe_allow_html=True)
    characters = {
        "Dante": {
            "name": "Dante",
            "image": "../dmc-images/dante.jpeg",
            "bio": "The legendary demon hunter, son of Sparda.  He is known for his cocky attitude and incredible power.",
            "style": "Trickster, Swordmaster, Gunslinger, Royal Guard",
        },
        "Vergil": {
            "name": "Vergil",
            "image": "../dmc-image/Vergil.jpeg",
            "bio": "Dante's twin brother, who seeks power above all else.  He is a master of the Yamato.",
            "style": "Darkslayer",
        },
        "Nero": {
            "name": "Nero",
            "image": "../dmc-images/Nero.jpeg",
            "bio": "A young demon hunter with a mysterious power, the Devil Bringer.  He is hotheaded but righteous.",
            "style": "Devil Bringer, Swordmaster, Gunslinger",
        },
        "Lady": {
            "name": "Lady",
            "image": "../dmc-images/Lady.jpeg",
            "bio": "A human demon hunter with a personal vendetta against demons.",
            "style": "Gunslinger",
        }
    }

    character_selection = st.selectbox("Select a Character", list(characters.keys()))
    character_display.display_character_info(characters[character_selection])  # Call the function

with st.container(border=True):
    st.markdown("<h2 class='header'>Weapon Showcase</h2>", unsafe_allow_html=True)
    weapons = {
        "Rebellion": {
            "name": "Rebellion",
            "description": "Dante's signature sword, inherited from his father Sparda.  It can transform into different forms.",
            "type": "Sword",
            "damage": "High",
        },
        "Ebony & Ivory": {
            "name": "Ebony & Ivory",
            "description": "Dante's custom-made handguns, effective at long range and for rapid firing.",
            "type": "Handguns",
            "damage": "Medium",
        },
        "Yamato": {
            "name": "Yamato",
            "description": "Vergil's katana, a powerful weapon that can slice through dimensions.",
            "type": "Katana",
            "damage": "Very High",
        },
        "Devil Bringer": {
            "name": "Devil Bringer",
            "description": "Nero's mysterious right arm, which can perform powerful demonic attacks and grab enemies.",
            "type": "Arm",
            "damage": "Variable",
        }
    }

    weapon_selection = st.selectbox("Select a Weapon", list(weapons.keys()))
    weapon_display.display_weapon_info(weapons[weapon_selection])  # Call the function

with st.container(border=True):
    st.markdown("<h2 class='header'>Enemy Database</h2>", unsafe_allow_html=True)
    enemies = {
        "Empusa": {
            "name": "Empusa",
            "description": "A basic, insect-like demon.  They are weak but can be numerous.",
            "weakness": "Fire",
            "attacks": "Bite, Claw Swipe",
        },
        "Hell Caina": {
            "name": "Hell Caina",
            "description": "A fiery demon that can teleport and attack with fire.",
            "weakness": "Water",
            "attacks": "Fire Breath, Teleport Slash",
        },
        "Death Scissor": {
            "name": "Death Scissor",
            "description": "A demon with large scissors, it can be very dangerous.",
            "weakness": "Quick attacks to the head",
            "attacks": "scissor attack",
        },
    }
    enemy_selection = st.selectbox("Select an Enemy", list(enemies.keys()))
    enemy_display.display_enemy_info(enemies[enemy_selection])  # Call the function

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