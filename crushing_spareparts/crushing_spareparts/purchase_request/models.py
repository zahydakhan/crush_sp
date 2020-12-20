from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class SitesPurchaseRequest(models.Model):

    part_number = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(max_length=250, null=True, blank=True)
    vendor_name = models.CharField(max_length=50, null=True, blank=True)
    unit_price = models.DecimalField(max_digits=20, decimal_places=2,null=True, blank=True)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=20, decimal_places=2,null=True, blank=True)
    pr_number = models.CharField(max_length=20, null=True, blank=True)
    line_number = models.IntegerField( null=True, blank=True)
    site_name = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
     

    def __str__(self):
        return str(self.pr_number)

class MainPurchaseRequest(models.Model):

    part_number = models.CharField(max_length=80, null=True, blank=True)
    description = models.TextField(max_length=250, null=True, blank=True)
    vendor_name = models.CharField(max_length=50, null=True, blank=True)
    unit_price = models.DecimalField(max_digits=20, decimal_places=2,null=True, blank=True)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=20, decimal_places=2,null=True, blank=True)
    pr_number = models.CharField(max_length=20, null=True, blank=True)
    line_number = models.IntegerField( null=True, blank=True)
    site_name = models.CharField(max_length=80, null=True, blank=True)
    month = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.pr_number)