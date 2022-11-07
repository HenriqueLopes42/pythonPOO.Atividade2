class Agenda:
    agendaLista = []

    def adicionarNaAgenda(self, contato):
        self.agendaLista.append(contato)

    def RemoverDaAgenda(self, nome):
        for item in self.agendaLista:
            if (nome == item.nome):
                self.agendaLista.remove(item)
                return "Contato deletado com sucesso."
        return "Não foi possivel deletar o contato."


    def ListarAgenda(self):
        for item in self.agendaLista:
            print(f"Nome: {item.nome}. Numero: {item.numero}")
