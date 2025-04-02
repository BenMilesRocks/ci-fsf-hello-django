'''Automated testing'''
from django.test import TestCase
from .models import Item

# Create your tests here.
class TestViews(TestCase):
    '''Testing test suite works'''

    def test_get_todo_list(self):
        '''Test todo list displays correctly'''
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_get_add_item(self):
        '''Test add_item displays correctly'''
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item(self):
        '''Test edit_item displays correctly'''
        item = Item.objects.create(name='Test Item') #pylint: disable=E1101
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_can_add_item(self):
        '''Test new items are added correctly'''
        response = self.client.post('/add', {'name': 'Test Added Item'})
        self.assertRedirects(response, '/')

    def test_can_delete_item(self):
        '''Test selected items are deleteed correctly'''
        item = Item.objects.create(name='Item to be deleted') #pylint: disable=E1101
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/')
        existing_items = Item.objects.filter(id=item.id) #pylint: disable=E1101
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle_item(self):
        '''Test selected items are toggled correctly'''
        item = Item.objects.create(name='Item to be toggled', done=True) #pylint: disable=E1101
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id) #pylint: disable=E1101
        self.assertFalse(updated_item.done)

    def test_can_edit_item(self):
        '''Test edit_item actually changes item details'''
        item = Item.objects.create(name='Test Item') #pylint: disable=E1101
        response = self.client.post(f'/edit/{item.id}', {'name':'Updated Name'})
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id) #pylint: disable=E1101
        self.assertEqual(updated_item.name, 'Updated Name')
