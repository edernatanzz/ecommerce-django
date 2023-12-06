from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
# Create your views here.


class ListaProdutos(View):
    def get(self, *args, **kwargs):
        return HttpResponse('listarprodutos')

class DetalheProduto(View):
    def get(self, *args, **kwargs):
        return HttpResponse('detalheproduto')

class AdicionarCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('adicionarcarrinho')

class RemoverCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('removercarrinho')

class Carrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('carrinho')

class Finalizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('finalizar')