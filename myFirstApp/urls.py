from django.urls import path
from . import views
from python_contester import settings

# if settings.DEBUG:  
#     urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    path('', views.index, name = 'mainPage'),
    path('currentTask/<int:task_id>/', views.currentTask, name='currentTask'),
]
