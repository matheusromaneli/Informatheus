from django.urls import path
from carrinho import views


app_name = 'carrinho'

urlpatterns = [
    path("", views.index, name="index"),
]