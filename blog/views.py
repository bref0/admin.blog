from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from .models import FeArticle


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return FeArticle.objects.order_by('-create_time')[:5]
