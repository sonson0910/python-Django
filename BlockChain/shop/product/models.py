from django.db import models

# Create your models here.

class Category(models.Model):
    Category_id = models.IntegerField()
    name = models.CharField(max_length=100, default = '')
    slug = models.CharField(max_length = 100, default = '')
    description = models.TextField(default = '')
    active = models.BooleanField(default = True)


class Product(models.Model):
    name = models.CharField(max_length=100, default='')
    description = models.TextField(default = '')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    active = models.BooleanField(default = True)


class Valiation(models.Model):
    product = models.ForeignKey
    name = models.CharField(max_length=100, default='')
    price = models.IntegerField(default=0)
    sale_price = models.IntegerField(default=0)
    inventory = models.IntegerField(default = 0)
    active = models.BooleanField(default=True)
