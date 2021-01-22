from django.db import models

# Create your models here.

class Product (models.Model):
    number = models.IntegerField(default=1)
    name = models.CharField(max_length=120, default=1)
    category = models.CharField(max_length=120, default=1)
    objects = models.Manager()

class Order (models.Model):
    number = models.IntegerField(default=1)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE, default=1)
    price = models.IntegerField(default=1)
    quantity = models.IntegerField(default=1)
    customer_data = models.CharField(max_length=120, default=1)
    locality_id = models.ForeignKey('Locality', on_delete=models.CASCADE, default=1)
    client_id = models.ForeignKey('Client', on_delete=models.CASCADE, default=1)
    objects = models.Manager()

class Locality (models.Model):
    country = models.CharField(max_length=120, default=1)
    name_locality = models.CharField(max_length=120, default=1)
    name_region = models.CharField(max_length=120, default=1)
    objects = models.Manager()

class Client (models.Model):
    number = models.IntegerField(default=1)
    title = models.CharField(max_length=120, default=1)
    name = models.CharField(max_length=120, default=1)
    adress = models.CharField(max_length=120, default=1)
    doc_num = models.IntegerField(default=1)
    doc_seria = models.IntegerField(default=1)
    account_details = models.IntegerField(default=1)
    objects = models.Manager()

class Backup_copy (models.Model):
    number = models.IntegerField(default=1)
    name = models.CharField(max_length=120, default=1)
    objects = models.Manager()

class User (models.Model):
    name = models.CharField(max_length=120, default=1)
    login = models.CharField(max_length=120, default=1)
    password = models.IntegerField(default=1)
    objects = models.Manager()
