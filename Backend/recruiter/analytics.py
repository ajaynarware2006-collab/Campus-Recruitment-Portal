from Backend.database.connection import connect_db


def applications_per_job(connecting, recruiter_profile_id):

    connection = connecting()

    try:
        with connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT
                    j.job_id,
                    j.job_title,
                    COUNT(a.application_id)
                FROM jobs j
                LEFT JOIN applications a
                    ON j.job_id = a.job_id
                WHERE j.recruiter_profile_id = %s
                GROUP BY
                    j.job_id,
                    j.job_title
                ORDER BY COUNT(a.application_id) DESC;
                """,
                (recruiter_profile_id,)
            )

            return cursor.fetchall()

    finally:
        connection.close()


def application_status_summary(connecting, recruiter_profile_id):

    connection = connecting()

    try:
        with connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT
                    a.application_status,
                    COUNT(*)
                FROM applications a
                JOIN jobs j
                    ON a.job_id = j.job_id
                WHERE j.recruiter_profile_id = %s
                GROUP BY a.application_status
                ORDER BY a.application_status;
                """,
                (recruiter_profile_id,)
            )

            return cursor.fetchall()

    finally:
        connection.close()


def hiring_rate(connecting, recruiter_profile_id):

    connection = connecting()

    try:
        with connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT
                    COUNT(*) FILTER (
                        WHERE a.application_status = 'Accepted'
                    ),
                    COUNT(*)
                FROM applications a
                JOIN jobs j
                    ON a.job_id = j.job_id
                WHERE j.recruiter_profile_id = %s;
                """,
                (recruiter_profile_id,)
            )

            accepted, total = cursor.fetchone()

            accepted = accepted or 0

            if total == 0:
                return 0

            return round((accepted / total) * 100, 2)

    finally:
        connection.close()


def most_applied_job(connecting, recruiter_profile_id):

    connection = connecting()

    try:
        with connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT
                    j.job_title,
                    COUNT(a.application_id) AS total
                FROM jobs j
                JOIN applications a
                    ON j.job_id = a.job_id
                WHERE j.recruiter_profile_id = %s
                GROUP BY j.job_title
                ORDER BY total DESC
                LIMIT 1;
                """,
                (recruiter_profile_id,)
            )

            return cursor.fetchone()

    finally:
        connection.close()


def monthly_applications(connecting, recruiter_profile_id):

    connection = connecting()

    try:
        with connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT
                    DATE_TRUNC('month', a.applied_at) AS month,
                    COUNT(*)
                FROM applications a
                JOIN jobs j
                    ON a.job_id = j.job_id
                WHERE j.recruiter_profile_id = %s
                GROUP BY month
                ORDER BY month;
                """,
                (recruiter_profile_id,)
            )

            return cursor.fetchall()

    finally:
        connection.close()