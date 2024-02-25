import psycopg2
import bcrypt


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
            hashed_password_from_db = cur.fetchone()[0]
            conn.close()

            # Hash the provided password using the same salt as the stored password
            bytes_password = user_password.encode('utf-8')
            hashed_password_new = bcrypt.hashpw(bytes_password, hashed_password_from_db.encode('utf-8'))

            if hashed_password_new != hashed_password_from_db.encode('utf-8'):
                return False

            else:
                return True

        else:
            return False


# Database setting
name = 'demo'
user = 'postgres'
password = '123'
host = 'localhost'
port = '5432'
table = 'users_pdp'

db = Database(name, user, password, host, port, table)
db.create_table()
