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

    return shortlist_application(
        connect_db,
        application_id
    )


def reject_candidate(application_id):

    return reject_application(
        connect_db,
        application_id
    )


def accept_candidate(application_id):

    return accept_application(
        connect_db,
        application_id
    )