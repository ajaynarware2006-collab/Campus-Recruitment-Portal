from Backend.database.connection import connect_db
from Backend.database.admin_queries import (
    total_platform_statistics,
    get_all_users
)


def platform_summary():

    return total_platform_statistics(
        connect_db
    )


def generate_user_report():

    return get_all_users(
        connect_db
    )


def total_users():

    summary = total_platform_statistics(
        connect_db
    )

    return summary[0]


def total_students():

    summary = total_platform_statistics(
        connect_db
    )

    return summary[1]


def total_recruiters():

    summary = total_platform_statistics(
        connect_db
    )

    return summary[2]


def total_jobs():

    summary = total_platform_statistics(
        connect_db
    )

    return summary[3]


def total_applications():

    summary = total_platform_statistics(
        connect_db
    )

    return summary[4]