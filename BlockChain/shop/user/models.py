from django.db import models
from django.contrib.auth.models import AbstractUser
from nft.models import Nft

# Create your models here.

class CustomerUser(models.Model):
    user_id = models.IntegerField(default=0)
    phone_number = models.CharField(default='', max_length=15)
    address = models.CharField(default='', max_length=255)
    nft = models.ForeignKey(Nft, on_delete = models.CASCADE)


class Collection(models.Model):
    Collection_id = models.IntegerField(default=0)
    collection_name = models.CharField(max_length=100, default='')
    user_id = models.ForeignKey(CustomerUser, on_delete= models.CASCADE)