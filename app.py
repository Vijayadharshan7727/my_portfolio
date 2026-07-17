import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Vijayadharshan | AI Portfolio",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ----------------------------
# LOAD CSS
# ----------------------------

def load_css():
    with open("css/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# ----------------------------
# SIDEBAR
# ----------------------------

with st.sidebar:

    st.image("assets/1758645602569.png", width=180)

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

# ----------------------------
# HOME
# ----------------------------

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
