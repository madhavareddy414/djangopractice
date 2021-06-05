from django.shortcuts import render

def home(request):
    return render(request,'testapp/home.html')

def sportsinfo(request):
    news1='Indian won the world cup'
    news2= 'Sachin made his 3rd centurary'
    news3= 'Sehawag retired from cricket'
    my_dict={
        'news1':news1,
        'news2':news2,
        'news3':news3
    }
    return render(request,'testapp/sports.html',my_dict)

def politicsinfo(request):
    news1='MOdi visited West bengal'
    news2= 'CBN lost in 2019 elections'
    news3= 'Panchayat elections recheduled'
    my_dict={
        'news1':news1,
        'news2':news2,
        'news3':news3
    }
    return render(request,'testapp/politics.html',my_dict)

def moviesinfo(request):
    news1='Chiranjeevi new movie released tomorrow'
    news2= 'Balakrishna movied colleced 100 crores for his latest movie'
    news3= 'RRR will release on 2022 summer'
    my_dict={
        'news1':news1,
        'news2':news2,
        'news3':news3
    }
    return render(request,'testapp/movies.html',my_dict)