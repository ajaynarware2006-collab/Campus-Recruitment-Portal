from database.connection import connect_db


def apply_job(connecting, job_id, student_profile_id):

    connection = connecting()

    with connection.cursor() as cursor:

        cursor.execute(
            """
            SELECT job_id
            FROM jobs
            WHERE job_id=%s
            AND status='Open';
            """,
            (job_id,)
        )

        job = cursor.fetchone()

        if not job:
            return None

        cursor.execute(
            """
            SELECT student_profile_id
            FROM student_profiles
            WHERE student_profile_id=%s;
            """,
            (student_profile_id,)
        )

        student = cursor.fetchone()

        if not student:
            return None

        cursor.execute(
            """
            SELECT application_id
            FROM applications
            WHERE job_id=%s
            AND student_profile_id=%s;
            """,
            (
                job_id,
                student_profile_id
            )
        )

        application = cursor.fetchone()

        if application:
            return None

        cursor.execute(
            """
            INSERT INTO applications(
                job_id,
                student_profile_id
            )
            VALUES(%s,%s)
            RETURNING application_id;
            """,
            (
                job_id,
                student_profile_id
            )
        )

        application_id = cursor.fetchone()

        connection.commit()

        return application_id[0]


def withdraw_application(connecting, application_id):

    connection = connecting()

    with connection.cursor() as cursor:

        cursor.execute(
            """
            SELECT application_id
            FROM applications
            WHERE application_id=%s;
            """,
            (application_id,)
        )

        application = cursor.fetchone()

        if not application:
            return False

        cursor.execute(
            """
            UPDATE applications
            SET
                application_status='Withdrawn',
                updated_at=CURRENT_TIMESTAMP
            WHERE application_id=%s;
            """,
            (application_id,)
        )

        connection.commit()

        return True


def shortlist_application(connecting, application_id):

    connection = connecting()

    with connection.cursor() as cursor:

        cursor.execute(
            """
            UPDATE applications
            SET
                application_status='Shortlisted',
                updated_at=CURRENT_TIMESTAMP
            WHERE application_id=%s
            RETURNING application_id;
            """,
            (application_id,)
        )

        application = cursor.fetchone()

        connection.commit()

        return application is not None


def reject_application(connecting, application_id):

    connection = connecting()

    with connection.cursor() as cursor:

        cursor.execute(
            """
            UPDATE applications
            SET
                application_status='Rejected',
                updated_at=CURRENT_TIMESTAMP
            WHERE application_id=%s
            RETURNING application_id;
            """,
            (application_id,)
        )

        application = cursor.fetchone()

        connection.commit()

        return application is not None


def accept_application(connecting, application_id):

    connection = connecting()

    with connection.cursor() as cursor:

        cursor.execute(
            """
            UPDATE applications
            SET
                application_status='Accepted',
                updated_at=CURRENT_TIMESTAMP
            WHERE application_id=%s
            RETURNING application_id;
            """,
            (application_id,)
        )

        application = cursor.fetchone()

        connection.commit()

        return application is not None


def get_student_applications(connecting, student_profile_id):

    connection = connecting()

    with connection.cursor() as cursor:

        cursor.execute(
            """
            SELECT *
            FROM applications
            WHERE student_profile_id=%s
            ORDER BY applied_at DESC;
            """,
            (student_profile_id,)
        )

        return cursor.fetchall()


def get_job_applications(connecting, job_id):

    connection = connecting()

    with connection.cursor() as cursor:

        cursor.execute(
            """
            SELECT *
            FROM applications
            WHERE job_id=%s
            ORDER BY applied_at DESC;
            """,
            (job_id,)
        )

        return cursor.fetchall()


def get_application(application_id, connecting):

    connection = connecting()

    with connection.cursor() as cursor:

        cursor.execute(
            """
            SELECT *
            FROM applications
            WHERE application_id=%s;
            """,
            (application_id,)
        )

        return cursor.fetchone()