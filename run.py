from main import *

while True:
    user_input = input(
        """
            Choose from the following commands: 
                delete
                insert
                select
                test
                update
                end
        """).lower()

    # if user_input == "create":
    #     table_name = input("Table name? ")
    #     create(table_name)

    if user_input == "delete":
        _id = input("Which id would you like to delete? ")
        delete(_id)

    if user_input == "insert":
        _name = input("What do you want to name your insert? ")
        insert(_name)

    if user_input == "select":
        select()

    if user_input == "test":
        test()

    if user_input == "update":
        _id = input("Which id would you like to update? ")
        _name = input("What do you want to update the name to? ")
        update(_id, _name)

    if user_input == "end":
        break