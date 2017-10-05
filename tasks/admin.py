from django.contrib import admin
from .models import Task, TaskBucket, Bucket

# Register your models here.
admin.site.register(Task)
admin.site.register(TaskBucket)
admin.site.register(Bucket)