# Tämä tiedosto on itse tehty ja tämä on includattu taskmanager/urls.py:n reittiin:
# "path('tasks/', include('tasks.urls'))"

from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.task_listing),
    path('tietoa/', views.tietoa),
    path('add_task/', views.add_task, name='add_task'),
    path('delete_task/<int:task_id>', views.delete_task, name='delete_task')
]