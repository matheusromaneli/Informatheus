from django.urls import path
from produto import views


app_name = 'produto'

urlpatterns = [
    path("", views.index, name="index"),
    path("controle/", views.controle, name="controle"),
    path("cadastra_produto/", views.cadastra_produto, name="cadastra_produto"),
    path("lista_produtos/", views.lista_produtos, name="lista_produtos"),
]