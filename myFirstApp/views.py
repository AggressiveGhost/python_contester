from django.shortcuts import render
from django.shortcuts import *
from django import *
from .models import *

# Create your views here.

def index(request): # shows 4 last popular tasks by number of clics
    allTasks = Task.objects.all()
    count = int(0)
    for i in allTasks:
        count += 1
    popular = Task.objects.filter(clicks__gt = 3).order_by('-clicks')[:3]
    return render(request, 'myFirstApp/popTask.html', context={'popularTask':popular, 'countTask':count})


def currentTask(request, task_id):
    taskEvery = Task.objects.get(id = task_id)
    taskEvery.clicks += 1
    return render(request, 'myFirstApp/every.html', {'task':taskEvery})

