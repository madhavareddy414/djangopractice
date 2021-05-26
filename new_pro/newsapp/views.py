from django.shortcuts import render

# Create your views here.

def index(request):
    return render (request,'newsapp/index.html')

def moviesinfo(request):
    head_msg ='Latest Movies info'
    msg1='Uppena movie getting hure response'
    msg2='Rajamouli started new movie shooting in next month'
    msg3='Mega star Chiranjeevi latest Syra movie running successfully in the theatres'
    msg4 = "DSP music is awesome in uppena movie"
    my_dict = {'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3,'msg4':msg4}
    return render(request,'newsapp/news.html',context=my_dict)

def sportsinfo(request):
    head_msg ='Latest Sports info'
    msg1='India won the test match against Australia'
    msg2='Dhoni given Retirement'
    msg3='Ind Vs England test match planned next month'
    msg4 = "Ashwini player very well yesterday's match"
    my_dict = {'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3,'msg4':msg4}
    return render(request,'newsapp/news.html',context=my_dict)

def moviesinfo(request):
    head_msg ='Latest Movies info'
    msg1='India won the test match against Australia'
    msg2='Narendra Modi visited Nepal yesterday'
    msg3='Mega star Chiranjeevi latest Syra movie running successfully in the theatres'
    msg4 = "Dhoni announced his retirement for test cricket"
    my_dict = {'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3,'msg4':msg4}
    return render(request,'newsapp/news.html',context=my_dict)

def politicsinfo(request):
    head_msg ='Latest Politics info'
    msg1='Municipla elections schedule released by SEC'
    msg2='Modi oath as PM yesterday'
    msg3='AP CM is going to visit vizag today'
    msg4 = "AP panchayat elections results will announce tomorrow"
    my_dict = {'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3,'msg4':msg4}
    return render(request,'newsapp/news.html',context=my_dict)

