from django.shortcuts import render

# Create your views here.
# tutorial/views.py
# tutorial/views.py
from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import Person
from .tables import PersonTable
from MoneyRelations.models import Expense
from .tables import ExpenseTable

def people(request):
    table = PersonTable(Person.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'tutorial\people.html', {'table': table})


def expense(request):
    expenseTable = ExpenseTable(Person.objects.all())
    RequestConfig(request).configure(expenseTable)
    return render(request, 'tutorial\people.html', {'table': expenseTable})