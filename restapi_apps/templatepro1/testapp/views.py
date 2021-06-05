from django.shortcuts import render
import datetime

def template_view(request):
    dt = datetime.datetime.now()
    name = 'ram'
    mob= 8985566
    addr = 'bglr'
    my_dic ={'name':name,'mob':mob,'addr':addr}
    return render(request,'testapp/results.html',my_dic)


