from django.contrib import admin
from django.urls import path, include
from Trello.views import home_page

urlpatterns = [
    path('', home_page, name='home_page'),
    path('admin/', admin.site.urls),
    path('auth/', include("authentication.urls")),
    path('project/', include('project.urls')),
    path('landing/', include('landing.urls')),
    path('task/', include('task.urls'))
]
