from django.urls import path,include
from . import views
from .views import PlayerListView,PlayerDetailView,PlayerCreateView,PlayerUpdateView,PlayerDeleteView
urlpatterns = [
    path('',PlayerListView.as_view(),name='team-home'),
    path('<int:pk>/',PlayerDetailView.as_view(),name='team-detail'),
    path('create/',PlayerCreateView.as_view(),name='team-create'),
    path('<int:pk>/update',PlayerUpdateView.as_view(),name='team-update'),
    path('<int:pk>/delete',PlayerDeleteView.as_view(),name='team-delete')
]