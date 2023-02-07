from django.shortcuts import render, redirect
from .models import Tarefa
from .forms import TaskForms

# Create your views here.
def list_task(request):
    task = Tarefa.objects.all()
    return render(request, 'home.html', {'task': task})

def add_task(request):
    if request.method == "POST":
        form = TaskForms(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            form.save()
            return redirect('home')
    else:
        form = TaskForms()
    return render(request, 'task/add_task.html', {'form': form})

