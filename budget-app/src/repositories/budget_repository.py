from database_connection import get_database_connection

class BudgetRepository:
    def __init__(self,connection):
        self._connection = connection

    def create(self, expense):
        cursor = self._connection.cursor()
        cursor.execute("INSERT into Expense (amount, category, username) VALUES (?, ?, ?)", [
                       expense.amount, expense.category, expense.username])
        self._connection.commit()
        return "Expense entered successfully"

    def find_all_expense(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM Expense")
        rows = cursor.fetchall()
        list = []
        for i in rows:
            list.append((i['amount'], i['category']))
        return list

    def delete_all_expenses(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM Expense")
        self._connection.commit()

budget_repository = BudgetRepository(get_database_connection())
        