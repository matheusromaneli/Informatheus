from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from produto.models import Produto


def index(request):
    produto_id = request.GET.get('prod_id')
    if produto_id != None:
        return redirect('produto/modal_compra.html', id = produto_id)
    lista_produtos = Produto.objects.all()
    paginator = Paginator(lista_produtos, 5)
    pagina = request.GET.get('pagina')
    page_obj = paginator.get_page(pagina)

    print (lista_produtos)
    print(pagina)
    return render(request, 'produto/index.html', {"produtos": page_obj})

def modal_compra(request, id):
    produto = get_object_or_404(Produto, pk=id)
    return render (request, 'produto/modal_compra.html', {"item_id": produto.id})