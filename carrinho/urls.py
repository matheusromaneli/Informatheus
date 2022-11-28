from django.urls import path
from carrinho import views


app_name = 'carrinho'

urlpatterns = [
    path("", views.index, name="index"),
    path("atualiza_carrinho/", views.atualiza_carrinho, name='atualiza_carrinho'),
    path("lista_produtos/", views.lista_produtos, name="lista_produtos"),
]