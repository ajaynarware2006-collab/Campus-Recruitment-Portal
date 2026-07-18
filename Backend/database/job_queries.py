from Backend.database.connection import connect_db


def create_job(
    connecting,
    recruiter_profile_id,
    job_title,
    job_description,
    job_type,
    work_mode,
    location,
    salary_min,
    salary_max,
    experience_required,
    cgpa_required,
    skills_required,
    openings,
    application_deadline,
    status="Open"
):

    connection = connecting()

    try:
        with connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT recruiter_profile_id
                FROM recruiter_profiles
                WHERE recruiter_profile_id = %s;
                """,
                (recruiter_profile_id,)
            )

            recruiter = cursor.fetchone()

            if recruiter is None:
                return None

            cursor.execute(
                """
                INSERT INTO jobs (
                    recruiter_profile_id,
                    job_title,
                    job_description,
                    job_type,
                    work_mode,
                    location,
                    salary_min,
                    salary_max,
                    experience_required,
                    cgpa_required,
                    skills_required,
                    openings,
                    application_deadline,
                    status
                )
                VALUES (
                    %s, %s, %s, %s,
                    %s, %s, %s, %s,
                    %s, %s, %s, %s,
                    %s, %s
                )
                RETURNING job_id;
                """,
                (
                    recruiter_profile_id,
                    job_title,
                    job_description,
                    job_type,
                    work_mode,
                    location,
                    salary_min,
                    salary_max,
                    experience_required,
                    cgpa_required,
                    skills_required,
                    openings,
                    application_deadline,
                    status
                )
            )

            job = cursor.fetchone()

            connection.commit()

            if job is None:
                return None

            return job[0]

    except Exception:
        connection.rollback()
        return None

    finally:
        connection.close()


def update_job(
    connecting,
    job_id,
    job_title,
    job_description,
    job_type,
    work_mode,
    location,
    salary_min,
    salary_max,
    experience_required,
    cgpa_required,
    skills_required,
    openings,
    application_deadline,
    status
):

    connection = connecting()

    try:
        with connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT job_id
                FROM jobs
                WHERE job_id = %s;
                """,
                (job_id,)
            )

            if cursor.fetchone() is None:
                return False

            cursor.execute(
                """
                UPDATE jobs
                SET
                    job_title = %s,
                    job_description = %s,
                    job_type = %s,
                    work_mode = %s,
                    location = %s,
                    salary_min = %s,
                    salary_max = %s,
                    experience_required = %s,
                    cgpa_required = %s,
                    skills_required = %s,
                    openings = %s,
                    application_deadline = %s,
                    status = %s,
                    updated_at = CURRENT_TIMESTAMP
                WHERE job_id = %s
                RETURNING job_id;
                """,
                (
                    job_title,
                    job_description,
                    job_type,
                    work_mode,
                    location,
                    salary_min,
                    salary_max,
                    experience_required,
                    cgpa_required,
                    skills_required,
                    openings,
                    application_deadline,
                    status,
                    job_id
                )
            )

            updated = cursor.fetchone()

            connection.commit()

            return updated is not None

    except Exception:
        connection.rollback()
        return False

    finally:
        connection.close()

def delete_job(connecting, job_id):

    connection = connecting()

    try:
        with connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT job_id
                FROM jobs
                WHERE job_id = %s;
                """,
                (job_id,)
            )

            if cursor.fetchone() is None:
                return False

            cursor.execute(
                """
                DELETE FROM jobs
                WHERE job_id = %s
                RETURNING job_id;
                """,
                (job_id,)
            )

            deleted = cursor.fetchone()

            connection.commit()

            return deleted is not None

    except Exception:
        connection.rollback()
        return False

    finally:
        connection.close()


def get_job(job_id, connecting):

    connection = connecting()

    try:
        with connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT *
                FROM jobs
                WHERE job_id = %s;
                """,
                (job_id,)
            )

            return cursor.fetchone()

    finally:
        connection.close()


def get_all_jobs(connecting):

    connection = connecting()

    try:
        with connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT *
                FROM jobs
                WHERE status = 'Open'
                ORDER BY created_at DESC;
                """
            )

            return cursor.fetchall()

    finally:
        connection.close()


def get_recruiter_jobs(connecting, recruiter_profile_id):

    connection = connecting()

    try:
        with connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT *
                FROM jobs
                WHERE recruiter_profile_id = %s
                ORDER BY created_at DESC;
                """,
                (recruiter_profile_id,)
            )

            return cursor.fetchall()

    finally:
        connection.close()