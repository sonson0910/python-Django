from django.db import models

# Create your models here.

class Transaction(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(default='')
    buyer = models.CharField(max_length=25, default='')
    seller = models.CharField(max_length=25, default='')


class Contract(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    buyer_id = models.CharField(default='0x...', max_length=100)
    seller_id = models.CharField(default='0x...', max_length=100)
    contract_address = models.CharField(default='0x...', max_length=100)
