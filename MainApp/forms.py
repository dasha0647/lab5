from django import forms
from .models import Product, Locality, Client

class FormProduct (forms.Form):
    number = forms.IntegerField(label="номер")
    name = forms.CharField(label="название")
    category = forms.CharField(label="категория")

class FormOrder (forms.Form):
    number = forms.IntegerField(label="номер")
    product_id = forms.ModelChoiceField(label="продукт", queryset=Product.objects.all().order_by('id'))
    price = forms.IntegerField(label="цена")
    quantity = forms.IntegerField(label="количество")
    customer_data = forms.CharField(label="пользовательские данные")
    locality_id = forms.ModelChoiceField(label="местонахождение", queryset=Locality.objects.all().order_by('id'))
    client_id = forms.ModelChoiceField(label="клиент", queryset=Client.objects.all().order_by('id'))

class FormLocality (forms.Form):
    country = forms.CharField(label="страна")
    name_locality = forms.CharField(label="название населенного пункта")
    name_region = forms.CharField(label="название региона")

class FormClient (forms.Form):
    number = forms.IntegerField(label="номер")
    title = forms.CharField(label="лицо")
    name = forms.CharField(label="имя")
    adress = forms.CharField(label="адрес")
    doc_num = forms.IntegerField(label="номер документа")
    doc_seria = forms.IntegerField(label="серия документа")
    account_details = forms.IntegerField(label="банковские реквизиты")

class FormBackup_copy (forms.Form):
    number = forms.IntegerField(label="номер")
    name = forms.CharField(label="имя")

class FormUser (forms.Form):
    name = forms.CharField(label="имя")
    login = forms.CharField(label="логин")
    password = forms.IntegerField(label="пароль")
