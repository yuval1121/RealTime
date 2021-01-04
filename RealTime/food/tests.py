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
        

    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        from .models import Item
        self.a = Item(item_name="Hello")
        self.assertEqual(self.a.item_name,"Hello")