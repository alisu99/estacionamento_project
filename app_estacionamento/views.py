from django.shortcuts import render, get_object_or_404, redirect
from .models import Mensalista, Usuario

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
