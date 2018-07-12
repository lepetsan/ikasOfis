from django.db import models


# Create your models here.

class Member(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    age = models.CharField(max_length=3)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.firstname + " " + self.lastname