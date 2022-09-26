
# **Projeto** **Agenda** 
Um projeto extremamente simples de Agenda feito com :
Django 3.2.15 e Python 3.10.7.

### Conteúdo educacional
Este  foi projeto criado do   [Curso de Python 3 - Do Básico Ao Avançado (Completo)](https://www.udemy.com/course/python-3-do-zero-ao-avancado/) sem a intenção de 
ser utilizado em produção, mas como recurso educacional.

Isso não impede que você baixe, altere, use e/ou distribua o seu conteúdo conforme preferir.

### Tutorial para iniciantes
Abaixo uma lista de comandos para clonar e configurar este projeto na sua 
máquina local:

**- Instalar git (Windowsc)** 


- **Para** **Windows**:

```
--> criar uma pasta no disco local:
pip install virtualenv

--> cria uma pasta no projeto chamada env:
py -m venv env

--> ativar os projetos com comando 
.\env\scripts\activate

--> depois que entrou no projeto instalar o django com comando dentro da pasta do projeto, 
veja que o projeto esta ativo pois esta (env) no começo do disco
pip install django

--> aqui voçe cria o nome do projeto com comando django-admin startproject loja exemplo eu coloquei como loja 
django-admin startproject loja

-->depois eu acesso a pasta loja
cd loja

--> agora vou cria a aplicaçao da loja com comando py manage.py startapp main
py manage.py startapp main

--> aqui vou dar um start no server vai me indicar qual porta esta meu serviço 
py manage.py runserver

--> aqui vamos usar nosso gerenciador de arquivos com comando ->  py manage.py migrate
py manage.py migrate

--> aqui vc cria seu usuario padrao com comando py manage.py createsuperuser

Pronto!