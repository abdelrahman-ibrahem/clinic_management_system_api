from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

# TESTING USER MODEL

class UserTesting(TestCase):
    def test_create_user(self):
        user = User.objects.create(username="abdelrahman", email="abdelrahman@gmail.com",
                                    role="user", password="passwrd")
        self.assertEqual(user.username, "abdelrahman")
        self.assertEqual(user.email, "abdelrahman@gmail.com")
        self.assertEqual(user.role, "user")