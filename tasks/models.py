from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    time_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    description = models.TextField()
    due_date = models.DateTimeField()

    def __str__(self):
        return self.title

class Bucket(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class TaskBucket(models.Model):
    task = models.ForeignKey(Task)
    bucket = models.ForeignKey(Bucket)
    last_modified = models.DateTimeField(auto_now=True)
    priority = models.CharField(max_length=60)

    def __str__(self):
        return self.task.title +" -- " + self.bucket.title