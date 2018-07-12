from django.db import models

# Create your models here.
# tutorial/models.py
class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name='full name')

