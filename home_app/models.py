from django.db import models

# Create your models here.


class Menu(models.Model):
    name = models.CharField( max_length=150)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.URLField(max_length=500)
    
class User(models.Model):
    name = models.CharField( max_length=50)


class Order(models.Model):
    account_name = models.CharField( max_length=150)
    ordered_by = models.CharField( max_length=150)
    address = models.TextField(max_length=500)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
