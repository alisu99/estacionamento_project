from django.shortcuts import render, get_object_or_404, redirect
from .models import Mensalista
from .forms import MensalistaModelForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required


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
        cep = request.POST.get(
            "cep",
        )
        endereco = request.POST.get("endereco")
        bairro = request.POST.get("bairro")
        cidade = request.POST.get("cidade")
        uf = request.POST.get("uf")
        obs = request.POST.get("obs")

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
        )
    return redirect("index")


def login(request):
    print(request.user)
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

def usuario(request):
    return render(request, 'usuario.html')