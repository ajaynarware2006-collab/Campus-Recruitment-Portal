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

    with connection.cursor() as cursor:

        cursor.execute(
            "SELECT user_role FROM users WHERE user_id=%s;",
            (user_id,)
        )

        user = cursor.fetchone()

        if not user:
            return None

        if user[0] != "Recruiter":
            return None

        cursor.execute(
            "SELECT recruiter_profile_id FROM recruiter_profiles WHERE user_id=%s;",
            (user_id,)
        )

        recruiter = cursor.fetchone()

        if recruiter:

            cursor.execute(
                """
                UPDATE recruiter_profiles
                SET
                    hr_name=%s,
                    company_name=%s,
                    designation=%s,
                    company_email=%s,
                    company_contact=%s,
                    company_website=%s,
                    industry=%s,
                    company_size=%s,
                    headquarters=%s,
                    company_logo=%s,
                    company_description=%s
                WHERE user_id=%s;
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

            connection.commit()

            return recruiter[0]

        cursor.execute(
            """
            INSERT INTO recruiter_profiles(
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
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
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

        recruiter_profile_id = cursor.fetchone()

        connection.commit()

        if not recruiter_profile_id:
            return None

        return recruiter_profile_id[0]