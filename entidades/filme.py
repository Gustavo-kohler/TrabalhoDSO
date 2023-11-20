from entidades.genero import Genero


class Filme():
    def __init__(self, nome: str, codigo: int, preco: float) -> None:
        self.__nome = nome
        self.__codigo = codigo
        self.__generos = []  # type: list
        self.__preco = preco

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco: float):
        if isinstance(novo_preco, float):
            self.__preco = novo_preco
        else:
            raise TypeError("O argumento fornecido não é do tipo float.")

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, novo_nome: str) -> None:
        if isinstance(novo_nome, str):
            self.__nome = novo_nome
        else:
            raise TypeError("O argumento fornecido não é do tipo str.")

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, novo_codigo: int) -> None:
        if isinstance(novo_codigo, int):
            self.__codigo = novo_codigo
        else:
            raise TypeError("O argumento fornecido não é do tipo int.")

    @property
    def generos(self) -> list:
        return self.__generos

    def inclui_genero(self, novo_genero) -> None:
        if isinstance(novo_genero, Genero):
            self.__generos.append(novo_genero)
        else:
            raise TypeError("O argumento fornecido não é do tipo Genero.")
