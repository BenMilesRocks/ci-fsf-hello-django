'''Automated testing'''
from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):
    '''Testing ItemForm class'''

    def test_item_name_is_required(self):
        '''Tests item_name is a required field'''
        form = ItemForm({'name':''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        '''tests that done_field is not required to submit'''
        form = ItemForm({'name':'Item Name'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        '''tests that only name and done are displayed on the form'''
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
