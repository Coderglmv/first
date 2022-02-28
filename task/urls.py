from django.urls import path
from .views import task_create

app_name = 'tasks'
urlpatterns = [
    path('task_create/<int:pk>', task_create, name='task_create')
]