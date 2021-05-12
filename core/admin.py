from django.contrib import admin

from .models import Cargo, Servico, Equipe, Adicionais

# Configurando a página de admin


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificado')


@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'modificado', 'ativo')


@admin.register(Adicionais)
class AdicionaisAdmin(admin.ModelAdmin):
    list_display = ('nome', 'icone', 'ativo', 'modificado')
