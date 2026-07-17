import streamlit as st

from Backend.student.dashborad import dashboard

from components.navbar import render_navbar
from components.sidebar import render_sidebar
from components.footer import render_footer

from components.metrics import student_dashboard_metrics
from components.charts import donut_chart

from utils.session import get_user_id


def show_student_dashboard():

    render_navbar()

    render_sidebar()

    st.title("Student Dashboard")

    student_id = get_user_id()

    data = dashboard(student_id)

    (
        applied,
        under_review,
        shortlisted,
        accepted,
        rejected,
        withdrawn
    ) = data

    student_dashboard_metrics(
        applied,
        under_review,
        shortlisted,
        accepted,
        rejected,
        withdrawn
    )

    chart_data = {
        "Status": [
            "Applied",
            "Under Review",
            "Shortlisted",
            "Accepted",
            "Rejected",
            "Withdrawn"
        ],
        "Count": [
            applied,
            under_review,
            shortlisted,
            accepted,
            rejected,
            withdrawn
        ]
    }

    st.write("")

    donut_chart(
        chart_data,
        names="Status",
        values="Count",
        title="Application Status Overview"
    )

    render_footer()