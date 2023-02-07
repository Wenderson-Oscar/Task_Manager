from django.db import models

# Create your models here.
class Tarefa(models.Model):

    STATUS_CHOICES = (
        ('Pendente', 'Pendente'),
        ('Concluído', 'Concluído')
    )

    titulo = models.CharField(max_length=200, null=False, blank=False)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_conclusao = models.DateTimeField(null=True, blank=True)
    status = models.CharField( max_length=10, choices=STATUS_CHOICES, default='Pendente')

    def __str__(self) -> str:
        return self.titulo