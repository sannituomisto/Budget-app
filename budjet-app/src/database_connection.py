import os
import sqlite3
from config import DATABASE_FILE_PATH


connection = sqlite3.connect(DATABASE_FILE_PATH)
connection.row_factory = sqlite3.Row
print("THE REAL SQLPATH is", os.path.realpath(connection))



def get_database_connection():
    return connection
