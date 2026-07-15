import os
from pathlib import Path

import streamlit as st


UPLOAD_DIRECTORY = "uploads"


def ensure_upload_directory():

    Path(
        UPLOAD_DIRECTORY
    ).mkdir(
        parents=True,
        exist_ok=True
    )


def save_uploaded_file(uploaded_file, subdirectory):

    if uploaded_file is None:
        return None

    ensure_upload_directory()

    folder = Path(
        UPLOAD_DIRECTORY
    ) / subdirectory

    folder.mkdir(
        parents=True,
        exist_ok=True
    )

    file_path = folder / uploaded_file.name

    with open(file_path, "wb") as file:

        file.write(
            uploaded_file.getbuffer()
        )

    return str(file_path)


def upload_resume():

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf"]
    )

    if uploaded_file:

        return save_uploaded_file(
            uploaded_file,
            "resumes"
        )

    return None


def upload_profile_image():

    uploaded_file = st.file_uploader(
        "Upload Profile Image",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_file:

        return save_uploaded_file(
            uploaded_file,
            "profile_images"
        )

    return None


def upload_company_logo():

    uploaded_file = st.file_uploader(
        "Upload Company Logo",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_file:

        return save_uploaded_file(
            uploaded_file,
            "company_logos"
        )

    return None


def delete_uploaded_file(file_path):

    if not file_path:

        return False

    if os.path.exists(file_path):

        os.remove(file_path)

        return True

    return False