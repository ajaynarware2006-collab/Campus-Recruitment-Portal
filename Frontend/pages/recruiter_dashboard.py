import streamlit as st

from Backend.recruiter.dashboard import dashboard

from components.navbar import render_navbar
from components.sidebar import render_sidebar
from components.footer import render_footer

from components.metrics import recruiter_dashboard_metrics
from components.charts import donut_chart

from utils.session import get_user_id


def show_recruiter_dashboard():

    render_navbar()

    render_sidebar()

    st.title("Recruiter Dashboard")

    recruiter_id = get_user_id()

    (
        job_stats,
        total_applications
    ) = dashboard(recruiter_id)

    (
        total_jobs,
        open_jobs,
        closed_jobs,
        draft_jobs
    ) = job_stats

    recruiter_dashboard_metrics(
        total_jobs,
        open_jobs,
        closed_jobs,
        draft_jobs,
        total_applications
    )

    chart_data = {
        "Status": [
            "Open",
            "Closed",
            "Draft"
        ],
        "Jobs": [
            open_jobs,
            closed_jobs,
            draft_jobs
        ]
    }

    st.write("")

    donut_chart(
        chart_data,
        names="Status",
        values="Jobs",
        title="Job Status Distribution"
    )

    render_footer()