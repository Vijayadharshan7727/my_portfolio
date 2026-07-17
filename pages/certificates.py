import streamlit as st

certificates = [

("🏆 AI Internship - Elevate Labs",
"Best Performer Certificate",
"https://drive.google.com/file/d/1ZpnFJ-K4yQ7x8rq1rmvMxn0UUlKDuek0/view"),

("🤖 IBM AI",
"Coursera",
"https://www.coursera.org/account/accomplishments/verify/DU13YJ7YDRM2"),

("📊 IBM Data Science",
"Coursera",
"https://www.coursera.org/account/accomplishments/verify/OW437Z6XYLGS"),

("🛡 Ethical Hacking",
"LearnKart",
"https://www.coursera.org/account/accomplishments/verify/6UH0M19B1WK0"),

("📈 Excel",
"Macquarie University",
"https://www.coursera.org/account/accomplishments/verify/0JN1HAX20V9H"),

("🐙 Git & GitHub",
"Google",
"https://www.coursera.org/account/accomplishments/verify/EMA7AAF6V4N1"),

("📊 Power BI",
"Corporate Finance Institute",
"https://www.coursera.org/account/accomplishments/verify/C9J80X99KUBW"),

("☕ Java",
"HackerRank",
"https://drive.google.com/file/d/1jCpHb5szaaVEt4zAUAyTFNh2TKfnXQZA/view"),

("🌐 HTML & CSS",
"Scrimba",
"https://www.coursera.org/account/accomplishments/verify/27BGX4NFZV97"),

("💡 Design Thinking",
"University of Virginia",
"https://www.coursera.org/account/accomplishments/verify/J67TRNBGGGQP")
]

def certificates():

    st.markdown("<div class='section'>🏆 Certifications</div>", unsafe_allow_html=True)

    cols = st.columns(2)

    for i, cert in enumerate(certificates):

        with cols[i % 2]:

            st.markdown(f"""
<div class="cert-card">

<h3>{cert[0]}</h3>

<p>{cert[1]}</p>

</div>
""", unsafe_allow_html=True)

            st.link_button(
                "📜 View Certificate",
                cert[2],
                use_container_width=True
            )
