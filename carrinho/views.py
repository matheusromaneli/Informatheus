from decimal import Decimal
from django.http import HttpResponse
from django.shortcuts import render

from carrinho.carrinho import Carrinho
from carrinho.forms import QuantidadeForm

# Create your views here.
def index(request):
    carrinho = Carrinho(request)

    produtos_carrinho = carrinho.get_produtos()

    valor_carrinho = carrinho.get_preco_carrinho()

    return render(request, 'carrinho/index.html', {
        "has_product": len(produtos_carrinho) > 0, 
        "produtos": produtos_carrinho, 
        "total": valor_carrinho, 
        "frete": "%.2f" % float(valor_carrinho * Decimal(0.2)), 
        "total_frete": "%.2f" % float(valor_carrinho * Decimal(1.2))
    })

def atualiza_carrinho(request):
    form = QuantidadeForm(request.POST)
    if form.is_valid():
        produto_id = form.cleaned_data['produto_id']
        quantidade = form.cleaned_data['quantidade']

        carrinho = Carrinho(request)
        if quantidade == 0:
            carrinho.remover(produto_id)
            preco_total = 0.0
        else:
            carrinho.atualiza(produto_id, quantidade)
            preco_total = carrinho.get_preco_total(produto_id)

        qtd = carrinho.get_quantidade_carrinho()
        preco_carrinho = carrinho.get_preco_carrinho()

        return HttpResponse('Ok')
    else:
        raise ValueError('Erro inesperado ao adicionar um produto ao carrinho')