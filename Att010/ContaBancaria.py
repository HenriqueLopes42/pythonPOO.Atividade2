import datetime

class ContaBancaria:
    def __init__(self):
        self.__saldo = float(0.0)
        self.__dataAbertura = datetime.datetime.now()

    def ObterSaldoAtual(self):
        return self.__saldo

    def ObterSaldoFormatado(self):
        return f"R$ {self.__saldo:,.2f}".replace('.','v').replace(',','.').replace('v',',')


    def ObterDataAbertura(self):
        return self.__dataAbertura

    def ObterDataAberturaFormatada(self):
         return self.__dataAbertura.strftime("%d/%m/%y")


    def depositar(self, valorDepositado):
        if (valorDepositado > 0):
            self.__saldo = self.__saldo + valorDepositado
            return f"Valor de R${valorDepositado:.2f} depositado com sucesso."
        return f"Não foi possivel realizar o deposido ."

    def sacar(self, valorDoSaque):
        if (valorDoSaque > 0):
            if ((self.__saldo - valorDoSaque) >= 0):
                self.__saldo = self.__saldo - valorDoSaque
                return f"Valor de R${valorDoSaque:.2f} sacado com sucesso."
        return f"Não foi possivel realizar o saque."




