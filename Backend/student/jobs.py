from Backend.database.connection import connect_db
from Backend.database.search_queries import (
    get_latest_jobs,
    get_job_by_id,
    search,
    filter_by_location,
    filter_by_job_type,
    filter_by_work_mode,
    filter_by_min_cgpa,
    get_recommended_jobs,
    get_jobs,
    details
)


def latest_jobs():

    return get_latest_jobs(connect_db)


def job_details(job_id):

    return get_job_by_id(
        connect_db,
        job_id
    )


def search_by_keyword(keyword):

    return search(
        connect_db,
        keyword
    )


def location_filter(location):

    return filter_by_location(
        connect_db,
        location
    )


def job_type_filter(job_type):

    return filter_by_job_type(
        connect_db,
        job_type
    )


def work_mode_filter(work_mode):

    return filter_by_work_mode(
        connect_db,
        work_mode
    )


def cgpa_filter(cgpa):

    return filter_by_min_cgpa(
        connect_db,
        cgpa
    )


def recommended_jobs(cgpa):

    return get_recommended_jobs(
        connect_db,
        cgpa
    )


def get_all_jobs():

    return get_jobs(connect_db)


def get_job_details(job_id):

    return details(
        connect_db,
        job_id
    )