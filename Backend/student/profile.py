from Backend.auth.validator import validate_branch,validate_cgpa,validate_contact,validate_email,validate_enroll,validate_name,validate_profile_image,validate_resume,validate_semester
from Backend.database.user_queries import email_exists
from Backend.database.student_queries import create_profile
from Backend.database.connection import connect_db

def complete_profile(role,
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
    if not validate_name(full_name):
        return False
    if not validate_enroll(enroll):
        return False
    if not validate_contact(contact):
        return False
    if not validate_branch(branch):
        return False
    if not validate_semester(semester):
        return False
    if not validate_cgpa(cgpa):
        return False
    if not validate_profile_image(profile_img_path):
        return False
    if not validate_resume(resume_path):
        return False
    
    if role != "Student":
        return False
    
    result=create_profile(connect_db,user_id,full_name,enroll,contact,branch,semester,cgpa,profile_img_path)
    if not result:
        return False

    return True

    