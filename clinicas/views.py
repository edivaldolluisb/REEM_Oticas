from django.shortcuts import render

from .models import Blog, Produto, Encomenda, Agendamento

# Create your views here.


def index(request):
    return render(request, 'clinicas/index.html')


def produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'clinicas/produtoos.html')
