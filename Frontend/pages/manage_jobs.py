import streamlit as st

from Backend.recruiter.job import (
    get_all_jobs,
    delete_job,
    update_job_status
)

from components.navbar import render_navbar
from components.sidebar import render_sidebar
from components.footer import render_footer

from components.tables import jobs_table
from components.forms import (
    status_input
)

from utils.session import (
    get_user_id
)


def show_manage_jobs():

    render_navbar()

    render_sidebar()

    st.title("Manage Jobs")

    recruiter_id = get_user_id()

    jobs = get_all_jobs(
        recruiter_id
    )

    if not jobs:

        st.info(
            "No jobs found."
        )

        render_footer()

        return

    jobs_table(
        jobs
    )

    st.divider()

    st.subheader(
        "Update Job Status"
    )

    job_id = st.number_input(
        "Job ID",
        min_value=1,
        step=1
    )

    status = status_input()

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "Update Status",
            use_container_width=True
        ):

            success = update_job_status(
                job_id,
                status
            )

            if success:

                st.success(
                    "Job status updated successfully."
                )

                st.rerun()

            else:

                st.error(
                    "Unable to update job status."
                )

    with col2:

        if st.button(
            "Delete Job",
            use_container_width=True
        ):

            success = delete_job(
                job_id
            )

            if success:

                st.success(
                    "Job deleted successfully."
                )

                st.rerun()

            else:

                st.error(
                    "Unable to delete job."
                )

    render_footer()