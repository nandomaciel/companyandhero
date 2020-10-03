from .models import Empresa
from rest_framework import serializers, fields

from funcionario.serializers import FuncionarioSerializer

class EmpresaSerializer(serializers.ModelSerializer):
    
    funcionarios = FuncionarioSerializer(many=True, read_only=True)

    class Meta:
        model = Empresa
        fields = ['id', 'nome', 'cnpj', 'funcionarios']

