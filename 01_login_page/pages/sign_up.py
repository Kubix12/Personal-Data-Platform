import streamlit as st
from


def sign_up():
    st.title("Sign up")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Sign up"):

        st.success("Sign up successfully!")


def main():
    sign_up()


if __name__ == "__main__":
    main()
