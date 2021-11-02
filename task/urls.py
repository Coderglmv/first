from django.ulrs import path
from .views import create_task

app_name = 'tasks'
urlpatterns = [
    path('create_task', create_task, name='create_task')
]