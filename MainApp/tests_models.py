from django.test import TestCase
import unittest
from .models import Product, Order, Locality, Client, Backup_copy, User

class ProductModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Product.objects.create(number='1', name='1', category='1')

    def test_number_label(self):
        ad = Product.objects.get(id=1)
        field_label = ad._meta.get_field('number').verbose_name
        self.assertEquals(field_label, 'number')

    def test_name_label(self):
        ad = Product.objects.get(id=1)
        field_label = ad._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_category_label(self):
        ad = Product.objects.get(id=1)
        field_label = ad._meta.get_field('category').verbose_name
        self.assertEquals(field_label, 'category')

class OrderModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Order.objects.create(number='1', product_id=1, price='1', quantity='1', customer_data='1', locality_id=1, client_id=1)

    def test_number_label(self):
        ad = Order.objects.get(id=1)
        field_label = ad._meta.get_field('number').verbose_name
        self.assertEquals(field_label, 'number')

    def test_product_id_label(self):
        ad = Order.objects.get(id=1)
        field_label = ad._meta.get_field('product_id').verbose_name
        self.assertEquals(field_label, 'product_id')

    def test_price_label(self):
        ad = Order.objects.get(id=1)
        field_label = ad._meta.get_field('price').verbose_name
        self.assertEquals(field_label, 'price')

    def test_quantity_label(self):
        ad = Order.objects.get(id=1)
        field_label = ad._meta.get_field('quantity').verbose_name
        self.assertEquals(field_label, 'quantity')

    def test_customer_data_label(self):
        ad = Order.objects.get(id=1)
        field_label = ad._meta.get_field('customer_data').verbose_name
        self.assertEquals(field_label, 'customer_data')

    def test_locality_id_label(self):
        ad = Order.objects.get(id=1)
        field_label = ad._meta.get_field('locality_id').verbose_name
        self.assertEquals(field_label, 'locality_id')

    def test_client_id_label(self):
        ad = Order.objects.get(id=1)
        field_label = ad._meta.get_field('client_id').verbose_name
        self.assertEquals(field_label, 'client_id')

class LocalityModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Locality.objects.create(country='1', name_locality='1', name_region='1')

    def test_country_label(self):
        ad = Locality.objects.get(id=1)
        field_label = ad._meta.get_field('country').verbose_name
        self.assertEquals(field_label, 'country')

    def test_name_locality_label(self):
        ad = Locality.objects.get(id=1)
        field_label = ad._meta.get_field('name_locality').verbose_name
        self.assertEquals(field_label, 'name_locality')

    def test_name_region_label(self):
        ad = Locality.objects.get(id=1)
        field_label = ad._meta.get_field('name_region').verbose_name
        self.assertEquals(field_label, 'name_region')

class ClientModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Client.objects.create(number='1', title='1', name='1', adress='1', doc_num='1', doc_seria='1', account_details='1')

    def test_number_label(self):
        ad = Client.objects.get(id=1)
        field_label = ad._meta.get_field('number').verbose_name
        self.assertEquals(field_label, 'number')

    def test_title_label(self):
        ad = Client.objects.get(id=1)
        field_label = ad._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_name_label(self):
        ad = Client.objects.get(id=1)
        field_label = ad._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_adress_label(self):
        ad = Client.objects.get(id=1)
        field_label = ad._meta.get_field('adress').verbose_name
        self.assertEquals(field_label, 'adress')

    def test_doc_num_label(self):
        ad = Client.objects.get(id=1)
        field_label = ad._meta.get_field('doc_num').verbose_name
        self.assertEquals(field_label, 'doc_num')

    def test_doc_seria_label(self):
        ad = Client.objects.get(id=1)
        field_label = ad._meta.get_field('doc_seria').verbose_name
        self.assertEquals(field_label, 'doc_seria')

    def test_account_details_label(self):
        ad = Client.objects.get(id=1)
        field_label = ad._meta.get_field('account_details').verbose_name
        self.assertEquals(field_label, 'account_details')

class Backup_copyModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Backup_copy.objects.create(number='1', name='1')

    def test_number_label(self):
        ad = Backup_copy.objects.get(id=1)
        field_label = ad._meta.get_field('number').verbose_name
        self.assertEquals(field_label, 'number')

    def test_name_label(self):
        ad = Backup_copy.objects.get(id=1)
        field_label = ad._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(name='1', login='1', password='1')

    def test_name_label(self):
        ad = User.objects.get(id=1)
        field_label = ad._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_login_label(self):
        ad = User.objects.get(id=1)
        field_label = ad._meta.get_field('login').verbose_name
        self.assertEquals(field_label, 'login')

    def test_password_label(self):
        ad = User.objects.get(id=1)
        field_label = ad._meta.get_field('password').verbose_name
        self.assertEquals(field_label, 'password')

