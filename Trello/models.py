from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Auditable(models.Model):
    deleted = models.IntegerField(default=0, null=True)
    created_at = models.DateTimeField(default=now, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+", null=True)
    updated_at = models.DateTimeField(default=now, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name="+", null=True)

    class Meta:
        abstract = True
