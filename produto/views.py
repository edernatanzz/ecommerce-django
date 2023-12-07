from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from . import models 

# Create your views here.


class ListaProdutos(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name='produtos'
    paginate_by= 10
    
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