from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Site(models.Model):

    options = (
        ('ACT', 'ACT'),
        ('QLD', 'QLD'),
        ('NSW', 'NSW'),
        ('SA', 'SA'),
        ('VIC', 'VIC'),
        ('TAS', 'TAS'),
    )
    site = models.CharField(max_length=50)
    address = models.TextField(max_length=250)
    state = models.CharField(max_length=10, choices=options, default="VIC")
    manager_name = models.CharField(max_length=50, null=True, blank=True)
    manager_email = models.EmailField(max_length=100, null=True, blank=True)
    manager_phone = models.CharField(max_length=50, null=True, blank=True)
    supervisor_name = models.CharField(max_length=50, null=True, blank=True)
    supervisor_email = models.EmailField(max_length=100, null=True, blank=True)
    supervisor_phone = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.site