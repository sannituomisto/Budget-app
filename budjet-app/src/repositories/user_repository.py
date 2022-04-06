from entities.user import User
from database_connection import get_database_connection

def get_user_by_row(row):
    return User(row['username'], row['password']) if row else None


class UserRepository:
    def __init__(self, connection):
        self._connection=connection

    def create(self, user):
        cursor = self._connection.cursor()
        cursor.execute("INSERT into Users (username, password) VALUES (?, ?)",[user.username, user.password])
        self._connection.commit()
        return 

    def find_by_username(self, username):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM Users WHERE username = ?", [username])
        row = cursor.fetchone()
        return row

    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM Users")
        rows = cursor.fetchall()
        return rows
        
    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM Users")
        self._connection.commit()

user_repository = UserRepository(get_database_connection())