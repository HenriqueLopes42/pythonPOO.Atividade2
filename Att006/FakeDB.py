from Model import Produto

class FakeDB:
    estoqueProduto = []

    def __init__(self):
        self.GerarBancoProdutos()

    def GerarBancoProdutos(self):
        self.estoqueProduto.append(Produto(1, "Bolacha", 3.20, 9))
        self.estoqueProduto.append(Produto(2, "Arroz 10kg", 15.30, 11))
        self.estoqueProduto.append(Produto(3, "Feijao 1kg", 7.55, 15))
        self.estoqueProduto.append(Produto(4, "Macarrão", 4.75, 4))
        self.estoqueProduto.append(Produto(5, "Óleo", 8.60, 10))

    def VerificaPossuiEstoque(self, codigo, qts):
        for item in self.estoqueProduto:
            if (item.codigo == codigo and item.qtEstoque >= qts):
                return True
        return False

    def retirarDoEstoque(self, codigo, qts):
        for item in self.estoqueProduto:
            if (item.codigo == codigo):
                item.qtEstoque = item.qtEstoque - qts







