from Pessoa import Pessoa

class FakeDB:
    def __init__(self):
        self.pessoaList = []

    def cadastrarPessoa(self, nome, idade, nomePai, nomeMae):
        for pessoa in self.pessoaList:
            if (pessoa.nome == nome and pessoa.idade == idade):
                return "A pessoa informada ja esta cadastrada."

        self.pessoaList.append(Pessoa(nome, idade, nomePai, nomeMae))
        #TODO cadastrar parentes
        return "Pessoa cadastrada com sucesso."
