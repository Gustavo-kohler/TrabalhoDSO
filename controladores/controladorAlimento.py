from telas.telaAlimento import TelaAlimento
from DAO.dao import DAO


class ControladorAlimento():
    def __init__(self) -> None:
        self.__tela_cinema = TelaAlimento()
        self.__evento = None
        self.__alimentosDAO = DAO()

    @property
    def evento(self) -> str:
        return self.__evento

    def gerencia_tela_principal(self) -> None:
        self.__evento = self.__tela_cinema.run_tela_principal()
