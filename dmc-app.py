import streamlit as st
from PIL import Image  # Import Pillow for image handling

# --- 1. Basic Setup ---
# Set the page title and theme
st.set_page_config(
    page_title="Devil May Cry App",
    page_icon="😈",
    layout="wide",
)

# Apply a dark theme with custom CSS
st.markdown(
    """
    <style>
    body {
        background-color: #111111;
        color: #ffffff;
    }
    .title {
        color: #ff0000;
        font-size: 48px;
        font-family: 'Metal Gear Solid', sans-serif;  /* Example font */
        text-shadow: 2px 2px 5px #000000;
    }
    .header {
        color: #d3d3d3;
        font-size: 24px;
        padding-bottom: 10px;
        border-bottom: 1px solid #4a4a4a;
    }
    .section {
        margin-bottom: 40px;
    }
    .character-name {
        color: #ff8c00;
        font-size: 30px;
        margin-top: 20px;
    }
    .weapon-name {
        color: #b22222;
        font-size: 24px;
        margin-top: 15px;
    }
    .enemy-name {
        color: #adff2f;
        font-size: 24px;
        margin-top: 15px;
    }
    .lore-title{
        color: #87CEFA;
        font-size: 24px;
        margin-top: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- 2. Helper Functions ---
# Function to display character information


def display_character_info(character):
    st.markdown(f"<h2 class='character-name'>{character['name']}</h2>", unsafe_allow_html=True)
    try:
        image = Image.open(character["image"])  # Use Pillow to open the image
        st.image(image, width=300)
    except FileNotFoundError:
        st.warning(f"Image not found: {character['image']}")
    st.write(character["bio"])
    st.write(f"**Style:** {character['style']}")


# Function to display weapon information
def display_weapon_info(weapon):
    st.markdown(f"<h3 class='weapon-name'>{weapon['name']}</h3>", unsafe_allow_html=True)
    st.write(weapon["description"])
    st.write(f"**Type:** {weapon['type']}")
    st.write(f"**Damage:** {weapon['damage']}")


# Function to display enemy information
def display_enemy_info(enemy):
    st.markdown(f"<h3 class='enemy-name'>{enemy['name']}</h3>", unsafe_allow_html=True)
    st.write(enemy["description"])
    st.write(f"**Weakness:** {enemy['weakness']}")
    st.write(f"**Attacks:** {enemy['attacks']}")

# --- 3. App Content ---
# Homepage
st.markdown('<h1 class="title">Devil May Cry</h1>', unsafe_allow_html=True)
try:
    dante_image = Image.open("dmc-images/dante_image.jpeg")
    st.image(dante_image, width=400)
except FileNotFoundError:
    st.warning("Dante image not found.  Please make sure you have dante.jpg in the same directory")

if st.button("Enter"):
    st.write("Welcome to the world of Devil May Cry!")

# Character Profiles Section
st.markdown("<h2 class='header'>Character Profiles</h2>", unsafe_allow_html=True)
characters = {
    "Dante": {
        "name": "Dante",
        "image": "dmc-images/dante.jpeg",
        "bio": "The legendary demon hunter, son of Sparda.  He is known for his cocky attitude and incredible power.",
        "style": "Trickster, Swordmaster, Gunslinger, Royal Guard",
    },
    "Vergil": {
        "name": "Vergil",
        "image": "dmc-images/Vergil.jpeg",
        "bio": "Dante's twin brother, who seeks power above all else.  He is a master of the Yamato.",
        "style": "Darkslayer",
    },
    "Nero": {
        "name": "Nero",
        "image": "dmc-images/Nero.jpeg",
        "bio": "A young demon hunter with a mysterious power, the Devil Bringer.  He is hotheaded but righteous.",
        "style": "Devil Bringer, Swordmaster, Gunslinger",
    },
    "Lady": {
        "name": "Lady",
        "image": "dmc-images/Lady.jpeg",
        "bio": "A human demon hunter with a personal vendetta against demons.",
        "style": "Gunslinger",
    }
}

character_selection = st.selectbox("Select a Character", list(characters.keys()))
display_character_info(characters[character_selection])

# Weapon Showcase Section
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
display_weapon_info(weapons[weapon_selection])

# Enemy Database Section
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
display_enemy_info(enemies[enemy_selection])

# Lore Section
st.markdown("<h2 class='header'>Lore</h2>", unsafe_allow_html=True)
lore_sections = {
    "Mythology": "The story of Sparda, the legendary dark knight, and his rebellion against the demon world.",
    "History": "Important events in the Devil May Cry timeline, including the battles between Dante and Vergil.",
    "Characters": "Backstories of the main characters and their motivations.",
    "Devil Arms":"Powerful weapons forged from the remains of defeated demons"
}
lore_selection = st.selectbox("Select a Lore Section", list(lore_sections.keys()))
st.markdown(f"<h3 class='lore-title'>{lore_selection}</h3>", unsafe_allow_html=True)
st.write(lore_sections[lore_selection])

# Style Meter Section
st.markdown("<h2 class='header'>Style Meter</h2>", unsafe_allow_html=True)
st.write("The Style Meter reflects the player's combat performance, ranging from 'D' (Dismal) to 'SSS' (Stylish).")
#  use স্টাইল মিটার visualize
style_level = st.slider("Simulate Style Level", 0, 100, 50)  # Slider to simulate style
style_levels = ["D", "C", "B", "A", "S", "SS", "SSS"]
level_index = min(style_level // 15, 6)  # Map slider to style levels
st.write(f"**Current Style:** {style_levels[level_index]}")
