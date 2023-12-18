from django.shortcuts import render, get_object_or_404, redirect
from .models import Mensalista
from .forms import MensalistaModelForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django, logout as logout_django
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import csv
from django.http import HttpResponse
from openpyxl import Workbook
from django.utils.formats import date_format
import locale
from openpyxl.styles import Font, Alignment
from datetime import datetime



@login_required(login_url="login/")
def index(request):
    mensalistas = Mensalista.objects.order_by("nome")
    conteudo = {"mensalistas": mensalistas}
    return render(request, "index.html", conteudo)


@login_required(login_url="login/")
def mensalista(request, pk):
    men = get_object_or_404(Mensalista, id=pk)
    conteudo = {"mensalista": men}
    return render(request, "mensalista.html", conteudo)


@login_required(login_url="login/")
def cadastrar_mensalista(request):
    if request.method == "GET":
        return render(request, "cadastro.html")
    else:
        form = MensalistaModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mensalista adicionado com sucesso!")
            form = MensalistaModelForm()
        else:
            messages.error(request, "Não foi possível completar!")
        return redirect("cadastrar_mensalista")


@login_required(login_url="login/")
def order_by_vencimento(request):
    conteudo = {"mensalistas": Mensalista.objects.order_by("dia_vencimento")}
    return render(request, "index.html", conteudo)


@login_required(login_url="login/")
def excluir(request, pk):
    mensalista = Mensalista.objects.filter(pk=pk)
    mensalista.delete()
    return redirect("index")


@login_required(login_url="login/")
def atualizar_mensalista(request, pk):
    if request.method == "GET":
        men = {"mensalista": Mensalista.objects.filter(pk=pk).first()}
        return render(request, "atualizar.html", men)
    else:
        valor = request.POST.get("valor")
        data_inicial = request.POST.get("data_inicial")
        dia_vencimento = request.POST.get("dia_vencimento")
        cep = request.POST.get("cep")
        endereco = request.POST.get("endereco")
        bairro = request.POST.get("bairro")
        cidade = request.POST.get("cidade")
        uf = request.POST.get("uf")
        obs = request.POST.get("obs")
        situacao = request.POST.get("situacao")

        Mensalista.objects.filter(pk=pk).update(
            valor=valor,
            data_inicial=data_inicial,
            dia_vencimento=dia_vencimento,
            cep=cep,
            endereco=endereco,
            bairro=bairro,
            cidade=cidade,
            uf=uf,
            obs=obs,
            situacao=situacao,
        )
    return redirect("index")


def login(request):
    if request.method == "GET":
        return render(request, "login/login.html")
    else:
        usuario = request.POST.get("usuario")
        senha = request.POST.get("senha")
        user = authenticate(request=None, username=usuario, password=senha)
        if user:
            login_django(request, user)
            return redirect("index")
        else:
            messages.error(request, "Usuário não encontrado! Tente novamente")
            return redirect("login")
        

@login_required(login_url='login/')
def usuario(request):
    return render(request, 'usuario.html')


def logout(request):
    logout_django(request)
    return redirect(reverse('login'))


@login_required(login_url='login/')
def to_excel(request):
    locale.setlocale(locale.LC_NUMERIC, 'pt_BR.UTF-8')
    # Criar um objeto Workbook do openpyxl
    workbook = Workbook()
    sheet = workbook.active

    # Adicionar cabeçalhos
    sheet.append(['Nome', 'CPF', 'Valor', 'Venc.', 'Início', 'Observações'])
    for cell in sheet[1]:
        cell.font = Font(bold=True)  # Tornar o texto em negrito
        cell.alignment = Alignment(horizontal='center')


    # Adicionar dados
    dados_tabela = Mensalista.objects.all()
    for linha in dados_tabela:
        data_formatada = date_format(linha.data_inicial, format='SHORT_DATE_FORMAT')
        valor_formatado = locale.format('%.2f', linha.valor, grouping=True)
        sheet.append([linha.nome, linha.cpf, valor_formatado, linha.dia_vencimento, data_formatada, linha.obs])

    # Definir larguras das colunas (ajuste conforme necessário)
    sheet.column_dimensions['A'].width = 30
    sheet.column_dimensions['B'].width = 15
    sheet.column_dimensions['C'].width = 10
    sheet.column_dimensions['D'].width = 6
    sheet.column_dimensions['E'].width = 13
    sheet.column_dimensions['F'].width = 35

    #adicionando a data de download no nome da tabela
    data = datetime.now
    # Criar uma resposta HTTP com o conteúdo do arquivo XLSX
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename=tabela_estacionamento - {data}.xlsx'
    workbook.save(response)

    return response
