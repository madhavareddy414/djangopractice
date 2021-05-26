"""new_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include

from api import views
from apvap.views import Institute
from studentrestapp.views import studentList
from appviewwithser import views as appvserv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('login.urls')),
    path('',include('newsapp.urls')),
    path('',include('formTest.urls')),
    path('api/', include('api.urls')),
    path('task-list/',views.taskList,name= 'task-list'),
    path('task-view/<str:pk>/',views.taskDetailView,name= 'task-DetailView'),
    path('task-create/',views.taskCreate,name= 'task-create'),
    path('task-update/<str:pk>/',views.taskUpdate,name= 'task-update'),
    path('task-delete/<str:pk>/', views.taskDelete, name='task-delete'),
    path('student', studentList),
    path('apvap1', Institute.as_view()),
    url(r'appvserup/(?P<pk>\d)', appvserv.EmpDet.as_view()),
    url(r'appvser', appvserv.EmpView.as_view()),



]
