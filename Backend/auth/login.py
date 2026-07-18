from Backend.database.user_queries import check_login_details
from Backend.auth.validator import validate_email, validate_password
from Backend.database.connection import connect_db
from Backend.auth.password import check_password


def login_user(email, password):

    if not validate_email(email):
        return "Invalid Email"

    if not validate_password(password):
        return "Invalid Password Structure"

    user = check_login_details(connect_db, email)

    if user is None:
        return "User Not Found"

    account_status, role, user_id, password_hash = user

    if account_status != "Active":
        return "User is Suspended or Inactive"

    if not check_password(password, password_hash):
        return "Invalid Password"

    return role, user_id