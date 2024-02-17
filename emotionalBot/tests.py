import unittest

from django.test import TestCase
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from emotionalIntelligentBotv1.task import preprocess_input
from emotionalIntelligentBotv1.user import UserConsumer
from emotionalIntelligentBotv1.utils import get_db_handle


class ViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='yuceltan', password='yuceltan')

    def test_bot_login(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)

    def test_bot_register(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('register'), {'username': 'newuser', 'password1': 'newpassword', 'password2': 'newpassword'})
        self.assertEqual(response.status_code, 302)

    def test_bot_logout(self):
        self.client.login(username='yuceltan', password='yuceltan')

        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
class TestPreprocessInput(unittest.TestCase):
    def test_preprocess_input(self):
        input_text = "What is your name"
        processed_text = preprocess_input(input_text)
        self.assertEqual(processed_text, "What is your name?")

class TestUserConsumer(unittest.TestCase):
    def test_get_response(self):
        channel_name = "mock_channel_name"

        user_consumer = UserConsumer()

        user_consumer.get_response(channel_name, "hello")


    def test_fuzzy_match(self):
        user_consumer = UserConsumer()

        input_text = "What is your name"
        responses = ["What's your name?", "My name is John"]

        matched_response = user_consumer.fuzzy_match(input_text, responses)


class TestGetDBHandle(unittest.TestCase):
    def test_get_db_handle(self):
        # Define test database parameters
        db_name = "test_db"
        host = "localhost"
        port = "27017"
        username = "test_user"
        password = "test_password"

        db_handle, client = get_db_handle(db_name, host, port, username, password)


if __name__ == '__main__':
    unittest.main()