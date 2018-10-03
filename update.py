import psycopg2
from config import config

def update_data(_id, _name):
    command = (
        """
            UPDATE table_one
            SET _name = %s
            WHERE _id = %s
        """
    )

    connection = None
    updated_rows = 0

    try:
        params = config()
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()

        cursor.execute(command, (_name, _id))

        updated_rows = cursor.rowcount

        connection.commit()

        connection.close()
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connection is not None:
            connection.close()

    return updated_rows

update_data(19, "World of Warcraft")