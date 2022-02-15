from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('produto/', views.produto, name='produto'),
    path('carrinho/', views.carrinho, name='carrinho'),
    path('agendamento/', views.agendamento, name='agendamento'),
    path('blog/', views.blog, name='blog'),
    path('api/', views.apiOverview, name='api-overview'),
]

