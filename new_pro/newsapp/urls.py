from sys import path

from django.conf.urls import url
from django.urls import path

from newsapp.views import moviesinfo, sportsinfo, politicsinfo, index

urlpatterns = [
    url('index/', index),
    path('moviesinfo/', moviesinfo),
    url('sportsinfo/', sportsinfo),
    url('politicsinfo/', politicsinfo),
    ]