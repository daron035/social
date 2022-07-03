from django.test import TestCase, Client

from user.forms import RegisterUserForm


class TestRegistrationForm(TestCase):
    
    def test_registration_form(self):
        # test invalid data
        invalid_data = {
          "username": "user@test.com",
          "password1": "secret",
          "password2": "secret",
          "email": "not email"
        }
        form = RegisterUserForm(data=invalid_data)
        form.is_valid()
        self.assertTrue(form.errors)

         # test valid data
        valid_data = {
          "username": "user@test.com",
          "password1": "secrdfjshghdfj383838et",
          "password2": "secrdfjshghdfj383838et",
          "email": "user@mail.ru"
        }
        form = RegisterUserForm(data=valid_data)
        form.is_valid()
        self.assertFalse(form.errors)