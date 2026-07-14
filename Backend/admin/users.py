from database.connection import connect_db
from database.admin_queries import (
    get_all_users,
    get_user,
    update_account_status,
    delete_user
)


def view_all_users():

    return get_all_users(
        connect_db
    )


def view_user(user_id):

    return get_user(
        connect_db,
        user_id
    )


def activate_user(user_id):

    return update_account_status(
        connect_db,
        user_id,
        "Active"
    )


def block_user(user_id):

    return update_account_status(
        connect_db,
        user_id,
        "Blocked"
    )


def suspend_user(user_id):

    return update_account_status(
        connect_db,
        user_id,
        "Suspended"
    )


def remove_user(user_id):

    return delete_user(
        connect_db,
        user_id
    )