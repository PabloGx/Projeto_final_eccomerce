from django.contrib import admin
from .models import *


class VariacaoInline(admin.TabularInline):
    model = Variacao
    extra = 1


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome','categoria','descricao_curta','get_preco_formatado','get_preco_promocional_formatado']
    inlines = [
        VariacaoInline
    ]


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Variacao)
admin.site.register(Categoria)
