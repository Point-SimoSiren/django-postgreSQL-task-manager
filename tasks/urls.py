# Tämä tiedosto on itse tehty ja tämä on includattu taskmanager/urls.py:n reittiin:
# "path('tasks/', include('tasks.urls'))"

from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_listing), # aukeaa http://127.0.0.1:8000/tasks/
    path('tietoa/', views.tietoa), # aukeaa http://127.0.0.1:8000/tasks/tietoa
    path('add_task/', views.add_task, name='add_task'),
    path('filter_tasks/', views.filter_tasks, name='filter_tasks'),
    path('delete_task/<int:task_id>', views.delete_task, name='delete_task')
]