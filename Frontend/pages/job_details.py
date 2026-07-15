import streamlit as st

from Backend.student.jobs import (
    get_job_details
)

from components.navbar import render_navbar
from components.sidebar import render_sidebar
from components.footer import render_footer

from utils.session import (
    set_current_page
)


def show_job_details():

    render_navbar()

    render_sidebar()

    job_id = st.session_state.get(
        "selected_job"
    )

    if job_id is None:

        st.warning(
            "No job selected."
        )

        render_footer()

        return

    job = get_job_details(
        job_id
    )

    if not job:

        st.error(
            "Job not found."
        )

        render_footer()

        return

    (
        job_title,
        company_name,
        location,
        job_type,
        work_mode,
        salary,
        experience,
        description,
        skills_required,
        deadline
    ) = job

    st.title(job_title)

    st.subheader(company_name)

    st.write(f"📍 Location : {location}")

    st.write(f"💼 Job Type : {job_type}")

    st.write(f"🏢 Work Mode : {work_mode}")

    st.write(f"💰 Salary : {salary}")

    st.write(f"⭐ Experience : {experience}")

    st.write(f"📅 Last Date : {deadline}")

    st.divider()

    st.subheader("Job Description")

    st.write(description)

    st.divider()

    st.subheader("Required Skills")

    st.write(skills_required)

    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "Apply Now",
            use_container_width=True
        ):

            set_current_page(
                "apply_job"
            )

            st.rerun()

    with col2:

        if st.button(
            "Back",
            use_container_width=True
        ):

            set_current_page(
                "browse_jobs"
            )

            st.rerun()

    render_footer()