from entities.user import User

from repositories.user_repository import (user_repository as default_user_repository)

class UsernameExistsError(Exception):
    pass

class BudjetServices:
    def __init__(self, user_repository=default_user_repository):
        #self._user = None
        self._user_repository = user_repository

    def create_user(self, username, password):

        existing_user = self._user_repository.find_by_username(username)

        if existing_user:
            raise UsernameExistsError(f'Username {username} already exists')

        user = self._user_repository.create(User(username, password))


        return user


budjet_services = BudjetServices()


    