import streamlit as st
import psycopg2
from database import Database
import pages


def main():
    if 'is_authenticated' not in st.session_state:
        st.session_state.is_authenticated = False
    if not st.session_state.is_authenticated:
        page = pages.main()
        if page == 1:
            pages.sign_up_page()
        else:
            if pages.login_page():
                st.session_state.is_authenticated = True
                pages.dashboard()
    else:
        pages.dashboard()


if __name__ == "__main__":
    main()
