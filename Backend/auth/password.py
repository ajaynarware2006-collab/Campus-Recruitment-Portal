import bcrypt


def hash_password(password):
    """
    Hash a plain text password.
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def check_password(entered_password, stored_hash):
    """
    Verify entered password against stored hash.
    """
    if isinstance(stored_hash, str):
        stored_hash = stored_hash.encode("utf-8")

    return bcrypt.checkpw(
        entered_password.encode("utf-8"),
        stored_hash
    )


def change_password(connecting, email, new_password):
    """
    Change user's password.
    """

    connection = connecting()

    if connection is None:
        return False

    try:
        hashed_password = hash_password(new_password)

        with connection.cursor() as cursor:
            cursor.execute(
                """
                UPDATE users
                SET hashed_password = %s
                WHERE email = %s;
                """,
                (hashed_password, email)
            )

        connection.commit()
        return True

    except Exception:
        connection.rollback()
        return False

    finally:
        connection.close()