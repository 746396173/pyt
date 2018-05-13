# models.py
from django.db import models


class userinfo(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=40)

# Create your models here.
