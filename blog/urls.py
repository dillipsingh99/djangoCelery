from django.urls import path
from blog.views import *

urlpatterns = [
    path('', blog, name='blog' ),
    path('celerytask', test, name='test'),
    path('sendmail', send_mail_to_all, name = 'send mail'),  
] 