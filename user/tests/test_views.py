from user.models import User
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
# from django import setup
from django.urls import reverse
# from django.test.utils import setup_test_environment
# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "social.settings")
# setup()


class UserTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(username='root', email='root@mail.ru', password='1111')

    def test_user(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)

    def test_login(self):
        r = self.client.login(username='root', password='1111')
        r2 = self.client.post(reverse('login'), {'username':'root', 'password':'1111'})
        self.assertTrue(r)
        self.assertTrue(r2)

    