import streamlit as st

from utils.session import initialize_session
from utils.navigation import render_page


def configure_page():

    st.set_page_config(
        page_title="Campus Recruitment Portal",
        page_icon="🎓",
        layout="wide",
        initial_sidebar_state="collapsed"
    )


def load_css():

    with open("assets/style.css") as css:
        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True
        )


def main():

    configure_page()

    load_css()

    initialize_session()

    render_page()


if __name__ == "__main__":
    main()