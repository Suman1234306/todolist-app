from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):

    id = models.AutoField(primary_key=True)
    task_title = models.CharField(max_length=300)
    task_description = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=False)
    create_datetime = models.DateTimeField(auto_created=True)
    end_datetime = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.task_title

    class Meta:
        ordering = ['status']
