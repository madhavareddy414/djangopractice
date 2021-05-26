from django.shortcuts import render
from todo.forms import ListForm
from todo.models import List
from django.contrib import messages

def hello(request):
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = List.objects.all()
            messages.success(request,('Item has been added to List'))
            return render(request,'todo/home.html',{'all_itmes':all_items})
        else:

            all_items = List.objects.all()
            return render(request,'todo/home.html',{'all_itmes':all_items})