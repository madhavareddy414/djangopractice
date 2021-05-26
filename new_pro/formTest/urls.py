from  django.urls import path

from formTest import views

urlpatterns = [
path(r'form/',views.studentinputview),

]