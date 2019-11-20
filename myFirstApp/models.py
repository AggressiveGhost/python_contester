from django.db import models
from django.urls import *

# Create your models here.

class Task(models.Model):
    task_name = models.CharField(max_length = 1000)
    task_img = models.ImageField(upload_to='task_img/', default='NULL')
    task_text = models.TextField(default="")
    task_code = models.TextField(default="")
    isSolved = models.BooleanField(default=False)
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return str(self.task_name)

    def getCurrentTask(self):
        return reverse('currentTask', kwargs={'currentId':self.id})


