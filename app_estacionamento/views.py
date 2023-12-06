from django.shortcuts import render, get_object_or_404, redirect
from . models import Mensalista
from .forms import MensalistaModelForm
from django.contrib import messages

def login(request):
    pass

def index(request):
    conteudo = {
        "mensalistas": Mensalista.objects.all()
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