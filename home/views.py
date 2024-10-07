from django.shortcuts import render,redirect
from .models import Todo
from django.contrib import messages
from.forms import TodoCreateForm,TodoUpdatelForm
def home(request):
    alldata = Todo.objects.all()
    return render(request, 'home.html', {'alldata':alldata})

def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)

    return render(request, 'detail.html', {'todo':todo})

def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.success(request, 'todo deleted successfully', 'success')
    return redirect('home')

def create(request):
    if request.method == 'POST':
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(title=cd['title'], body=cd['body'], created=cd['created'])
            messages.success(request, 'todo created successfully', 'success')
            return redirect('home')
    else:
        pass    
        form = TodoCreateForm()
    return render(request, 'create.html', {'form':form})

def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        form = TodoUpdatelForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'your todo updated successfully', 'success')
            return redirect('detail', todo_id)

    else:
        form = TodoUpdatelForm(instance=todo)
    return render(request, 'update.html', {'form':form})