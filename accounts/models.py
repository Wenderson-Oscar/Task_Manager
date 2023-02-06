from django.db import models
from django.contrib.auth.models import User

class Cliente(User):

    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino')
    )

    nome = models.CharField(max_length=200, null=False, blank=False)
    sobrenome = models.CharField(max_length=100, null=False, blank=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=False, blank=False)
    nascimento = models.DateField()

    def __str__(self) -> str:
        return self.nome

