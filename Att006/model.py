class Produto:
    def __init__(self, nome,preco, qtEstoque):
        self.nome = nome
        self.preco = preco
        self.qtEstoque = qtEstoque

class Pedido:
    def __init__(self, compra, quantidade):
        self.compra = compra
        self.quantidade = quantidade

class Compra:
    def __init__(self,item, quantidade):
        self.item = item
        self.quantidade = quantidade

class Estoque:
    def __init__(self,item):
        self.item = item
        self.quantidade = quantidade