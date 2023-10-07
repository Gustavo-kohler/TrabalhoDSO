

class Cinema():
    def __init__(self, nome: str, cidade: str) -> None:
        self.__nome = nome
        self.__cidade = cidade

    @property
    def nome(self):
        return self.__nome

    @property
    def cidade(self):
        return self.__cidade
