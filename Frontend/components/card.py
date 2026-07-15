import streamlit as st


def statistic_card(title, value, icon):

    st.markdown(
        f"""
        <div class="card">
            <h3>{icon} {title}</h3>
            <h1>{value}</h1>
        </div>
        """,
        unsafe_allow_html=True
    )


def job_card(
    job_title,
    company_name,
    location,
    job_type,
    work_mode,
    salary,
    deadline
):

    st.markdown(
        f"""
        <div class="card">

        <h3>{job_title}</h3>

        <p><b>Company:</b> {company_name}</p>

        <p><b>Location:</b> {location}</p>

        <p><b>Job Type:</b> {job_type}</p>

        <p><b>Work Mode:</b> {work_mode}</p>

        <p><b>Salary:</b> {salary}</p>

        <p><b>Deadline:</b> {deadline}</p>

        </div>
        """,
        unsafe_allow_html=True
    )


def recruiter_card(
    company_name,
    recruiter_name,
    industry,
    company_size
):

    st.markdown(
        f"""
        <div class="card">

        <h3>{company_name}</h3>

        <p><b>Recruiter:</b> {recruiter_name}</p>

        <p><b>Industry:</b> {industry}</p>

        <p><b>Company Size:</b> {company_size}</p>

        </div>
        """,
        unsafe_allow_html=True
    )


def student_card(
    student_name,
    branch,
    semester,
    cgpa
):

    st.markdown(
        f"""
        <div class="card">

        <h3>{student_name}</h3>

        <p><b>Branch:</b> {branch}</p>

        <p><b>Semester:</b> {semester}</p>

        <p><b>CGPA:</b> {cgpa}</p>

        </div>
        """,
        unsafe_allow_html=True
    )


def application_card(
    student_name,
    job_title,
    status
):

    color = {

        "Applied": "#3b82f6",
        "Under Review": "#f59e0b",
        "Shortlisted": "#8b5cf6",
        "Accepted": "#10b981",
        "Rejected": "#ef4444",
        "Withdrawn": "#6b7280"

    }.get(status, "#94a3b8")

    st.markdown(
        f"""
        <div class="card">

        <h3>{student_name}</h3>

        <p><b>Job:</b> {job_title}</p>

        <p>
            <b>Status:</b>
            <span style="color:{color};">
                {status}
            </span>
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )