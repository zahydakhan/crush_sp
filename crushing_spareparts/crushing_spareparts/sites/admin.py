from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Site

@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('id','state', 'manager_name', 'supervisor_name',)
