import pandas as pd
import plotly.express as px
import streamlit as st


def bar_chart(data, x, y, title):

    dataframe = pd.DataFrame(data)

    figure = px.bar(
        dataframe,
        x=x,
        y=y,
        title=title,
        text=y
    )

    figure.update_layout(
        xaxis_title=x,
        yaxis_title=y
    )

    st.plotly_chart(
        figure,
        use_container_width=True
    )


def line_chart(data, x, y, title):

    dataframe = pd.DataFrame(data)

    figure = px.line(
        dataframe,
        x=x,
        y=y,
        title=title,
        markers=True
    )

    figure.update_layout(
        xaxis_title=x,
        yaxis_title=y
    )

    st.plotly_chart(
        figure,
        use_container_width=True
    )


def pie_chart(data, names, values, title):

    dataframe = pd.DataFrame(data)

    figure = px.pie(
        dataframe,
        names=names,
        values=values,
        title=title
    )

    st.plotly_chart(
        figure,
        use_container_width=True
    )


def donut_chart(data, names, values, title):

    dataframe = pd.DataFrame(data)

    figure = px.pie(
        dataframe,
        names=names,
        values=values,
        title=title,
        hole=0.5
    )

    st.plotly_chart(
        figure,
        use_container_width=True
    )


def horizontal_bar_chart(data, x, y, title):

    dataframe = pd.DataFrame(data)

    figure = px.bar(
        dataframe,
        x=x,
        y=y,
        orientation="h",
        title=title,
        text=x
    )

    figure.update_layout(
        xaxis_title=x,
        yaxis_title=y
    )

    st.plotly_chart(
        figure,
        use_container_width=True
    )