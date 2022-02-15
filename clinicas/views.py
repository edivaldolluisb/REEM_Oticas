from django.shortcuts import render
from django.http import JsonResponse
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


def apiOverview(request):
    return JsonResponse('api base point', safe=False)


def agendamento(request):
    # if request.method == 'POST':
    #     print('clicou no submit')
    #     nome = request.POST.get('nome', None)
    #     idade = request.POST.get('idade', None)
    #     morada = request.POST.get('morada', None)
    #     telefone = request.POST.get('telefone', None)
    #     data = request.POST.get('data', None)
    #     print(nome, idade, morada, telefone, data)
    return render(request, 'clinicas/agendamento.html')


def blog(request):
    posts = Blog.objects.all()
    return render(request, 'clinicas/blog.html', {
        'posts': posts
    })
