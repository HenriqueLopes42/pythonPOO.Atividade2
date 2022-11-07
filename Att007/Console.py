from Contato import Contato
from Agenda import Agenda

agenda = Agenda()

op = -1
while (op != 0):
  print('1. Cadastrar contato;')
  print('2. Listar todos os contatos;')
  print('3. Apagar contato;')
  print('0. Sair.')

  op = int(input('Entre com a opção: '))
  print("")

  if op == 1:
    nomeContato = input('Digite o nome:')
    numero = int(input('Digite o numero de telefone:'))
    agenda.adicionarNaAgenda(Contato(nomeContato, numero))

  elif op == 2:
    agenda.ListarAgenda()

  elif op == 3:
    nome = input('Digite o nome para deletar:')
    print(agenda.RemoverDaAgenda(nome))

  elif op == 0:
    print('Encerrando programa.')
    break

  else:
    print('Digite a opção correta!')

  print("")