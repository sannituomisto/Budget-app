from database_connection import get_database_connection


class BudgetRepository:
    def __init__(self, connection):
        self._connection = connection

    def create_expense(self, expense):
        cursor = self._connection.cursor()
        cursor.execute("INSERT into Expense (amount, category, username) VALUES (?, ?, ?)", [
                       expense.amount, expense.category, expense.username])
        self._connection.commit()
        return "Expense entered successfully"

    def create_income(self, income):
        cursor = self._connection.cursor()
        cursor.execute("INSERT into Income (amount, username) VALUES (?, ?)", [
                       income.amount, income.username])
        self._connection.commit()
        return "Income entered successfully"

    def find_all_expense(self, username):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM Expense WHERE username= ?", [username])
        rows = cursor.fetchall()
        list_ = []
        for i in rows:
            list_.append((i['amount'], i['category']))
        return list_

    def find_all_income(self, username):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM Income WHERE username= ?", [username])
        rows = cursor.fetchall()
        list_ = []
        for i in rows:
            list_.append((i['amount']))
        return list_

    def delete_all_expenses(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM Expense")
        self._connection.commit()

    def delete_all_incomes(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM Income")
        self._connection.commit()


budget_repository = BudgetRepository(get_database_connection())
