import streamlit as st

from Backend.recruiter import (
    get_job_applications,
    update_application_status
)

from components.navbar import render_navbar
from components.sidebar import render_sidebar
from components.footer import render_footer

from components.tables import applications_table


from utils.session import (
    get_user_id
)


def show_view_applications():

    render_navbar()

    render_sidebar()

    st.title("View Applications")

    recruiter_id = get_user_id()

    applications = get_job_applications(
        recruiter_id
    )

    if not applications:

        st.info(
            "No applications received yet."
        )

        render_footer()

        return

    applications_table(
        applications
    )

    st.divider()

    st.subheader(
        "Update Application Status"
    )

    application_id = st.number_input(
        "Application ID",
        min_value=1,
        step=1
    )

    status = st.selectbox(
        "Application Status",
        [
            "Applied",
            "Under Review",
            "Shortlisted",
            "Accepted",
            "Rejected"
        ]
    )

    if st.button(
        "Update Status",
        use_container_width=True
    ):

        success = update_application_status(
            application_id,
            status
        )

        if success:

            st.success(
                "Application status updated successfully."
            )

            st.rerun()

        else:

            st.error(
                "Failed to update application status."
            )

    render_footer()