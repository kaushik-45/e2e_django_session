from django.db import models

class School(models.Model):
    name = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    language = models.CharField(max_length=255)