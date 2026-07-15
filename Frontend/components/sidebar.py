import streamlit as st

from utils.session import (
    get_user_role,
    set_current_page
)


def render_sidebar():

    role = get_user_role()

    with st.sidebar:

        st.title("Navigation")

        if role == "Student":
            student_sidebar()

        elif role == "Recruiter":
            recruiter_sidebar()

        elif role == "Admin":
            admin_sidebar()


def student_sidebar():

    if st.button("🏠 Dashboard", use_container_width=True):
        set_current_page("student_dashboard")
        st.rerun()

    if st.button("👤 My Profile", use_container_width=True):
        set_current_page("student_profile")
        st.rerun()

    if st.button("💼 Browse Jobs", use_container_width=True):
        set_current_page("browse_jobs")
        st.rerun()

    if st.button("📄 Application History", use_container_width=True):
        set_current_page("application_history")
        st.rerun()


def recruiter_sidebar():

    if st.button("🏠 Dashboard", use_container_width=True):
        set_current_page("recruiter_dashboard")
        st.rerun()

    if st.button("🏢 Company Profile", use_container_width=True):
        set_current_page("recruiter_profile")
        st.rerun()

    if st.button("➕ Post Job", use_container_width=True):
        set_current_page("post_job")
        st.rerun()

    if st.button("📋 Manage Jobs", use_container_width=True):
        set_current_page("manage_jobs")
        st.rerun()

    if st.button("👨‍🎓 Applications", use_container_width=True):
        set_current_page("view_applications")
        st.rerun()

    if st.button("📊 Analytics", use_container_width=True):
        set_current_page("recruiter_analytics")
        st.rerun()


def admin_sidebar():

    if st.button("🏠 Dashboard", use_container_width=True):
        set_current_page("admin_dashboard")
        st.rerun()

    if st.button("👥 Manage Users", use_container_width=True):
        set_current_page("manage_users")
        st.rerun()

    if st.button("📈 Reports", use_container_width=True):
        set_current_page("reports")
        st.rerun()