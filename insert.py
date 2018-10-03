import psycopg2
from config import config

def insert_data(_name):
    command = (
        """
            INSERT INTO table_one
                (_name)
            VALUES(%s)
            RETURNING _id;
        """
    )

    connection = None
    _id = None

    try:
        params = config()
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()

        cursor.execute(command, (_name,))

        _id = cursor.fetchone()[0]

        connection.commit()

        connection.close()
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connection is not None:
            connection.close()

    return _id

# insert_data("Chutes and Ladders")

def insert_data_list(data_list):
    command = (
        """
            INSERT INTO table_one
                (_name)
            VALUES(%s)
            RETURNING _id;
        """
    )

    connection = None

    try:
        params = config()
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()

        cursor.executemany(command, data_list)

        connection.commit()

        connection.close()
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connection is not None:
            connection.close()

data = [("Sorry",), ("Skyrim",), ("Starcraft",), ("Mariocart",), ("Warcraft",)]

insert_data_list(data)