from django.contrib import admin

# Register your models here.
from .models import Produto, Encomenda, Agendamento, Blog


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')


class EncomendaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'morada')
    list_display_links = ('nome', 'telefone')


class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'data_agendada')


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'cabecalho', 'texto_span')


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Encomenda, EncomendaAdmin)
admin.site.register(Agendamento, AgendamentoAdmin)
admin.site.register(Blog, BlogAdmin)
