def email_exists(connection,email):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE email=%s;",(email,))
        user=cursor.fetchone()

        if user:
            return True
        return False
    
def email_enroll(connecting,enroll):
    connection=connecting()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE enrollment_no=%s;",(enroll,))
        user=cursor.fetchone()

        if user:
            return True
        return False
    
def create_user(connecting,email,hash_pass,role):
    connection=connecting()
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO users(email,password_hash,user_role) VALUES(%s,%s,%s) RETURNING user_id;",(email,hash_pass,role))
        user_id=cursor.fetchone()
        if not user_id:
            return None
        
        return user_id[0]
