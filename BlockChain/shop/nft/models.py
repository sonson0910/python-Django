from django.db import models

# Create your models here.

class Nft(models.Model):
    token_id = models.CharField(default = '', max_length=100)
    name = models.CharField(default='', max_length=100)
    transaction_time = models.DateTimeField(auto_now_add=True)
    Type = models.CharField(max_length=10, default='')
    metadata = models.CharField(default='', max_length=100)
    policy_id = models.CharField(default='', max_length=50)
    asset_id = models.CharField(default='', max_length=50)
    data = models.CharField(default='', max_length=255)

