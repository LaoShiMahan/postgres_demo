import psycopg2
from config import config

def select_data():
    command = (
        """
            SELECT
                _id,
                _name
            FROM table_one
        """
    )

    connection = None

    try:
        params = config()
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()

        cursor.execute(command)

        row = cursor.fetchone()

        while row is not None:
            print(row)
            row = cursor.fetchone()

        cursor.close()
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connection is not None:
            connection.close()

select_data()