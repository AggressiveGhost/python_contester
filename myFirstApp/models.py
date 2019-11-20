from django.db import models
from django.urls import *

# Create your models here.

class Code(models.Model):
    task_code = models.TextField(default="")
    isSolved = models.BooleanField(default=False)
    # user = models.ManyToManyField(User)

class Task(models.Model):
    task_name = models.CharField(max_length = 1000)
    task_img = models.ImageField(upload_to='task_img/', default='NULL')
    task_text = models.TextField(default="")
    code = models.ForeignKey(Code, on_delete = models.CASCADE)
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return str(self.task_name)

    def getCurrentTask(self):
        return reverse_lazy('currentTask', kwargs={'currentId':self.id})


