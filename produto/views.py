from django.shortcuts import render

from produto.models import Produto


def index(request):
    lista_produtos = Produto.objects.all()
    
    return render(request, 'produto/index.html', {"produtos": lista_produtos})