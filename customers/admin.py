from django.contrib import admin

# Register your models here.


from .import models

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['admin_name', 'name']
    search_fields = ['name', 'admin_name']





@admin.register(models.Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['customer','placed_at','payment','total']
    #list_editable = ['payment']
    ordering = ['placed_at']




admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.PurchaseItem)

