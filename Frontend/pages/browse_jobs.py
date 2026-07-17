import streamlit as st

from Backend.student.jobs import get_all_jobs,search_by_keyword

from components.navbar import render_navbar
from components.sidebar import render_sidebar
from components.footer import render_footer

from components.card import job_card

from utils.session import (
    set_current_page
)


def show_browse_jobs():

    render_navbar()

    render_sidebar()

    st.title("Browse Jobs")

    search = st.text_input(
        "Search by Job Title, Company or Location"
    )

    if search.strip():

        jobs = search_by_keyword(search)

    else:

        jobs = get_all_jobs()

    if not jobs:

        st.info(
            "No jobs available."
        )

        render_footer()

        return

    for job in jobs:

        (
            job_id,
            job_title,
            company_name,
            location,
            job_type,
            work_mode,
            salary,
            deadline
        ) = job

        job_card(
            job_title,
            company_name,
            location,
            job_type,
            work_mode,
            salary,
            deadline
        )

        if st.button(
            f"View Details ({job_title})",
            key=f"view_{job_id}",
            use_container_width=True
        ):

            st.session_state.selected_job = job_id

            set_current_page(
                "job_details"
            )

            st.rerun()

        st.divider()

    render_footer()