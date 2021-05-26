from django .http import JsonResponse
from django.urls import path

from api import views

urlpatterns = [
    path('',views.apiOverview,name='api-overview')]