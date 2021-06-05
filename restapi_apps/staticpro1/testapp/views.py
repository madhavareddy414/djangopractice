from django.shortcuts import render
import datetime

def static_view(request):
    date = datetime.datetime.now()
    h = int(date.strftime('%H'))
    if h<12:
        msg = 'HI boss good mng'
    elif h<16:
        msg = 'HI boss good noon'
    elif h<21:
        msg= 'Hi boss good evg'
    else:
        msg= 'HI boss good night'

    return render(request,'testapp/results.html',{'date':date,'msg':msg})
