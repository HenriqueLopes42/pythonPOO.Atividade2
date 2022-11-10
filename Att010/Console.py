from ContaBancaria import ContaBancaria

conta = ContaBancaria()

print("")
print("Conta para Teste foi inicializada")
print("")

op = -1
while (op != 0):
    print('1. Depositar;')
    print('2. Sacar;')

    print('3. Saldo não formatado;')
    print('4. Saldo formatado;')

    print('5. Data Abertura;')
    print('6. Data abertura Formatado;')

    print('0. Sair.')

    op = int(input('Entre com a opção: '))
    print("")

    if op == 1:
        print(conta.depositar(float(input("Digite um valor a depositar: "))))
    elif op == 2:
        print(conta.sacar(float(input("Digite um valor para sacar: "))))
    elif op == 3:
        print(conta.ObterSaldoAtual())
    elif op == 4:
        print(conta.ObterSaldoFormatado())
    elif op == 5:
        print(conta.ObterDataAbertura())
    elif op == 6:
        print(f"Data: {conta.ObterDataAberturaFormatada()}")
    elif op == 0:
        print('Encerrando programa!')
    else:
        print('Digite a opção valida!')
    print("")