from django.contrib import admin
from .models import Funcionario

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'username',
        'get_empresas',
    )
    
    fieldsets = (
        ('Informações do funcionario', {'fields': ('nome', 'username')}),
        ('Informações das empresas', {'fields': ('empresas',)})
    )