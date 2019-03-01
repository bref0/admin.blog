from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)
    # return HttpResponse(template.render(context, request))


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = 'you are look at result questions %s.'
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse('you are voting on question %s.' % question_id)
