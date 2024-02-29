import streamlit as st
import psycopg2
from database import Database
import pages


if pages.main() == 1:
    pages.sign_up_page()
else:
    if pages.login_page():
        pages.dashboard()
