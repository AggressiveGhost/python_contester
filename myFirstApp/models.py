from django.db import models
from django.urls import *
from django.contrib.auth.models import *
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    task_name   = models.CharField(max_length = 1000)
    task_img    = models.ImageField(upload_to='task_img/', default='NULL')
    task_text   = models.TextField(default="")
    clicks      = models.IntegerField(default=0)

    def __str__(self):
        return str("{0} {1}".format(self.id ,self.task_name))

    def getCurrentTask(self):
        return reverse_lazy('currentTask', kwargs={'currentId':self.id})




class Code(models.Model):
    task        = models.ForeignKey(Task, on_delete = models.CASCADE)
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    task_code   = models.TextField(default="")
    isSolved    = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.username)
    
    
 


class UserProfileInfo(models.Model):
    user        = models.OneToOneField(User,on_delete=models.CASCADE)
    link        = models.URLField(blank=True)
    avatar      = models.ImageField(upload_to='profile_pics',blank=True,default='NULL')

def __str__(self):
  return self.user.username