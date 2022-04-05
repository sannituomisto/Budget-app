from entities.user import User
from repositories.user_repository import user_repository

class UsernameExistsError(Exception):
    pass

class BudjetServices:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def create_user(self, username, password):
        user_existing = self._user_repository.find_by_username(username)
        if user_existing:
            raise UsernameExistsError(f'This username already exists')
        user = self._user_repository.create(User(username, password))
        return user


budjet_services = BudjetServices()


    
