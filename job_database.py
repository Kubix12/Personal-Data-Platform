import psycopg2
from datetime import datetime


class JobDatabase:
    def __init__(self, database_name, database_user, database_password, database_host, database_port, table_name):
        self.database_name = database_name
        self.database_user = database_user
        self.database_password = database_password
        self.database_host = database_host
        self.database_port = database_port
        self.table_name = table_name

    def save_data(self, job_title, company_name, notes):
        conn = psycopg2.connect(dbname=self.database_name, user=self.database_user, password=self.database_password,
                                host=self.database_host, port=self.database_port)
        cur = conn.cursor()
        query = f"INSERT INTO {self.table_name} (date, job_title, company_name, notes) VALUES (%s, %s, %s, %s);"
        cur.execute(query, (datetime.now(), job_title, company_name, notes))
        conn.commit()
        conn.close()

    def get_data_sorted_by_date(self):
        conn = psycopg2.connect(dbname=self.database_name, user=self.database_user, password=self.database_password,
                                host=self.database_host, port=self.database_port)
        cur = conn.cursor()
        query = f"SELECT * FROM {self.table_name} ORDER BY date;"
        cur.execute(query)
        data = cur.fetchall()
        conn.commit()
        conn.close()
        return data

    def get_data_by_date(self, date):
        conn = psycopg2.connect(dbname=self.database_name, user=self.database_user, password=self.database_password,
                                host=self.database_host, port=self.database_port)
        cur = conn.cursor()
        query = f"SELECT * FROM {self.table_name} WHERE date = %s"
        cur.execute(query, (date,))
        data = cur.fetchall()
        conn.commit()
        conn.close()
        return data
