from accounts.models import Account
from celery import shared_task
from django.core.mail import send_mail
from demo import settings
from django.contrib import messages
from django.shortcuts import render
import csv, io
from . models import TryDemo
from django.http import HttpResponse



@shared_task(bind=True)
def send_mail_func(self):
    users = Account.objects.all()
    for user in users:
        mail_subject = "Hi! Celery Testing"
        message = "Checking weather celery is working or not."
        to_email = user.email
        send_mail(
            subject = mail_subject,
            message = message,
            from_email = settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently = True,
        )
    return "Done"

from time import sleep
import base64

@shared_task(bind=True)
def upload_csv(data):
    print('Uploading image.......')
    sleep(10)
    data_set = data['csv_file'].encode(encoding='utf-8')
    print(data_set)
    b = base64.b64encode(data_set)
    print(b)
        # print(data_set)
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=",", quotechar="|"):
        _, created = TryDemo.objects.update_or_create(
            name = column[0],
            city = column[1],
            number = column[2],
            Country = column[3],
        )


# @shared_task(bind=True)
# def upload_csv(self):
#     template = 'trydemo.html'
#     prompt = {
#         'order': 'Order of the CSV should be name, city, number, country'
#     }
#     if request.method == "GET":
#         return render(request, template,prompt)

#     csv_file=request.FILES['file']

#     if not csv_file.name.endswith('.csv'):
#         messages.error(request, 'File is not csv type')
    
#     data_set = csv_file.read().decode('UTF-8')
#     io_string = io.StringIO(data_set)
#     next(io_string)
#     for column in csv.reader(io_string, delimiter=",", quotechar="|"):
#         _, created = TryDemo.objects.update_or_create(
#             name = column[0],
#             city = column[1],
#             number = column[2],
#             Country = column[3],
#         )
#     data = TryDemo.objects.all()
#     context = {'data':data}
#     return HttpResponse("Done")
    
