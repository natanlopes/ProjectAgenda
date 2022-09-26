from django.shortcuts import render,get_object_or_404
from .models import Contato
from django.http import Http404
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    contatos = Contato.objects.all()
    paginator = Paginator(contatos, 20)  # Show 25 contacts per page.
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })


def ver_contato(request, contato_id):
    # contato = Contato.objects.get(id=contato_id)
    contato = get_object_or_404(Contato,id=contato_id)
    if not contato.mostrar:
        raise Http404('Você não está autorizado a visualizar esta página')
    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })
