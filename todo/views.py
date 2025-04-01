'''Import Django Shortcuts'''
from django.shortcuts import render
# Create your views here.
def get_todo_list(request):
    '''To Do homepage'''
    return render(request, 'todo/todo_list.html')
