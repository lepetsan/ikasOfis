from django.contrib import admin

from MoneyRelations.utils import get_currencies
from .models import Expense
from datetime import datetime
from . import models
from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect


def payment(modeladmin, request, queryset):
    queryset.update(
        BooleanPayment=True,
        PaymentDate=datetime.now()
    )


payment.short_description = "Mark expenses as paid now."


class ExpenseAdmin(admin.ModelAdmin):
    change_form_template = "expense/change_form.html"
    actions = [payment]
    date_hierarchy = 'PaymentDate'
    list_display = (
        'PaymentDate', 'PaymentStatus', 'TypeOfDocument', 'DocumentID', 'PaidName_text', 'PaymentSum', 'Currency','TotalSum',
        'MainCategory', 'SubCategory','MethodOfPayment', )
    list_filter = ('PaymentDate', 'TypeOfDocument', 'MainCategory', 'SubCategory',)
    search_fields = ('PaidName_text', 'DateOfDocument', 'DocumentID', 'PaymentSum', 'TypeOfDocument',
                     'PaymentDate', 'MainCategory', 'SubCategory', 'MethodOfPayment', 'PayingEmployee',
                     'BooleanPayment')
    # list_editable = ('TypeOfDocument', 'BooleanPayment')
    save_on_top = True
    save_as = True
    ordering = ['-DateOfDocument']
    list_display_links = (
        'PaymentDate', 'PaymentStatus', 'TypeOfDocument', 'DocumentID', 'PaidName_text', 'PaymentSum', 'Currency',
        'MainCategory', 'SubCategory','MethodOfPayment', 'TotalSum',)
    radio_fields = {'Currency': admin.HORIZONTAL}
    fieldsets = (
        (None, {
            'fields': ('PaidName_text',
                       'TypeOfDocument', 'DocumentID',
                       ('PaymentStatus', 'PaymentDate'),
                       ('MainCategory', 'SubCategory'),
                       ('PaymentSum', 'Currency'),
                       'MethodOfPayment',
                       'description',
                       'PayingEmployee'
                       )

        }

         ),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields' : ( 'DateOfDocument',
)
        }),
    )


    # def response_add(self, request, obj):
    #     """ if user clicked "edit this page", return back to main site """
    #     response = super(ExpenseAdmin, self).response_change(request, obj)
    #
    #     if (isinstance(response, HttpResponseRedirect) and
    #             response['location'] == '../' and
    #             request.GET.get('source') == 'main'):
    #         response['location'] = obj.get_absolute_url()
    #
    #     return response


    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        TRYpEUR, TRYpUSD = get_currencies()
        extra_context = extra_context or {}
        extra_context["euro"] = TRYpEUR
        extra_context["dolar"] = TRYpUSD
        return super(ExpenseAdmin, self).changeform_view(request, object_id=object_id, form_url=form_url,

                                             extra_context=extra_context)
    def response_change(self, request, obj):
            """ if user clicked "edit this page", return back to main site """
            response = super(ExpenseAdmin, self).response_change(request, obj)

            if (isinstance(response, HttpResponseRedirect) and
                    response['location'] == '../' and
                    request.GET.get('source') == 'main'):
                response['location'] = obj.get_absolute_url()

            return response

    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',  # jquery

        )


admin.site.register(Expense, ExpenseAdmin)
# Register your adminmodels here.
