import streamlit as st

from Backend.recruiter import (
    create_job
)

from components.navbar import render_navbar
from components.sidebar import render_sidebar
from components.footer import render_footer

from components.forms import (
    job_type_input,
    work_mode_input,
    status_input,
    submit_button
)

from utils.session import (
    get_user_id
)


def show_post_job():

    render_navbar()

    render_sidebar()

    st.title("Post New Job")

    recruiter_id = get_user_id()

    with st.form("post_job_form"):

        job_title = st.text_input(
            "Job Title"
        )

        location = st.text_input(
            "Job Location"
        )

        job_type = job_type_input()

        work_mode = work_mode_input()

        salary = st.text_input(
            "Salary Package"
        )

        experience = st.text_input(
            "Experience Required"
        )

        openings = st.number_input(
            "Number of Openings",
            min_value=1,
            step=1
        )

        deadline = st.date_input(
            "Application Deadline"
        )

        skills_required = st.text_area(
            "Required Skills",
            height=150
        )

        eligibility = st.text_area(
            "Eligibility Criteria",
            height=150
        )

        job_description = st.text_area(
            "Job Description",
            height=250
        )

        status = status_input()

        submitted = submit_button(
            "Post Job"
        )

    if submitted:

        success = create_job(
            recruiter_id,
            job_title,
            location,
            job_type,
            work_mode,
            salary,
            experience,
            openings,
            deadline,
            skills_required,
            eligibility,
            job_description,
            status
        )

        if success:

            st.success(
                "Job posted successfully."
            )

            st.balloons()

        else:

            st.error(
                "Failed to post job."
            )

    render_footer()