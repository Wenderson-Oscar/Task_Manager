from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClienteForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def register_client(request):
    """Registra o Cliente no Sistema"""
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

# // Deletar Conta //

@login_required
def confirm_delete_client(request):
    """Processo para confirmar a deletação da conta"""
    client_del = get_object_or_404(User, pk=request.user.id)
    return render(request, 'client/del_client.html', {'del_client': client_del})

@login_required
def delete_client(request):
    """Deleta a Conta"""
    client_del = get_object_or_404(User, pk=request.user.id)
    client_del.delete()
    return redirect('home')