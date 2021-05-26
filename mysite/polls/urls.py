
from django.urls import path
from . import views
from .views import Index,DetailView

urlpatterns = [
    path('',Index.as_view() ,name='index'),
    path('<int:pk>/detail/',DetailView.as_view(),name='detail'),
#     path('<int:pk>/results/', views.results, name='results'),
#     path('<int:pk>/vote/', views.vote, name='vote'),
]
