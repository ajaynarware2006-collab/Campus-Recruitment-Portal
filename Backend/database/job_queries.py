from database.connection import connect_db


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

    with connection.cursor() as cursor:

        cursor.execute(
            """
            SELECT recruiter_profile_id
            FROM recruiter_profiles
            WHERE recruiter_profile_id=%s;
            """,
            (recruiter_profile_id,)
        )

        recruiter = cursor.fetchone()

        if not recruiter:
            return None

        cursor.execute(
            """
            INSERT INTO jobs(
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
            VALUES(
                %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
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

        job_id = cursor.fetchone()

        connection.commit()

        if not job_id:
            return None

        return job_id[0]


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

    with connection.cursor() as cursor:

        cursor.execute(
            """
            SELECT job_id
            FROM jobs
            WHERE job_id=%s;
            """,
            (job_id,)
        )

        job = cursor.fetchone()

        if not job:
            return False

        cursor.execute(
            """
            UPDATE jobs
            SET
                job_title=%s,
                job_description=%s,
                job_type=%s,
                work_mode=%s,
                location=%s,
                salary_min=%s,
                salary_max=%s,
                experience_required=%s,
                cgpa_required=%s,
                skills_required=%s,
                openings=%s,
                application_deadline=%s,
                status=%s,
                updated_at=CURRENT_TIMESTAMP
            WHERE job_id=%s;
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

        connection.commit()

        return True


def delete_job(connecting, job_id):

    connection = connecting()

    with connection.cursor() as cursor:

        cursor.execute(
            """
            SELECT job_id
            FROM jobs
            WHERE job_id=%s;
            """,
            (job_id,)
        )

        job = cursor.fetchone()

        if not job:
            return False

        cursor.execute(
            """
            DELETE FROM jobs
            WHERE job_id=%s;
            """,
            (job_id,)
        )

        connection.commit()

        return True


def get_job(job_id, connecting):

    connection = connecting()

    with connection.cursor() as cursor:

        cursor.execute(
            """
            SELECT *
            FROM jobs
            WHERE job_id=%s;
            """,
            (job_id,)
        )

        return cursor.fetchone()


def get_all_jobs(connecting):

    connection = connecting()

    with connection.cursor() as cursor:

        cursor.execute(
            """
            SELECT *
            FROM jobs
            WHERE status='Open'
            ORDER BY created_at DESC;
            """
        )

        return cursor.fetchall()


def get_recruiter_jobs(connecting, recruiter_profile_id):

    connection = connecting()

    with connection.cursor() as cursor:

        cursor.execute(
            """
            SELECT *
            FROM jobs
            WHERE recruiter_profile_id=%s
            ORDER BY created_at DESC;
            """,
            (recruiter_profile_id,)
        )

        return cursor.fetchall()