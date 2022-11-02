from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')

app = Celery('demo')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kathmandu')
app.config_from_object(settings, namespace='CELERY')

#Celery Beat Settings
app.conf.beat_schedule = {
    'send-mail-every-day-at-02:55':{
        'task': 'send_mail_app.tasks.send_mail_func',
        'schedule':crontab(hour=15, minute=35),
    }
}
app.autodiscover_tasks()
@app.task(bind=True)
def debug_task(self):
    print(f'Request:{self.request!r}')

# import os
# from celery import Celery

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings")
# app = Celery("demo")
# app.config_from_object("django.conf:settings", namespace="CELERY")
# app.autodiscover_tasks()