from django.urls import path
from . import views
from python_contester import settings
from django.contrib.auth.views import LogoutView
from django.urls import *



urlpatterns = [
    path('', views.index, name = 'index'),
    path('currentTask <int:task_id>', views.currentTask, name='currentTask'),#every task
    path('moreProblems', views.moreProblems, name = 'moreProblems'),
    path('currentTask <int:task_id> code', views.addCode, name = 'addCode'),
    path('forum', views.forum, name = 'forum'),
    # path('search/<string:text>', name = 'search'),

    path('rating', views.rating ,name ='rating' ),
    path('userpage', views.userpage ,name = 'userpage'),
    

    path('register', views.register,name='register'),
    path('user_login', views.user_login, name='user_login'),
    path('user_logout', LogoutView.as_view(next_page = reverse_lazy('index')), name = 'user_logout'),
]
