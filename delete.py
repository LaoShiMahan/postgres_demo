import psycopg2
from config import config

def delete_data(_id):
    command = (
        """
            DELETE
            FROM table_one
            WHERE _id = %s
        """
    )

    connection = None
    rows_deleted = 0

    try:
        params = config()
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()

        cursor.execute(command, (_id,))

        rows_deleted = cursor.rowcount

        connection.commit()

        cursor.close()
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connection is not None:
            connection.close()

    return rows_deleted

delete_data(15)