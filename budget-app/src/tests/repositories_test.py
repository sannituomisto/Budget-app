import unittest
from repositories.user_repository import user_repository
from repositories.budget_repository import budget_repository
from entities.user import User
from entities.expense import Expense
from entities.income import Income


class TestRepositories(unittest.TestCase):
    def setUp(self):
        self.testrepo = user_repository
        self.testrepo2 = budget_repository
        self.testrepo.delete_all_users()
        self.testrepo2.delete_all_expenses()
        self.testrepo2.delete_all_incomes()
        self.user_1 = User('user1', 'user123')
        self.user_2 = User('user2', 'user456')
        self.expense_1 = Expense(100, 'Food', self.user_1.username)
        self.expense_2 = Expense(50, 'House', self.user_1.username)
        self.income_1 = Income(500, self.user_1.username)
        self.income_2 = Income(100, self.user_1.username)

    def test_create_user(self):
        test = self.testrepo.create(self.user_1)
        self.assertEqual(test, "User created successfully")

    def test_find_by_username(self):
        self.testrepo.create(self.user_2)
        test_user = user_repository.find_by_username(self.user_2.username)
        self.assertEqual(
            test_user, (self.user_2.username, self.user_2.password))

    def test_find_all_users(self):
        self.testrepo.create(self.user_1)
        self.testrepo.create(self.user_2)
        test_users = user_repository.find_all_users()
        self.assertEqual(len(test_users), 2)
        self.assertEqual(
            test_users[0], (self.user_1.username, self.user_1.password))
        self.assertEqual(
            test_users[1], (self.user_2.username, self.user_2.password))

    def test_create_expense(self):
        self.testrepo.create(self.user_1)
        test = self.testrepo2.create_expense(self.expense_1)
        self.assertEqual(test, "Expense entered successfully")

    def test_find_all_expense(self):
        self.testrepo.create(self.user_1)
        self.testrepo2.create_expense(self.expense_1)
        self.testrepo2.create_expense(self.expense_2)
        test = budget_repository.find_all_expense(self.user_1.username)
        self.assertEqual(len(test), 2)
        self.assertEqual(
            test[0], (self.expense_1.amount, self.expense_1.category))
        self.assertEqual(
            test[1], (self.expense_2.amount, self.expense_2.category))

    def test_create_income(self):
        self.testrepo.create(self.user_1)
        test = self.testrepo2.create_income(self.income_1)
        self.assertEqual(test, "Income entered successfully")

    def test_find_all_income(self):
        self.testrepo.create(self.user_1)
        self.testrepo2.create_income(self.income_1)
        self.testrepo2.create_income(self.income_2)
        test = budget_repository.find_all_income(self.user_1.username)
        self.assertEqual(len(test), 2)
        self.assertEqual(
            test[0], (self.income_1.amount))
        self.assertEqual(
            test[1], (self.income_2.amount))
