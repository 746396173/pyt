from django.db import models

# Create your models here.
# models.py

class DJ1(models.Model):
    name = models.CharField(max_length=20)