"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""


import django
from django.test import TestCase
from django.urls import reverse,resolve







# TODO: Configure your database in settings.py and sync before running tests.

class SimpleTest(TestCase):
    """Tests for the application views."""

    # Django requires an explicit setup() when running tests in PTVS
    @classmethod
    def setUpClass(cls):
        super(SimpleTest, cls).setUpClass()
        django.setup()
        
        

        #tests item field
    def test_Item(self):
        from .models import Item
        Item.objects.create(item_name='Avi')
        item = Item.objects.get(id=1)
        field_label = item._meta.get_field('item_name').verbose_name
        self.assertEqual(field_label,'item name')


        #checks root url
    def test_root_url_exists(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)


        #checks register url
    def test_register_url_exists(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)

        #checks login url
    def test_login_url_exists(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

        #tests add url
    def test_add_url(self):
         c = self.client
         c.login(username='yuval',password='1234')
         res = c.get('/add/')
         self.assertEqual(res.status_code, 200)

         #tests add function
    def test_add_to_url(self):
        c = self.client
        c.login(username='yuval',password='1234')
        res = c.post('/add/',{'item_name':'Test'})
        self.assertEqual(res.status_code, 200)

        #test if objects really adds to db
    def test_add_to_db(self):
        from .models import Item
        name = Item.objects.create(item_name='Test')
        test = Item.objects.filter(item_name='Test')
        self.assertEqual(name, test[0])

        #test login
    def test_login_url(self):
        c = self.client
        res = c.login(username='yuval',password='1234')
        self.assertEqual(res,True)

        #test edit url
    def test_edit_url(self):
        from .models import Item
        c = self.client
        c.login(username='yuval',password='1234')
        res = c.post('/update/1/')
        self.assertEqual(res.status_code,200)

        #test delete url
    def test_del_url(self):
        from .models import Item
        c = self.client
        c.login(username='yuval',password='1234')
        res = c.get('/delete/1/')
        self.assertEqual(res.status_code,200)


        #test detail url
    def test_detail_url(self):
        from .models import Item
        item = Item.objects.all()
        item = item[0].id
        res = self.client.get(f'/{item}/')
        self.assertEqual(res.status_code,200)