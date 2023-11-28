from django.contrib import admin

from . import models


class VariacoesInline(admin.TabularInline):
    model = models.Variacoes
    extra = 1

class ProdutoAdmin(admin.ModelAdmin):
    inlines = [
        VariacoesInline
    ]

# Register your models here.
admin.site.register(models.Produto, ProdutoAdmin)
admin.site.register(models.Variacoes)
