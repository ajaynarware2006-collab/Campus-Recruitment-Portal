from database.user_queries import email_exists,check_login_details
from validator import validate_email,validate_password
from database.connection import connect_db
from password import check_password

def login_user(email,password):
    if not validate_email(email):
        return False
    if not validate_password(password):
        return False
    
    user=check_login_details(connect_db,email)
    if not user:
        return False
    status=user[0]
    role=user[1]
    user_id=user[2]
    password_hash=user[3]

    if status != "Active":
        return False
    
    if not check_password(password,password_hash):
        return False
    
    return role,user_id
    

    
    
