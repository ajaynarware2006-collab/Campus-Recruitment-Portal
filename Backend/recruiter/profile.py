from Backend.auth.recruiter_validator import (
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

from Backend.database.recruiter_queries import create_recruiter_profile
from Backend.database.connection import connect_db


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
        return "Invalid HR name."

    if not validate_company_name(company_name):
        return "Invalid company name."

    if not validate_designation(designation):
        return "Invalid designation."

    if not validate_company_email(company_email):
        return "Invalid company email."

    if not validate_company_contact(company_contact):
        return "Invalid company contact."

    if not validate_company_website(company_website):
        return "Invalid company website."

    if not validate_industry(industry):
        return "Invalid industry."

    if not validate_company_size(company_size):
        return "Invalid company size."

    if not validate_headquarters(headquarters):
        return "Invalid headquarters."

    if not validate_company_logo(company_logo):
        return "Invalid company logo."

    if not validate_company_description(company_description):
        return "Invalid company description."

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
        return "Unable to create recruiter profile."

    return recruiter_profile_id