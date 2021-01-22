from django.contrib import admin
from .models import Backup_copy, Client, Locality, Order, Product, User
from django.utils.http import urlencode
from django.urls import reverse

@admin.register(Backup_copy)
class Backup_copyAdmin(admin.ModelAdmin):
    list_display = ('number', 'name')

@admin.register(Client)
class Client_Admin(admin.ModelAdmin):
    list_display = ('number', 'title', 'name', 'adress', 'doc_num', 'doc_seria', 'account_details')

@admin.register(Locality)
class LocalityAdmin(admin.ModelAdmin):
    list_display = ('country', 'name_locality', 'name_region')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('number', 'price', 'quantity', 'customer_data')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'category')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'login', 'password')

