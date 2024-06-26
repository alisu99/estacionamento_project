# Generated by Django 5.0 on 2023-12-07 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mensalista',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50, verbose_name='Nome *')),
                ('cpf', models.CharField(max_length=14, verbose_name='CPF *')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Valor *')),
                ('data_inicial', models.DateField(verbose_name='Data de início *')),
                ('dia_vencimento', models.CharField(max_length=2, verbose_name='Dia de vencimento *')),
                ('cep', models.CharField(blank=True, max_length=9, verbose_name='CEP')),
                ('endereco', models.CharField(max_length=255, verbose_name='Endereço')),
                ('bairro', models.CharField(max_length=255, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=255, verbose_name='Cidade')),
                ('uf', models.CharField(max_length=2, verbose_name='UF')),
                ('obs', models.CharField(blank=True, max_length=500, verbose_name='Observações')),
            ],
        ),
    ]
