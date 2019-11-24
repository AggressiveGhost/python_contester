from django.urls import path
from . import views
from python_contester import settings

# if settings.DEBUG:  
#     urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    path('', views.index, name = 'mainPage'),
    path('index/', views.index, name = 'mainPage'),
    path('currentTask/<int:task_id>/', views.currentTask, name='currentTask'),#every task
    path('moreProblems/', views.moreProblems, name = 'moreProblems'),
    #path('article/<int:article_id>/comment', views.addComment, name='addComment'),
    path('currentTask/<int:task_id>/code', views.addCode, name = 'addCode'),


    path('rating/', views.rating ,name ='rating' ),
    path('signIn/',views.signIn ,name = 'signIn'),
    path('signUp/', views.signUp ,name = 'signUp'),
    path('userpage/', views.userpage ,name = 'userpage'),


    path('register/', views.register,name='register'),
    path('user_login', views.user_login,name='user_login'),
    path('user_logout', views.user_logout, name = 'user_logout'),
]
