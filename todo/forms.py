'''Form control for ToDo'''
from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    '''Item class form'''
    class Meta:
        '''Item metaclass inheritance'''
        model = Item
        fields = ['name', 'done']
