from django.db import models
from django.utils import timezone

# Create your models here.


class Produto(models.Model):
    nome = models.CharField(max_length=250)
    preco = models.FloatField
    data_criacao = models.DateTimeField(default=timezone.now)


class Encomenda(models.Model):
    nome = models.CharField(max_length=250)
    telefone = models.PositiveIntegerField
    distrito = models.CharField
    morada = models.CharField  # localidade
    email = models.EmailField
    lista_produtos = models.TextField(verbose_name='Lista de produtos')
    total = models.PositiveSmallIntegerField(verbose_name='Valor total da compra')


class Agendamento(models.Model):
    nome = models.CharField(max_length=250)
    idade = models.PositiveSmallIntegerField
    telefone = models.PositiveIntegerField
    # email = models.EmailField
    data_agendada = models.DateTimeField(default=timezone.now, verbose_name='Data agendada')
    data_criacao = models.DateTimeField(default=timezone.now,
                                        verbose_name='Data da criacao ')


class Blog(models.Model):
    cabecalho = models.CharField(max_length=300)
    corpo = models.TextField
    texo_span = models.CharField(max_length=100)
