from django import forms
from .models import Cliente
from django.contrib.auth.forms import UserCreationForm

class ClienteForm(UserCreationForm):

    class Meta:
        model = Cliente
        fields = ('nome','sobrenome','email','sexo','nascimento','username','password1','password2')

        widgets = {
            'nome': forms.TextInput(attrs={ 'class': 'form-control', }),
            'sobrenome': forms.TextInput(attrs={ 'class': 'form-control', }),
            'email': forms.TextInput(attrs={ 'class': 'form-control', }),            
            'sexo': forms.Select(attrs={ 'class': 'form-control', }),
            'nascimento': forms.DateInput(attrs={ 'class': 'form-control', }),                        
            'username': forms.TextInput(attrs={ 'class': 'form-control',}),
            'password1': forms.TextInput(attrs={ 'class': 'form-control',}),
            'password2': forms.TextInput(attrs={ 'class': 'form-control',}),                        
        }

