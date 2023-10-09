

class Relatorio():
    def __init__(self, codigo, nome, quantidade) -> None:
        self.__codigo = codigo
        self.__nome = nome
        self.__quantidade = quantidade

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nome(self):
        return self.__nome

    @property
    def quantidade(self):
        return self.__quantidade
