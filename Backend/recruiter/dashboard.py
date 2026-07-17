from Backend.database.connection import connect_db
from Backend.database.dashboard_queries import recruiter_dashboard


def dashboard(recruiter_profile_id):

    return recruiter_dashboard(
        connect_db,
        recruiter_profile_id
    )


def total_jobs(recruiter_profile_id):

    dashboard_data = recruiter_dashboard(
        connect_db,
        recruiter_profile_id
    )

    return dashboard_data[0][0]


def open_jobs(recruiter_profile_id):

    dashboard_data = recruiter_dashboard(
        connect_db,
        recruiter_profile_id
    )

    return dashboard_data[0][1]


def closed_jobs(recruiter_profile_id):

    dashboard_data = recruiter_dashboard(
        connect_db,
        recruiter_profile_id
    )

    return dashboard_data[0][2]


def draft_jobs(recruiter_profile_id):

    dashboard_data = recruiter_dashboard(
        connect_db,
        recruiter_profile_id
    )

    return dashboard_data[0][3]


def total_applications(recruiter_profile_id):

    dashboard_data = recruiter_dashboard(
        connect_db,
        recruiter_profile_id
    )

    return dashboard_data[1]