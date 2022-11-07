class Produto:
    def __init__(self, codigo, nome, preco, qtEstoque):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.qtEstoque = qtEstoque


class Pedido:
    def __init__(self):
        self.listaItens = []
        self.formaPagamento = ""

    def adicionarNaLista(self, compra):
        self.listaItens.append(compra)

    def selecionarFormaPagamento(self, tipoPagamento):
        self.formaPagamento = tipoPagamento


class Compra:
    def __init__(self, item, quantidade):
        self.item = item
        self.quantidade = quantidade
