from Backend.auth.validator import (
    validate_branch,
    validate_cgpa,
    validate_contact,
    validate_enroll,
    validate_name,
    validate_profile_image,
    validate_resume,
    validate_semester
)

from Backend.student.student_queries import create_profile
from Backend.database.connection import connect_db


def complete_profile(
    role,
    user_id,
    full_name,
    enroll,
    contact,
    branch,
    semester,
    cgpa,
    profile_img_path,
    resume_path
):

    if role != "Student":
        return "Unauthorized Access"

    if not validate_name(full_name):
        return "Invalid Name"

    if not validate_enroll(enroll):
        return "Invalid Enrollment Number"

    if not validate_contact(contact):
        return "Invalid Contact Number"

    if not validate_branch(branch):
        return "Invalid Branch"

    if not validate_semester(semester):
        return "Invalid Semester"

    if not validate_cgpa(cgpa):
        return "Invalid CGPA"

    if not validate_profile_image(profile_img_path):
        return "Invalid Profile Image"

    if not validate_resume(resume_path):
        return "Invalid Resume"

    profile_id = create_profile(
        connect_db,
        user_id,
        full_name,
        enroll,
        contact,
        branch,
        semester,
        cgpa,
        profile_img_path
    )

    if profile_id is None:
        return "Profile Creation Failed"

    return profile_id