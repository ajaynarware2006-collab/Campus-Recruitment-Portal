import streamlit as st

from Backend.recruiter.analytics import (
    get_recruiter_analytics
)

from components.navbar import render_navbar
from components.sidebar import render_sidebar
from components.footer import render_footer

from components.metrics import (
    recruiter_dashboard_metrics
)

from components.charts import (
    bar_chart,
    pie_chart,
    line_chart
)

from utils.session import (
    get_user_id
)


def show_recruiter_analytics():

    render_navbar()

    render_sidebar()

    st.title("Recruiter Analytics")

    recruiter_id = get_user_id()

    analytics = get_recruiter_analytics(
        recruiter_id
    )

    if not analytics:

        st.info(
            "No analytics available."
        )

        render_footer()

        return

    (
        metrics,
        monthly_applications,
        application_status,
        top_jobs
    ) = analytics

    (
        total_jobs,
        open_jobs,
        closed_jobs,
        draft_jobs,
        total_applications
    ) = metrics

    recruiter_dashboard_metrics(
        total_jobs,
        open_jobs,
        closed_jobs,
        draft_jobs,
        total_applications
    )

    st.divider()

    st.subheader(
        "Monthly Applications"
    )

    line_chart(
        monthly_applications,
        x="Month",
        y="Applications",
        title="Monthly Applications"
    )

    st.divider()

    st.subheader(
        "Application Status"
    )

    pie_chart(
        application_status,
        names="Status",
        values="Count",
        title="Application Status Distribution"
    )

    st.divider()

    st.subheader(
        "Top Performing Jobs"
    )

    bar_chart(
        top_jobs,
        x="Job Title",
        y="Applications",
        title="Applications Per Job"
    )

    render_footer()