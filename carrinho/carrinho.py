from decimal import Decimal
from produto.models import Produto
from project import settings

class Carrinho(object):

    def __init__(self, request):
        self.session = request.session
        self.carrinho = self.session.get(settings.CARRINHO_SESSION_ID)

        if not self.carrinho:
            self.carrinho = self.session[settings.CARRINHO_SESSION_ID] = {}

    def atualiza(self, id, quantidade):

        produto = Produto.objects.get(id=id)

        if id not in self.carrinho:
            self.carrinho[id] = {'id': id, 'preco': str(produto.valorComDesconto()), 'quantidade': quantidade, 'preco_total': str(produto.valorComDesconto() * quantidade)}
        else:
            self.carrinho[id]['quantidade'] = quantidade
            self.carrinho[id]['preco_total'] = str(Decimal(self.carrinho[id]['preco']) * quantidade)
        
        self.salvar()

    def salvar(self):
        self.session.modified = True

    def remover(self, id):
        if id in self.carrinho:
            del self.carrinho[id]
            self.salvar()

    def get_preco_total(self, id):
        return self.carrinho[id]['preco_total']
    
    def get_quantidade_total(self, id):
        id = str(id)
        if id in self.carrinho:
            return self.carrinho[id]['quantidade']
        else:
            return 0

    def get_preco_carrinho(self):
        return sum(Decimal(item['preco_total']) for item in self.carrinho.values())

    def get_quantidade_carrinho(self):
        return sum(item['quantidade'] for item in self.carrinho.values())

    def get_produtos(self):

        lista=[]
        for item in self.carrinho.values():
            produto = Produto.objects.get(id=item['id'])
            lista.append({'produto': produto,
                          'id': item['id'],
                          'preco': Decimal(item['preco']),
                          'quantidade': item['quantidade'],
                          'preco_total': item['preco_total']})
        
        return lista

    