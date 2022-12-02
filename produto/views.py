from django.http import JsonResponse
from carrinho.carrinho import Carrinho
from carrinho.forms import QuantidadeForm
from django.template.defaultfilters import slugify
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from produto.models import Produto
from produto.forms import NomeForm, ProdutoForm
from django.contrib import messages

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
            produto = produto_form.save(commit=False)
            produto.slug = slugify(produto.nome)
            produto.save()
            messages.add_message(request, messages.INFO, 'Produto cadastrado com sucesso!')
    else:
        produto_form = ProdutoForm()
    
    produtos = Produto.objects.all()
    lista_form = []
    for produto in produtos:
        lista_form.append(NomeForm(
            initial={
                'nome': produto.nome,
                'produto_id': produto.id
            }
        ))

    return render(request, 'produto/cadastra_produto.html', {
        "listas": zip(produtos, lista_form), 
        "form": produto_form})

def lista_produtos(request):
    produtos = Produto.objects.all()
    lista_form = []
    for produto in produtos:
        print(produto.nome)
        lista_form.append(NomeForm(
            initial={
                'nome': produto.nome,
                'produto_id': produto.id
            }
        ))
    return render(request, 'produto/lista_produtos.html', {"listas": zip(produtos, lista_form)})

def atualiza_produto(request):
    id = request.body.produto_id
    nome = request.body.nome
    produto = Produto.objects.get(id)
    print(id, nome, produto)
    produto['nome']= nome
    produto.save()
    return JsonResponse({'nome': nome})

def remove_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('produto/cadastra_produto.html')
