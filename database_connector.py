from database import Database
from job_database import JobDatabase


# -- connector with database.py --
def connection():
    name = 'demo'
    user = 'postgres'
    password = '123'
    host = 'localhost'
    port = '5432'
    table = 'users_pdp'

    db = Database(name, user, password, host, port, table)
    return db


def authenticate(username, password):
    if connection().login_data(username, password):
        return True
    else:
        return False


# -- connector with job_database.py --

def connection_job():
    name = 'demo'
    user = 'postgres'
    password = '123'
    host = 'localhost'
    port = '5432'
    table = 'job_application'

    db_job = JobDatabase(name, user, password, host, port, table)
    return db_job
