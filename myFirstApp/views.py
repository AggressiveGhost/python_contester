from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import *
from django import *
from .models import *
from .forms import *

# Create your views here.

def index(request): # shows 4 last popular tasks by number of clics
    taskTitle = 'Polular Tasks'
    allTasks = Task.objects.all()
    count = int(0)
    for i in allTasks:
        count += 1
    popular = Task.objects.filter(clicks__gt = 3).order_by('-clicks')[:3]
    # return render(request, 'myFirstApp/index.html')
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
    return render(request, 'myFirstApp/signUp.html')

def userpage(request):
    return render(request, 'myFirstApp/userPage.html')




# @login_required   
def special(request):
    return HttpResponse("You are logged in !")

# @login_required
def user_logout(request):
    logout(request)
    return reverse_lazy('index')




def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'avatar' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['avatar']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'myFirstApp/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponse('hello wworld')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'myFirstApp/login.html', {})