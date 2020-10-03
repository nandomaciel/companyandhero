from django.shortcuts import render
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Funcionario
from .serializers import FuncionarioSerializer


from empresa.models import Empresa

class FuncionariosViewSets(viewsets.ModelViewSet):
    serializer_class = FuncionarioSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']


    def get_queryset(self):
        funcionario = Funcionario.objects.all()
        return funcionario

    def create(self, request,*args, **kwargs):
        data = request.data
        funcionario = Funcionario.objects.create(nome=data["nome"], username=data["username"])
        funcionario.save()

        for empresa in data["empresas"]:
            empresa = Empresa.objects.get(nome=empresa["nome"])
            print(empresa)
            funcionario.empresas.add(empresa)

        serializer = FuncionarioSerializer(funcionario)

        return Response(serializer.data)
