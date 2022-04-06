import unittest
from repositories.user_repository import user_repository
from entities.user import User

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.testrepo=user_repository
        self.user_1 = User('user1', 'user123')
        self.user_2 = User('user2', 'user456')

    def test_create_user(self):
        self.testrepo.create(self.user_1)