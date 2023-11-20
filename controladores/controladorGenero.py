from telas.telaGenero import TelaGenero
from entidades.genero import Genero
from DAO.dao_genero import daoGenero as DAO


class ControladorGenero():
    def __init__(self) -> None:
        self.__tela = TelaGenero()
        self.__dao_generos = DAO('generos.pkl')

    def generos(self):
        return self.__dao_generos.get_all()

    def get(self, key):
        return self.__dao_generos.get(key)

    def adiciona_genero(self):
        generos_existentes = []

        for genero in self.__dao_generos.get_all():
            genero_existente = f'({genero.codigo}) {genero.nome["nome"]}'

            generos_existentes.append(genero_existente)

        nome = self.__tela.run_tela_genero(generos_existentes)
        codigo = len(self.__dao_generos.get_all()) + 1

        self.__dao_generos.add(codigo, nome)
