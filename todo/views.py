'''Import Django Shortcuts'''
from django.shortcuts import render
from .models import Item
# Create your views here.


def get_todo_list(request):
    '''To Do homepage'''
    items = Item.objects.all()
    context ={
        'items' : items
    }
    return render(request, 'todo/todo_list.html', context)
