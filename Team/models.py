from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Player(models.Model):
    name = models.CharField(max_length=100)
    skill = models.CharField(max_length=100,default='-')
    team=models.CharField(max_length=100,default='-')
    dept=models.CharField(max_length=100,default='-')
    user_name=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('team-home')


