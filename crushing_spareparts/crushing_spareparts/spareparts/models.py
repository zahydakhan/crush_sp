from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class SparePart(models.Model):

    class GetObj(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(sp_type="ground engaging tools")

    class MnLinerObj(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(sp_type="manganese liners")

    class MpObj(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(sp_type="mechanical parts")

    types_options = (
        ('ground engaging tools', 'ground engaging tools'),
        ('manganese liners', 'manganese liners'),
        ('mechanical parts', 'mechanical parts'),
    )
    
    part_number = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=250, null=True, blank=True)
    vendor_name = models.CharField(max_length=200, null=True, blank=True)
    vendor_status = models.CharField(max_length=200, null=True, blank=True)
    sp_type = models.CharField(max_length=50, choices=types_options, default="mechanical parts", null=True, blank=True)
    weight_kg = models.CharField(max_length=50, null=True, blank=True)
    machine = models.CharField(max_length=50, null=True, blank=True)
    model_number = models.CharField(max_length=50, null=True, blank=True)
    aud = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)
    usd = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=50, decimal_places=2,null=True, blank=True)
    created_at =models.DateTimeField(default=timezone.now)
    objects = models.Manager()
    GetObjects = GetObj()
    MnLinerObjects = MnLinerObj()
    MpObjects = MpObj()

    class Meta:
        ordering = ("-vendor_status",)

    def __str__(self):
        return str(self.part_number)

class Local_Comparison_SparePart(models.Model):

    types_options = (
        ('ground engaging tools', 'ground engaging tools'),
        ('manganese liners', 'manganese liners'),
        ('mechanical parts', 'mechanical parts'),
    )
    
    part_number = models.ForeignKey(SparePart, on_delete=models.CASCADE, related_name='comparison_sparepart')
    description = models.TextField(max_length=250, null=True, blank=True)
    vendor_name = models.CharField(max_length=200, null=True, blank=True)
    vendor_status = models.CharField(max_length=50, null=True, blank=True)
    sp_type = models.CharField(max_length=50, choices=types_options, default="mechanical parts", null=True, blank=True)
    weight_kg = models.CharField(max_length=50, null=True, blank=True)
    machine = models.CharField(max_length=50, null=True, blank=True)
    model_number = models.CharField(max_length=50, null=True, blank=True)
    aud = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)
    usd = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=50, decimal_places=2,null=True, blank=True)
    created_at =models.DateTimeField(default=timezone.now)
    objects = models.Manager()

    class Meta:
        ordering = ("-vendor_status",)

    def __str__(self):
        return str(self.part_number)


class Roller(models.Model):

    class DesObj(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(description="Steel Trough Roller")

    options = (
        ('Steel Trough Roller', 'Steel Trough Roller'),
        ('Steel Return Roller', 'Steel Return Roller'),
        ('HDPE Trough Roller', 'HDPE Trough Roller'),
        ('HDPE Return Roller', 'HDPE Return Roller'),
        ('Impact Roller', 'Impact Roller'),
    )
    description = models.TextField(max_length=50, choices=options, default="Steel Trough Roller", null=True, blank=True)
    roller_diameter = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)
    wall_thickness = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)
    roller_length = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)
    shaft_diameter = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)
    bearing = models.CharField(max_length=100, null=True, blank=True)
    aud = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)
    usd = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)
    vendor_name = models.CharField(max_length=100, null=True, blank=True)
    price = models.DecimalField(max_digits=50, decimal_places=2,null=True, blank=True)
    created_at =models.DateTimeField(default=timezone.now)
    objects = models.Manager()
    desObjects = DesObj()

    class Meta:
        ordering = ("-description",)

    def __str__(self):
        return self.description
