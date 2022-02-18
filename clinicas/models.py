from django.db import models
from django.utils import timezone

# Create your models here.


class Produto(models.Model):
    nome = models.CharField(max_length=250)
    preco = models.FloatField(default=0.0)
    imagem = models.ImageField(blank=True)
    data_criacao = models.DateTimeField(default=timezone.now, blank=True)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Encomenda(models.Model):
    nome = models.CharField(max_length=250)
    telefone = models.PositiveIntegerField(blank=True, null=True)
    distrito = models.CharField(max_length=20, blank=True)
    morada = models.CharField(max_length=300, default='Sem morada')  # localidade
    email = models.EmailField(blank=True)
    lista_produtos = models.TextField(verbose_name='Lista de produtos')
    total = models.PositiveSmallIntegerField(verbose_name='Valor total da compra')  # editable=False
    entregue = models.BooleanField(default=False)

    def __str__(self):
        return self.nome


class Agendamento(models.Model):
    nome = models.CharField(max_length=250)
    idade = models.PositiveSmallIntegerField(null=True, blank=True)
    morada = models.CharField(max_length=300, default='Sem morada')  # localidade
    telefone = models.PositiveIntegerField(blank=True, null=True)
    email = models.EmailField(blank=True)
    data_agendada = models.DateTimeField(default=timezone.now, verbose_name='Data agendada')
    data_criacao = models.DateTimeField(default=timezone.now, verbose_name='Data da criacao ')
    finalizado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome


class Blog(models.Model):
    cabecalho = models.CharField(max_length=300)
    corpo = models.TextField(blank=True)
    texto_span = models.CharField(max_length=100)

    def __str__(self):
        return self.cabecalho