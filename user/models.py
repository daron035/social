from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.urls import reverse


def get_default_user_image():
    return 'user/paimon.png'

class User(AbstractUser):
    email = models.EmailField(blank=True, unique=True)
    image = models.ImageField(upload_to='user/', default=get_default_user_image)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username

    # def get_absolute_url(self):
    #     return reverse("account", kwargs={"pk": self.pk})