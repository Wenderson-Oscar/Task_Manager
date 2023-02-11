from django import forms
from .models import Tarefa

class TaskForms(forms.ModelForm):

    class Meta:
        model = Tarefa
        fields = ('titulo','descricao','status')

        widgets = {
            'titulo': forms.TextInput(attrs={ 'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={ 'class': 'form-control'}),
        }