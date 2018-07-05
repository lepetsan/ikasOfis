from django.core.validators import MaxValueValidator
from django.db import models


class Customer(models.Model):
    CustomerName_text=models.CharField('Name of the Customer',max_length=200, help_text="Please enter the name of the Customer")
    FirmName_text = models.CharField('Name of the Firm', max_length=200, help_text="Please enter the name of the Firm")
    description = models.TextField('Description of the Customer',blank=True,help_text="Write a brief description",max_length=100)
    CustomerCellNumber=models.DecimalField('Cell Phone Number',decimal_places=0, max_digits=12, default=90, validators=[MaxValueValidator(999999999999)])
    CustomerWorkNumber=models.DecimalField('Work Phone Number', decimal_places=0, max_digits=12, default=90,validators=[MaxValueValidator(999999999999)])
    Subscription_date=models.DateTimeField('Start of the Subscription')
    IsHeStillSub = models.BooleanField('Still Subscribed?',default=False)
    def __str__(self):
        return self.CustomerName_text

class Product(models.Model):
    CustomerName_text=models.CharField('Name of the Customer',max_length=200, help_text="Please enter the name of the Customer")
    FirmName_text = models.CharField('Name of the Firm', max_length=200, help_text="Please enter the name of the Firm")
    description = models.TextField('Description of the Customer',blank=True,help_text="Write a brief description",max_length=100)
    CustomerCellNumber=models.DecimalField('Cell Phone Number',decimal_places=0, max_digits=12, default=90, validators=[MaxValueValidator(999999999999)])
    CustomerWorkNumber=models.DecimalField('Work Phone Number', decimal_places=0, max_digits=12, default=90,validators=[MaxValueValidator(999999999999)])
    Subscription_date=models.DateTimeField('Start of the Subscription')
    IsHeStillSub = models.BooleanField('Still Subscribed?',default=False)
    def __str__(self):
        return self.CustomerName_text


# Create your models here.
