from django.contrib import admin

# Register your models here.
from .models import SparePart, Local_Comparison_SparePart, Roller

admin.site.register(SparePart)
admin.site.register(Local_Comparison_SparePart)
admin.site.register(Roller)