from django.contrib import admin
from .models import Expense

class ExpenseAdmin(admin.ModelAdmin):
   list_display = ('PayerName_text','DateOfDocument','PaymentDate')


admin.site.register(Expense)
# Register your adminmodels here.
