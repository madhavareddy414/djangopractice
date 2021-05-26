from django.urls import path
from login import views
from .views import Login

urlpatterns = [
    path('login/',views.login1),
    path('login2/',views.login2),
    path('labour/',Login.as_view()),
    path('list/',views.labout_list),
]