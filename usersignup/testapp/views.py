from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from testapp.forms import UserRegisterForm
from django.shortcuts import redirect


def home(request):
    return render(request,'testapp/home.html')

def register(request):
    if request.method == 'POST':
        form= UserRegisterForm(request.POST or None)
        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
            messages.success(request,f'{username} has been created successfully')
            return redirect('login')
    else:
        form=UserRegisterForm
    return render(request,'testapp/register.html',{'form':form})
@login_required()
def profile(request):
    return render(request,'testapp/profile.html')