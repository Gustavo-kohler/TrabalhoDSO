from telas.telaGenero import TelaGenero
from entidades.genero import Genero


class ControladorGenero():
    def __init__(self) -> None:
        self.__tela = TelaGenero()
        self.__generos = []  # type: list

    def lista_generos(self):
        return self.__tela.mostra_generos(self.__generos)

    def busca_genero(self, codigo: int):
        for genero in self.__generos:
            if genero.codigo == codigo:
                return genero

    def adiciona_genero(self):
        nome = self.__tela.escolhe_nome()

        lista_codigos = [genero.codigo for genero in self.__generos]

        if len(lista_codigos) == 0:
            codigo = 1
        else:
            codigo = max(lista_codigos) + 1

        self.__generos.append(Genero(nome, codigo))
