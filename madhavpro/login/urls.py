from django.urls import path
from login.views import hello, loginhandler

urlpatterns = [

    path('login/', hello),
    path('loginhand/', loginhandler),

]