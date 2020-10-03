from .models import Funcionario
from rest_framework import serializers, fields

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ['id', 'nome', 'username', 'empresas']
        depth = 1
