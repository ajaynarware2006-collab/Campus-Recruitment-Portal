from Backend.database.connection import connect_db


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

    connection = connecting()

    if connection is None:
        return None

    try:
        with connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT 1
                FROM users
                WHERE user_id = %s;
                """,
                (user_id,)
            )

            if cursor.fetchone() is None:
                return None

            cursor.execute(
                """
                SELECT profile_id
                FROM student_profiles
                WHERE user_id = %s;
                """,
                (user_id,)
            )

            existing_profile = cursor.fetchone()

            if existing_profile is None:

                cursor.execute(
                    """
                    INSERT INTO student_profiles
                    (
                        full_name,
                        enrollment_no,
                        contact,
                        branch,
                        semester,
                        cgpa,
                        profile_img_path,
                        user_id
                    )
                    VALUES
                    (%s,%s,%s,%s,%s,%s,%s,%s)
                    RETURNING profile_id;
                    """,
                    (
                        full_name,
                        enroll,
                        contact,
                        branch,
                        semester,
                        cgpa,
                        profile_img_path,
                        user_id
                    )
                )

                profile_id = cursor.fetchone()[0]

                connection.commit()

                return profile_id

            cursor.execute(
                """
                UPDATE student_profiles
                SET
                    full_name=%s,
                    enrollment_no=%s,
                    contact=%s,
                    branch=%s,
                    semester=%s,
                    cgpa=%s,
                    profile_img_path=%s
                WHERE user_id=%s
                RETURNING profile_id;
                """,
                (
                    full_name,
                    enroll,
                    contact,
                    branch,
                    semester,
                    cgpa,
                    profile_img_path,
                    user_id
                )
            )

            profile_id = cursor.fetchone()[0]

            connection.commit()

            return profile_id

    except Exception:

        connection.rollback()
        return None

    finally:

        connection.close()