from django.conf.urls import url
from django.urls import path
from login.views import hello, loginhandler, SayHitoUser, SayHitoUser1

urlpatterns = [
path('login/',hello),
path('loginhand/',loginhandler),
url(r'^(?P<age>\d{2})/$',SayHitoUser),
url(r'^about/$',SayHitoUser1)
]