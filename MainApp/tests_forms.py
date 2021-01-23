from django.test import TestCase
import unittest
from .forms import FormProduct, FormOrder, FormUser, FormClient, FormBackup_copy, FormLocality

class FormProductFormTest(TestCase):

    def test_number_label(self):
        form = FormProduct()
        self.assertTrue(form.fields['number'].label == None or form.fields['number'].label == 'номер')

    def test_name_label(self):
        form = FormProduct()
        self.assertTrue(form.fields['name'].label == None or form.fields['name'].label == 'название')

    def test_type_category_label(self):
        form = FormProduct()
        self.assertTrue(form.fields['category'].label == None or form.fields['category'].label == 'категория')

    def test_resoult(self):
        form = FormProduct(data={'number': "1", 'name': "1", 'category': "1"})
        self.assertTrue(form.is_valid())

class FormOrderFormTest(TestCase):

    def test_number_label(self):
        form = FormOrder()
        self.assertTrue(form.fields['number'].label == None or form.fields['number'].label == 'номер')

    def test_product_id_label(self):
        form = FormOrder()
        self.assertTrue(form.fields['product_id'].label == None or form.fields['product_id'].label == 'продукт')

    def test_price_label(self):
        form = FormOrder()
        self.assertTrue(form.fields['price'].label == None or form.fields['price'].label == 'цена')

    def test_quantity_label(self):
        form = FormOrder()
        self.assertTrue(form.fields['quantity'].label == None or form.fields['quantity'].label == 'количество')

    def test_customer_data_label(self):
        form = FormOrder()
        self.assertTrue(form.fields['customer_data'].label == None or form.fields['customer_data'].label == 'пользовательские данные')

    def test_locality_id_label(self):
        form = FormOrder()
        self.assertTrue(form.fields['locality_id'].label == None or form.fields['locality_id'].label == 'местонахождение')

    def test_client_id_label(self):
        form = FormOrder()
        self.assertTrue(form.fields['client_id'].label == None or form.fields['client_id'].label == 'клиент')

    def test_resoult(self):
        form = FormOrder(data={'number': "1", 'product_id': 1, 'price': "1", 'quantity': "1", 'customer_data': "1", 'name': "1", 'locality_id': 1, 'client_id': 1})
        self.assertTrue(form.is_valid())

class FormUserFormTest(TestCase):

    def test_country_label(self):
        form = FormUser()
        self.assertTrue(form.fields['country'].label == None or form.fields['country'].label == 'страна')

    def test_name_locality_label(self):
        form = FormUser()
        self.assertTrue(form.fields['name_locality'].label == None or form.fields['name_locality'].label == 'название населенного пункта')

    def test_name_region_label(self):
        form = FormUser()
        self.assertTrue(form.fields['name_region'].label == None or form.fields['name_region'].label == 'название региона')

    def test_resoult(self):
        form = FormUser(data={'country': "1", 'name_locality': "1", 'name_region': "1"})
        self.assertTrue(form.is_valid())

class FormClientFormTest(TestCase):

    def test_number_label(self):
        form = FormClient()
        self.assertTrue(form.fields['number'].label == None or form.fields['number'].label == 'номер')

    def test_title_label(self):
        form = FormClient()
        self.assertTrue(form.fields['title'].label == None or form.fields['title'].label == 'лицо')

    def test_name_label(self):
        form = FormClient()
        self.assertTrue(form.fields['name'].label == None or form.fields['name'].label == 'имя')

    def test_adress_label(self):
        form = FormClient()
        self.assertTrue(form.fields['adress'].label == None or form.fields['adress'].label == 'адрес')

    def test_doc_num_label(self):
        form = FormClient()
        self.assertTrue(form.fields['doc_num'].label == None or form.fields['doc_num'].label == 'номер документа')

    def test_doc_seria_label(self):
        form = FormClient()
        self.assertTrue(form.fields['doc_seria'].label == None or form.fields['doc_seria'].label == 'серия документа')

    def test_account_details_label(self):
        form = FormClient()
        self.assertTrue(form.fields['account_details'].label == None or form.fields['account_details'].label == 'банковские реквизиты')

    def test_resoult(self):
        form = FormClient(data={'number': "1", 'title': "1", 'name': "1", 'adress': "1", 'doc_num': "1", 'doc_seria': "1", 'account_details': "1"})
        self.assertTrue(form.is_valid())

class FormBackup_copyFormTest(TestCase):

    def test_number_label(self):
        form = FormBackup_copy()
        self.assertTrue(form.fields['number'].label == None or form.fields['number'].label == 'номер')

    def test_name_label(self):
        form = FormBackup_copy()
        self.assertTrue(form.fields['name'].label == None or form.fields['name'].label == 'имя')

    def test_resoult(self):
        form = FormBackup_copy(data={'number': "1", 'name': "1"})
        self.assertTrue(form.is_valid())

class FormLocalityFormTest(TestCase):

    def test_name_label(self):
        form = FormLocality()
        self.assertTrue(form.fields['name'].label == None or form.fields['name'].label == 'имя')

    def test_login_label(self):
        form = FormLocality()
        self.assertTrue(form.fields['login'].label == None or form.fields['login'].label == 'логин')

    def test_password_label(self):
        form = FormLocality()
        self.assertTrue(form.fields['password'].label == None or form.fields['password'].label == 'пароль')

    def test_resoult(self):
        form = FormLocality(data={'name': "1", 'login': "1", 'password': "1"})
        self.assertTrue(form.is_valid())
