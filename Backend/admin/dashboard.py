from database.connection import connect_db
from database.dashboard_queries import admin_dashboard


def dashboard():

    return admin_dashboard(
        connect_db
    )


def total_users():

    dashboard_data = admin_dashboard(
        connect_db
    )

    return dashboard_data[0]


def total_students():

    dashboard_data = admin_dashboard(
        connect_db
    )

    return dashboard_data[1]


def total_recruiters():

    dashboard_data = admin_dashboard(
        connect_db
    )

    return dashboard_data[2]


def total_jobs():

    dashboard_data = admin_dashboard(
        connect_db
    )

    return dashboard_data[3]


def total_applications():

    dashboard_data = admin_dashboard(
        connect_db
    )

    return dashboard_data[4]