class Income:
    """Tuloja kuvaava luokka

    Attributes:
        amount: Tulon suuruus lukuarvona
        username: Käyttäjän merkkijonoarvoinen käyttäjätunnus
    """

    def __init__(self, amount, username):
        """Konstruktori, jolla luodaan uusi tulo

        Args:
            amount: Tulon suuruus lukuarvona
            username: Käyttäjän merkkijonoarvoinen käyttäjätunnus
        """

        self.amount = amount
        self.username = username
