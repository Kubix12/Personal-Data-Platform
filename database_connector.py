from database import Database


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
