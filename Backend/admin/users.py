from Backend.database.connection import connect_db
from Backend.database.admin_queries import (
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

    result = update_account_status(
        connect_db,
        user_id,
        "Active"
    )

    if not result:
        return "Unable to activate user."

    return result


def block_user(user_id):

    result = update_account_status(
        connect_db,
        user_id,
        "Blocked"
    )

    if not result:
        return "Unable to block user."

    return result


def suspend_user(user_id):

    result = update_account_status(
        connect_db,
        user_id,
        "Suspended"
    )

    if not result:
        return "Unable to suspend user."

    return result


def remove_user(user_id):

    result = delete_user(
        connect_db,
        user_id
    )

    if not result:
        return "Unable to delete user."

    return result