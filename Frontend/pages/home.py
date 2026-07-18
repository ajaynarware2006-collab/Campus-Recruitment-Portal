import streamlit as st

from utils.session import (
    set_current_page,
    user_logged_in,
    get_user_role
)


def redirect_dashboard():

    role = get_user_role()

    if role == "Student":
        set_current_page("student_profile")

    elif role == "Recruiter":
        set_current_page("recruiter_dashboard")

    elif role == "Admin":
        set_current_page("admin_dashboard")

    st.rerun()


def show_home():

    if user_logged_in():
        redirect_dashboard()
        return

    _, center, _ = st.columns([1, 2, 1])

    with center:

        st.markdown(
            """
            <h1 style="text-align:center;">
                🎓 Campus Recruitment Portal
            </h1>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <p style="text-align:center;font-size:18px;color:gray;">
                Connect Students, Recruiters and Opportunities
            </p>
            """,
            unsafe_allow_html=True
        )

        st.write("")
        st.write("")

        st.info(
            "Build your profile, explore jobs, apply with one click, "
            "and track your applications—all from one platform."
        )

        st.write("")
        st.write("")

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "🔑 Login",
                use_container_width=True
            ):
                set_current_page("login")
                st.rerun()

        with col2:

            if st.button(
                "📝 Sign Up",
                use_container_width=True
            ):
                set_current_page("signup")
                st.rerun()