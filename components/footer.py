import streamlit as st

def footer():

    st.markdown("---")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("### 👨‍💻 Vijayadharshan R")

    with c2:
        st.markdown(
            "[GitHub](https://github.com/Vijayadharshan7727)"
        )

    with c3:
        st.markdown(
            "[LinkedIn](https://www.linkedin.com/in/dharshanvijay7727/)"
        )

    st.markdown(
        """
<div style='text-align:center;
padding:25px;
font-size:18px;
color:#94a3b8;'>

Made with ❤️ using Streamlit

© 2026 Vijayadharshan R

</div>
""",
        unsafe_allow_html=True
    )
