from database.connection import connect_db
from database.application_queries import (
    apply_job,
    withdraw_application,
    get_student_applications,
    get_application
)


def apply_for_job(
    job_id,
    student_profile_id
):

    application_id = apply_job(
        connect_db,
        job_id,
        student_profile_id
    )

    if application_id is None:
        return False

    return application_id


def withdraw_job_application(
    application_id
):

    return withdraw_application(
        connect_db,
        application_id
    )


def view_my_applications(
    student_profile_id
):

    return get_student_applications(
        connect_db,
        student_profile_id
    )


def view_application(
    application_id
):

    return get_application(
        application_id,
        connect_db
    )