from django.shortcuts import render

# Create your views here.
def index(request):
    titulo = 'Informatheus'
    frase = 'Frase exibida no index.html'
    return render(request, 'index.html', {'frase':frase, 'titulo':titulo})