from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Events(models.Model):
    name = models.CharField(max_length=200, default='none')
    location = models.CharField(max_length=200)
    datetime = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    cost = models.CharField(max_length=6, default='0')

class Payment(models.Model):
    check = models.CharField(max_length=3, default='No')
    name = models.CharField(max_length=50, default='None')
    email = models.CharField(max_length=50, default='None')
    phone = models.CharField(max_length=50, default='None')

class Scores(models.Model):
    golfername = models.CharField(max_length=200, default='none')
    score = models.CharField(max_length=6, default='0')
    handicap = models.CharField(max_length=6, default='0')
