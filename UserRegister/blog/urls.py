from django.urls import path
from users import views as users_views
from blog.views import PostListView,PostDetailView

urlpatterns = [

    path('',users_views.home,name='home'),
    path('list/',PostListView.as_view() ,name='post-list'),
    path('detail/<int:pk>/',PostDetailView.as_view() ,name='post-detail'),
    ]