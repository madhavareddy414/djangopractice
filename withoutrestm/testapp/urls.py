from django.conf.urls import url
from django.urls import path
from testapp import views

urlpatterns = [

    url(r'^api/(?P<id>\d+)/$',views.EmployeedetailCBV.as_view()),
    path('api/',views.EmployeeListCBV.as_view()),
]