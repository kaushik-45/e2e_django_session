from django.db import models

# Create your models here.

class MatchModel(models.Model):
    year = models.CharField(max_length=200)
    winner = models.CharField(max_length=200)
   
