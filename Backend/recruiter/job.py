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

    if not job_title.strip():
        return "Job title cannot be empty."

    if not job_description.strip():
        return "Job description cannot be empty."

    if openings <= 0:
        return "Openings must be greater than 0."

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
        return "Unable to create job."

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

    if not job_title.strip():
        return "Job title cannot be empty."

    if not job_description.strip():
        return "Job description cannot be empty."

    if openings <= 0:
        return "Openings must be greater than 0."

    updated = update_job(
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

    if not updated:
        return "Unable to update job."

    return updated


def remove_job(job_id):

    deleted = delete_job(
        connect_db,
        job_id
    )

    if not deleted:
        return "Unable to delete job."

    return deleted


def view_job(job_id):

    return get_job(
        job_id,
        connect_db
    )


def view_all_jobs():

    return get_all_jobs(
        connect_db
    )


def view_my_jobs(recruiter_profile_id):

    return get_recruiter_jobs(
        connect_db,
        recruiter_profile_id
    )