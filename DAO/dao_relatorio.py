from entidades.relatorio import Relatorio
from DAO.dao import DAO


class daoRelatorio(DAO):
    def __init__(self, datasource='') -> None:
        super().__init__(datasource)

    def add(self, key, objeto, quantidade):
        if key in self.__cache:
            raise KeyError
        self.__cache[key] = Relatorio(key, objeto, quantidade)
        self.__dump()
