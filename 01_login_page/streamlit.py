import streamlit as st


class Login:

    @staticmethod
    def dashboard_page():
        st.write("""
        # Dashboard
        Welcome to the dashboard!
        """)
    @staticmethod
    def login_page():
        st.write("""
        # Login
        Please enter your credentials
        """)

    # Add login form inputs
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Add login button
    if st.button("Login"):
        # Perform login authentication here (replace this with your authentication logic)
        if username == "example" and password == "password":
            session_state.page = "dashboard"  # Change to dashboard page

# Determine which page to show based on session state
if session_state.page == "dashboard":
    dashboard_page()
else:
    login_page()
