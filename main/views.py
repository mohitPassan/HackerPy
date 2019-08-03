from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
# Create your views here.
from main import models

class Index(TemplateView):
    template_name = 'main/index.html'

class Contests(ListView):
    model = models.Contest
    template_name = 'main/contests.html'

class Contest(DetailView):
    model = models.Contest
    template_name = 'main/contest.html'

class Problem(DetailView):
    template_name = 'main/problem.html'

    def get_queryset(self):
        return models.Contest.objects.get(id = self.kwargs['contest_id']).problems

class Submit(CreateView):
    model = models.Submission
    template_name = 'main/submit.html'
    fields = ('user', 'contest', 'problem', 'source', 'language')

