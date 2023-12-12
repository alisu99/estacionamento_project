from django.shortcuts import render, get_object_or_404, redirect
from . models import Mensalista
from .forms import MensalistaModelForm
from django.contrib import messages

def index(request):
    if str(request.user) == 'AnonymousUser':
        return redirect('admin/') 
    
    else:
        mensalistas = Mensalista.objects.order_by('nome')
        conteudo = {
            "mensalistas": mensalistas
            }
        return render(request, "index.html", conteudo)


def mensalista(request, pk):
    men = get_object_or_404(Mensalista, id=pk)
    conteudo = {"mensalista": men}
    return render(request, "mensalista.html", conteudo)

#função para renderizar apenas
def cadastrar_mensalista(request):
    return render(request, 'cadastro.html')

#função usada depois de renderizar
def cadastrar_mensalista(request):
    if request.method == "POST":
        form = MensalistaModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mensalista adicionado com sucesso!")
            form = MensalistaModelForm()
        else:
            messages.error(request, "Não foi possível completar!")
        return redirect('cadastrar_mensalista')
    else:
        form = MensalistaModelForm()

    context = {
        "form": form
    }
    return render(request, "cadastro.html", context)

def order_by_vencimento(request):
    conteudo = {
        "mensalistas": Mensalista.objects.order_by('dia_vencimento')
    }
    return render(request, "index.html", conteudo)

def excluir(request, pk):
    mensalista = Mensalista.objects.filter(pk=pk)
    mensalista.delete()
    return redirect('index')

def atualizar_mensalista(request, pk):
    men = {
        'mensalista': Mensalista.objects.filter(pk=pk).first()
    }
    return render(request, 'atualizar.html', men)

def atualizar(request, pk):
    mensalista = get_object_or_404(Mensalista, pk=pk)
    if request.method == 'POST':
        "nome = request.POST.get('nome')"
        "cpf = request.POST.get('cpf')"
        valor = request.POST.get('valor')
        data_inicial = request.POST.get('data_inicial')
        dia_vencimento = request.POST.get('dia_vencimento')
        cep = request.POST.get('cep',)
        endereco = request.POST.get('endereco')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        uf = request.POST.get('uf')
        obs = request.POST.get('obs')

        Mensalista.objects.filter(pk=pk).update(valor=valor, data_inicial=data_inicial, dia_vencimento=dia_vencimento, cep=cep, endereco=endereco, bairro=bairro, cidade=cidade, uf=uf, obs=obs)
    return redirect('index')

