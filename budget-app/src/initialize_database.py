from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS Users;")
    cursor.execute("DROP TABLE IF EXISTS Expense")
    cursor.execute("DROP TABLE IF EXISTS Income")
    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE Users (username TEXT PRIMARY KEY,password TEXT);")
    cursor.execute(
        "CREATE TABLE Expense(id INTEGER PRIMARY KEY, amount INT, category TEXT, username TEXT)")
    cursor.execute(
        "CREATE TABLE Income(id INTEGER PRIMARY KEY, amount INT, username TEXT)")
    connection.commit()


def initialize_database():
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
