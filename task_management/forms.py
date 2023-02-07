from django import forms
from .models import Tarefa

class TaskForms(forms.ModelForm):

    class Meta:
        model = Tarefa
        fields = '__all__'