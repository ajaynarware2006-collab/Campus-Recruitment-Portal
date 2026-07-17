import psycopg as pg
import streamlit as st

def connect_db():
    try:
        connection=pg.connect(
            host=st.secrets["DB_HOST"],
            dbname=st.secrets["DB_NAME"],
            user=st.secrets["DB_USER"],
            password=st.secrets["DB_PASSWORD"],
            port=st.secrets["DB_PORT"])
            
        return connection
    
    except Exception as e:
        return e
