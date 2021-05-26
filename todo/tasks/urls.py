from django.urls import path

from tasks.views import index, updateTask, deleteTask,time

urlpatterns = [
    path('',index,name='list'),
    path('update_task/<str:pk>/',updateTask,name='update_task'),
    path('delete/<str:pk>/', deleteTask, name="delete"),
    path('current_time/', time, name="current_time"),
]