from telas.telaGenero import TelaGenero
from entidades.genero import Genero


class controladorGenero():
    def __init__(self) -> None:
        self.__tela = TelaGenero()
        self.__generos = []  # type: list

    def lista_generos(self):
        self.__tela.mostra_generos()

    def __busca_genero(self, codigo: int):
        for genero in self.__generos:
            if genero.codigo == codigo:
                return genero

    def adiciona_genero(self):
        nome = self.__tela.escolhe_nome()

        lista_codigos = [genero.codigo for genero in self.__generos]
        codigo = max(lista_codigos) + 1

        self.__filmes.append(Genero(nome, codigo))
