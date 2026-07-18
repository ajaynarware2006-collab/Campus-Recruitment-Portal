from Backend.database.connection import connect_db
from Backend.database.dashboard_queries import recruiter_dashboard


def dashboard(recruiter_profile_id):

    return recruiter_dashboard(
        connect_db,
        recruiter_profile_id
    )