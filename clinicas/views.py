from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Blog, Produto, Encomenda, Agendamento
from .serializers import AgendamentoSerializer

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


@api_view(['GET'])
def agendamentolist(request):
    agendamentos = Agendamento.objects.all()
    serializer = AgendamentoSerializer(agendamentos, many=True)
    return Response(serializer.data)


@api_view(['POST'])
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
    return render(request, 'clinicas/blog.html', {
        'posts': posts
    })
