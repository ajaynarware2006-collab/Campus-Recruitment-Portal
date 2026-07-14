from validator import validate_email,validate_name,validate_password
from password import hash_password
from database.user_queries import email_exists,create_user
from database.connection import connect_db

def register_user(name,email,password,role):

    if not validate_name(name):
        return "name is Invalid"

    if not validate_email(email):
        return "email is Invalid"

    if not validate_password(password):
        return "password is Invalid"
    
    hash_pass=hash_password(password)

    if email_exists(connect_db,email):
        return False
    
    user_id=create_user(connect_db,email,hash_pass,role)
    return user_id

    

    