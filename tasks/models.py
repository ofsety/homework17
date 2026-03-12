from django.db import models
from django.conf import settings

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank = True, null = True)
    deadline = models.DateField()
    is_complited = models.BooleanField()
    created_at = models.DateField(auto_now_add =True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
    )