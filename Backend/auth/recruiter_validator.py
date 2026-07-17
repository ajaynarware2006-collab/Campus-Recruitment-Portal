from Backend.auth.validator import (
    validate_contact,
    validate_email,
    validate_name
)


def validate_hr_name(hr_name):
    return validate_name(hr_name)


def validate_company_name(company_name):
    company_name = company_name.strip()

    if len(company_name) < 2 or len(company_name) > 100:
        return False

    return True


def validate_designation(designation):
    designation = designation.strip()

    allowed = [
        "HR",
        "Recruiter",
        "Talent Acquisition"
    ]

    if designation not in allowed:
        return False

    return True


def validate_company_email(email):
    return validate_email(email)


def validate_company_contact(contact):
    return validate_contact(contact)


def validate_company_website(website):
    website = website.strip().lower()

    if website == "":
        return True

    prefixes = (
        "https://",
        "http://",
        "www."
    )

    if not website.startswith(prefixes):
        return False

    return True


def validate_industry(industry):
    industry = industry.strip()

    if len(industry) < 2 or len(industry) > 100:
        return False

    return True


def validate_company_size(company_size):
    allowed = [
        "Startup",
        "Small",
        "Medium",
        "Enterprise"
    ]

    if company_size not in allowed:
        return False

    return True


def validate_headquarters(headquarters):
    headquarters = headquarters.strip()

    if len(headquarters) < 2 or len(headquarters) > 100:
        return False

    return True


def validate_company_logo(path):
    path = path.lower()

    if path.endswith((".png", ".jpg", ".jpeg")):
        return True

    return False


def validate_company_description(description):
    description = description.strip()

    if len(description) > 1000:
        return False

    return True

