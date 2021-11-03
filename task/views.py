# from django.shortcuts import render
# from .forms import Task_form
# from .models import Task
#
#
# # Create your views here.
#
# def task_create(request):
#     form = Task_form()
#     if request.POST:
#         form = Task_form(request.POST)
#         if form.is_valid():
#             form.save()
#     return render(request, "task_create.html", {'form': form})
