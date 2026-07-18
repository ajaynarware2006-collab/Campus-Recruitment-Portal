from Backend.database.connection import connect_db


def get_application_history(connecting, student_profile_id):

    connection = connecting()

    try:
        with connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT
                    a.application_id,
                    sp.full_name AS student,
                    j.job_title AS job,
                    rp.company_name AS company,
                    a.applied_at,
                    a.application_status
                FROM applications AS a

                JOIN student_profiles AS sp
                ON a.student_profile_id = sp.student_profile_id

                JOIN jobs AS j
                ON a.job_id = j.job_id

                JOIN recruiter_profiles AS rp
                ON j.recruiter_profile_id = rp.recruiter_profile_id

                WHERE a.student_profile_id = %s

                ORDER BY a.applied_at DESC;
                """,
                (student_profile_id,)
            )

            return cursor.fetchall()

    finally:
        connection.close()


def apply_job(connecting, job_id, student_profile_id):

    connection = connecting()

    try:
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

            if cursor.fetchone() is None:
                return None

            cursor.execute(
                """
                SELECT student_profile_id
                FROM student_profiles
                WHERE student_profile_id=%s;
                """,
                (student_profile_id,)
            )

            if cursor.fetchone() is None:
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

            if cursor.fetchone():
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

            application = cursor.fetchone()

            connection.commit()

            return application[0]

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


def withdraw_application(connecting, application_id):

    connection = connecting()

    try:
        with connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT application_id
                FROM applications
                WHERE application_id=%s;
                """,
                (application_id,)
            )

            if cursor.fetchone() is None:
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

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()

def shortlist_application(connecting, application_id):

    connection = connecting()

    try:
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

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


def reject_application(connecting, application_id):

    connection = connecting()

    try:
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

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


def accept_application(connecting, application_id):

    connection = connecting()

    try:
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

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


def get_student_applications(connecting, student_profile_id):

    connection = connecting()

    try:
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

    finally:
        connection.close()


def get_job_applications(connecting, job_id):

    connection = connecting()

    try:
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

    finally:
        connection.close()


def get_application(application_id, connecting):

    connection = connecting()

    try:
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

    finally:
        connection.close()