from Backend.database.connection import connect_db


def student_dashboard(connecting, student_profile_id):

    connection = connecting()

    with connection.cursor() as cursor:

        cursor.execute(
            """
            SELECT
                COUNT(*) FILTER (WHERE application_status='Applied'),
                COUNT(*) FILTER (WHERE application_status='Under Review'),
                COUNT(*) FILTER (WHERE application_status='Shortlisted'),
                COUNT(*) FILTER (WHERE application_status='Accepted'),
                COUNT(*) FILTER (WHERE application_status='Rejected'),
                COUNT(*) FILTER (WHERE application_status='Withdrawn')
            FROM applications
            WHERE student_profile_id=%s;
            """,
            (student_profile_id,)
        )

        return cursor.fetchone()


def recruiter_dashboard(connecting, recruiter_profile_id):

    connection = connecting()

    with connection.cursor() as cursor:

        cursor.execute(
            """
            SELECT
                COUNT(*),
                COUNT(*) FILTER (WHERE status='Open'),
                COUNT(*) FILTER (WHERE status='Closed'),
                COUNT(*) FILTER (WHERE status='Draft')
            FROM jobs
            WHERE recruiter_profile_id=%s;
            """,
            (recruiter_profile_id,)
        )

        job_stats = cursor.fetchone()

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM applications a
            JOIN jobs j
            ON a.job_id=j.job_id
            WHERE j.recruiter_profile_id=%s;
            """,
            (recruiter_profile_id,)
        )

        application_count = cursor.fetchone()[0]

        return job_stats, application_count


def admin_dashboard(connecting):

    connection = connecting()

    with connection.cursor() as cursor:

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM users;
            """
        )

        total_users = cursor.fetchone()[0]

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM student_profiles;
            """
        )

        total_students = cursor.fetchone()[0]

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM recruiter_profiles;
            """
        )

        total_recruiters = cursor.fetchone()[0]

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM jobs;
            """
        )

        total_jobs = cursor.fetchone()[0]

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM applications;
            """
        )

        total_applications = cursor.fetchone()[0]

        return (
            total_users,
            total_students,
            total_recruiters,
            total_jobs,
            total_applications
        )