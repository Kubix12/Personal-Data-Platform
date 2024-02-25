import streamlit as st
import sys

sys.path.append(r'C:\Users\banas\Desktop\ProjectsPython\Personal-Data-Platform\02_database')
from db_users import Database


def authenticate(username, password):
    if Database.login_data(username, password):
        return True
    else:
        return False


def login_page():
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate(username, password):
            st.success("Logged in successfully!")
            return True
        else:
            st.error("Invalid username or password. Try Sign up")
    return False


def main():
    is_authenticated = login_page()

    if is_authenticated:
        st.title("Dashboard")
        st.write("Welcome to the dashboard!")


if __name__ == "__main__":
    main()
