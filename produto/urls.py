from django.urls import path
from . import views


app_name = 'produto'

urlpatterns = [
    path('',views.ListaProdutos.as_view(), name ="Lista" ),
    path('<slug>', views.DetalheProduto.as_view(), name='detalhe'),
    path('adicionarcarrinho/',views.AdicionarCarrinho.as_view(), name="adicionarcarrinho" ),
    path('removerdocarrinho/', views.RemoverCarrinho.as_view(), name="removerdocarrinho"),
    path('carrinho/', views.Carrinho.as_view() , name="carrinho"),
    path('finalizar/', views.Finalizar.as_view() , name="finalizar"),
]