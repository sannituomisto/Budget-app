from entities.income import Income
from entities.user import User
from entities.expense import Expense
from repositories.user_repository import (
    user_repository as default_user_repository)
from repositories.budget_repository import (
    budget_repository as default_budget_repository)


class UsernameError(Exception):
    pass


class InvalidCredentialsError(Exception):
    pass


class BudgetServices:
    def __init__(self, user_repository=default_user_repository, budget_repository=default_budget_repository):
        self._user_repository = user_repository
        self._budget_repository = budget_repository
        self._user = None

    def create_user(self, username, password):
        user_existing = self._user_repository.find_by_username(username)
        if user_existing:
            raise UsernameError(
                f'Choose another username, {username} already exists')
        user = self._user_repository.create(User(username, password))
        return user

    def login(self, username, password):
        user = self._user_repository.find_by_username(username)
        if not user or user[1] != password:
            raise InvalidCredentialsError(
                'The username or password is incorrect')
        self._user = user
        return user

    def get_current_user(self):
        return self._user

    def create_expense(self, amount, category, username):
        expense = self._budget_repository.create_expense(
            Expense(amount, category, username))
        return expense

    def create_income(self, amount, username):
        income = self._budget_repository.create_income(
            Income(amount, username))
        return income


budget_services = BudgetServices()
