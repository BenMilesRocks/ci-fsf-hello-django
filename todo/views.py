'''Render HTML pages & handle form requests'''
from django.shortcuts import render, redirect, get_object_or_404
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
    item = get_object_or_404(Item, id=item_id)
    form = ItemForm(instance=item)
    context = {
        'form' : form
    }

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')

    return render(request, 'todo/edit_item.html', context)

def toggle_item(request, item_id): #pylint: disable=unused-argument
    '''Toggle DONE status'''
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect('get_todo_list')

def delete_item(request, item_id): #pylint: disable=unused-argument
    '''Delete task from Database'''
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_todo_list')
