from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('produto/', views.produto, name='produto'),
    path('carrinho/', views.carrinho, name='carrinho'),
    path('agendamento/', views.agendamento, name='agendamento'),
    path('blog/', views.blog, name='blog'),
    path('api/agendamento', views.apiAgendamento, name='api-agendamento'),
    path('api/agendamento-list/', views.agendamentolist, name='api-agendamento-list'),
    path('api/agendamento-create/', views.agendamentocreate, name='api-agendamento-create'),
]

