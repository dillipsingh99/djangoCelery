from django.shortcuts import render
from django.http import HttpResponse
from . tasks import test_func
from send_mail_app.tasks import send_mail_func

def blog(request):
    return render(request, 'blog.html')

def test(request):
    test_func.delay()
    return HttpResponse("Done")

def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Sent")
