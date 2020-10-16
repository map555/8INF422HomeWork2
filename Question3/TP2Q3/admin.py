from django.contrib import admin
from TP2Q3.models import *
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    list_display = ('id','manufacturer','model','trim','mileage',
                    'year','weight','condition','color','price','sold')
    List_filter=('id','manufacturer','model','trim','mileage',
                    'year','weight','condition','color','price','sold')
    search_fields = ('id','manufacturer','model','trim','mileage',
                    'year','weight','condition','color','price','sold')

class BillAdmin(admin.ModelAdmin):
    list_display = ('id','clientName','Car')
    list_filter = ('id','clientName','Car')
    search_fields = ('id','clientName','Car')

admin.site.register(Car,CarAdmin)
admin.site.register(Bill,BillAdmin)





