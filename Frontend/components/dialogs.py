import streamlit as st


def success(message):

    st.success(
        message,
        icon="✅"
    )


def error(message):

    st.error(
        message,
        icon="❌"
    )


def warning(message):

    st.warning(
        message,
        icon="⚠️"
    )


def info(message):

    st.info(
        message,
        icon="ℹ️"
    )


def delete_confirmation(item_name):

    return st.checkbox(
        f"I confirm deleting '{item_name}'."
    )


def confirm_button(label="Confirm"):

    return st.button(
        label,
        type="primary",
        use_container_width=True
    )


def cancel_button(label="Cancel"):

    return st.button(
        label,
        use_container_width=True
    )


def operation_result(successful, success_message, error_message):

    if successful:

        success(
            success_message
        )

    else:

        error(
            error_message
        )