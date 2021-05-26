from django.urls import path, include

from ece.views import (
    Home, register, totalstudents, delete, search, fregister, totalfac, contact,studentUpdateView,
    studentUpdateView)

urlpatterns = [
    path('', Home),
    path('registration/', register,name='Student Registration'),
    path('all/', totalstudents),
    path('del/', delete),
    path('find/', search),
    path('freg/', fregister),
    path('fac/', totalfac),
    path('cont/', contact),
    path('student-detail/<int:pk>/', studentUpdateView),

]
