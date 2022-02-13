from django.shortcuts import render

from .models import Blog, Produto, Encomenda, Agendamento

# Create your views here.


def index(request):
    return render(request, 'clinicas/index.html')


def produto(request):
    produtos = Produto.objects.all()
    return render(request, 'clinicas/produtos.html', {
        'produtos': produtos
    })


def carrinho(request):
    return render(request, 'clinicas/carrinho.html')


def agendamento(request):
    return render(request, 'clinicas/agendamento.html')


def blog(request):
    return render(request, 'clinicas/blog.html')
