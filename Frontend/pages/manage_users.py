import streamlit as st

from Backend.admin.users import (
    get_all_users,
    update_user_status,
    delete_user
)

from components.navbar import render_navbar
from components.sidebar import render_sidebar
from components.footer import render_footer

from components.tables import users_table


def show_manage_users():

    render_navbar()

    render_sidebar()

    st.title("Manage Users")

    users = get_all_users()

    if not users:

        st.info(
            "No users found."
        )

        render_footer()

        return

    users_table(
        users
    )

    st.divider()

    st.subheader(
        "Manage User"
    )

    user_id = st.number_input(
        "User ID",
        min_value=1,
        step=1
    )

    status = st.selectbox(
        "Account Status",
        [
            "Active",
            "Inactive",
            "Suspended"
        ]
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "Update Status",
            use_container_width=True
        ):

            success = update_user_status(
                user_id,
                status
            )

            if success:

                st.success(
                    "User status updated successfully."
                )

                st.rerun()

            else:

                st.error(
                    "Failed to update user status."
                )

    with col2:

        if st.button(
            "Delete User",
            use_container_width=True
        ):

            success = delete_user(
                user_id
            )

            if success:

                st.success(
                    "User deleted successfully."
                )

                st.rerun()

            else:

                st.error(
                    "Failed to delete user."
                )

    render_footer()