import streamlit as st

def statistics():

    st.markdown(
        "<div class='section'>📈 Portfolio Highlights</div>",
        unsafe_allow_html=True
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Projects", "3+")

    with c2:
        st.metric("Certificates", "10+")

    with c3:
        st.metric("Technologies", "20+")

    with c4:
        st.metric("Programming Languages", "6+")
