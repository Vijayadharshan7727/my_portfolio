import streamlit as st

def home():

    col1, col2 = st.columns([1, 2])

    with col1:

        st.image(
            "assets/1758645602569.png",
            width=280
        )

    with col2:

        st.markdown("""
<div class="hero">

<div class="big">

Vijayadharshan R

</div>

<div class="small">

🚀 AI Engineer

📊 Data Scientist

🤖 Machine Learning Developer

</div>

<br>

Artificial Intelligence & Data Science undergraduate passionate about
building intelligent systems using AI, Machine Learning,
Data Science and Full Stack Development.

<br><br>

📍 Coimbatore

📧 dharshanvijay7727@gmail.com

📱 +91 63842 27515

</div>

""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:

        st.link_button(
            "🐙 GitHub",
            "https://github.com/Vijayadharshan7727"
        )

    with c2:

        st.link_button(
            "💼 LinkedIn",
            "https://www.linkedin.com/in/dharshanvijay7727/"
        )

    with c3:

        with open("assets/resume.pdf", "rb") as file:

            st.download_button(
                "📄 Resume",
                file=file,
                file_name="Vijayadharshan_Resume.pdf"
            )

    st.markdown("<div class='section'>Career Objective</div>", unsafe_allow_html=True)

    st.markdown("""

I am an aspiring AI Engineer passionate about solving real-world
problems through Artificial Intelligence, Machine Learning,
Deep Learning, and Data Science.

My goal is to build impactful AI-powered products that improve
people's lives while continuously learning modern technologies.

""")
