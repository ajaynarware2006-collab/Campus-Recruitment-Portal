import streamlit as st


def initialize_session():

    defaults = {
        "logged_in": False,
        "user_id": None,
        "role": None,
        "email": None,
        "current_page": "home",
        "profile_completed": False,
        "theme": "dark"
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def login_user(user_id, email, role):

    st.session_state.logged_in = True
    st.session_state.user_id = user_id
    st.session_state.email = email
    st.session_state.role = role


def logout_user():

    st.session_state.logged_in = False
    st.session_state.user_id = None
    st.session_state.email = None
    st.session_state.role = None
    st.session_state.current_page = "home"
    st.session_state.profile_completed = False
    st.session_state.theme = "dark"


def set_current_page(page):

    st.session_state.current_page = page


def get_current_page():

    return st.session_state.get("current_page", "home")


def user_logged_in():

    return st.session_state.get("logged_in", False)


def get_user_role():

    return st.session_state.get("role")


def get_user_id():

    return st.session_state.get("user_id")


def profile_completed():

    return st.session_state.get("profile_completed", False)


def complete_profile():

    st.session_state.profile_completed = True