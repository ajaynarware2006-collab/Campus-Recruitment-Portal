from datetime import datetime


def current_timestamp():

    return datetime.now()


def format_name(name):

    return " ".join(name.strip().title().split())


def format_email(email):

    return email.strip().lower()


def clean_text(text):

    return " ".join(text.strip().split())


def format_contact(contact):

    return contact.strip()


def is_admin(role):

    return role == "Admin"


def is_student(role):

    return role == "Student"


def is_recruiter(role):

    return role == "Recruiter"


def account_is_active(status):

    return status == "Active"


def calculate_percentage(obtained, total):

    if total == 0:
        return 0

    return round((obtained / total) * 100, 2)