from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=255)
    created_at = models.DateTimeField("Created At")
    complete = models.BooleanField(default=False)