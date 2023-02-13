from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cliente

class ClienteForm(UserCreationForm):
    sexo = forms.ChoiceField(choices=Cliente.SEXO_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    nascimento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'format': 'dd/mm/yyyy'}))
    email = forms.EmailField(required=True, help_text='Obrigatório', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


    def save(self):
        user = super().save(commit=False)
        user.save()
        cliente = Cliente.objects.create(
            user=user,
            sexo=self.cleaned_data.get('sexo'),
            nascimento=self.cleaned_data.get('nascimento')
        )
        return user
