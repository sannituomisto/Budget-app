from entities.user import User
from database_connection import get_database_connection


class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, user):
        cursor = self._connection.cursor()
        cursor.execute("INSERT into Users (username, password) VALUES (?, ?)", [
                       user.username, user.password])
        self._connection.commit()
        return "User created successfully"

    def find_by_username(self, username):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM Users WHERE username = ?", [username])
        row = cursor.fetchone()
        if row:
            return (row['username'], row['password'])
        else:
            return None

    def find_all_users(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM Users")
        rows = cursor.fetchall()
        list = []
        for i in rows:
            list.append((i['username'], i['password']))
        return list

    def delete_all_users(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM Users")
        self._connection.commit()


user_repository = UserRepository(get_database_connection())
