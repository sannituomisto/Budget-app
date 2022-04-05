import os
import sqlite3

dirname = os.path.dirname(__file__)
print("MYDIR = ", os.path.realpath(dirname))

connection = sqlite3.connect(os.path.join(dirname, "..", "data", "database.sqlite"))
connection.row_factory = sqlite3.Row
print("THE REAL SQLPATH is", os.path.realpath(connection))



def get_database_connection():
    return connection
