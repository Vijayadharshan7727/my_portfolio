import os
import streamlit as st
from streamlit_option_menu import option_menu

# ============================
# PAGE CONFIG
# ============================

st.set_page_config(
    page_title="Vijayadharshan | AI Portfolio",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================
# LOAD CSS
# ============================

def load_css():
    css_path = "css/style.css"

    if os.path.exists(css_path):
        with open(css_path) as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

load_css()

# ============================
# THEME
# ============================

theme = st.toggle("🌙 Dark Theme", value=True)

if theme:
    st.markdown("""
    <style>
    .stApp{
        background:#020617;
        color:white;
    }
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <style>
    .stApp{
        background:white;
        color:black;
    }
    </style>
    """, unsafe_allow_html=True)

# ============================
# SIDEBAR
# ============================

with st.sidebar:

    image_path = "assets/profile.png"

    if os.path.isfile(image_path):
        try:
            st.image(image_path, width=180)
        except Exception:
            st.warning("Unable to open profile image.")
    else:
        st.warning("profile.png not found inside assets folder.")

    st.markdown("## Vijayadharshan R")
    st.markdown("AI Engineer")

    selected = option_menu(
        menu_title=None,
        options=[
            "Home",
            "About",
            "Skills",
            "Projects",
            "Certificates",
            "Contact"
        ],
        icons=[
            "house",
            "person",
            "cpu",
            "code-slash",
            "award",
            "telephone"
        ],
        default_index=0
    )

# ============================
# PAGE ROUTING
# ============================

if selected == "Home":
    from pages.home import home
    home()

elif selected == "About":
    from pages.about import about
    about()

elif selected == "Skills":
    from pages.skills import skills
    skills()

elif selected == "Projects":
    from pages.projects import projects
    projects()

elif selected == "Certificates":
    from pages.certificates import certificates
    certificates()

elif selected == "Contact":
    from pages.contact import contact
    contact()

# ============================
# FOOTER
# ============================

try:
    from components.statistics import statistics
    statistics()
except Exception:
    pass

try:
    from components.footer import footer
    footer()
except Exception:
    pass
