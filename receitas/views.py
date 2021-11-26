from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Receita

def index(request):
    receitas = Receita.objects.all()

    dados = {
        'receitas': receitas
    }

    return render(request, 'index.html', dados)

def receita(request, id):
    receita = get_object_or_404(Receita, pk=id)

    dados = {
        'receita': receita
    }
    return render(request, 'receita.html', dados)
