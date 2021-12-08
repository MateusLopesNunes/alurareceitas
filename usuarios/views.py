from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receita

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(username=nome, password=senha)

            if user is not None:
                auth.login(request, user)
                print('Usuario logado')
                return redirect('dashboard')

    return render(request, 'usuarios/login.html')

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        if campo_em_branco(nome):
            messages.error(request, 'O nome não pode ficar em branco')
            return redirect('cadastro')

        if campo_em_branco(email):
            messages.error(request, 'O email não pode ficar em branco')
            return redirect('cadastro')

        if senhas_nao_sao_iguais(senha, senha2):
            messages.error(request, 'As senhas não são iguais')
            return redirect('cadastro')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Voçê ja possui uma conta')
            return redirect('cadastro')

        if User.objects.filter(username=nome).exists():
            messages.error(request, 'Voçê ja possui uma conta')
            return redirect('cadastro')

        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        messages.success(request, 'Usuário cadastrado com sucesso')

        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        receitas = Receita.objects.order_by('data_receita').filter(pessoa=id)

        dados = {
            'receitas': receitas
        }

        return render(request, 'usuarios/dashboard.html', dados)
    else:
        redirect('index')

def cria_receita(request):
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']
        user = get_object_or_404(User, pk=request.user.id)

        if campo_em_branco(nome_receita):
            messages.error(request, 'O campo nome da receita não pode ficar em branco')
            return redirect('cria_receita')

        if campo_em_branco(ingredientes):
            messages.error(request, 'O campo de ingredientes não pode ficar em branco')
            return redirect('cria_receita')

        if campo_em_branco(modo_preparo):
            messages.error(request, 'O campo modo de preparo não pode ficar em branco')
            return redirect('cria_receita')

        if campo_em_branco(tempo_preparo):
            messages.error(request, 'O campo tempo de preparo não pode ficar em branco')
            return redirect('cria_receita')

        if campo_em_branco(rendimento):
            messages.error(request, 'O campo rendimento não pode ficar em branco')
            return redirect('cria_receita')

        if campo_em_branco(categoria):
            messages.error(request, 'O campo categoria não pode ficar em branco')
            return redirect('cria_receita')

        if campo_em_branco(foto_receita):
            messages.error(request, 'O campo foto da receita não pode ficar em branco')
            return redirect('cria_receita')

        receita = Receita.objects.create(pessoa=user, nome_receita=nome_receita, ingredientes=ingredientes, modo_preparo=modo_preparo, tempo_preparo=tempo_preparo, rendimento=rendimento, categoria=categoria, foto_receita=foto_receita)

        receita.save()
        return redirect('dashboard')
    else:
        return render(request, 'usuarios/cria_receita.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

# utils

def campo_em_branco(campo):
    return not campo.strip()

def senhas_nao_sao_iguais(senha, senha2):
    return senha != senha2