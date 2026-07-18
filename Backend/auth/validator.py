import re


def validate_name(name):
    name = name.strip()

    if not name:
        return False

    words = re.split(r"[,\-\s]+", name)

    for word in words:
        if word and not word.isalpha():
            return False

    return True


def validate_email(email):
    email = email.strip().lower()

    if email.endswith("@gmail.com"):
        username = email.split("@")[0]

    elif email.endswith(".ies@ipsacademy.org"):
        username = email.split(".ies@")[0]

    else:
        return False

    return username.isalnum()


def validate_enroll(enroll):
    enroll = enroll.strip()

    if not enroll.isalnum():
        return False

    return 9 <= len(enroll) <= 13


def validate_contact(contact):
    contact = str(contact).strip()

    if not contact.isdigit():
        return False

    return 10 <= len(contact) <= 13


def validate_password(password):
    if len(password) < 8 or len(password) > 20:
        return False

    if not re.search(r"[A-Z]", password):
        return False

    if not re.search(r"[a-z]", password):
        return False

    if not re.search(r"\d", password):
        return False

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=/\\[\]]", password):
        return False

    return True


def validate_branch(branch):
    branch = branch.strip()

    if not branch.isalpha():
        return False

    return 2 <= len(branch) <= 5


def validate_semester(sem):
    if not str(sem).isdigit():
        return False

    sem = int(sem)

    return 1 <= sem <= 8


def validate_cgpa(cgpa):
    try:
        cgpa = float(cgpa)
    except ValueError:
        return False

    return 0 <= cgpa <= 10


def validate_profile_image(path):
    path = path.lower()

    return path.endswith((".png", ".jpg", ".jpeg"))


def validate_resume(path):
    path = path.lower()

    return path.endswith(".pdf")