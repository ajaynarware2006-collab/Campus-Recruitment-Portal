import streamlit as st

from Backend.auth.signup import register_user

from utils.session import (
    login_user,
    set_current_page
)


def show_signup():

    st.title("Create Account")

    st.write("")

    with st.form("signup_form"):

        name = st.text_input(
            "Full Name"
        )

        email = st.text_input(
            "Email Address"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        confirm_password = st.text_input(
            "Confirm Password",
            type="password"
        )

        role = st.selectbox(
            "Select Role",
            [
                "Student",
                "Recruiter",
                "Admin"
            ]
        )

        submitted = st.form_submit_button(
            "Create Account",
            use_container_width=True
        )

    if submitted:

        if password != confirm_password:

            st.error(
                "Passwords do not match."
            )

            return

        result = register_user(
            name,
            email,
            password,
            role
        )

        if result is False:

            st.error(
                "Email already exists."
            )

            return

        if isinstance(result, str):

            st.error(
                result
            )

            return

        login_user(
            user_id=result,
            email=email,
            role=role
        )

        if role == "Student":

            set_current_page(
                "student_profile"
            )

        elif role == "Recruiter":

            set_current_page(
                "recruiter_profile"
            )

        elif role == "Admin":

            set_current_page(
                "admin_dashboard"
            )

        st.success(
            "Account created successfully."
        )

        st.rerun()

    st.write("")
    st.write("")

    if st.button(
        "Already have an account?",
        use_container_width=True
    ):

        set_current_page(
            "login"
        )

        st.rerun()