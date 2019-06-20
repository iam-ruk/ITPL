from django.shortcuts import render
from django.views.generic import ListView,DetailView
# Create your views here.
from .models import Match,MatchDescription

class MatchListView(ListView):
    model = Match
    template_name = 'tournament/schedule.html'
    context_object_name = 'matches'



class MatchDetailView(DetailView):
    model = Match
    template_name ='tournament/detail.html'
    context_object_name = 'match'