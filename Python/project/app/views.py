from django.shortcuts import render, redirect, get_object_or_404
from app.models import Task
from app.forms import TaskForm  # Import the form
from datetime import date

# List all tasks
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)  # Use Django form for validation
        if form.is_valid():
            Task.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                due_date=form.cleaned_data['due_date'] 
            )
            return redirect('task_list')

    else:
        form = TaskForm()

    return render(request, 'task_form.html', {'form': form})

# Here magupdate
def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    form = TaskForm(request.POST or None, initial={
        'title': task.title,
        'description': task.description,
        'due_date': task.due_date
    })

    if request.method == "POST" and form.is_valid():
        task.title = form.cleaned_data['title']
        task.description = form.cleaned_data['description']
        task.due_date = form.cleaned_data['due_date']
        task.save()
        return redirect('task_list')

    return render(request, 'task_form.html', {'form': form})

# D2 mag delete
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.delete()
        return redirect('task_list')

    return render(request, 'task_confirm_delete.html', {'task': task})
