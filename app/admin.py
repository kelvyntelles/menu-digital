from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import UsuarioPerfil, Estabelecimento, CategoriaProduto, Produto

class UsuarioPerfilInline(admin.StackedInline):
    model = UsuarioPerfil
    can_delete = False
    verbose_name_plural = 'Informações do usuário'

# Inline para Estabelecimento no cadastro de usuário
class EstabelecimentoInline(admin.StackedInline):
    model = Estabelecimento
    can_delete = False
    verbose_name_plural = 'Estabelecimento'


# Substitui o UserAdmin padrão e adiciona o inline do Estabelecimento
class CustomUserAdmin(DefaultUserAdmin):
    inlines = (UsuarioPerfilInline, EstabelecimentoInline)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


@admin.register(Estabelecimento)
class EstabelecimentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'usuario', 'is_ativo')
    list_filter = ('is_ativo',)
    search_fields = ('nome', 'usuario__username')
