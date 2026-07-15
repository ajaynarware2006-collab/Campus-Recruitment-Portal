import streamlit as st


def email_input():

    return st.text_input(
        "Email Address",
        placeholder="example@gmail.com"
    )


def password_input(label="Password"):

    return st.text_input(
        label,
        type="password",
        placeholder="Enter password"
    )


def name_input(label="Full Name"):

    return st.text_input(
        label,
        placeholder="Enter full name"
    )


def contact_input():

    return st.text_input(
        "Contact Number",
        placeholder="+91XXXXXXXXXX"
    )


def enrollment_input():

    return st.text_input(
        "Enrollment Number"
    )


def cgpa_input():

    return st.number_input(
        "CGPA",
        min_value=0.0,
        max_value=10.0,
        step=0.01
    )


def semester_input():

    return st.selectbox(
        "Semester",
        list(range(1, 9))
    )


def branch_input():

    return st.selectbox(
        "Branch",
        [
            "CSE",
            "CS-AIML",
            "IT",
            "ECE",
            "EE",
            "ME",
            "CE"
        ]
    )


def role_input():

    return st.selectbox(
        "Role",
        [
            "Student",
            "Recruiter",
            "Admin"
        ]
    )


def job_type_input():

    return st.selectbox(
        "Job Type",
        [
            "Full-Time",
            "Internship",
            "Part-Time",
            "Contract"
        ]
    )


def work_mode_input():

    return st.selectbox(
        "Work Mode",
        [
            "On-Site",
            "Remote",
            "Hybrid"
        ]
    )


def company_size_input():

    return st.selectbox(
        "Company Size",
        [
            "Startup",
            "Small",
            "Medium",
            "Enterprise"
        ]
    )


def status_input():

    return st.selectbox(
        "Status",
        [
            "Open",
            "Closed",
            "Draft"
        ]
    )


def resume_upload():

    return st.file_uploader(
        "Upload Resume",
        type=["pdf"]
    )


def image_upload(label="Upload Image"):

    return st.file_uploader(
        label,
        type=["png", "jpg", "jpeg"]
    )


def submit_button(label):

    return st.form_submit_button(
        label,
        use_container_width=True
    )