from django.urls import path,include
from .views import MatchListView,MatchDetailView
urlpatterns = [
    path('',MatchListView.as_view(),name='tournament-home'),
    path('<int:pk>/',MatchDetailView.as_view(),name='tournament-detail')
]