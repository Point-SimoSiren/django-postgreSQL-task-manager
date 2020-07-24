from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Task


def task_listing(request):
    context = {'task_list' : Task.objects.all()}
    return render(request,'tasks/task_list.html', context)

def tietoa(request):
    return HttpResponse('<h3>Django & postgreSQL app</h3>')

def insert_task_item(request:HttpRequest):
    task = Task(content = request.POST['content'])
    task.save()
    return redirect('/tasks/list/')