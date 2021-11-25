from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    dados = {
        1: 'Lasanha',
        2: 'Bolo de chocolate',
        3: 'Purê de batatass'
    }

    receitas = {
        'nome_das_receitas': dados
    }

    return render(request, 'index.html', receitas)

def receita(request):
    return render(request, 'receita.html')
