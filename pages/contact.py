import streamlit as st

def contact():

    st.markdown("<div class='section'>📬 Contact Me</div>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])

    with col1:

        st.markdown("""
<div class="contact-card">

<h2>Let's Connect 🚀</h2>

<p>📧 dharshanvijay7727@gmail.com</p>

<p>📱 +91 63842 27515</p>

<p>📍 Coimbatore, Tamil Nadu</p>

</div>

""", unsafe_allow_html=True)

        st.link_button(
            "💼 LinkedIn",
            "https://www.linkedin.com/in/dharshanvijay7727/",
            use_container_width=True
        )

        st.link_button(
            "🐙 GitHub",
            "https://github.com/Vijayadharshan7727",
            use_container_width=True
        )

    with col2:

        st.text_input("Your Name")

        st.text_input("Email")

        st.text_input("Subject")

        st.text_area(
            "Message",
            height=180
        )

        if st.button("🚀 Send Message", use_container_width=True):
            st.success("Thanks! Your message has been received.")
