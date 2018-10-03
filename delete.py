import psycopg2
from config import config
from commands import Command

def delete(_id):
    connection = None
    rows_deleted = 0

    try:
        params = config()
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()

        cursor.execute(Command.delete(), (_id,))

        rows_deleted = cursor.rowcount

        connection.commit()

        cursor.close()
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connection is not None:
            connection.close()

    return rows_deleted