from django.db import *
from django.urls import *
from django.contrib.auth.models import *
from django.conf import settings
from datetime import datetime    
import os
# ---> User Model
class UserProfileInfo(models.Model):
    user        = models.OneToOneField(User,on_delete=models.CASCADE)
    link        = models.URLField(blank=True)
    avatar      = models.ImageField(upload_to='profile_pics',blank=True,default='profile_pics/user.png')

    def __str__(self):
        return self.user.username



# ---> Task model
class Task(models.Model):
    task_name   = models.CharField(max_length = 1000)
    task_img    = models.ImageField(upload_to='task_img/', default='NULL')
    task_text   = models.TextField(default="")
    clicks      = models.IntegerField(default=0)

    def __str__(self):
        return str("{0} {1}".format(self.id ,self.task_name))



# ---> Code model
class Code(models.Model):
    task        = models.ForeignKey(Task, on_delete = models.CASCADE)
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    task_code   = models.TextField(default="")
    date        = models.DateTimeField(default=datetime.now, blank=True)
    score       = models.IntegerField(default=0)
    isSolved    = models.BooleanField(default=False)

    def __str__(self):
        return self.task.task_name + " " + self.user.username + " " + self.date.strftime("%H:%M:%S")



# ---> Question model
class Question(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title       = models.TextField(default="")
    text        = models.TextField(default="")
    img         = models.ImageField(upload_to='Q_img/', default='NULL')
    date        = models.DateTimeField(default=datetime.now, blank=True)
    isSolved    = models.BooleanField(default=False)
    clicks      = models.IntegerField(default=0)

    def __str__(self):
        return str(self.title)



# ---> Answer model
class Answer(models.Model):
    question    = models.ForeignKey(Question, on_delete=models.CASCADE)
    text        = models.TextField(default="")
    date        = models.DateTimeField(default=datetime.now, blank=True)
    author      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    isHelped    = models.BooleanField(False) # <--- Can change only author of Question
    likes       = models.IntegerField(default=0)
    def __str__(self):
        return str(self.author.username)
    

    


    