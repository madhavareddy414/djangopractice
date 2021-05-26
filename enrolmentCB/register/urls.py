from django.urls import path

from register import views
from .views import StudentUpdateView, stud_update
from register.views import home, StudDetailView,StudentRegister,StudListView
urlpatterns = [
    path('', home,name='home'),

    path('stud-reg/',StudentRegister.as_view(),name='Student-Registration'),
    # path('stud-update/<int:pk>/',StudentUpdateView.as_view(),name='student-update1'),
    path('stud-all/', StudListView.as_view(), name='Students-list'),
    path('stud-detail/<int:pk>/',StudDetailView.as_view(),name='Student1-detailview'),
    path('stud-update/', stud_update, name='student-update'),


]
