def email_exists(connection,email):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE email=%s;",(email,))
        user=cursor.fetchone()

        if user:
            return True
        return False

    
def create_user(connecting,email,hash_pass,role):
    connection=connecting()
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO users(email,password_hash,user_role) VALUES(%s,%s,%s) RETURNING user_id;",(email,hash_pass,role))
        cursor.commit()
        user_id=cursor.fetchone()
        if not user_id:
            return None
        
        return user_id[0]

def check_login_details(connecting,email):
    connection=connecting()
    with connection.cursor() as cursor:
        cursor.execute("SELECT account_status,user_role,user_id,password_hash FROM users WHERE email=%s;",(email,))
        user=cursor.fetchone()
        if not user:
            return None
        
        return user

def create_profile(
    connecting,
    user_id,
    full_name,
    enroll,
    contact,
    branch,
    semester,
    cgpa,
    profile_img_path
):
    connection=connecting()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE user_id=%s;",(user_id,))
        user=cursor.fetchone()
        if not user:
            return None
        
        cursor.execute("SELECT * FROM student_profiles WHERE user_id=%s;",(user_id,))
        check_profile=cursor.fetchone()
        if not check_profile:
            cursor.execute("INSERT INTO student_profiles(full_name,enrollment_no,cgpa,profile_img_path,user_id,branch,semester,contact) VALUES(%s,%s,%s,%s,%s,%s,%s,%s) RETURNING profile_id;",(full_name,enroll,cgpa,profile_img_path,user_id,branch,semester,contact))
            cursor.commit()
            profile_id=cursor.fetchone()
            if not profile_id:
                return None

            return profile_id
        
        else:
            cursor.execute("UPDATE student_profiles SET full_name=%s,enrollment_no=%s,cgpa=%s,profile_img_path=%s,branch=%s,semester=%s,contact=%s) WHERE user_id=%s;",(full_name,enroll,cgpa,profile_img_path,branch,semester,contact,user_id))
            cursor.commit()






    
    
        
