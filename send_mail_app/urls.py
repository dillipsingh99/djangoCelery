from django.urls import path
from . views import *

app_name = 'send_mail_app'
# pattern_name = 'demo'


urlpatterns = [
    path('demo/', solo, name='solo'),
    path('upload/', upload, name='upload')
]