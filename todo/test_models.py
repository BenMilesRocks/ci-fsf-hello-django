'''Automated testing'''
from django.test import TestCase
from .models import Item

class TestModels(TestCase):
    '''Test models.py behaviours'''

    def test_done_defaults_to_false(self):
        '''Test done field defaults to False'''
        item = Item.objects.create(name='Test Todo Item') #pylint: disable=E1101
        self.assertFalse(item.done)

    def test_item_string_method(self):
        '''Test string method for Item class'''
        item = Item.objects.create(name='Test Todo Item') #pylint: disable=E1101
        self.assertEqual(str(item),'Test Todo Item')
