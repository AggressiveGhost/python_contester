from django.shortcuts import render
from django.shortcuts import *
from django import *
from .models import *

# Create your views here.

def index(request): # shows 4 last popular tasks by number of clics
    popular = Task.objects.filter(clicks__gt = 3).order_by('-clicks')[:3]
    return render(request, 'myFirstApp/popTask.html', context={'popularTask':popular})


def currentTask(request, task_id):
    taskEvery = Task.object.get(id = task_id)
    taskEvery.clicks += 1
    return render(request, 'myFirstApp/every.html', content={'task':taskEvery})

# def getImg(request):
#     if request.method == 'GET':
#         img = Task.objects.all()
#         return render(request, 'myFirstApp/popTask.html', context= {'img'})
#         pass
#     pass