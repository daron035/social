from django.conf import settings
from django.core.mail import send_mail

import random


def generate_numbers():
    return random.randint(1000, 9999)

def send(user_email):
    send_mail(
        'Вы подписались на рассылку',
        'та-дам',
        settings.EMAIL_HOST_USER,
        [user_email],
        fail_silently=False
    )
    
def verify_email(user_email):
    send_mail(
        'Подтвердите почту',
        f'{generate_numbers()}',
        'testf6194@gmail.com',
        [user_email],
        fail_silently=False
    )