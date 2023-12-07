from django.db import models

class Mensalista(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField('Nome *', max_length=50)
    cpf = models.CharField('CPF *', max_length=14)
    valor = models.DecimalField('Valor *', max_digits=8, decimal_places=2)
    data_inicial = models.DateField('Data de início *')
    dia_vencimento = models.IntegerField('Dia de vencimento *')
    cep = models.CharField('CEP', max_length=9, blank=True)
    endereco = models.CharField('Endereço', max_length=255)
    bairro = models.CharField('Bairro', max_length=255)
    cidade = models.CharField('Cidade', max_length=255)
    uf = models.CharField('UF', max_length=2)
    obs = models.TextField('Observações', max_length=500, blank=True)

    def __str__(self):
        return self.nome
