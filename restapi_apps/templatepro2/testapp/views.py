from django.shortcuts import render
import datetime

# Create your views here.
def wish_template(request):
    date = datetime.datetime.now()
    h = int(date.strftime('%H'))
    msg = 'HI boss !!'
    if h<12:
        msg= msg+'Good morning'
    elif h<16:
        msg= msg+'Good afternoon'
    elif h<21:
        msg=msg+'Good evg'
    else:
        msg= msg+'Good night'
    return render(request,'testapp/results.html',{'msg':msg,'date':date})