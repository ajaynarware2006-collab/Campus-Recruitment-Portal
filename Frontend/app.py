import streamlit as st
from pathlib import Path

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

    css_path = Path("assets/style.css")

    if css_path.exists():
        st.markdown(
            f"<style>{css_path.read_text(encoding='utf-8')}</style>",
            unsafe_allow_html=True
        )


def main():

    configure_page()

    load_css()

    initialize_session()

    render_page()


if __name__ == "__main__":
    main()