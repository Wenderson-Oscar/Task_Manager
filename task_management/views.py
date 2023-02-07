from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa
from .forms import TaskForms

# Create your views here.
def list_task(request):
    task = Tarefa.objects.all()
    return render(request, 'task/list_task.html', {'task': task})

def add_task(request):
    if request.method == "POST":
        form = TaskForms(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            form.save()
            return redirect('detail_task', id=task.id)
    else:
        form = TaskForms()
    return render(request, 'task/add_task.html', {'form': form})

def detail_task(request, id):
    task = get_object_or_404(Tarefa, pk=id)
    return render(request, 'task/detail_task.html', {'task': task})

def edit_task(request, id):
    task = get_object_or_404(Tarefa, pk=id)
    if request.method == "POST":
        form = TaskForms(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            form.save()
            return redirect('detail_task', id=task.id)
    else:
        form = TaskForms(instance=task)
    return render(request, 'task/edit_task.html', {'form': form})

def delete_task(request, id):
    task = get_object_or_404(Tarefa, pk=id)
    task.delete()
    return redirect('list_task')