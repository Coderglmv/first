from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from project.models import Project, ProjectColumn


def project(request):
    user = request.user
    list_project = Project.objects.filter(deleted=0, created_by_id=user)
    return render(request, "project_list.html", {"list_project": list_project})


def project_detail(request, pk):
    project = Project.objects.get(id=pk)
    project_column = ProjectColumn.objects.all()
    return render(request, 'project_detail.html', {'project': project, 'project_column': project_column})


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
            messages.error(request, "You must enter the date", extra_tags='danger')
    return render(request, "landing.html")


def project_delete(request):
    return None


def project_update(request):
    return None


def project_column(request, pk):
    name = request.POST['product_column']
    column = ProjectColumn(name=name, created_by=request.user, project_id=pk)
    column.save()
    return redirect('projects:project_detail', pk)
