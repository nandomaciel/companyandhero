from django.db import models
from empresa.models import Empresa


class Funcionario(models.Model):
    nome = models.CharField(max_length=250)
    username = models.CharField(max_length=100, unique=True)
    empresas = models.ManyToManyField(Empresa)

    def __str__(self):
        return self.nome