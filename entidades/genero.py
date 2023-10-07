

class Genero():
    def __init__(self, nome: str, codigo: int) -> None:
        self.__nome = nome
        self.__codigo = codigo

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def codigo(self) -> int:
        return self.__codigo
