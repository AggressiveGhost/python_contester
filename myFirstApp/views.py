from django.shortcuts import render
from django.shortcuts import *
from django import *
from .models import *

# Create your views here.

def index(request): # shows 4 last popular tasks by number of clics
    taskTitle = 'Polular Tasks'
    allTasks = Task.objects.all()
    count = int(0)
    for i in allTasks:
        count += 1
    popular = Task.objects.filter(clicks__gt = 3).order_by('-clicks')[:3]
    return render(request, 'myFirstApp/popTask.html', context={'title':taskTitle,'task':popular, 'countTask':count})


def currentTask(request, task_id):
    taskEvery = Task.objects.get(id = task_id)
    taskEvery.clicks += 1
    return render(request, 'myFirstApp/popTask.html', {'everyTask':taskEvery})#expection change key



def moreProblems(request):
    taskTitle = 'All Tasks'
    allTask = Task.objects.all()
    return render(request, 'myFirstApp/popTask.html', {'title':taskTitle,'task':allTask})


def rating(request):
    return render(request, 'myFirstApp/rayting.html')

def signIn(request):
    return render(request, 'myFirstApp/signIn.html')

def signUp(request):
    return render(request, 'myFirstApp/registr.html')

def userpage(request):
    return render(request, 'myFirstApp/userPage.html')