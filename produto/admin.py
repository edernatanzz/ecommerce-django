from django.contrib import admin

from . import models


class VariacoesInline(admin.TabularInline):
    model = models.Variacoes
    extra = 1

class ProdutoAdmin(admin.ModelAdmin):
    list_display=['nome', 'descricao_curta',
             'get_preco_formatado', 'get_preco_promocional_formatado']
    inlines = [
        VariacoesInline
    ]

# Register your models here.
admin.site.register(models.Produto, ProdutoAdmin)
admin.site.register(models.Variacoes)
