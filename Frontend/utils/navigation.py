import streamlit as st

from pages.home import show_home
from pages.login import show_login
from pages.signup import show_signup
from pages.forgot_password import show_forgot_password

from pages.student_dashboard import show_student_dashboard
from pages.student_profile import show_student_profile
from pages.browse_jobs import show_browse_jobs
from pages.job_details import show_job_details
from pages.application_history import show_application_history

from pages.recruiter_dashboard import show_recruiter_dashboard
from pages.recruiter_profile import show_recruiter_profile
from pages.post_job import show_post_job
from pages.manage_jobs import show_manage_jobs
from pages.view_applications import show_view_applications
from pages.recruiter_analytics import show_recruiter_analytics

from pages.admin_dashboard import show_admin_dashboard
from pages.manage_users import show_manage_users
from pages.reports import show_reports


def render_page():

    page = st.session_state.current_page

    page_routes = {

        "home": show_home,
        "login": show_login,
        "signup": show_signup,
        "forgot_password": show_forgot_password,

        "student_dashboard": show_student_dashboard,
        "student_profile": show_student_profile,
        "browse_jobs": show_browse_jobs,
        "job_details": show_job_details,
        "application_history": show_application_history,

        "recruiter_dashboard": show_recruiter_dashboard,
        "recruiter_profile": show_recruiter_profile,
        "post_job": show_post_job,
        "manage_jobs": show_manage_jobs,
        "view_applications": show_view_applications,
        "recruiter_analytics": show_recruiter_analytics,

        "admin_dashboard": show_admin_dashboard,
        "manage_users": show_manage_users,
        "reports": show_reports
    }

    page_function = page_routes.get(page)

    if page_function:
        page_function()
    else:
        st.error("Page not found.")