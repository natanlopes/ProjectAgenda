from django.shortcuts import render, get_object_or_404
from .models import Contato
from django.http import Http404
from django.core.paginator import Paginator
from django.db.models import Q,Value
from django.db.models.functions import Concat


# Create your views here.
def index(request):
    contatos = Contato.objects.order_by('-id', 'nome')
    paginator = Paginator(contatos, 20)  # Show 25 contacts per page.
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })


def ver_contato(request, contato_id):
    # contato = Contato.objects.get(id=contato_id)
    contato = get_object_or_404(Contato, id=contato_id)
    if not contato.mostrar:
        raise Http404('Você não está autorizado a visualizar esta página')
    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })


def busca(request):
    termo = request.GET.get('termo')
    if termo is None or not termo:
        raise Http404('Pagina não Encontrada')
    campo = Concat('nome', Value(''), 'sobrenome')
    contatos = Contato.objects.annotate(
        nome_completo=campo).filter(
        Q(nome_completo__icontains=termo) | Q(sobrenome__icontains=termo) | Q(email__icontains=termo) |
        Q(telefone__icontains=termo)
    )
    paginator = Paginator(contatos, 20)  # Show 25 contacts per page.
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/busca.html', {
        'contatos': contatos
    })
