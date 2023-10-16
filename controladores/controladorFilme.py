from telas.telaFilme import TelaFilme
from controladores.controladorGenero import ControladorGenero
from entidades.filme import Filme


class ControladorFilme():
    def __init__(self) -> None:
        self.__tela = TelaFilme()
        self.__ctrl_genero = ControladorGenero()
        self.__filmes = []  # type: list

    def lista_operacoes(self):
        self.__tela.imprime_operacoes()
        operacao = self.__tela.escolhe_operacao()

        if operacao == 1:
            self.adiciona_item()
        elif operacao == 2:
            self.remove_item()
        elif operacao == 3:
            self.edita_item()
        elif operacao == 4:
            self.lista_itens()
        elif operacao == 5:
            return self.vende_filme()
        elif operacao == 6:
            self.__ctrl_genero.adiciona_genero()
        elif operacao == 7:
            self.__ctrl_genero.lista_generos()

    def __busca_filme(self, codigo: int):
        for filme in self.__filmes:
            if filme.codigo == codigo:
                return filme
        raise EOFError

    def adiciona_item(self):
        nome = self.__tela.escolhe_nome()

        lista_codigos = [filme.codigo for filme in self.__filmes]

        if len(lista_codigos) == 0:
            codigo = 1
        else:
            codigo = max(lista_codigos) + 1

        self.__filmes.append(Filme(nome, codigo))

    def remove_item(self):
        codigo = self.__tela.escolhe_codigo()
        filme = self.__busca_filme(codigo)

        self.__filmes.remove(filme)

    def vende_filme(self):
        codigo = self.__tela.escolhe_codigo()
        quantidade = self.__tela.escolhe_quantidade()

        filme = self.__busca_filme(codigo)

        return [filme.nome, quantidade]

    def edita_item(self):
        tem_filmes = self.lista_itens()
        if not tem_filmes:
            return False
        filme_codigo = self.__tela.escolhe_codigo()

        tem_generos = self.__ctrl_genero.lista_generos()
        if not tem_generos:
            return False
        genero_codigo = self.__tela.escolhe_codigo()

        filme = self.__busca_filme(filme_codigo)
        genero = self.__ctrl_genero.busca_genero(genero_codigo)

        filme.adiciona_genero(genero)

    def lista_itens(self):
        return self.__tela.mostra_itens(self.__filmes)
