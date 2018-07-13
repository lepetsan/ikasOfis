import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ikasOfis.settings')
import django,random
django.setup()



from faker import Faker
from MoneyRelations.models import Expense, subcategory,maincategory
from django.utils import timezone


fake= Faker()

keyword1, _ = maincategory.objects.get_or_create(name='keyword_name')
keyword2, _ = subcategory.objects.get_or_create(name='keyword_name')
maincategory, flag = Expense.objects.get_or_create(name='maincategory_name', keywords=keyword1)
subcategory, flag = Expense.objects.get_or_create(name='subcategory_name', keywords=keyword2)



maincategories = ['Yatırım', 'Pazarlama', 'Sabit Gider', 'Demirbaş']
subcategories = ['Bilgisayar']





# def add_expense():
#
#     subcatego = subcategory.objects.get_or_create()
#
#
#     expense = Expense.objects.get_or_create(
#
#         PaidName_text = fake.name(),
#         TypeOfDocument = "Fatura",
#         DateOfDocument = timezone.now(),
#         DocumentID = fake.text(),
#         PaymentStatus = 'Yes',
#         PaymentDate = timezone.now(),
#         mainCategoryExpense = 'Demirbaş',
#         SubCategoryExpense = 'Bilgisayar',
#         PaymentSum = random.randint(500, 700),
#         UltraTotalSum = 0,
#         Currency = 'USD',
#         TotalSum = 700,
#         description = "description",
#         MethodOfPayment = "Kredi Kartı",
#         PayingEmployee = "Mustafa Namoglu",
#         BooleanPayment = True
#     )
#     return expense
#
#
# def populate(N):
#     for entry in range(N):
#         expense=add_expense()





add_expense()
# def create_Expenses(N):
#     fake=Faker()
#     for _ in range(N):
#         Expense.PaidName_text = fake.name()
#         Expense.TypeOfDocument = "Fatura"
#         Expense.DateOfDocument = timezone.now()
#         Expense.DocumentID = fake.text()
#         Expense.PaymentStatus = 'Yes'
#         Expense.PaymentDate = timezone.now()
#         Expense.mainCategoryExpense = ''
#         Expense.SubCategoryExpense = ''
#         Expense.PaymentSum = random.randint(500,700)
#         Expense.UltraTotalSum = 0
#         Expense.Currency = 'USD'
#         Expense.TotalSum = 700
#         Expense.description= "description"
#         Expense.MethodOfPayment = "Kredi Kartı"
#         Expense.PayingEmployee = "Mustafa Namoglu"
#         Expense.BooleanPayment = True
#         Expense.save()
# create_Expenses(100)
# print("Data is populated succesfully")