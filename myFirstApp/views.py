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
from django.core.paginator import Paginator

# Create your views here.
rating = dict()

def index(request): 
    # ---> Quantity of Tasks
    tasks   = Task.objects.all().count() 
    # ---> Quantity of Users
    users   = UserProfileInfo.objects.all().count() 
    # ---> Quantity of Solved Tasks
    solved  = Code.objects.filter(isSolved = False).count() 
     # ---> Last 3 popular Tasks
    popular = Task.objects.filter(clicks__gt = 3).order_by('-clicks')[:3]

    dic = {
        'countTask':tasks,
        'countUser':users,
        'countSolved':solved
    }
    return render(request, 'myFirstApp/popTask.html', context={'title':'Polular Tasks','task':popular, 'dic':dic})


def forum(requrest):
    dic = dict()
    questions  = Question.objects.order_by('-date')
    for i in questions:
        count = Answer.objects.filter(question = i).count()
        dic[i] = [count]
    return render(requrest, 'myFirstApp/forum.html',{'dic':dic})

def ask(request):
    return render(request, 'myFirstApp/ask.html')



def addQuestion(request):
    print(request.POST)
    try:
        title       = request.POST.get("title")
        text        = request.POST.get("text")
        user        = User.objects.get(username = request.POST.get('username'))
        question    = Question(user = user, title = title, text = text)
        question.save()
        return HttpResponseRedirect(reverse_lazy('forum'))
    except:
        return HttpResponse('W*f whats going on!s')



def currentTask(request, task_id):
    dic                 = dict()
    currentTask         = Task.objects.get(id = task_id)
    dic['currentTask']  = currentTask

    # ---> Increase number of clics
    currentTask.clicks  += 1
    # ---> Codes of current User
    if request.user.id  != None:
        code = Code.objects.filter(user = request.user, task = currentTask).order_by('-date')
        dic['code'] = code
   
    return render(request, 'myFirstApp/everyTask.html', {'dic':dic}) 



def moreProblems(request):
    allTask     = Task.objects.all()
    paginator   = Paginator(allTask,3) 
    page        = request.GET.get('page')
    allTask     = paginator.get_page(page)
    return render(request, 'myFirstApp/allTask.html', {'title':"All Tasks",'task':allTask})


def rating(request):
    diсScore = dict()
    # ---> Sum of scores
    def getScore(code:Code):
        score = int()
        for i in code:
            score += int(i.score)
        return score
    # ---> get all users
    users = User.objects.all()
    for user in users:
        code = Code.objects.filter(score__gt = 1, user = user)
        if code: # ---> if user's score exists
            count = code.count()
            score = getScore(code)
            # ---> key(User) = values(score, count)
            diсScore["{}".format(user.username)] = [score, count]
    # ---> sort dictionary by scores
    diсScore = sorted(diсScore.items(),key = lambda x : x[0] )
    global rating
    rating = diсScore
    return render(request, 'myFirstApp/rayting.html', {'dicScore':diсScore})

def signIn(request):
    return render(request, 'myFirstApp/signIn.html')

def signUp(request):
    return render(request, 'myFirstApp/signUp.html')

def userpage(request):
    print(request.user)
    user          = request.user
    # ---> set of codes
    codes         = Code.objects.filter(user = user).order_by('-date')
    # ---> set of answers
    answers       = Answer.objects.filter(author = user).order_by('-likes')
    # ---> set of questions
    questions     = Question.objects.filter(user = user).order_by('-clicks')

    codeCount     = codes.filter(isSolved = False).count()
    # answerCount = answers.filter(isHelped = False).count()
    answerCount   = answers.count()
    # questionCount = questions.filter(clicks__gt = 3).count()
    questionCount = questions.count()

    dic = {
        'codeCount':codeCount,
        'answerCount':answerCount,
        'questionCount':questionCount,

        'codes':codes,
        'answers':answers,
        'questions':questions
    }

    return render(request, 'myFirstApp/userPage.html', {'dic':dic})






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
        username      = request.POST.get('username')
        password      = request.POST.get('password')
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
        print(code.request.POST.get('username'))

        score = int(0)
        score = randint(60, 100)
        print(score)
        
        co = Code(user = User.objects.get(username= request.POST.get('username')), task_code = code, task = Task.objects.get(pk=task_id), score = score)
        print(co)
        co.save()
        taskEvery = Task.objects.get(pk=task_id)
        # return render(request, 'myFirstApp/popTask.html', {'everyTask':taskEvery})#expection change key
        # return HttpResponseRedirect(reverse_lazy('currentTask/{}/'.format(taskEvery.id)))
        return currentTask(request, task_id) #баг
        # return HttpResponseRedirect(reverse_lazy('currentTask', args=(task_id)))
    except:
        return HttpResponse('unSuccess')

