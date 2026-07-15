import streamlit as st

from utils.session import (
    user_logged_in,
    get_user_role,
    logout_user,
    set_current_page
)


def render_navbar():

    left, middle, right = st.columns([2, 6, 2])

    with left:

        st.markdown("## 🎓 Campus Portal")

    with middle:

        if user_logged_in():

            role = get_user_role()

            st.markdown(
                f"### Welcome, **{role}**"
            )

    with right:

        if user_logged_in():

            if st.button(
                "Logout",
                use_container_width=True
            ):

                logout_user()

                set_current_page("home")

                st.rerun()