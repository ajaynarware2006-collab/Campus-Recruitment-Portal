import streamlit as st

from Backend.student.profile import (
    get_profile,
    update_profile
)

from components.navbar import render_navbar
from components.sidebar import render_sidebar
from components.footer import render_footer

from components.forms import (
    contact_input,
    enrollment_input,
    cgpa_input,
    semester_input,
    branch_input,
    image_upload,
    resume_upload,
    submit_button
)

from utils.session import (
    get_user_id,
    complete_profile
)


def show_student_profile():

    render_navbar()

    render_sidebar()

    st.title("Student Profile")

    student_id = get_user_id()

    profile = get_profile(student_id)

    if profile:

        st.success(
            "Profile loaded successfully."
        )

    with st.form("student_profile_form"):

        enrollment = enrollment_input()

        contact = contact_input()

        branch = branch_input()

        semester = semester_input()

        cgpa = cgpa_input()

        profile_image = image_upload(
            "Profile Image"
        )

        resume = resume_upload()

        submitted = submit_button(
            "Save Profile"
        )

    if submitted:

        image_path = None
        resume_path = None

        if profile_image:

            image_path = profile_image.name

        if resume:

            resume_path = resume.name

        success = update_profile(
            student_id,
            enrollment,
            contact,
            branch,
            semester,
            cgpa,
            image_path,
            resume_path
        )

        if success:

            complete_profile()

            st.success(
                "Profile updated successfully."
            )

            st.balloons()

        else:

            st.error(
                "Failed to update profile."
            )

    render_footer()