import streamlit as st

from Backend.recruiter.profile import (
    get_profile,
    update_profile
)

from components.navbar import render_navbar
from components.sidebar import render_sidebar
from components.footer import render_footer

from components.forms import (
    contact_input,
    company_size_input,
    image_upload,
    submit_button
)

from utils.session import (
    get_user_id,
    complete_profile
)


def show_recruiter_profile():

    render_navbar()

    render_sidebar()

    st.title("Recruiter Profile")

    recruiter_id = get_user_id()

    profile = get_profile(
        recruiter_id
    )

    if profile:

        st.success(
            "Profile loaded successfully."
        )

    with st.form("recruiter_profile_form"):

        company_name = st.text_input(
            "Company Name"
        )

        hr_name = st.text_input(
            "HR Name"
        )

        contact = contact_input()

        company_email = st.text_input(
            "Company Email"
        )

        website = st.text_input(
            "Website"
        )

        industry = st.text_input(
            "Industry"
        )

        headquarters = st.text_input(
            "Headquarters"
        )

        company_size = company_size_input()

        founded_year = st.number_input(
            "Founded Year",
            min_value=1900,
            max_value=2100,
            step=1
        )

        company_description = st.text_area(
            "Company Description",
            height=180
        )

        company_logo = image_upload(
            "Company Logo"
        )

        submitted = submit_button(
            "Save Company Profile"
        )

    if submitted:

        logo_path = None

        if company_logo:

            logo_path = company_logo.name

        success = update_profile(
            recruiter_id,
            company_name,
            hr_name,
            contact,
            company_email,
            website,
            industry,
            headquarters,
            company_size,
            founded_year,
            company_description,
            logo_path
        )

        if success:

            complete_profile()

            st.success(
                "Company profile updated successfully."
            )

            st.balloons()

        else:

            st.error(
                "Failed to update company profile."
            )

    render_footer()