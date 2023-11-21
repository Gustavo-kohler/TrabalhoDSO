from entidades.genero import Genero
from DAO.dao import DAO


class daoGenero(DAO):
    def __init__(self, datasource='') -> None:
        super().__init__(datasource)

    def add(self, key, nome):
        if key in self._DAO__cache:
            raise KeyError
        self._DAO__cache[key] = Genero(nome, key)
        self._DAO__dump()
