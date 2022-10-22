from django.shortcuts import render


def index(request):
    frase = 'essa pagina é do produto'
    titulo = 'Produtos'
    return render(request, 'produto/index.html', {'frase':frase, 'titulo':titulo})