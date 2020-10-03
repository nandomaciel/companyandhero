from django.db import models
from empresa.models import Empresa


class Funcionario(models.Model):
    nome = models.CharField('Nome', max_length=250)
    username = models.CharField('Username', max_length=100, unique=True)
    empresas = models.ManyToManyField(Empresa)

    def __str__(self):
        return self.nome

    def get_empresas(self):
        return ", ".join([str(e) for e in self.empresas.all()])
