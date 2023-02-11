from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):

    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=False, blank=False)
    nascimento = models.DateField()

    def __str__(self) -> str:
        return self.user.email

