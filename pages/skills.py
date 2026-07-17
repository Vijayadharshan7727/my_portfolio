import streamlit as st

def skill_bar(title,value):

    st.markdown(f"### {title}")

    st.progress(value)

    st.write(f"{value}%")

def skills():

    st.markdown("<div class='section'>💻 Technical Skills</div>", unsafe_allow_html=True)

    col1,col2=st.columns(2)

    with col1:

        skill_bar("Python",95)

        skill_bar("Java",92)

        skill_bar("Machine Learning",90)

        skill_bar("Deep Learning",85)

        skill_bar("Data Science",90)

        skill_bar("SQL",88)

    with col2:

        skill_bar("HTML & CSS",90)

        skill_bar("JavaScript",80)

        skill_bar("Node JS",78)

        skill_bar("Power BI",88)

        skill_bar("AWS",80)

        skill_bar("Git & GitHub",90)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("<div class='section'>⚙ Technologies</div>", unsafe_allow_html=True)

    c1,c2,c3=st.columns(3)

    with c1:

        st.markdown("""

<div class="card">

### 🤖 AI

• Machine Learning

• Deep Learning

• NLP

• Computer Vision

• Generative AI

</div>

""",unsafe_allow_html=True)

    with c2:

        st.markdown("""

<div class="card">

### 📊 Data Science

• Pandas

• NumPy

• Matplotlib

• Scikit-learn

• Power BI

• Excel

</div>

""",unsafe_allow_html=True)

    with c3:

        st.markdown("""

<div class="card">

### 💻 Development

• Java

• Python

• C++

• HTML

• CSS

• JavaScript

• Node.js

• MySQL

</div>

""",unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("<div class='section'>🚀 Strengths</div>", unsafe_allow_html=True)

    c1,c2=st.columns(2)

    with c1:

        st.success("✔ Logical Thinking")

        st.success("✔ Problem Solving")

        st.success("✔ Quick Learner")

        st.success("✔ Team Work")

    with c2:

        st.success("✔ Leadership")

        st.success("✔ Communication")

        st.success("✔ Time Management")

        st.success("✔ Creativity")
