from django.shortcuts import render
from django.http import HttpResponse # itse lisätty import

# Create your views here.

def task_listing(request):
    return render(request,'tasks/task_list.html')

def tietoa(request):
    return HttpResponse('<h3>Django & postgreSQL app</h3>')