import psycopg2
from config import config
from commands import Command

def insert(_name):
    connection = None
    _id = None

    try:
        params = config()
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()

        cursor.execute(Command.insert(), (_name,))

        _id = cursor.fetchone()[0]

        connection.commit()

        connection.close()
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connection is not None:
            connection.close()

    return _id

def insert_list(data_list):
    connection = None

    try:
        params = config()
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()

        cursor.executemany(Command.insert_list(), data_list)

        connection.commit()

        connection.close()
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connection is not None:
            connection.close()