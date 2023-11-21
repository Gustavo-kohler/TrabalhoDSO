from entidades.adicional import Adicional


class Alimento():
    def __init__(self, nome, codigo, preco) -> None:
        self.__nome = nome
        self.__codigo = codigo
        self.__preco = preco
        self.__adicionais = []

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, novo_nome: str):
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
    def preco(self) -> float:
        return self.__preco

    @preco.setter
    def preco(self, novo_preco: float):
        if isinstance(novo_preco, float):
            self.__preco = novo_preco
        else:
            raise TypeError("O argumento fornecido não é do tipo float.")

    @property
    def adicionais(self) -> list:
        return self.__adicionais

    def inclui_adicional(self, nome):
        if isinstance(nome, str):
            self.__adicionais.append(Adicional(nome))
        else:
            raise TypeError("O argumento fornecido não é do tipo str.")
