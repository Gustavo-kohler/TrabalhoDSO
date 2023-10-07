

class Cinema():
    def __init__(self, nome: str, cidade: str) -> None:
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise TypeError("O argumento fornecido não é do tipo string.")
        if isinstance(cidade, str):
            self.__cidade = cidade
        else:
            raise TypeError("O argumento fornecido não é do tipo string.")

    @property
    def nome(self):
        return self.__nome

    @property
    def cidade(self):
        return self.__cidade
