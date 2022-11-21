from django.urls import path
from produto import views


app_name = 'produto'

urlpatterns = [
    path("", views.index, name="index"),
    path("cadastra_produto/", views.cadastra_produto, name="cadastra_produto"),
]