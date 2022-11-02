from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from carrinho.carrinho import Carrinho
from carrinho.forms import QuantidadeForm
from produto.models import Produto


def index(request):
    produtos = Produto.objects.all()
    paginator = Paginator(produtos, 5)
    pagina = request.GET.get('pagina')
    page_obj = paginator.get_page(pagina)

    print (produtos)
    print(pagina)

    carrinho = Carrinho(request)
    lista_de_forms = []
    for produto in produtos:
        qtd = carrinho.get_quantidade_total(produto.id)
        form = QuantidadeForm(initial={'quantidade': qtd, 'produto_id': produto.id})
        lista_de_forms.append(form)

    return render(request, 'produto/index.html', {"listas": zip(page_obj, lista_de_forms), "produtos": page_obj})