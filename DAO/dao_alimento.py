from entidades.alimento import Alimento
from DAO.dao import DAO


class daoAlimentos(DAO):
    def __init__(self, datasource='') -> None:
        super().__init__(datasource)

    def add(self, key, nome, preco):
        if key in self.__cache:
            raise KeyError
        self.__cache[key] = Alimento(nome, key, preco)
        self.__dump()
