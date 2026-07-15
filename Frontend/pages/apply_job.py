import streamlit as st

from Backend.student.application import (
    apply_for_job
)

from components.navbar import render_navbar
from components.sidebar import render_sidebar
from components.footer import render_footer

from components.dialogs import (
    success,
    error,
    warning
)

from utils.session import (
    get_user_id,
    set_current_page
)


def show_apply_job():

    render_navbar()

    render_sidebar()

    st.title("Apply for Job")

    student_id = get_user_id()

    job_id = st.session_state.get(
        "selected_job"
    )

    if job_id is None:

        warning(
            "Please select a job first."
        )

        if st.button(
            "Browse Jobs",
            use_container_width=True
        ):

            set_current_page(
                "browse_jobs"
            )

            st.rerun()

        render_footer()

        return

    st.info(
        f"You are applying for Job ID: {job_id}"
    )

    agree = st.checkbox(
        "I confirm that all the information in my profile is correct."
    )

    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        apply = st.button(
            "Apply",
            use_container_width=True
        )

    with col2:

        cancel = st.button(
            "Cancel",
            use_container_width=True
        )

    if apply:

        if not agree:

            warning(
                "Please confirm before applying."
            )

            render_footer()

            return

        result = apply_for_job(
            student_id,
            job_id
        )

        if result:

            success(
                "Application submitted successfully."
            )

            st.balloons()

        else:

            error(
                "Application submission failed."
            )

    if cancel:

        set_current_page(
            "job_details"
        )

        st.rerun()

    render_footer()