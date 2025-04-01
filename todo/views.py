'''Render HTML pages & handle form requests'''
from django.shortcuts import render, redirect
from .models import Item
# Create your views here.


def get_todo_list(request):
    '''To Do homepage'''
    items = Item.objects.all() #pylint: disable=no-member
    context ={
        'items' : items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    '''Add item to To Do list'''
    if request.method == 'POST':
        name = request.POST.get('item_name') #pylint: disable=undefined-variable
        done = request.POST.get('item_done') #pylint: disable=undefined-variable
        Item.objects.create(name = name, done = done) #pylint: disable=no-member

        return redirect('get_todo_list')
    return render(request, 'todo/add_item.html')
