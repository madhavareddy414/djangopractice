from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from django.views import generic

from polls.models import Question


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {
#         'latest_question_list':latest_question_list
#     }
#     return render(request,'polls/index.html',context)
# def detail(request,question_id):
#     try:
#         question= Question.objects.get(pk=question_id)
#     except Exception as e:
#         print(e)
#     return render(request,'polls/detail.html',{'question':question})
#
# def results(request,question_id):
#     response = 'You are looking at question %s.'
#     return HttpResponse (response % question_id)
#
# def vote(request,question_id):
#     return HttpResponse('You re voting on question %s'%question_id)


class Index(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request,question_id):
    return HttpResponse('You re voting on question %s'%question_id)
