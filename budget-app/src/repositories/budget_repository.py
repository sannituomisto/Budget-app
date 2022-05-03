from database_connection import get_database_connection


class BudgetRepository:
    def __init__(self, connection):
        """Luokka, joka vastaa tietokantaoperaatioista tuloihin ja kuluhin liittyen
        """

        self._connection = connection

    def create_expense(self, expense):
        """Kulun lisääminen tietokantaan

        Args:
            expense: Kulun Expense-olio, joka lisätään tietokantaan


        Returns:
            Ilmoitus, että kulun lisääminen onnistui.
        """

        cursor = self._connection.cursor()
        cursor.execute("INSERT into Expense (amount, category, username) VALUES (?, ?, ?)", [
                       expense.amount, expense.category, expense.username])
        self._connection.commit()
        return "Expense entered successfully"

    def create_income(self, income):
        """Tulon lisääminen tietokantaan

        Args:
            income: Tulon Income-olio, joka lisätään tietokantaan


        Returns:
            Ilmoitus, että tulon lisääminen onnistui.
        """

        cursor = self._connection.cursor()
        cursor.execute("INSERT into Income (amount, username) VALUES (?, ?)", [
                       income.amount, income.username])
        self._connection.commit()
        return "Income entered successfully"

    def find_all_expense(self, username):
        """Hakee kaikki kulut

        Returns:
            Palauttaa listan tupleja kuluista
        """

        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM Expense WHERE username= ?", [username])
        rows = cursor.fetchall()
        list_ = []
        for i in rows:
            list_.append((i['amount'], i['category']))
        return list_

    def find_all_income(self, username):
        """Hakee kaikki tulot

        Returns:
            Palauttaa listan tuloista
        """

        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM Income WHERE username= ?", [username])
        rows = cursor.fetchall()
        list_ = []
        for i in rows:
            list_.append((i['amount']))
        return list_

    def incomes_sum(self, username):
        """Hakee kaikkien tulojen yhteenlasketun summan

        Returns:
            Palauttaa summan
        """
        cursor=self._connection.cursor()
        cursor.execute("SELECT SUM(amount) FROM Income WHERE username= ?", [username])
        row = cursor.fetchone()[0]
        return row

    def expense_sum(self, username):
        """Hakee kaikkien kulujen yhteenlasketun summan

        Returns:
            Palauttaa summan
        """
        cursor=self._connection.cursor()
        cursor.execute("SELECT SUM(amount) FROM Expense WHERE username= ?", [username])
        row = cursor.fetchone()[0]
        return row


    def delete_all_expenses(self):
        """Poistaa kaikki kulut
        """
        
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM Expense")
        self._connection.commit()

    def delete_all_incomes(self):
        """Poistaa kaikki tulot
        """

        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM Income")
        self._connection.commit()


budget_repository = BudgetRepository(get_database_connection())
