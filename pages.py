import streamlit as st
import database_connector
import job_database
from database import Database
from job_database import JobDatabase
import pandas as pd
from streamlit_calendar import calendar
import calendar_page
import datetime


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

    st.title("Current application:")
    st.write('Get data sorted by date:')

    # -- GET DATA SORTED BY DATE --
    if st.button('Get data sorted by date'):
        sorted_data = database_connector.connection_job().get_data_sorted_by_date()
        st.write(pd.DataFrame(sorted_data, columns=["Date", "Job Title", "Company Name", "Notes"]))

    # -- GET DATA BY DATE
    st.write('Get data by date:')
    date_input = str(st.text_input('Enter date (YYYY-MM-DD):'))
    if st.button('Get data by date'):
        if date_input:
            data = database_connector.connection_job().get_data_by_date(date_input)
            if data:
                st.write(pd.DataFrame(data))
            else:
                st.write('No data found for data:', date_input)
        else:
            st.write('Waiting for "Get data" button to be clicked')
    else:
        st.write('Please enter a valid date')


def calendar_dashboard():
    st.title('Calendar App')
    calendar_1 = calendar(events=calendar_page.calendar_events, options=calendar_page.calendar_options,
                          custom_css=calendar_page.custom_css)
    print(calendar_1)
    st.write(calendar_1)


def to_do_list():
    todo_list = []
    st.title('To do list App')
    item = st.text_input('Enter to-do item')
    if st.button('Add'):
        if item:
            todo_list.append(item)
            st.success('Successfully added')
        else:
            st.warning("Please enter to-do item")

    if todo_list:
        st.write("To-Do List:")
        for i, val in enumerate(todo_list, start=1):
            st.write(i, val)

    else:
        st.write("Your current list is empty")


def dashboard():
    st.title("Personal Dashboard")
    if st.button("Logout", type="primary"):
        st.session_state.is_authenticated = False
    page = st.selectbox('Choose one', ['Job application', 'Calendar', 'To do list'])
    if page == 'Job application':
        job_application()
    elif page == 'Calendar':
        calendar()
    elif page == 'To do list':
        to_do_list()
