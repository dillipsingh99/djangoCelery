from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from . models import TryDemo
from django.contrib import messages
from django.urls import reverse
import io
import csv
from django.core.paginator import Paginator
from .tasks import upload_csv
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from .tasks import upload_csv

def solo(request):
    data = TryDemo.objects.all().order_by('id')
    p = Paginator(data, 15)
    page = request.GET.get('page')
    datas = p.get_page(page)
    context = {'data':data, 'datas':datas}
    if request.htmx:
        return render(request, 'list.html', context)
    return render(request, 'trydemo.html', context)

# def upload(request):
#     upload_csv.delay()
#     return HttpResponse("Work In Progress")
import base64

def upload(request): 
    template = 'trydemo.html'
    context = {
        'order': 'Order of the CSV should be name, city, number, country'
    }
    # print(prompt)
    if request.method == 'POST':
        csv_file=request.FILES['file']
        print(csv_file)
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'File is not csv type')
            # return HttpResponseRedirect(reverse("send_mail_app:demo"))
            return render(request, template, context)
        csv_file=request.FILES['file'].read()
        byte = base64.b64encode(csv_file)
        data = {
            'csv_file': byte.decode('utf-8'),
            'name':request.FILES['csv_file'].name,
        }
        upload_csv.delay(data=data)
        return HttpResponse("Uploading.....")

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
    
    # data = TryDemo.objects.all()
    # context['data'] = data
    # return render(request, 'trydemo.html',context)