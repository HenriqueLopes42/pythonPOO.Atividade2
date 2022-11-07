from Model import Compra, Pedido
from FakeDB import FakeDB

db = FakeDB()
CarrinhoDeCompra = Pedido()

print("Mercado ATT 1")







def SelecionarUmProduto():
    for item in db.estoqueProduto:
        if (item.qtEstoque > 0):
            print(f"Codigo: {item.codigo} Produto: {item.nome} Valor: R$ {item.preco:.2f} Estoque disponivel: {item.qtEstoque}")

    itemSelecionado = int(input("Digite o codigo produto desejado: "))
    Quantidade = int(input("Digite a quantidade do produto: "))

    if (db.VerificaPossuiEstoque(itemSelecionado, Quantidade)):
        CarrinhoDeCompra.adicionarNaLista(Compra(itemSelecionado, Quantidade))
        db.retirarDoEstoque(itemSelecionado, Quantidade)

    else:
        print("Codigo informado não existe ou quantidade de estoque nao suficiente.")



def finalizarCompra(carrinho):

    if(len(carrinho.listaItens) <= 0):
        print("Carrinho de compra esta vazio.")
        return 3

    print("1. Dinheiro.")
    print("2. Cheque.")
    print("1. Cartao.")

    menuPagamento = int(input("Selecione a forma de pagamento: "))

    if(menuPagamento == 1):
        menuPagamento = "Dinheiro"
    elif(menuPagamento == 2):
        menuPagamento = "Cheque"
    elif(menuPagamento == 3):
        menuPagamento = "Cartao"
    else:
        print("forma de pagamento invalida.")
        return 3

    print("Pagamento Realizado com sucesso")
    return 0






menu = 3
while (menu != 0):
    print("1. Selecioanr um produto")
    print("2. Finalizar compra")
    print("0. Encerrar sem comprar\n")
    menu = int(input("Digite uma opção: "))

    if(menu == 1):
        SelecionarUmProduto()
    elif(menu == 2):
        menu = finalizarCompra(CarrinhoDeCompra)