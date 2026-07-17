from Backend.database.connection import connect_db


def get_all_users(connecting):

    connection = connecting()

    with connection.cursor() as cursor:

        cursor.execute(
            """
            SELECT
                user_id,
                email,
                user_role,
                account_status,
                created_at
            FROM users
            ORDER BY created_at DESC;
            """
        )

        return cursor.fetchall()


def get_user(connecting, user_id):

    connection = connecting()

    with connection.cursor() as cursor:

        cursor.execute(
            """
            SELECT *
            FROM users
            WHERE user_id=%s;
            """,
            (user_id,)
        )

        return cursor.fetchone()


def update_account_status(connecting, user_id, status):

    connection = connecting()

    with connection.cursor() as cursor:

        cursor.execute(
            """
            UPDATE users
            SET account_status=%s
            WHERE user_id=%s
            RETURNING user_id;
            """,
            (
                status,
                user_id
            )
        )

        result = cursor.fetchone()

        connection.commit()

        return result is not None


def delete_user(connecting, user_id):

    connection = connecting()

    with connection.cursor() as cursor:

        cursor.execute(
            """
            DELETE FROM users
            WHERE user_id=%s
            RETURNING user_id;
            """,
            (user_id,)
        )

        result = cursor.fetchone()

        connection.commit()

        return result is not None


def total_platform_statistics(connecting):

    connection = connecting()

    with connection.cursor() as cursor:

        cursor.execute(
            """
            SELECT
                (SELECT COUNT(*) FROM users),
                (SELECT COUNT(*) FROM student_profiles),
                (SELECT COUNT(*) FROM recruiter_profiles),
                (SELECT COUNT(*) FROM jobs),
                (SELECT COUNT(*) FROM applications);
            """
        )

        return cursor.fetchone()