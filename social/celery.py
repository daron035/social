import os
from celery import Celery

from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social.settings')

app = Celery('social')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


# app.conf.beat_schedule = {
#     'spam': {
#         'task': 'contact.tasks.send_beat_email',
#         'schedule': crontab(minute='*/5'),
#         # 'schedule': 30.0,
#     },
# }