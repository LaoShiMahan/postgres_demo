import psycopg2
from config import config
from commands import Command

def create(table_name):
    connection = None

    try:
        params = config()
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()

        # for command in Command.create_table():
        #     print(command)
        #     cursor.execute(command)

        cursor.execute(Command.create(), (table_name,))

        cursor.close()

        connection.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connection is not None:
            connection.close()