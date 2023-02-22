from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa
from .forms import TaskForms
from accounts.models import Cliente

# Create your views here.
def list_task(request):
    """Lista todas as Tarefas"""
    task = Tarefa.objects.filter(user__user=request.user.id)
    return render(request, 'task/list_task.html', {'task': task})

def add_task(request):
    """Adiciona Tarefas"""
    cliente = Cliente.objects.get(user__id=request.user.id)
    if request.method == "POST":
        form = TaskForms(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = cliente
            task.save()
            return redirect('detail_task', id=task.id)
    else:
        form = TaskForms()
    return render(request, 'task/add_task.html', {'form': form})

def task_completed(request, id):
    """Conclue a Tarefa Selecionada"""
    task_compl = get_object_or_404(Tarefa, pk=id)
    task_compl.status = "Concluído"
    task_compl.save()
    return redirect('list_task')

def detail_task(request, id):
    """Detalhar as Tarefas"""
    task = get_object_or_404(Tarefa, pk=id)
    return render(request, 'task/detail_task.html', {'task': task})

def edit_task(request, id):
    """Edita as Tarefas"""
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
    """Delete as Tarefas"""
    task = get_object_or_404(Tarefa, pk=id)
    task.delete()
    return redirect('list_task')

# // TRATANDO PÁGINA DE ERRO / confirmação_submit //

def handler404(request, exception):
    return render(request, 'page_error/error_404.html')

def process_task(request):
    pass