from django.urls import path
from project.views import (project, project_detail, project_create, project_delete, project_update,
                           project_column, column_delete)

app_name = 'projects'
urlpatterns = [
    path("project/", project, name="projects"),
    path("project_detail/<int:pk>/", project_detail, name="project_detail"),
    path("project_create/", project_create, name="project_create"),
    path("project_delete/<int:pk>/", project_delete, name="project_delete"),
    path("project_update/", project_update, name="project_update"),
    path("project_column/<int:pk>/", project_column, name="project_column"),
    path("column_delete/<int:pk>/", column_delete, name="column_delete")
]
