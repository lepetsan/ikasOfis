from django.core.validators import MaxValueValidator
from django.db import models
from datetime import datetime
from decimal import Decimal
from .utils import get_currencies
from .utils import getTotal

DocumentChoices = (
    ('Fatura', 'Fatura'),
    ('Fiş', 'Fiş'),
    ('İrsaliye', 'İrsaliye'),
)

CurrencyChoices = (
    ('TL', 'TL'),
    ('USD', 'USD'),
    ('EUR', 'EUR'),
)

mainCategoryChoices = (
    ('1', 'Demirbaş'),
    ('2', 'Yatırım'),
    ('3', 'Sabit Gider'),
    ('4', 'Pazarlama'),

)

subCategoryChoices = (
    ('1', 'Ofis'),
    ('1', 'Bilgisayar'),
    ('1', 'Diğer'),
    ('2', 'Marka / Patent'),
    ('2', 'Diğer'),
    ('3', 'Ticket'),
    ('3', 'Ekip Yemek / Motivasyon'),
    ('3', 'IK'),
    ('3', 'Internet'),
    ('3', 'Aidat / Isınma'),
    ('3', 'Vergi/Harç/Noter'),
    ('3', 'Diğer'),
    ('4', 'POP'),
    ('4', 'Diğer'),

)

PaymentChoices = (
    ('Paid', 'Yes'),
    ('Not Paid', 'No'),
)

class Expense(models.Model):
    PaidName_text = models.CharField('Paid Person/Firm', max_length=200, help_text="Please enter the name of the Paid Employee/Firm", blank=False, default='')
    TypeOfDocument = models.CharField(max_length=9, choices=DocumentChoices, default='Fatura')
    DateOfDocument = models.DateField('The date of the Document', default=datetime.now, blank=True)
    DocumentID = models.CharField('Document ID', max_length=200, help_text="Please enter the document ID", blank=False, default='')
    PaymentStatus = models.CharField(max_length=9, choices=PaymentChoices,default='Yes')
    PaymentDate= models.DateField('Date of Payment', default=datetime.now, blank=False )
    # MainCategory = models.OneToOneField('MainCat',on_delete=models.CASCADE,default=True)
    # SubCategory = models.OneToOneField('SubCat',on_delete=models.CASCADE,default=True)
    MainCategory = models.CharField('Main Category',max_length=9, choices=mainCategoryChoices, default='')
    SubCategory = models.CharField('Sub Category',max_length=9, choices=subCategoryChoices, default='')

    PaymentSum = models.DecimalField('Payment Sum', default=0,max_digits=12,decimal_places=2,validators=[MaxValueValidator(999999999999)])
    UltraTotalSum = models.DecimalField('Payment Sum', default=0, max_digits=12, decimal_places=2,
                                     validators=[MaxValueValidator(999999999999)])
    Currency = models.CharField(max_length=9, choices=CurrencyChoices, default='TL')

    TotalSum = models.DecimalField('Total Sum in TL', editable=False, blank=False,max_digits=12, default=0,decimal_places=2)
    description = models.CharField('Description of the Customer',blank=True,help_text="Write a brief description",max_length=100)
    MethodOfPayment = models.CharField('Method Of Payment',max_length=200, help_text="Please enter the name of the Payer",blank=False)
    PayingEmployee = models.CharField('Name of the Paying Employee',max_length=100, help_text="Please enter the name of the Paying Employee")

    BooleanPayment = models.BooleanField(default=True, editable=False)




    class Meta:
        ordering = ['DateOfDocument']



    def __str__(self):
        return self.PaidName_text



    def save(self, *args, **kwargs):
        TRYpEUR,TRYpUSD = get_currencies() ##Get the data from .utils.get_currencies
        if self.Currency == 'TL':
            self.TotalSum = self.PaymentSum
        if self.Currency == 'USD':
            self.TotalSum = self.PaymentSum * Decimal(TRYpUSD)
        if self.Currency == 'EUR':
            self.TotalSum = self.PaymentSum * Decimal(TRYpEUR)




        super(Expense, self).save(*args, **kwargs)

