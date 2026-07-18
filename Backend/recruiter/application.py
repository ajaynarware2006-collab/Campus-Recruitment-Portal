from Backend.database.connection import connect_db
from Backend.database.application_queries import (
    shortlist_application,
    reject_application,
    accept_application,
    get_job_applications,
    get_application
)


def view_applicants(job_id):

    return get_job_applications(
        connect_db,
        job_id
    )


def view_applicant(application_id):

    return get_application(
        application_id,
        connect_db
    )


def shortlist_candidate(application_id):

    result = shortlist_application(
        connect_db,
        application_id
    )

    if not result:
        return "Unable to shortlist candidate."

    return result


def reject_candidate(application_id):

    result = reject_application(
        connect_db,
        application_id
    )

    if not result:
        return "Unable to reject candidate."

    return result


def accept_candidate(application_id):

    result = accept_application(
        connect_db,
        application_id
    )

    if not result:
        return "Unable to accept candidate."

    return result