import streamlit as st

from utils.session import (
    set_current_page,
    user_logged_in,
    get_user_role
)


def redirect_dashboard():

    role = get_user_role()

    if role == "Student":
        set_current_page("student_dashboard")

    elif role == "Recruiter":
        set_current_page("recruiter_dashboard")

    elif role == "Admin":
        set_current_page("admin_dashboard")

    st.rerun()


def show_home():

    if user_logged_in():
        redirect_dashboard()
        return

    left, center, right = st.columns([1, 2, 1])

    with center:

        st.markdown(
            "<h1 style='text-align:center;'>Campus Recruitment Portal</h1>",
            unsafe_allow_html=True
        )

        st.write("")
        st.write("")

        st.markdown(
            """
            <div style='text-align:center;font-size:18px;'>
                Find internships, jobs and connect students with recruiters.
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")
        st.write("")
        st.write("")

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "Login",
                use_container_width=True
            ):
                set_current_page("login")
                st.rerun()

        with col2:

            if st.button(
                "Sign Up",
                use_container_width=True
            ):
                set_current_page("signup")
                st.rerun()