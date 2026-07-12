import bcrypt

def hash_password(password):
    hashed_password=bcrypt.hashpw(password.encode(),bcrypt.gensalt())

    return hashed_password

def check_password(entered_password,stored_hash):
    return bcrypt.checkpw(entered_password.encode(),stored_hash)

