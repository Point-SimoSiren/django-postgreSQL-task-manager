# Tämä tiedosto on itse tehty ja tämä on includattu taskmanager/urls.py:n reittiin:
# "path('tasks/', include('tasks.urls'))"

from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.task_listing),
    path('tietoa/', views.tietoa),
    path('insert_task/', views.insert_task_item, name='insert_task_item')
]