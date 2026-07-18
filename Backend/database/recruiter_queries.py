from Backend.database.connection import connect_db


def create_recruiter_profile(
    connecting,
    user_id,
    hr_name,
    company_name,
    designation,
    company_email,
    company_contact,
    company_website,
    industry,
    company_size,
    headquarters,
    company_logo,
    company_description
):

    connection = connecting()

    try:
        with connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT user_role
                FROM users
                WHERE user_id = %s;
                """,
                (user_id,)
            )

            user = cursor.fetchone()

            if user is None:
                return None

            if user[0] != "Recruiter":
                return None

            cursor.execute(
                """
                SELECT recruiter_profile_id
                FROM recruiter_profiles
                WHERE user_id = %s;
                """,
                (user_id,)
            )

            recruiter = cursor.fetchone()

            if recruiter is not None:

                cursor.execute(
                    """
                    UPDATE recruiter_profiles
                    SET
                        hr_name = %s,
                        company_name = %s,
                        designation = %s,
                        company_email = %s,
                        company_contact = %s,
                        company_website = %s,
                        industry = %s,
                        company_size = %s,
                        headquarters = %s,
                        company_logo = %s,
                        company_description = %s
                    WHERE user_id = %s
                    RETURNING recruiter_profile_id;
                    """,
                    (
                        hr_name,
                        company_name,
                        designation,
                        company_email,
                        company_contact,
                        company_website,
                        industry,
                        company_size,
                        headquarters,
                        company_logo,
                        company_description,
                        user_id
                    )
                )

                updated = cursor.fetchone()

                connection.commit()

                if updated is None:
                    return None

                return updated[0]

            cursor.execute(
                """
                INSERT INTO recruiter_profiles (
                    user_id,
                    hr_name,
                    company_name,
                    designation,
                    company_email,
                    company_contact,
                    company_website,
                    industry,
                    company_size,
                    headquarters,
                    company_logo,
                    company_description
                )
                VALUES (
                    %s, %s, %s, %s,
                    %s, %s, %s, %s,
                    %s, %s, %s, %s
                )
                RETURNING recruiter_profile_id;
                """,
                (
                    user_id,
                    hr_name,
                    company_name,
                    designation,
                    company_email,
                    company_contact,
                    company_website,
                    industry,
                    company_size,
                    headquarters,
                    company_logo,
                    company_description
                )
            )

            recruiter_profile = cursor.fetchone()

            connection.commit()

            if recruiter_profile is None:
                return None

            return recruiter_profile[0]

    except Exception:
        connection.rollback()
        return None

    finally:
        connection.close()