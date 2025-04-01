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


def add_item(request):
    '''Add item to To Do list'''
    return render(request, 'todo/add_item.html')
