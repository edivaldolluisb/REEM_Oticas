from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Blog, Produto, Encomenda, Agendamento
from .serializers import AgendamentoSerializer, EncomendaSerializer
# paginação
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    return render(request, 'clinicas/index.html')


def produto(request):
    produtos_list = Produto.objects.all()

    # paginação dos produtos
    paginator = Paginator(produtos_list, 10)  # Show * contacts per page
    page = request.GET.get('page')
    produtos = paginator.get_page(page)
    return render(request, 'clinicas/produtos.html', {
        'produtos': produtos
    })


# api do carrinho/encomenda
@api_view(['GET'])
def apiEncomenda(request):
    api_urls = {
        'List': '/encomenda-list/',
        'Detail View': '/encomenda-detail/<str:pk>/',
        'Create': '/encomenda-create/',
        'Update': 'encomenda-update/<str:pk>/',
        'Delete': 'encomenda-delete/<str:pk>/',
    }

    return Response(api_urls)


@api_view(['GET'])  # retorna os agendamentos
def encomendalist(request):
    agendamentos = Encomenda.objects.all()
    serializer = EncomendaSerializer(agendamentos, many=True)
    return Response(serializer.data)


@api_view(['POST'])  # permite adicionar agendamentos na base de dados
def encomendacreate(request):
    serializer = EncomendaSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


def carrinho(request):
    return render(request, 'clinicas/carrinho.html')

# api do agendamento


@api_view(['GET'])
def apiAgendamento(request):
    api_urls = {
        'List': '/agendamento-list/',
        'Detail View': '/agendamento-detail/<str:pk>/',
        'Create': '/agendamento-create/',
        'Update': 'agendamento-update/<str:pk>/',
        'Delete': 'agendamento-delete/<str:pk>/',
    }

    return Response(api_urls)


@api_view(['GET'])  # retorna os agendamentos
def agendamentolist(request):
    agendamentos = Agendamento.objects.all()
    serializer = AgendamentoSerializer(agendamentos, many=True)
    return Response(serializer.data)


@api_view(['POST'])  # permite adicionar agendamentos na base de dados
def agendamentocreate(request):
    serializer = AgendamentoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


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
    
    # paginação dos produtos
    paginator = Paginator(posts, 10)  # Show * contacts per page
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'clinicas/blog.html', {
        'posts': posts
    })
