from django.contrib.auth.models import User
from django.db import models

from Trello.models import Auditable
from project.models import ProjectColumn


class Task(Auditable):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=400)
    column = models.ForeignKey(ProjectColumn, on_delete=models.CASCADE)
    hardest_level = models.SmallIntegerField(default=1)

    class Meta:
        db_table = "task"


class TaskMember(Auditable):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    member = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "task_member"
