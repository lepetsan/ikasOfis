from django.shortcuts import render
from MoneyRelations.models import Expense
from datetime import datetime, timedelta
from django.shortcuts import redirect


def index_redirect(request):
    return redirect('/table/')




# Create your views here.

def index(request):
    all_members = Expense.objects.all()
    return render(request, 'table/index.html', {'all_members': all_members})