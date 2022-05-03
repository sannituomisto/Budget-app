class Expense:
    """Kuluja kuvaava luokka

    Attributes:
        amount: Kulun suuruus lukuarvona
        category: Kulun merkkijonoarvoinen kategoria 
        username: Käyttäjän merkkijonoarvoinen käyttäjätunnus
    """

    def __init__(self, amount, category, username):
        """Konstruktori, jolla luodaan uusi kulu

        Args:
            amount: Kulun suuruus lukuarvona
            category: Kulun merkkijonoarvoinen kategoria 
            username: Käyttäjän merkkijonoarvoinen käyttäjätunnus
        """

        self.amount = amount
        self.category = category
        self.username = username
