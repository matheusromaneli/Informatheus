from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from carrinho.carrinho import Carrinho
from carrinho.forms import QuantidadeForm
from produto.forms import ProdutoForm
from produto.models import Produto


def index(request):
    produtos = Produto.objects.all()
    paginator = Paginator(produtos, 3)
    pagina = request.GET.get('pagina')
    page_obj = paginator.get_page(pagina)

    carrinho = Carrinho(request)
    lista_de_forms = []
    for produto in produtos:
        qtd = carrinho.get_quantidade_total(produto.id)
        form = QuantidadeForm(initial={'quantidade': qtd, 'produto_id': produto.id})
        lista_de_forms.append(form)

    paginator_forms = Paginator(lista_de_forms, 3)
    forms_obj = paginator_forms.get_page(pagina)

    return render(request, 'produto/index.html', {"listas": zip(page_obj, forms_obj), "produtos": page_obj})

def cadastra_produto(request):

    if request.POST:
        produto_form = ProdutoForm(request.POST)
        if produto_form.is_valid():
            pass
    else:
        produto_form = ProdutoForm()

    return render(request, 'produto/cadastra_produto.html', {'form': produto_form})