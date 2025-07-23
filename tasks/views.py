from django.shortcuts import render, redirect
from .models import Tasks
# Create your views here.


def task_list(request):
    tasks = Tasks.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Tasks.objects.create(title=title)
    return redirect('task_list')


def complete_task(request, task_id):
    task = Tasks.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('task_list')


def delete_task(request, task_id):
    Tasks.objects.get(id=task_id).delete()
    return redirect('task_list')