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
    """Luokka, joka vastaa sovelluslogiikasta"""

    def __init__(
        self,
        budget_repository=default_budget_repository,
        user_repository=default_user_repository
    ):
        """Luokan konstruktori

        Args:
            user_repository:
                Vapaaehtoinen ja oletusarvoltaan UserRepository-olio
                Olio, jolla on UserRepository-luokan metodit
            budget_repository:
                Vapaaehtoinen ja oletusarvoltaan BudgetRepository-olio
                Olio, jolla on BudgetRepository-luokan metodit
        """

        self._user_repository = user_repository
        self._budget_repository = budget_repository
        self._user = None

    def create_user(self, username, password):
        """Luo uuden käyttäjän

        Args:
            username: Käyttäjän merkkijonoarvoinen käyttäjätunnus
            password: Käyttäjän merkkijonoarvoinen salasana

        Raises:
            UsernameError: Virhe, joka syntyy jos käyttäjänimi on jo olemassa

        Returns:
            Käyttäjä User-oliona.
        """

        user_existing = self._user_repository.find_by_username(username)
        if user_existing:
            raise UsernameError(
                f'Choose another username, {username} already exists')
        user = self._user_repository.create(User(username, password))
        return user

    def login(self, username, password):
        """Käyttäjän kirjaaminen sisään sovellukseen

        Args:
            username: Käyttäjän merkkijonoarvoinen käyttäjätunnus
            password: Käyttäjän merkkijonoarvoinen salasana

        Raises:
            InvalidCredentialsError: Virhe, joka syntyy, jos käyttäjätunnus ja salasana eivät ole oikein

        Returns:
            Käyttäjä User-oliona
        """

        user = self._user_repository.find_by_username(username)
        if not user or user[1] != password:
            raise InvalidCredentialsError(
                'The username or password is incorrect')
        self._user = user
        return user

    def get_current_user(self):
        """Hakee kirjautuneen käyttäjän

        Returns:
            Kirjautunut käyttäjä User-oliona
        """
        return self._user

    def create_expense(self, amount, category, username):
        """Luo uuden kulun

        Args:
            amount: Kulun suuruus lukuarvona
            category: Kulun merkkijonoarvoinen kategoria 
            username: Käyttäjän merkkijonoarvoinen käyttäjätunnus

        Returns:
            Kulu Expense-oliona
        """

        expense = self._budget_repository.create_expense(
            Expense(amount, category, username))
        return expense

    def create_income(self, amount, username):
        """Luo uuden tulon

        Args:
            amount: Tulon suuruus lukuarvona
            username: Käyttäjän merkkijonoarvoinen käyttäjätunnus

        Returns:
            Tulo Income-oliona
        """

        income = self._budget_repository.create_income(
            Income(amount, username))
        return income

    def log_out(self):
        """Käyttäjän kirjaaminen ulos sovelluksesta"""

        self._user = None

    def get_income_sum(self, username):
        income_sum=self._budget_repository.incomes_sum(username)
        return income_sum

    def get_expense_sum(self, username):
        expense_sum=self._budget_repository.expense_sum(username)
        return expense_sum

    def get_expense_sum_by_category(self, username, category):
        expense_sum_by_category=self._budget_repository.expense_sum_by_category(username, category)
        return expense_sum_by_category

    def get_all_incomes(self, username):
        all_incomes=self._budget_repository.find_all_income(username)
        return all_incomes

    def get_all_expenses(self, username):
        all_expenses=self._budget_repository.find_all_expense(username)
        return all_expenses

    def delete_all_from_user(self, username):
        self._budget_repository.delete_all_from_user(username)


budget_services = BudgetServices()
