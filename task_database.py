import psycopg2


class TaskDatabase:
    def __init__(self, database_name, database_user, database_password, database_host, database_port, table_name):
        self.database_name = database_name
        self.database_user = database_user
        self.database_password = database_password
        self.database_host = database_host
        self.database_port = database_port
        self.table_name = table_name

    def save_data(self, task_description, due_time, status):
        conn = psycopg2.connect(dbname=self.database_name, user=self.database_user, password=self.database_password,
                                host=self.database_host, port=self.database_port)
        cur = conn.cursor()
        query = f"INSERT INTO {self.table_name} (description, due_date, status) VALUES (%s, %s, %s);"
        cur.execute(query, (task_description, due_time, status))
        conn.commit()
        conn.close()

    def get_data(self):
        conn = psycopg2.connect(dbname=self.database_name, user=self.database_user, password=self.database_password,
                                host=self.database_host, port=self.database_port)
        cur = conn.cursor()
        query = f"SELECT * FROM {self.table_name};"
        cur.execute(query)
        data = cur.fetchall()
        conn.commit()
        conn.close()
        return data

    def update_status(self, task_id, status):
        conn = psycopg2.connect(dbname=self.database_name, user=self.database_user, password=self.database_password,
                                host=self.database_host, port=self.database_port)
        cur = conn.cursor()
        query = f"UPDATE {self.table_name} SET status = %s WHERE task_id = %s"
        cur.execute(query, (status, task_id))
        conn.commit()
        conn.close()

    def delete_data(self, task_id):
        conn = psycopg2.connect(dbname=self.database_name, user=self.database_user, password=self.database_password,
                                host=self.database_host, port=self.database_port)
        cur = conn.cursor()
        query = f"DELETE FROM {self.table_name} WHERE task_id = %s"
        cur.execute(query, (task_id,))
        conn.commit()
        conn.close()