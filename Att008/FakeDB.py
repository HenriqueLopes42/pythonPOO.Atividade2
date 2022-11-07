from Livro import Livro
from Pessoa import Pessoa
from Emprestimo import Emprestimo

class FakeDB:
    def __init__(self):
        self.estoqueDeLivros = []
        self.emprestimoList = []
        self.pessoasList = []
        self.gerarEstoqueLivro()

    def gerarEstoqueLivro(self):
        self.estoqueDeLivros.append(Livro(1, "Jogador numero 1", 2015))
        self.estoqueDeLivros.append(Livro(2, "O guia do mochileiro das galáxias", 1990))
        self.estoqueDeLivros.append(Livro(3, "Overgeared", 2014))
        self.estoqueDeLivros.append(Livro(4, "Interligados", 2012))
        self.estoqueDeLivros.append(Livro(5, "The Beginning After the End", 2016))


    def realizarEmprestimo(self, nome, contato, codLivro, dataInicio, dataFim):
        pessoaEmprestimo = Pessoa(nome, contato)
        if(pessoaEmprestimo not in self.pessoasList):
            self.pessoasList.append(Pessoa(nome, contato))

        self.emprestimoList.append(Emprestimo(codLivro, nome, dataInicio, dataFim))

        return "Empretimos realizado com sucesso"


    def listarLivros(self):
        for item in self.estoqueDeLivros:
            print(f"Codigo: {item.codigo}  Nome: {item.nome} Ano: {item.ano}")

    def finalizarEmprestimo(self, nome, codLivro):
        for item in self.emprestimoList:
            if(item.NomePessoa == nome and item.codLivro == codLivro):
                self.emprestimoList.remove(item)
                return "Empretimos devolvido com sucesso"
