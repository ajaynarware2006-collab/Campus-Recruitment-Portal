from Backend.database.connection import connect_db


def get_latest_jobs(connecting):

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


def get_job_by_id(connecting, job_id):

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


def search(connecting, keyword):

    connection = connecting()

    try:
        with connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT *
                FROM jobs
                WHERE status='Open'
                AND (
                    LOWER(job_title) LIKE LOWER(%s)
                    OR LOWER(company_name) LIKE LOWER(%s)
                );
                """,
                (
                    f"%{keyword}%",
                    f"%{keyword}%"
                )
            )

            return cursor.fetchall()

    finally:
        connection.close()


def filter_by_location(connecting, location):

    connection = connecting()

    try:
        with connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT *
                FROM jobs
                WHERE status='Open'
                AND location=%s;
                """,
                (location,)
            )

            return cursor.fetchall()

    finally:
        connection.close()


def filter_by_job_type(connecting, job_type):

    connection = connecting()

    try:
        with connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT *
                FROM jobs
                WHERE status='Open'
                AND job_type=%s;
                """,
                (job_type,)
            )

            return cursor.fetchall()

    finally:
        connection.close()


def filter_by_work_mode(connecting, work_mode):

    connection = connecting()

    try:
        with connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT *
                FROM jobs
                WHERE status='Open'
                AND work_mode=%s;
                """,
                (work_mode,)
            )

            return cursor.fetchall()

    finally:
        connection.close()


def filter_by_min_cgpa(connecting, cgpa):

    connection = connecting()

    try:
        with connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT *
                FROM jobs
                WHERE status='Open'
                AND cgpa_required <= %s;
                """,
                (cgpa,)
            )

            return cursor.fetchall()

    finally:
        connection.close()


def get_recommended_jobs(connecting, cgpa):

    connection = connecting()

    try:
        with connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT *
                FROM jobs
                WHERE status='Open'
                AND cgpa_required <= %s
                ORDER BY created_at DESC;
                """,
                (cgpa,)
            )

            return cursor.fetchall()

    finally:
        connection.close()


def get_jobs(connecting):

    connection = connecting()

    try:
        with connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT
                    j.job_id,
                    j.job_title,
                    r.company_name,
                    j.location,
                    j.job_type,
                    j.work_mode,

                    CONCAT(
                        '₹',
                        j.salary_min,
                        ' - ₹',
                        j.salary_max
                    ) AS salary,

                    j.application_deadline

                FROM jobs AS j

                JOIN recruiter_profiles AS r
                ON j.recruiter_profile_id = r.recruiter_profile_id

                WHERE j.status='Open'

                ORDER BY j.application_deadline;
                """
            )

            return cursor.fetchall()

    finally:
        connection.close()


def details(connecting, job_id):

    connection = connecting()

    try:
        with connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT
                    j.job_title,
                    r.company_name,
                    j.location,
                    j.job_type,
                    j.work_mode,

                    CONCAT(
                        '₹',
                        j.salary_min,
                        ' - ₹',
                        j.salary_max
                    ) AS salary,

                    j.description,
                    j.skills_required,
                    j.application_deadline

                FROM jobs AS j

                JOIN recruiter_profiles AS r
                ON j.recruiter_profile_id = r.recruiter_profile_id

                WHERE
                    j.status='Open'
                    AND j.job_id=%s;
                """,
                (job_id,)
            )

            return cursor.fetchone()

    finally:
        connection.close()