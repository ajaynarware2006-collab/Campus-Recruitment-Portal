import streamlit as st

from Backend.auth.login import login_user

from utils.session import (
    login_user as session_login,
    set_current_page
)


def show_login():

    st.title("Login")

    with st.form("login_form"):

        email = st.text_input(
            "Email Address"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        submitted = st.form_submit_button(
            "Login",
            use_container_width=True
        )

    if submitted:

        result = login_user(
            email,
            password
        )

        if isinstance(result, str):
            st.error(result)
            return

        role, user_id = result

        session_login(
            user_id=user_id,
            email=email,
            role=role
        )

        if role == "Student":

            set_current_page(
                "student_profile"
            )

        elif role == "Recruiter":

            set_current_page(
                "recruiter_dashboard"
            )

        elif role == "Admin":

            set_current_page(
                "admin_dashboard"
            )

        st.success(
            f"Welcome {role}!"
        )

        st.rerun()

    st.write("")
    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "Create Account",
            use_container_width=True
        ):

            set_current_page(
                "signup"
            )

            st.rerun()

    with col2:

        if st.button(
            "Forgot Password",
            use_container_width=True
        ):

            set_current_page(
                "forgot_password"
            )

            st.rerun()