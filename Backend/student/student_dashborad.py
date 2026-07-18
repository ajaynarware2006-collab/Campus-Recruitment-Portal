from Backend.database.connection import connect_db
from Backend.database.dashboard_queries import student_dashboard


def dashboard(student_profile_id):

    return student_dashboard(
        connect_db,
        student_profile_id
    )