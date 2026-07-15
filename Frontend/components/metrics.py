import streamlit as st


def metric(
    title,
    value,
    delta=None,
    help_text=None
):

    st.metric(
        label=title,
        value=value,
        delta=delta,
        help=help_text
    )


def metric_row(metrics):

    columns = st.columns(len(metrics))

    for column, item in zip(columns, metrics):

        with column:

            st.metric(
                label=item["title"],
                value=item["value"],
                delta=item.get("delta"),
                help=item.get("help")
            )


def student_dashboard_metrics(
    applied,
    under_review,
    shortlisted,
    accepted,
    rejected,
    withdrawn
):

    metric_row([
        {
            "title": "Applied",
            "value": applied
        },
        {
            "title": "Under Review",
            "value": under_review
        },
        {
            "title": "Shortlisted",
            "value": shortlisted
        },
        {
            "title": "Accepted",
            "value": accepted
        },
        {
            "title": "Rejected",
            "value": rejected
        },
        {
            "title": "Withdrawn",
            "value": withdrawn
        }
    ])


def recruiter_dashboard_metrics(
    total_jobs,
    open_jobs,
    closed_jobs,
    draft_jobs,
    applications
):

    metric_row([
        {
            "title": "Total Jobs",
            "value": total_jobs
        },
        {
            "title": "Open",
            "value": open_jobs
        },
        {
            "title": "Closed",
            "value": closed_jobs
        },
        {
            "title": "Draft",
            "value": draft_jobs
        },
        {
            "title": "Applications",
            "value": applications
        }
    ])


def admin_dashboard_metrics(
    users,
    students,
    recruiters,
    jobs,
    applications
):

    metric_row([
        {
            "title": "Users",
            "value": users
        },
        {
            "title": "Students",
            "value": students
        },
        {
            "title": "Recruiters",
            "value": recruiters
        },
        {
            "title": "Jobs",
            "value": jobs
        },
        {
            "title": "Applications",
            "value": applications
        }
    ])