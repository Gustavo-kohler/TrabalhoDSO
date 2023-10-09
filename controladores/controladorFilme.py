from telas.telaFilme import TelaFilme
from controladorGenero import ControladorGenero
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

    def __busca_filme(self, codigo: int):
        for filme in self.__filmes:
            if filme.codigo == codigo:
                return filme

    def adiciona_item(self):
        nome = self.__tela.escolhe_nome()

        lista_codigos = [filme.codigo for filme in self.__filmes]
        codigo = max(lista_codigos) + 1

        self.__filmes.append(Filme(nome, codigo))

    def remove_item(self):
        codigo = self.__tela.escolhe_codigo()
        filme = self.__busca_filme(codigo)

        self.__filmes.remove(filme)

    def edita_item(self):
        self.__ctrl_genero.lista_generos()
        self.__ctrl_genero.adiciona_genero()

    def lista_itens(self):
        pass
