from database.connection import connect_db
from database.dashboard_queries import student_dashboard


def dashboard(student_profile_id):

    return student_dashboard(
        connect_db,
        student_profile_id
    )


def total_applications(student_profile_id):

    dashboard_data = student_dashboard(
        connect_db,
        student_profile_id
    )

    return dashboard_data[0]


def applications_under_review(student_profile_id):

    dashboard_data = student_dashboard(
        connect_db,
        student_profile_id
    )

    return dashboard_data[1]


def shortlisted_applications(student_profile_id):

    dashboard_data = student_dashboard(
        connect_db,
        student_profile_id
    )

    return dashboard_data[2]


def accepted_applications(student_profile_id):

    dashboard_data = student_dashboard(
        connect_db,
        student_profile_id
    )

    return dashboard_data[3]


def rejected_applications(student_profile_id):

    dashboard_data = student_dashboard(
        connect_db,
        student_profile_id
    )

    return dashboard_data[4]


def withdrawn_applications(student_profile_id):

    dashboard_data = student_dashboard(
        connect_db,
        student_profile_id
    )

    return dashboard_data[5]