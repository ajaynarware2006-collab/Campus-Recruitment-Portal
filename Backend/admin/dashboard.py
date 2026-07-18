from Backend.database.connection import connect_db
from Backend.database.dashboard_queries import admin_dashboard


def dashboard():

    return admin_dashboard(
        connect_db
    )