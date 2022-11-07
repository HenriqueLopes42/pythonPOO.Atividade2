from FakeDB import FakeDB

db = FakeDB()


op = -1
while (op != 0):
  print('1. Realizar emprestimo;')
  print('2. Listar todos os Livros;')
  print('3. Finalizar emprestimo;')
  print('0. Sair.')

  op = int(input('Entre com a opção: '))
  print("")

  if op == 1:
    nome = input('Digite o nome da pessoa: ')
    contato = int(input('Digite o contato da pessoa: '))
    codLivro = int(input('Digite o codigo do livro: '))
    dataInicio = input('Digite a data inicio: ')
    dataFim = input('Digite a data fim: ')

    print(db.realizarEmprestimo(nome, contato, codLivro, dataInicio, dataFim))
  elif op == 2:
    db.listarLivros()
  elif op == 3:
    nome = input('Digite o nome da pessoa: ')
    codLivro = int(input('Digite o codigo do livro: '))
    print(db.finalizarEmprestimo(nome, codLivro))

  elif op == 0:
    break

  else:
    print('Digite a opção correta!')

  print("")