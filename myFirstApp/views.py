from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import *
from django import *
from .models import *
from .forms import *
from django.contrib.auth.views import *
from random import *
from django.db.models import Count

# Create your views here.

def index(request): 
    # ---> Quantity of Tasks
    tasks = Task.objects.all().count() 
    # ---> Quantity of Users
    users = UserProfileInfo.objects.all().count() 
    # ---> Quantity of Solved Tasks
    solved = Code.objects.filter(isSolved = False).count() 
     # ---> Last 3 popular Tasks
    popular = Task.objects.filter(clicks__gt = 3).order_by('-clicks')[:3]

    dic = {
        'countTask':tasks,
        'countUser':users,
        'countSolved':solved
    }

    return render(request, 'myFirstApp/popTask.html', context={'title':'Polular Tasks','task':popular, 'dic':dic})


def forum(requrest):
    return render(requrest, 'myFirstApp/forum.html')


def currentTask(request, task_id):
    currentTask = Task.objects.get(id = task_id)
    # ---> Increase number of clics
    currentTask.clicks += 1
    # ---> Codes of current User
    code = Code.objects.filter(user = request.user, task = currentTask).order_by('-date')
    
    dic = {
        'currentTask' : currentTask,
        'code' : code
    }
    
    return render(request, 'myFirstApp/everyTask.html', {'dic':dic}) 



def moreProblems(request):
    taskTitle = 'All Tasks'
    allTask = Task.objects.all()
    return render(request, 'myFirstApp/popTask.html', {'title':taskTitle,'task':allTask})


def rating(request):

    def getScore(c:Code):
        n = Count(c.score)
        return n

    users = UserProfileInfo.objects.all()
    code = Code.objects.filter(score__gt = 1)
    # print(code, "------")    

    for user in users:
        code = Code.objects.filter(score__gt = 1, user = user)
        
        print(code)

    return render(request, 'myFirstApp/rayting.html')

def signIn(request):
    return render(request, 'myFirstApp/signIn.html')


def signUp(request):
    return render(request, 'myFirstApp/signUp.html')

def userpage(request):
    print(request.user)
    user = request.user
    return render(request, 'myFirstApp/userPage.html', {'user':user})






# @login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
    




def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            login(request,user)
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'avatar' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['avatar']
            profile.save()
            registered = True
            # ---> reverces to the main page
            return HttpResponseRedirect(reverse_lazy('index'))
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
                return HttpResponseRedirect(reverse_lazy('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'myFirstApp/login.html', {})




def addCode(request,task_id):
    print(request.POST)
    try:
        code = request.POST.get("code_text")
        print(code,request.POST.get('username'))

        score = int(0)
        score = randint(60, 100)
        print(score)

        co = Code(user = User.objects.get(username= request.POST.get('username')), task_code = code, task = Task.objects.get(pk=task_id), score = score)
        print(co)
        co.save()
        #everyTask
        taskEvery = Task.objects.get(pk=task_id)
        # return render(request, 'myFirstApp/popTask.html', {'everyTask':taskEvery})#expection change key
        # return HttpResponseRedirect(reverse_lazy('currentTask/{}/'.format(taskEvery.id)))
        return currentTask(request, task_id) #баг
        # return HttpResponseRedirect(reverse_lazy('currentTask', args=(task_id)))
    except:
        return HttpResponse('unSuccess')

