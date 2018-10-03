import psycopg2
from config import config

def update(_id, _name):
    connection = None
    updated_rows = 0

    try:
        params = config()
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()

        cursor.execute(Command.update, (_name, _id))

        updated_rows = cursor.rowcount

        connection.commit()

        connection.close()
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connection is not None:
            connection.close()

    return updated_rows