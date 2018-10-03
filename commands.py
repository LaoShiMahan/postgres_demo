class Command:
    def __init__(self):
        pass

    @classmethod
    def create(self):
        return (
            """
                CREATE TABLE %s (
                    _id     SERIAL       PRIMARY KEY          ,
                    _name   VARCHAR(50)               NOT NULL,
                    _price  INTEGER
                );
            """
        )

    @classmethod
    def delete(self):
        return (
            """
                DELETE
                FROM table_one
                WHERE _id = %s
            """
        )

    @classmethod
    def insert(self):
        return (
            """
                INSERT INTO table_one
                    (_name)
                VALUES(%s)
                RETURNING _id;
            """
        )

    @classmethod
    def insert_list(self):
        return (
            """
                INSERT INTO table_one
                    (_name)
                VALUES(%s)
                RETURNING _id;
            """
        )

    @classmethod
    def select(self):
        return (
            """
                SELECT *
                FROM table_one
            """
        )

    @classmethod
    def update(self):
        return (
        """
            UPDATE table_one
            SET _name = %s
            WHERE _id = %s
        """
    )