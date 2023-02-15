from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_list_or_404
from .models import Cliente
from .forms import ClienteForm
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'home.html')

def register_client(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = ClienteForm()
    return render(request, 'client/register.html', {'form': form})
        
def authenticate_client(request):
    """Autenticar o Cliente"""
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('list_task')
    else:
        return render(request, 'home.html')

def login_client(request):
    return render(request, 'home.html')

def logout_client(request):
    logout(request)
    return render(request, 'home.html')