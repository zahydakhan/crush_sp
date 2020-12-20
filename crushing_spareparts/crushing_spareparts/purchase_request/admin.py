from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import SitesPurchaseRequest, MainPurchaseRequest

@admin.register(SitesPurchaseRequest)
class SitesPRAdmin(admin.ModelAdmin):
    list_display = ('id','part_number', 'description', 'vendor_name', 'unit_price', 'quantity', 'total_price', 'pr_number', 'line_number', 'site_name',)

@admin.register(MainPurchaseRequest)
class MainPRAdmin(admin.ModelAdmin):
    list_display = ('id','part_number', 'description', 'vendor_name', 'unit_price', 'quantity', 'total_price', 'pr_number', 'line_number', 'site_name', 'month',)
