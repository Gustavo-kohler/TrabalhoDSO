

class Relatorio():
    def __init__(self, codigo, objeto, quantidade) -> None:
        self.__codigo = codigo
        self.__objeto = objeto
        self.__quantidade = quantidade

    @property
    def codigo(self):
        return self.__codigo

    @property
    def objeto(self):
        return self.__objeto

    @property
    def quantidade(self):
        return self.__quantidade
