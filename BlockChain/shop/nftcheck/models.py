from django.db import models
from django.utils import timezone

class Checker(models.Model):
    policyID = models.CharField(max_length=50, default='')
    assetID = models.CharField(max_length=50, default='')
    time_create = models.DateTimeField(default=timezone.now())