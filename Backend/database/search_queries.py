from database.connection import connect_db


def get_latest_jobs(connecting):

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


def get_job_by_id(connecting, job_id):

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


def search_jobs(connecting, keyword):

    connection = connecting()

    with connection.cursor() as cursor:

        cursor.execute(
            """
            SELECT *
            FROM jobs
            WHERE
                status='Open'
                AND
                (
                    LOWER(job_title) LIKE LOWER(%s)
                    OR
                    LOWER(company_name) LIKE LOWER(%s)
                );
            """,
            (
                f"%{keyword}%",
                f"%{keyword}%"
            )
        )

        return cursor.fetchall()


def filter_by_location(connecting, location):

    connection = connecting()

    with connection.cursor() as cursor:

        cursor.execute(
            """
            SELECT *
            FROM jobs
            WHERE
                status='Open'
                AND
                location=%s;
            """,
            (location,)
        )

        return cursor.fetchall()


def filter_by_job_type(connecting, job_type):

    connection = connecting()

    with connection.cursor() as cursor:

        cursor.execute(
            """
            SELECT *
            FROM jobs
            WHERE
                status='Open'
                AND
                job_type=%s;
            """,
            (job_type,)
        )

        return cursor.fetchall()


def filter_by_work_mode(connecting, work_mode):

    connection = connecting()

    with connection.cursor() as cursor:

        cursor.execute(
            """
            SELECT *
            FROM jobs
            WHERE
                status='Open'
                AND
                work_mode=%s;
            """,
            (work_mode,)
        )

        return cursor.fetchall()


def filter_by_min_cgpa(connecting, cgpa):

    connection = connecting()

    with connection.cursor() as cursor:

        cursor.execute(
            """
            SELECT *
            FROM jobs
            WHERE
                status='Open'
                AND
                cgpa_required <= %s;
            """,
            (cgpa,)
        )

        return cursor.fetchall()


def get_recommended_jobs(connecting, cgpa):

    connection = connecting()

    with connection.cursor() as cursor:

        cursor.execute(
            """
            SELECT *
            FROM jobs
            WHERE
                status='Open'
                AND
                cgpa_required <= %s
            ORDER BY created_at DESC;
            """,
            (cgpa,)
        )

        return cursor.fetchall()