from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_list_or_404
from .models import Cliente
from .forms import ClienteForm

def home(request):
    return render(request, 'client/home.html')

def register_client(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = ClienteForm()
    return render(request, 'client/register.html', {'form': form})

def authenticate_client(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        id = user.id
        client = get_list_or_404(Cliente, pk=id)
        return render(request, 'client/home.html', {'client': client})
    else:
        return render(request, 'client/home.html')

def login_client(request):
    return render(request, 'client/home.html')

def logout_client(request):
    logout(request)
    return render(request, 'client/home.html')