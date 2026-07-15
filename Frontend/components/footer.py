import streamlit as st


def render_footer():

    st.divider()

    left, center, right = st.columns(3)

    with left:

        st.caption(
            "© 2026 Campus Recruitment Portal"
        )

    with center:

        st.caption(
            "Version 1.0.0"
        )

    with right:

        st.caption(
            "Developed by Ajay Narware"
        )