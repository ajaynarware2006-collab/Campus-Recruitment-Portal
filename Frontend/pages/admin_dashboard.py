import streamlit as st

from Backend.admin.dashboard import (
    get_dashboard_statistics
)

from components.navbar import render_navbar
from components.sidebar import render_sidebar
from components.footer import render_footer

from components.metrics import (
    admin_dashboard_metrics
)

from components.charts import (
    bar_chart,
    donut_chart
)


def show_admin_dashboard():

    render_navbar()

    render_sidebar()

    st.title("Admin Dashboard")

    (
        metrics,
        user_distribution,
        monthly_registrations
    ) = get_dashboard_statistics()

    (
        total_users,
        total_students,
        total_recruiters,
        total_jobs,
        total_applications
    ) = metrics

    admin_dashboard_metrics(
        total_users,
        total_students,
        total_recruiters,
        total_jobs,
        total_applications
    )

    st.divider()

    donut_chart(
        user_distribution,
        names="Role",
        values="Count",
        title="Users Distribution"
    )

    st.divider()

    bar_chart(
        monthly_registrations,
        x="Month",
        y="Users",
        title="Monthly Registrations"
    )

    render_footer()