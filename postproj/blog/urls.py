from django.urls import path
from .views import HomeView,ArticleDetailView,CreatePost

urlpatterns = [
    # path('',views.hello),
    path('',HomeView.as_view(),name='home'),
    path('detail/<int:pk>',ArticleDetailView.as_view(),name='article-detail'),
    path('create-post/',CreatePost.as_view(),name='article-create')
]