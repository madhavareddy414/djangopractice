"""batch60pro URL Configuration

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
from django.urls import path, include

from apvapp.views import Institute
from modelApp.models import Employee
from sutdentrestapp.views import studentList
from appviewwithser import views as appvserv
from mixincla import views as mixinclaview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('login.urls')),
    path('',include('formTest.urls')),
    path("student", studentList),
    path("apvappapi", Institute.as_view()),
    url(r'appvserup/(?P<pk>\d)', appvserv.EmpDet.as_view()),
    url(r'appvser', appvserv.EmpView.as_view()),
    path(r'snippets/', mixinclaview.SnippetList.as_view()),
    path(r'snippets/<int:pk>/', mixinclaview.SnippetDetail.as_view()),

]

Employee