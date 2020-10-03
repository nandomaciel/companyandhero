from django.db import models

class Empresa(models.Model):
    nome = models.CharField('Nome', max_length=50)
    cnpj = models.CharField('CNPJ', max_length=100, unique=True)

    def __str__(self):
        return self.nome
