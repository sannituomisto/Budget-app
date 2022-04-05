import unittest
from repositories.user_repository import UserRepository
from entities.user import User

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.testrepo=UserRepository()
        self.user_1 = User('user1', 'user123')
        self.user_2 = User('user2', 'user456')

    def test_create(self):
        user_new=self.testrepo.create_user(self.user_1)
        self.assertEqual(user_new, "User created")