import unittest
from repositories.user_repository import user_repository
from entities.user import User

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.testrepo=user_repository
        self.testrepo.delete_all()
        self.user_1 = User('user1', 'user123')
        self.user_2 = User('user2', 'user456')

    def test_create_user(self):
        test=self.testrepo.create(self.user_1)
        self.assertEqual(test,"User created successfully")


    def test_find_by_username(self):
        self.testrepo.create(self.user_2)
        test_user=user_repository.find_by_username(self.user_2.username)
        self.assertEqual(test_user, (self.user_2.username, self.user_2.password))

    def test_find_all(self):
        self.testrepo.create(self.user_1)
        self.testrepo.create(self.user_2)
        test_users=user_repository.find_all()
        self.assertEqual(len(test_users), 2)
        self.assertEqual(test_users[0], (self.user_1.username, self.user_1.password))
        self.assertEqual(test_users[1], (self.user_2.username, self.user_2.password))
