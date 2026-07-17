import streamlit as st

def about():

    st.markdown("<div class='section'>👨 About Me</div>", unsafe_allow_html=True)

    st.markdown("""
<div class="card">

<h2>Who am I?</h2>

<p style="font-size:18px; line-height:1.8;">

I'm <b>Vijayadharshan R</b>, an aspiring
<b>Artificial Intelligence & Data Science Engineer</b>
passionate about solving real-world problems through intelligent systems.

I enjoy building AI-powered applications, creating data-driven
solutions, and continuously learning modern technologies.

My interests include Artificial Intelligence,
Machine Learning, Deep Learning,
Data Analytics, Computer Vision,
Natural Language Processing,
Backend Development, and Cloud Computing.

I believe technology should solve meaningful problems and
make people's lives easier.

</p>

</div>

""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("<div class='section'>🎓 Education</div>", unsafe_allow_html=True)

    st.markdown("""

<div class="card">

### 🎓 B.Tech Artificial Intelligence & Data Science

🏫 Rathinam Technical Campus

📍 Coimbatore

📅 2024 - 2028

Currently pursuing Bachelor's Degree with strong interest in
Machine Learning, Deep Learning, Data Science and Software Development.

</div>

""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    c1,c2,c3,c4=st.columns(4)

    with c1:
        st.metric("Projects","2+")

    with c2:
        st.metric("Certificates","10+")

    with c3:
        st.metric("Languages","6+")

    with c4:
        st.metric("AI Tools","20+")
