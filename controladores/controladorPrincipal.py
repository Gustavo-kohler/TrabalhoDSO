from controladores.controladorCinema import ControladorCinema
from controladores.controladorFilme import ControladorFilme
from controladores.controladorAlimento import ControladorAlimento
from controladores.controladorRelatorio import ControladorRelatorio


class ControladorPrincipal():
    def __init__(self) -> None:
        self.__ctrl_cinema = ControladorCinema()
        self.__ctrl_filme = ControladorFilme()
        self.__ctrl_alimento = ControladorAlimento()
        self.__ctrl_relatorio = ControladorRelatorio()

        self.inicia_sistema()

    def inicia_sistema(self):
        rodando = True

        while rodando:
            operacao = self.__ctrl_cinema.bem_vindo()

            if operacao == 1:
                self.__ctrl_alimento.lista_operacoes()
            elif operacao == 2:
                self.__ctrl_filme.lista_operacoes()
            elif operacao == 3:
                rodando = False

    def fornece_relatorio(self):
        self.__ctrl_relatorio.lista_relatorio()
