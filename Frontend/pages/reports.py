import streamlit as st

from Backend.admin.report import (
    generate_user_report,
    generate_job_report,
    generate_application_report
)

from components.navbar import render_navbar
from components.sidebar import render_sidebar
from components.footer import render_footer


def show_reports():

    render_navbar()

    render_sidebar()

    st.title("Reports")

    report_type = st.selectbox(
        "Select Report",
        [
            "Users",
            "Jobs",
            "Applications"
        ]
    )

    st.write("")

    if st.button(
        "Generate Report",
        use_container_width=True
    ):

        if report_type == "Users":

            report = generate_user_report()

        elif report_type == "Jobs":

            report = generate_job_report()

        else:

            report = generate_application_report()

        if not report:

            st.warning(
                "No data available."
            )

        else:

            st.success(
                "Report generated successfully."
            )

            st.dataframe(
                report,
                use_container_width=True,
                hide_index=True
            )

            csv = report.to_csv(
                index=False
            )

            st.download_button(
                label="Download CSV",
                data=csv,
                file_name=f"{report_type.lower()}_report.csv",
                mime="text/csv",
                use_container_width=True
            )

    render_footer()