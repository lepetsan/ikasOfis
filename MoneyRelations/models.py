from django.core.validators import MaxValueValidator
from django.db import models
from datetime import datetime



class Expense(models.Model):
    PayerName_text = models.CharField('Payer Person/Firm',max_length=200, help_text="Please enter the name of the Payer",blank=True)
    TypeOfDocument = models.CharField('Type of the Document', max_length=200, help_text="Please enter the type of the Document", blank=True)
    DateOfDocument = models.DateTimeField('The date of the Document', default=datetime.now, blank=True)
    PaymentStatus = models.BooleanField('Payment Status', default=True)
    PaymentDate= models.DateField('Date of Payment', default=datetime.now, blank=True )
    MainCategory = models.CharField('Payer Person/Firm',max_length=200, help_text="Please enter the name of the Category",blank=True)
    SubCategory = models.CharField('Payer Person/Firm',max_length=200, help_text="Please enter the name of the Payer",blank=True)
    PaymentSum = models.DecimalField('Cell Phone Number',decimal_places=0, max_digits=12, default=0, validators=[MaxValueValidator(999999999999)])
    description = models.TextField('Description of the Customer',blank=True,help_text="Write a brief description",max_length=100)
    MethodOfPayment = models.CharField('Payer Person/Firm',max_length=200, help_text="Please enter the name of the Payer",blank=True)
    PayingEmployee = models.CharField('Payer Person/Firm',max_length=200, help_text="Please enter the name of the Payer",blank=True)

    def __str__(self):
        return self.CustomerName_text



# Create your models here.
