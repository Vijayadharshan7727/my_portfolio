import streamlit as st

projects = [
    {
        "title": "☕ Coffee Sales Prediction",
        "tech": "Python • Machine Learning • Linear Regression • Streamlit",
        "desc": """
Forecasts coffee sales using weather, temperature,
customer count, staffing and promotions.

Provides real-time predictions through an interactive
Streamlit dashboard.
""",
        "github": "https://github.com/Vijayadharshan7727"
    },
    {
        "title": "🛡 Insurance Prediction",
        "tech": "Python • Logistic Regression • Streamlit",
        "desc": """
Predicts whether a customer will purchase insurance
based on age using Machine Learning.

Interactive web application built with Streamlit.
""",
        "github": "https://github.com/Vijayadharshan7727"
    },
    {
        "title": "🤖 AI Financial Operating System",
        "tech": "FastAPI • AI • ML • Streamlit",
        "desc": """
Next-generation AI Finance Assistant capable of
expense prediction, fraud detection,
budget forecasting and financial insights.
""",
        "github": "https://github.com/Vijayadharshan7727"
    }
]

def projects():

    st.markdown("<div class='section'>🚀 Featured Projects</div>", unsafe_allow_html=True)

    cols = st.columns(3)

    for i, p in enumerate(projects):

        with cols[i % 3]:

            st.markdown(f"""
<div class="project-card">

<h2>{p['title']}</h2>

<p style="color:#38bdf8;"><b>{p['tech']}</b></p>

<p>{p['desc']}</p>

</div>
""", unsafe_allow_html=True)

            st.link_button(
                "🔗 GitHub",
                p["github"],
                use_container_width=True
            )
