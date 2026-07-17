from Backend.database.connection import connect_db
from Backend.database.job_queries import (
    create_job,
    update_job,
    delete_job,
    get_job,
    get_all_jobs,
    get_recruiter_jobs
)


def post_job(
    recruiter_profile_id,
    job_title,
    job_description,
    job_type,
    work_mode,
    location,
    salary_min,
    salary_max,
    experience_required,
    cgpa_required,
    skills_required,
    openings,
    application_deadline,
    status="Open"
):

    if job_title.strip() == "":
        return False

    if job_description.strip() == "":
        return False

    if openings <= 0:
        return False

    job_id = create_job(
        connect_db,
        recruiter_profile_id,
        job_title,
        job_description,
        job_type,
        work_mode,
        location,
        salary_min,
        salary_max,
        experience_required,
        cgpa_required,
        skills_required,
        openings,
        application_deadline,
        status
    )

    if job_id is None:
        return False

    return job_id


def edit_job(
    job_id,
    job_title,
    job_description,
    job_type,
    work_mode,
    location,
    salary_min,
    salary_max,
    experience_required,
    cgpa_required,
    skills_required,
    openings,
    application_deadline,
    status
):

    if job_title.strip() == "":
        return False

    if job_description.strip() == "":
        return False

    if openings <= 0:
        return False

    return update_job(
        connect_db,
        job_id,
        job_title,
        job_description,
        job_type,
        work_mode,
        location,
        salary_min,
        salary_max,
        experience_required,
        cgpa_required,
        skills_required,
        openings,
        application_deadline,
        status
    )


def remove_job(job_id):

    return delete_job(connect_db, job_id)


def view_job(job_id):

    return get_job(job_id, connect_db)


def view_all_jobs():

    return get_all_jobs(connect_db)


def view_my_jobs(recruiter_profile_id):

    return get_recruiter_jobs(
        connect_db,
        recruiter_profile_id
    )