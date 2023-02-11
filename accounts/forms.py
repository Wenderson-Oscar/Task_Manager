from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cliente

class ClienteForm(UserCreationForm):
    sexo = forms.ChoiceField(choices=Cliente.SEXO_CHOICES)
    nascimento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

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
