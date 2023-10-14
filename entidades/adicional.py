

class Adicional():
    def __init__(self, nome) -> None:
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome
