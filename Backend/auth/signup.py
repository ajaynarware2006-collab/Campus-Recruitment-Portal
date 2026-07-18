from Backend.auth.validator import (
    validate_email,
    validate_name,
    validate_password
)

from Backend.auth.password import hash_password
from Backend.database.user_queries import (
    email_exists,
    create_user
)
from Backend.database.connection import connect_db


def register_user(name, email, password, role):

    if not validate_name(name):
        return "Invalid Name"

    if not validate_email(email):
        return "Invalid Email"

    if not validate_password(password):
        return "Invalid Password"

    connection = connect_db()

    if connection is None:
        return "Database Connection Failed"

    try:
        if email_exists(connection, email):
            return "Email Already Exists"

        hash_pass = hash_password(password)

        user_id = create_user(
            connect_db,
            email,
            hash_pass,
            role
        )

        if user_id is None:
            return "Registration Failed"

        return user_id

    finally:
        connection.close()