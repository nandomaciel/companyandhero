from django.shortcuts import render
from rest_framework import filters
from rest_framework import viewsets

from .models import Empresa
from .serializers import EmpresaSerializer


class EmpresasViewSets(viewsets.ModelViewSet):
    serializer_class = EmpresaSerializer

    def get_queryset(self):
        empresa = Empresa.objects.all()
        return empresa
