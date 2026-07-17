import streamlit as st
import os

def home():

    col1, col2 = st.columns([1, 2])

    with col1:
        image_path = "assets/profile.png"

        if os.path.exists(image_path):
            st.image(image_path, width=280)
        else:
            st.warning("Profile image not found.")

    with col2:

        st.markdown("""
<div class="hero">

<div class="big">
Vijayadharshan R
</div>

<div class="small">

🚀 AI Engineer<br>
📊 Data Scientist<br>
🤖 Machine Learning Developer

</div>

<br>

Artificial Intelligence & Data Science undergraduate passionate about
building intelligent AI applications, Machine Learning models,
Data Science solutions and Full Stack applications.

<br><br>

📍 Coimbatore

📧 dharshanvijay7727@gmail.com

📱 +91 63842 27515

</div>
""", unsafe_allow_html=True)

    st.write("")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.link_button(
            "🐙 GitHub",
            "https://github.com/Vijayadharshan7727",
            use_container_width=True
        )

    with c2:
        st.link_button(
            "💼 LinkedIn",
            "https://www.linkedin.com/in/dharshanvijay7727/",
            use_container_width=True
        )

    with c3:

        resume_path = "assets/resume.pdf"

        if os.path.exists(resume_path):

            with open(resume_path, "rb") as pdf_file:

                st.download_button(
                    label="📄 Download Resume",
                    data=pdf_file.read(),
                    file_name="Vijayadharshan_Resume.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )

        else:
            st.warning("Resume not found.")

    st.markdown("<div class='section'>Career Objective</div>", unsafe_allow_html=True)

    st.markdown("""

I am an aspiring Artificial Intelligence & Data Science Engineer
who enjoys building intelligent software using Machine Learning,
Deep Learning, Data Analytics and Full Stack Development.

I love solving real-world problems through AI and continuously
learning modern technologies.

""")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("<div class='section'>Quick Highlights</div>", unsafe_allow_html=True)

    a, b, c, d = st.columns(4)

    with a:
        st.metric("Projects", "3+")

    with b:
        st.metric("Certificates", "10+")

    with c:
        st.metric("Skills", "20+")

    with d:
        st.metric("Experience", "AI & DS Student")
