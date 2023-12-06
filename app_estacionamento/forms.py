from django import forms
from . models import Mensalista

class MensalistaModelForm(forms.ModelForm):
    class Meta:
        model = Mensalista
        fields = ['nome', 'cpf', 'valor', 'data_inicial', 'dia_vencimento', 'cep', 'endereco', 'cidade', 'uf']