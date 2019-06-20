from django.db import models

# Create your models here.
class Match(models.Model):
    match_date=models.DateField()
    team_a=models.CharField(max_length=20)
    team_b=models.CharField(max_length=20)



class MatchDescription(models.Model):
    match=models.OneToOneField(Match,on_delete=models.CASCADE)
    m_o_m=models.CharField(max_length=20,default='xyz')
    best_bowling=models.CharField(max_length=20)
    best_batsmen=models.CharField(max_length=20)
    desc=models.TextField()