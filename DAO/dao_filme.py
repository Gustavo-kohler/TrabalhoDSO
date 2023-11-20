from DAO.dao import DAO
from entidades.filme import Filme


class daoFilme(DAO):
    def __init__(self, datasource='') -> None:
        super().__init__(datasource)

    def add(self, key, nome, preco):
        if key in self._DAO__cache:
            raise KeyError
        self._DAO__cache[key] = Filme(nome, key, preco)
        self._DAO__dump()
