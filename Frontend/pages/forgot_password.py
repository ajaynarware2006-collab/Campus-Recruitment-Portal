import streamlit as st

from utils.session import set_current_page


def show_forgot_password():

    st.title("Forgot Password")

    st.write(
        """
        Enter your registered email address.
        Password reset functionality will be connected with the backend later.
        """
    )

    with st.form("forgot_password_form"):

        email = st.text_input(
            "Registered Email"
        )

        submitted = st.form_submit_button(
            "Send Reset Link",
            use_container_width=True
        )

    if submitted:

        if email.strip() == "":

            st.error(
                "Please enter your email."
            )

            return

        st.info(
            "Password reset service will be integrated in the next phase."
        )

    st.write("")
    st.write("")

    if st.button(
        "Back to Login",
        use_container_width=True
    ):

        set_current_page(
            "login"
        )

        st.rerun()