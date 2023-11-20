from controladores.controladorCinema import ControladorCinema
from controladores.controladorFilme import ControladorFilme
from controladores.controladorAlimento import ControladorAlimento
from controladores.controladorRelatorio import ControladorRelatorio


class ControladorPrincipal():
    def __init__(self) -> None:
        self.__ctrl_cinema = ControladorCinema()
        self.__ctrl_filme = ControladorFilme()
        # self.__ctrl_alimento = ControladorAlimento()
        # self.__ctrl_relatorio = ControladorRelatorio()

        self.gerencia_sistema()

    def gerencia_sistema(self):
        sistema_rodando = True
        while sistema_rodando:
            self.__ctrl_cinema.gerencia_tela_principal()
            evento = self.__ctrl_cinema.evento
            print(evento)
            if evento is None:
                sistema_rodando = False
            elif evento == 'Filmes':
                self.__ctrl_filme.gerencia_sistema()
