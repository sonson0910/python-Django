from django.db import models

# Create your models here.

class History(models.Model):
    contract_id = models.CharField(max_length=100, defautl = '')
    token_id = models.IntegerField(default = 0)
