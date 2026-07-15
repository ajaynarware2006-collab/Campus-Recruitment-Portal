import pandas as pd
import streamlit as st


def jobs_table(jobs):

    columns = [
        "Job ID",
        "Job Title",
        "Company",
        "Location",
        "Job Type",
        "Work Mode",
        "Salary",
        "Deadline",
        "Status"
    ]

    dataframe = pd.DataFrame(
        jobs,
        columns=columns
    )

    st.dataframe(
        dataframe,
        use_container_width=True,
        hide_index=True
    )


def students_table(students):

    columns = [
        "Student ID",
        "Name",
        "Branch",
        "Semester",
        "CGPA",
        "Contact"
    ]

    dataframe = pd.DataFrame(
        students,
        columns=columns
    )

    st.dataframe(
        dataframe,
        use_container_width=True,
        hide_index=True
    )


def recruiters_table(recruiters):

    columns = [
        "Recruiter ID",
        "Company",
        "HR Name",
        "Industry",
        "Company Size",
        "Email"
    ]

    dataframe = pd.DataFrame(
        recruiters,
        columns=columns
    )

    st.dataframe(
        dataframe,
        use_container_width=True,
        hide_index=True
    )


def applications_table(applications):

    columns = [
        "Application ID",
        "Student",
        "Job",
        "Company",
        "Applied On",
        "Status"
    ]

    dataframe = pd.DataFrame(
        applications,
        columns=columns
    )

    st.dataframe(
        dataframe,
        use_container_width=True,
        hide_index=True
    )


def users_table(users):

    columns = [
        "User ID",
        "Email",
        "Role",
        "Status",
        "Created At"
    ]

    dataframe = pd.DataFrame(
        users,
        columns=columns
    )

    st.dataframe(
        dataframe,
        use_container_width=True,
        hide_index=True
    )