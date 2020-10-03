from django.contrib import admin
from .models import Empresa

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'cnpj'
    )
    fieldsets = (
        ('Informações da empresa', {'fields': ('nome', 'cnpj')}),
    )