from django.shortcuts import render
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView


# def hello(request):
#     return render(request,'blog/index.html')

from blog.models import Post


class HomeView(ListView):
    model = Post
    template_name = 'blog/post_list.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class CreatePost(CreateView):
        model = Post
        fields = '__all__'
        template_name = 'blog/post_create.html'
