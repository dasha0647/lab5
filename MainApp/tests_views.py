from django.test import TestCase
import unittest
from .models import Product, Order, Locality, Client, Backup_copy, User
from django.urls import reverse

class View_Product_Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        Product.objects.create(number='1', name='1', category='1')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/product/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('product'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('owner'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'MainApp/Template_Product.html')

class View_Order_Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        Order.objects.create(number='1', product_id=1, price='1', quantity='1', customer_data='1', locality_id=1,
                             client_id=1)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/order/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('order'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('order'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'MainApp/Template_Order.html')

class View_Locality_Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        Locality.objects.create(country='1', name_locality='1', name_region='1')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/locality/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('locality'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('locality'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'MainApp/Template_Locality.html')

class View_Client_Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        Client.objects.create(number='1', title='1', name='1', adress='1', doc_num='1', doc_seria='1',
                              account_details='1')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/client/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('client'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('client'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'MainApp/Template_Client.html')

class View_Backup_copy_Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        Backup_copy.objects.create(number='1', name='1')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/backup_copy/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('backup_copy'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('backup_copy'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'MainApp/Template_Backup_copy.html')

class View_User_Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(name='1', login='1', password='1')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/user/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('user'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('user'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'MainApp/Template_User.html')
