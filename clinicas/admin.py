from django.contrib import admin

# Register your models here.
from .models import Produto, Encomenda, Agendamento, Blog


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'disponivel')
    search_fields = ('nome', 'preco')
    list_editable = ('preco', 'disponivel')
    list_per_page = 30



class EncomendaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'morada', 'entregue')
    list_display_links = ('nome', 'telefone')
    search_fields = ('nome', 'telefone', 'morada')
    list_editable = ('morada', 'entregue')
    list_per_page = 30


class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'data_agendada', 'finalizado')
    search_fields = ('nome', 'telefone', 'data_agendada',)
    list_editable = ('telefone', 'finalizado')
    list_per_page = 30


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'cabecalho', 'texto_span')
    list_display_links = ('id', 'cabecalho')
    search_fields = ('cabecalho', 'texto_span')
    list_per_page = 30


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Encomenda, EncomendaAdmin)
admin.site.register(Agendamento, AgendamentoAdmin)
admin.site.register(Blog, BlogAdmin)
