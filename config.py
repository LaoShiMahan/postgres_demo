from configparser import ConfigParser

def config(file_name = "database.ini", section = "postgresql"):
    parser = ConfigParser()
    parser.read(file_name)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception("Section {0} not found in the {1} file".format(section, file_name))
    
    return db