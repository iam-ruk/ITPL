from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.register,name='register-home'),
    path('profile/',views.profile,name='profile')
]