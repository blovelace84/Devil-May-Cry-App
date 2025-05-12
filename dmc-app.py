import streamlit as st

# Set the page title and theme
st.set_page_config(
    page_title="Devil May Cry App",
    page_icon="😈",  # You could find a cool icon
    layout="wide",
)

# Apply a dark theme (you might need custom CSS for more detailed styling)
st.markdown(
    """
    <style>
    body {
        background-color: #111111;  /* Dark background */
        color: #ffffff;             /* White text */
    }
    .title {
        color: #ff0000;           /* Red title */
        font-size: 48px;
        font-family: "Metal Gear Solid", sans-serif; /* Example font */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Display the title
st.markdown('<h1 class="title">Devil May Cry</h1>', unsafe_allow_html=True)

# Display an image
st.image("dmc-images/dante_image.jpeg", width=400) # Replace with actual image

# Add a button
if st.button("Enter"):
    st.write("Welcome to the world of Devil May Cry!")
    #  You could use st.session_state to control page flow
