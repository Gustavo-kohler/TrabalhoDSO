from telas.telaFilme import TelaFilme
from controladorGenero import ControladorGenero


class ControladorFilme():
    def __init__(self) -> None:
        self.__tela = TelaFilme()
        self.__ctrl_genero = ControladorGenero()
        self.__filmes = []  # type: list

    def lista_operacoes(self):
        self.__tela.imprime_operacoes()
        operacao = self.__tela.escolhe_operacao()

        if operacao == 1:
            self.adiciona_item(self.__filmes)
        elif operacao == 2:
            self.remove_item(self.__filmes)
        elif operacao == 3:
            self.edita_item(self.__filmes)
        elif operacao == 4:
            self.lista_itens(self.__filmes)

    def edita_item(self):
        self.__ctrl_genero.lista_generos()
        self.__ctrl_genero.adiciona_genero()
