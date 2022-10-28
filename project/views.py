from django.shortcuts import render

# Create your views here.
def cadastro(request):
    return render(request, 'cadastro.html')

def carrinho(request):
    return render(request, 'carrinho.html')