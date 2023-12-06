from django.contrib import admin
from . models import Mensalista

@admin.register(Mensalista)
class MensalistasAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'valor', 'dia_vencimento', 'data_inicial']
 