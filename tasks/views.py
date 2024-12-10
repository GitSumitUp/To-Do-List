from django.shortcuts import redirect, render, get_object_or_404

from django.shortcuts import render
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})  


def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title and not Task.objects.filter(title=title).exists(): 
            Task.objects.create(title=title)
        return redirect('task_list')
    return render(request, 'tasks/add_task.html')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')
