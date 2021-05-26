from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from login.views import hello, loginHandler,sayHitoUser,sayHitoUser1

urlpatterns = [
    path('login', hello),
    path('loginhand', loginHandler),
    url(r'^(?P<age>\d{2})/$', sayHitoUser),
    url(r'^about/$',sayHitoUser1)
]

