'''Render HTML pages & handle form requests'''
from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm


def get_todo_list(request):
    '''To Do homepage'''
    items = Item.objects.all() #pylint: disable=no-member
    context ={
        'items' : items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    '''Add item to To Do list'''
    form = ItemForm()
    context = {
        'form' : form
    }

    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')

    return render(request, 'todo/add_item.html', context)

def edit_item(request, item_id):
    '''Edit item on To Do list'''

    return render(request, 'todo/edit_item.html')
