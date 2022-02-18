from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('produto/', views.produto, name='produto'),
    path('pesquisa/', views.pesquisa, name='pesquisa'),  # pesquisa de produtos
    path('carrinho/', views.carrinho, name='carrinho'),
    path('agendamento/', views.agendamento, name='agendamento'),
    path('blog/', views.blog, name='blog'),

    # api para agendamento
    path('api/agendamento/', views.apiAgendamento, name='api-agendamento'),
    path('api/agendamento-list/', views.agendamentolist, name='api-agendamento-list'),
    path('api/agendamento-create/', views.agendamentocreate, name='api-agendamento-create'),
    # api para carrinho/encomenda
    path('api/encomenda/', views.apiEncomenda, name='api-encomenda'),
    path('api/encomenda-list/', views.encomendalist, name='api-encomenda-list'),
    path('api/encomenda-create/', views.encomendacreate, name='api-encomenda-create'),
]

