import streamlit as st
from database.db_users import Database


def sign_up():
    st.title("Sign up")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Sign up"):
        Database.sign_up(username, password)
        st.success("Sign up successfully!")


def main():
    sign_up()


if __name__ == "__main__":
    main()
