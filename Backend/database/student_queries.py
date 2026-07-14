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