import streamlit as st
import database_connector
from database import Database
from job_database import JobDatabase
import pandas as pd


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


def job_application():
    st.title('Job application App')
    st.subheader("Save Data:")
    job_title = st.text_input("Job title:")
    company_name = st.text_input("Company name:")
    notes = st.text_input("Important notes:")
    if st.button("Save"):
        database_connector.connection_job().save_data(job_title, company_name, notes)
        st.success("Data saved successfully!")
    sorted_data = database_connector.connection_job().get_data_sorted_by_date()
    st.write(pd.DataFrame(sorted_data, columns=["Date", "Job Title", "Company Name", "Notes"]))


def calendar():
    st.title('Calendar')


def to_do_list():
    st.title('To do list')


def dashboard():
    st.title("Dashboard")
    page = st.selectbox('Choose one', ['Job application', 'Calendar', 'To do list'])
    if st.button("Logout"):
        st.session_state.is_authenticated = False
    if page == 'Job application':
        job_application()
    elif page == 'Calendar':
        calendar()
    elif page == 'To do list':
        to_do_list()
