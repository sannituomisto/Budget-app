class User:
    """Käyttäjää kuvaava luokka
    
    Attributes:
        username: Käyttäjän merkkijonoarvoinen käyttäjätunnus
        password: Käyttäjän merkkijonoarvoinen salasana
    """

    def __init__(self, username, password):
        """Konstruktori, jolla luodaan uusi käyttäjä
    
        Args:
            username: Käyttäjän merkkijonoarvoinen käyttäjätunnus
            password: Käyttäjän merkkijonoarvoinen salasana
        """
        
        self.username = username
        self.password = password
