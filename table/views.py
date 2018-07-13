from django.shortcuts import render
from MoneyRelations.models import Expense, mainCategoryChoices, subCategoryChoices, mainCategorySubCategoryRelation
from datetime import datetime, timedelta
from django.shortcuts import redirect


def index_redirect(request):
    return redirect('/table/')




# Create your views here.

def index(request):
    all_members = Expense.objects.all()
    # for a in all_members:
        # a.MainCategory = mainCategoryChoices[a.MainCategory]
        # a.SubCategory = subCategoryChoices[a.SubCategory]
    return render(request, 'table/index.html', {'all_members': all_members})