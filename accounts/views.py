from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.error(request, 'Usuario ou senha invalida.')
        return render(request, 'accounts/cadastro.html')
    else:
        auth.login(request, user)
        messages.error(request, 'voce fez login com sucesso.')
        return redirect('dashbord')


def logout(request):
    auth.logout(request)
    return redirect('dashbord')


def cadastro(request):
    # cadastrando no metado post passando os campos do formulario
    if request.method != 'POST':
        return render(request, 'accounts/cadastro.html')
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')
    # verficando os campos vazio no formulario e passando uma mensagem de aviso que esta vazio
    if not nome or sobrenome or not email or not usuario or not senha or not senha2:
        messages.error(request, 'Campo vazio! nenhum campo nao pode fica vazio')
        return render(request, 'accounts/cadastro.html')
    # tratamento de erro no email
    try:
        validate_email(email)
    except:
        messages.error(request, 'email invalido')
        return render(request, 'accounts/cadastro.html')
    # tratamento de senha se a senha for menor que 6
    if len(senha) < 6:
        messages.error(request, 'senha curta ')
        return render(request, 'accounts/cadastro.html')
    # tratamento de usuario se a senha for menor que 6
    if len(usuario) < 6:
        messages.error(request, 'usuario muito curto ')
        return render(request, 'accounts/cadastro.html')
    # tratamento de senhas iguais as senhas tem que ser igual a senha1  e passando uma mensagem de erro caso nao for
    if senha != senha2:
        messages.error(request, 'senhas não confere ')
        return render(request, 'accounts/cadastro.html')
    # verficcando se o usuario ja existe no banco e passando mensagem
    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'usuario nao existe')
        return render(request, 'accounts/cadastro.html')
    # verficcando se o email ja existe no banco e passando mensagem
    if User.objects.filter(email=email).exists():
        messages.error(request, 'email ja existe')
        return render(request, 'accounts/cadastro.html')
    # mensagem de cadastrp com sucesso
    messages.success(request, 'casdastrado com sucesso')
    # joagando para a tela de login
    user = User.objects.create_user(username=usuario, email=email, password=senha, first_name=nome, last_name=sobrenome)
    user.save()
    return redirect('login')


@login_required(redirect_field_name='login')
def dashbord(request):
    return render(request, 'accounts/dashbord.html')
