import psycopg2
from config import config

def create_table():
    commands = (
        "SELECT version();",
        """
            CREATE TABLE table_one (
                _id     SERIAL       PRIMARY KEY          ,
                _name   VARCHAR(50)               NOT NULL,
                _price  INTEGER
            );
        """
    )

    connection = None

    try:
        params = config()
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()

        for command in commands:
            print(command)
            cursor.execute(command)

        cursor.close()

        connection.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connection is not None:
            connection.close()

create_table()