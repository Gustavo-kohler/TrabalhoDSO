from telas.telaCinema import TelaCinema
from entidades.cinema import Cinema


class ControladorCinema():
    def __init__(self) -> None:
        self.__tela = TelaCinema()
        self.__cinema = Cinema("CineFalcão", "Florianópolis")

    def bem_vindo(self):
        self.__tela.chama_bem_vindo(self.__cinema.nome,
                                    self.__cinema.cidade)
        return self.__tela.escolhe_operacao()
