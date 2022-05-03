from database_connection import get_database_connection

class UserRepository:
    """Luokka, joka vastaa tietokantaoperaatioista käyttäjiin liittyen"""

    def __init__(self, connection):
        self._connection = connection
        """Luokan konstruktori

        Args:
            connection: Tietokantayhteyden Connection-olio
        """

    def create(self, user):
        """Käyttäjän lisääminen tietokantaan

        Args:
            user: Käyttäjän User-olio, joka lisätään tietokantaan

        Returns:
            Ilmoitus, että käyttäjän lisääminen onnistui.
        """

        cursor = self._connection.cursor()
        cursor.execute("INSERT into Users (username, password) VALUES (?, ?)", [
                       user.username, user.password])
        self._connection.commit()

        return "User created successfully"

    def find_by_username(self, username):
        """Hakee tietyn käyttäjän käyttäjätunnuksen perusteella

        Args:
            username: Käyttätunnus, jonka käyttäjä haetaan

        Returns:
            Palauttaa käyttäjän tuplena, jos käyttäjätunnus oli olemassa
            Palauttaa None, jos käyttäjätunnusta ei ole olemassa
        """

        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM Users WHERE username = ?", [username])
        row = cursor.fetchone()
        if row:
            return (row['username'], row['password'])
        return None

    def find_all_users(self):
        """Hakee kaikki käyttäjät

        Returns:
            Palauttaa listan tupleja käyttäjistä
        """

        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM Users")
        rows = cursor.fetchall()
        list_ = []
        for i in rows:
            list_.append((i['username'], i['password']))
        return list_

    def delete_all_users(self):
        """Poistaa kaikki käyttäjät
        """
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM Users")
        self._connection.commit()


user_repository = UserRepository(get_database_connection())
