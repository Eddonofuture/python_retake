class Database:
    # db implementation
    pass

database = None

def initialize_database():
    global database # dice que es un nivel de modulo
    database = Database()