import streamlit as st
import psycopg2


class Database:
    def __init__(self, database_name, database_user, database_password, database_host, database_port, table_name):
        self.database_name = database_name
        self.database_user = database_user
        self.database_password = database_password
        self.database_host = database_host
        self.database_port = database_port
        self.table_name = table_name

    def create_table(self):
        conn = psycopg2.connect(dbname=self.database_name, user=self.database_user, password=self.database_password,
                                host=self.database_host, port=self.database_port)
        cur = conn.cursor()
        query = (f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema = 'public' AND table_name "
                 f"= %s);")
        cur.execute(query, (self.table_name,))
        result_tables = cur.fetchone()[0]
        if result_tables:
            print('table exists')
        else:
            cur.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name}(ID SERIAL PRIMARY KEY, LOGIN TEXT, PASSWORD "
                        f"TEXT);")
            print('create table')
            conn.commit()
            conn.close()

    def sign_up(self, login, user_password):
        conn = psycopg2.connect(dbname=self.database_name, user=self.database_user, password=self.database_password,
                                host=self.database_host, port=self.database_port)
        cur = conn.cursor()

        query = f'INSERT INTO {self.table_name}(login, password) VALUES (%s, %s);'
        cur.execute(query, (login, user_password))
        print("Data inserted successfully")
        conn.commit()
        conn.close()

    def login_data(self, login, user_password):
        conn = psycopg2.connect(dbname=self.database_name, user=self.database_user, password=self.database_password,
                                host=self.database_host, port=self.database_port)
        cur = conn.cursor()
        query = f'SELECT COUNT(*) FROM {self.table_name} WHERE login= %s;'
        cur.execute(query, (login,))
        result = cur.fetchone()
        count = result[0]
        if count == 1:
            query = f'SELECT password FROM {self.table_name} WHERE login = %s;'
            cur.execute(query, (login,))
            password_from_db = cur.fetchone()[0]
            conn.close()

            if user_password != password_from_db:
                return False
            else:
                return True
        else:
            return False


def connection():
    name = 'demo'
    user = 'postgres'
    password = '123'
    host = 'localhost'
    port = '5432'
    table = 'users_pdp'

    db = Database(name, user, password, host, port, table)
    return db


def main():
    st.title("Welcome in Personal Data Platform!")
    page = st.radio("Choose one", ["Login", "Sign Up"])

    if page == "Sign Up":
        sign_up_page()
    elif page == "Login":
        if login_page():
            dashboard()
        else:
            st.write("Please login first to access the dashboard")

    connection().create_table()


def dashboard():
    st.title("Dashboard")
    st.write("Welcome to the dashboard!")


def authenticate(username, password):
    if connection().login_data(username, password):
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
            st.error("Invalid username or password. Try Sign up!")
    return False


def sign_up_page():
    st.title("Sign Up")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Sign Up"):
        connection().sign_up(username, password)
        st.success("Sign up successful! Please log in.")


if __name__ == "__main__":
    main()
