from django.http import HttpResponse
from django.shortcuts import render, redirect
import datetime

from tasks.forms import TaskForm
from tasks.models import Task

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'tasks/ack.html', {'title': 'New record added successfully'})
            # return redirect('/')

    content = {'tasks':tasks,'form':form}
    return render(request,'tasks/list.html',content)

def updateTask(request,pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if form.is_valid():
        form.save()
        return render(request, 'tasks/ack.html',{'title':'updated successfully'})
        # return redirect('/')
    content = {'form':form}
    return render(request,'tasks/update_task.html',content)

def deleteTask(request,pk):
    item = Task.objects.get(id=pk)
    if request.method== 'POST':
        item.delete()
        # return redirect('/')
        return render(request, 'tasks/ack.html', {'title': 'record deleted successfully'})
    context={'item':item}
    return render(request,'tasks/delete.html',context)

def time(request):
    current = datetime.datetime.now()
    now = "<html><body> It is now %s.</body></html>"%current
    return HttpResponse(now)