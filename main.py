import psycopg2
from config import config

def connect():
    connection = None

    try:
        params = config()

        print("Connecting to the database")

        connection = psycopg2.connect(**params)
        cursor = connection.cursor()

        print("Database version: ")
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print(db_version)

        cursor.close()
    
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: ")
        print(error)

    finally:
        if connection is not None:
            connection.close()

connect()