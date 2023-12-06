from django.db import models


class Mensalista(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField('Nome *', max_length=50)
    cpf = models.CharField('CPF *', max_length=11)
    valor = models.DecimalField('Valor *', max_digits=8, decimal_places=2)
    data_inicial = models.DateField('Data de início *')
    dia_vencimento = models.IntegerField('Dia de vencimetno *', null=True)
    cep = models.IntegerField('CEP', null=True)
    endereco = models.CharField('Endereço', max_length=255, null=True)
    cidade = models.CharField('Cidade', max_length=255, null=True)
    uf = models.CharField('UF', max_length=2, null=True)

    def __str__(self):
        return self.nome
