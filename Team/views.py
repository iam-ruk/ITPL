from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Player
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse_lazy
# Create your views here.


class PlayerListView(LoginRequiredMixin,ListView):
    model=Player
    template_name = 'Team/home.html'
    context_object_name = 'players'
    ordering = ['name']


class PlayerDetailView(LoginRequiredMixin,DetailView):
    model = Player
    template_name = 'Team/detail.html'
    context_object_name = 'player'


class PlayerCreateView(LoginRequiredMixin,CreateView):
    model = Player
    fields = ['name','skill','team','dept']
    template_name = 'Team/create.html'


    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)



class PlayerUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Player
    fields = ['name','skill','team','dept']
    template_name = 'Team/update.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)

    def test_func(self):
        player=self.get_object()
        if player.user_name == self.request.user:
            return True
        return False

class PlayerDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Player
    template_name = 'Team/delete.html'
    success_url = reverse_lazy('team-home')

    def test_func(self):
        player = self.get_object()
        if player.user_name == self.request.user:
            return True
        return False

def contact(request):
    return render(request,'Team/contacts.html')