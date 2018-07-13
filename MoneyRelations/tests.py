import os, django, random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()


from .models import Expense
from faker import Faker
from MoneyRelations.models import Expense
from django.utils import timezone

def create_Expenses(N):
    fake=Faker()
    for _ in range(N):
        Expense.PaidName_text = fake.name()
        Expense.TypeOfDocument = "Fatura"
        Expense.DateOfDocument = timezone.now()
        Expense.DocumentID = fake.text()
        Expense.PaymentStatus = 'Yes'
        Expense.PaymentDate = timezone.now()
        Expense.mainCategoryExpense = ''
        Expense.SubCategoryExpense = ''
        Expense.PaymentSum = random.randint(500,700)
        Expense.UltraTotalSum = 0
        Expense.Currency = 'USD'
        Expense.TotalSum = 700
        Expense.description= "description"
        Expense.MethodOfPayment = "Kredi Kartı"
        Expense.PayingEmployee = "Mustafa Namoglu"
        Expense.BooleanPayment = True

create_Expenses(100)
print("Data is populated succesfully")