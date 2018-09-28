import psycopg2
import psycopg2.extras
from os import getenv
from functools import wraps

def get_connection_string():
    db_name = getenv('SAMPLER_DB', False)
    db_user = getenv('PSQL_USER_NAME', False)
    db_password = getenv('PSQL_PASSWORD', False)
    db_host = getenv('PSQL_HOST', False)

    if db_name and db_user and db_password and db_host:
        return f'postgresql://{db_user}:{db_password}@{db_host}/{db_name}'
    else:
        print('Some enviromental variables are not set!')
        raise KeyError


def get_connection():
    try:
        connection = psycopg2.connect( get_connection_string() )
        connection.autocommit = True
        return connection
    except psycopg2.DatabaseError as e:
        print('Database connection problem!')
        raise e


def connection_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        connection = get_connection()
        cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cursor.close()
        connection.close()
        return func(cursor, *args, **kwargs)
    return wrapper