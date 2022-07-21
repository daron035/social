from social.celery import app

from .models import Contact
from .service import send, verify_email 


@app.task
def send_verify_email(user_email):
    verify_email(user_email)    

@app.task
def send_spam_email(user_email):
    send(user_email)
    
@app.task
def send_beat_email():
    # for u in Contact.objects.values('email').distinct():
    #     send(u.get('email'))
    send(Contact.objects.all()[0])