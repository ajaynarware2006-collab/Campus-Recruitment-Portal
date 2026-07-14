import re

def validate_name(name):
    name=name.strip()
    name=re.split(r'[,-/s]+',name)

    for word in name:
        if not word.isalpha():
            return False
    return True

def validate_email(email):
    if not email.endswith(("@gmail.com",".ies@ipsacademy.org")):
        return False
    else:
        if email.endswith("@gmail.com"):
            email=email.split("@")
        else:
            email=email.split(".ies@")
    
    if not email[0].isalnum():
        return False

    return True


def validate_enroll(enroll):
    if not enroll.isalnum():
        return False
    elif len(enroll) > 13 or len(enroll) < 9:
        return False
    
    return True

def validate_contact(contact):
    if not contact.isdigit():
        return False
    elif len(contact) > 13 or len(contact) < 9:
        return False
    
    return True

def validate_password(password,confirm_pass):
    if len(password) < 8 or len(password) > 20:
        return False

    elif len(confirm_pass) < 8 or len(confirm_pass) > 20:
        return False

    elif password != confirm_pass:
        return False
    
    return True
    
def validate_branch(branch):
    if not branch.isalpha():
        return False
    elif len(branch) > 5 or len(branch) < 2:
        return False
    
    return True

def validate_semester(sem):
    if not sem.isnum():
        return False
    elif sem > 8 or sem < 0:
        return False
    
    return True

def validate_cgpa(cgpa):
    if not cgpa.isdecimal():
        return False
    elif cgpa > 10 or cgpa < 0:
        return False
    
    return True

def validate_profile_image(path):
    if not path.endswith((".png",".jpg","jpeg")):
        return False
    
    return True

def validate_resume(path):
    if not path.endswith(".pdf"):
        return False
    
    return True