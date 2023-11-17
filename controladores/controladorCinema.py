from telas.telaCinema import TelaCinema
from entidades.cinema import Cinema


class ControladorCinema():
    def __init__(self) -> None:
        self.__tela_cinema = TelaCinema()
        self.__evento = None

    @property
    def evento(self) -> str:
        return self.__evento

    def gerencia_tela_principal(self) -> None:
        self.__evento = self.__tela_cinema.run_tela_principal()
