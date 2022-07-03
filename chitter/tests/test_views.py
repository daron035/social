from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from chitter.models import FriendRequest
from chitter.models import Profile
from chitter.views import send_friend_request


class UserTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        

    def test_send_friend_request(self):
        e = self.client.get('/', follow=True)
        user = get_user_model().objects.create_user(username='root', email='root@mail.ru', password='1111')
        user.save()
        i = get_user_model().objects.create_user(username='root2', email='root2@mail.ru', password='11112')
        i.save()
        self.client.force_login(user)
        r = self.client.get(reverse('send_friend_request', kwargs={'pk': i.pk}), follow=True)

    def test_profile(self):
        user = get_user_model().objects.create_user(username='root', email='root@mail.ru', password='1111')
        profile = Profile.objects.get(user=user)
        self.assertEqual(profile.user, user)