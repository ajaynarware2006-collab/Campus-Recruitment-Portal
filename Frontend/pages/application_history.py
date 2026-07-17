import streamlit as st

from Backend.student.application import (
    view_application_history,
    withdraw_application
)

from components.navbar import render_navbar
from components.sidebar import render_sidebar
from components.footer import render_footer

from components.tables import applications_table

from utils.session import (
    get_user_id
)


def show_application_history():

    render_navbar()

    render_sidebar()

    st.title("Application History")

    student_id = get_user_id()

    applications = view_application_history(
        student_id
    )

    if not applications:

        st.info(
            "You haven't applied for any jobs yet."
        )

        render_footer()

        return

    applications_table(
        applications
    )

    st.write("")

    application_id = st.number_input(
        "Application ID",
        min_value=1,
        step=1
    )

    if st.button(
        "Withdraw Application",
        use_container_width=True
    ):

        success = withdraw_application(
            application_id
        )

        if success:

            st.success(
                "Application withdrawn successfully."
            )

            st.rerun()

        else:

            st.error(
                "Unable to withdraw application."
            )

    render_footer()