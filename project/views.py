from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from project.models import Project, ProjectColumn
from task.models import Task

def project(request):
    user = request.user
    list_project = Project.objects.filter(deleted=0, created_by_id=user)
    return render(request, "project_list.html", {"list_project": list_project})


def project_detail(request, pk):
    project = Project.objects.get(id=pk)
    project_column = ProjectColumn.objects.all()
    task = Task.objects.all()
    return render(request, 'project_detail.html', {'project': project,
    'tasks': task, 'project_column': project_column})


@login_required
def project_create(request):
    if request.POST:
        name = request.POST["project_name"]
        deadline = request.POST["project_deadline"]
        one = Project(name=name, created_by=request.user, deadline=deadline)
        if deadline:
            Project(name=name, deadline=deadline, created_by=request.user).save()
            messages.success(request, "Created Successfully")

        else:
            Project(name=name, created_by=request.user).save()
            messages.success(request, "Created Successfully")

    return redirect('projects:projects')


def project_delete(request, pk):
    project = Project.objects.get(id=pk)
    project.delete()
    return redirect('projects:projects')


def project_update(request):
    return None


def project_column(request, pk):
    name = request.POST['product_column']
    column = ProjectColumn(name=name, created_by=request.user, project_id=pk)
    column.save()
    return redirect('projects:project_detail', pk)


def column_delete(request, pk):
    column = ProjectColumn.objects.get(id=pk)
    project = column.project_id
    column.delete()
    return redirect('projects:project_detail', project)
