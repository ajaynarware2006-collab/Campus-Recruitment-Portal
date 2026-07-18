def email_exists(connection, email):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM users WHERE email=%s;",
            (email,)
        )
        return cursor.fetchone() is not None


def create_user(connecting, email, hash_pass, role):
    connection = connecting()

    if connection is None:
        return None

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO users(email, password_hash, user_role)
                VALUES(%s, %s, %s)
                RETURNING user_id;
                """,
                (email, hash_pass, role)
            )

            user_id = cursor.fetchone()[0]

        connection.commit()
        return user_id

    except Exception:
        connection.rollback()
        return None

    finally:
        connection.close()


def check_login_details(connecting, email):
    connection = connecting()

    if connection is None:
        return None

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT account_status,
                       user_role,
                       user_id,
                       password_hash
                FROM users
                WHERE email=%s;
                """,
                (email,)
            )

            return cursor.fetchone()

    finally:
        connection.close()


def block_user(connecting, email):
    connection = connecting()

    if connection is None:
        return False

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                UPDATE users
                SET account_status = 'Suspended'
                WHERE email = %s;
                """,
                (email,)
            )

        connection.commit()
        return True

    except Exception:
        connection.rollback()
        return False

    finally:
        connection.close()