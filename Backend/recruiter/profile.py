from auth.recruiter_validator import (
    validate_hr_name,
    validate_company_name,
    validate_designation,
    validate_company_email,
    validate_company_contact,
    validate_company_website,
    validate_industry,
    validate_company_size,
    validate_headquarters,
    validate_company_logo,
    validate_company_description
)

from database.recruiter_queries import create_recruiter_profile
from database.connection import connect_db


def complete_recruiter_profile(
    user_id,
    hr_name,
    company_name,
    designation,
    company_email,
    company_contact,
    company_website,
    industry,
    company_size,
    headquarters,
    company_logo,
    company_description
):

    if not validate_hr_name(hr_name):
        return False

    if not validate_company_name(company_name):
        return False

    if not validate_designation(designation):
        return False

    if not validate_company_email(company_email):
        return False

    if not validate_company_contact(company_contact):
        return False

    if not validate_company_website(company_website):
        return False

    if not validate_industry(industry):
        return False

    if not validate_company_size(company_size):
        return False

    if not validate_headquarters(headquarters):
        return False

    if not validate_company_logo(company_logo):
        return False

    if not validate_company_description(company_description):
        return False

    recruiter_profile_id = create_recruiter_profile(
        connect_db,
        user_id,
        hr_name,
        company_name,
        designation,
        company_email,
        company_contact,
        company_website,
        industry,
        company_size,
        headquarters,
        company_logo,
        company_description
    )

    if recruiter_profile_id is None:
        return False

    return True