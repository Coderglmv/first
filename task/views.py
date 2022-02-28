from django.shortcuts import render, redirect

from .models import Task
from project.models import ProjectColumn, Project
from django.views.generic.edit import CreateView


# Create your views here.

# def task_create(request):
#     form = Task_form()
#     if request.POST:
#         form = Task_form(request.POST)
#         if form.is_valid():
#             form.save()
#     return render(request, "task_create.html", {'form': form})

def task_create(request, pk):
	name = request.POST['task_name']
	task = Task(name=name, column_id=pk)
	task.save()
	tasks = Task.objects.all()
	d = task['column']
	f = ProjectColumn.objects.get(id=task)
	q = f['project_id']
	r = Project.objects.get(id=q)

	return redirect('projects:project_detail', r)
