from django.contrib import admin
from . models import Mensalista, Usuario

@admin.register(Mensalista)
class MensalistasAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'valor', 'dia_vencimento', 'data_inicial']
 
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'email', 'senha']