from entities.user import User
from repositories.user_repository import (user_repository as default_user_repository)

class UsernameError(Exception):
    pass

class InvalidCredentialsError(Exception):
    pass

class BudjetServices:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def create_user(self, username, password):
        user_existing = self._user_repository.find_by_username(username)
        if user_existing:
            raise UsernameError(f'Choose another username, {username} already exists')
        user = self._user_repository.create(User(username, password))
        return user

    def login(self, username, password):
        user = self._user_repository.find_by_username(username)
        if not user or user[1] != password:
            raise InvalidCredentialsError('The username or password is incorrect')
        self._user = user
        return user


budjet_services = BudjetServices()


    
