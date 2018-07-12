# tutorial/tables.py
import django_tables2 as tables
from .models import Person
from MoneyRelations.models import  Expense

class PersonTable(tables.Table):
    class Meta:
        model = Person
        template_name = 'django_tables2/bootstrap.html'


class ExpenseTable(tables.Table):
    class Meta:
        model = Expense
        template_name = 'django_tables2/bootstrap.html'