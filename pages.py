import streamlit as st
import database_connector
from database import Database


def main():
    st.title("Welcome in Personal Data Platform!")
    page = st.radio("Choose one", ["Login", "Sign Up"])
    database_connector.connection().create_table()
    if page == "Sign Up":
        return 1
    elif page == "Login":
        return 2
    database_connector.connection().create_table()


def login_page():
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if database_connector.authenticate(username, password):
            st.success("Logged in successfully!")
            return True
        else:
            st.error("Invalid username or password. Try Sign up!")
    return False


def sign_up_page():
    st.title("Sign Up")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Sign Up"):
        s = database_connector.connection().sign_up(username, password)
        if s:
            st.success("Sign up successful! Please log in.")
        else:
            st.success("Username already exist. Please try another username")


def dashboard():
    st.title("Dashboard")
    left_column, right_column = st.columns(2)
    with left_column:
        if st.button("To-Do list"):
            todo_list_page()
    with right_column:
        if st.button("Calendar"):
            calendar()
