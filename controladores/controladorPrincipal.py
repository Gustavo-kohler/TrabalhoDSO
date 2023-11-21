from controladores.controladorCinema import ControladorCinema
from controladores.controladorFilme import ControladorFilme
from controladores.controladorAlimento import ControladorAlimento
from controladores.controladorRelatorio import ControladorRelatorio

from telas.telaFilme import TelaFilme
from telas.telaAlimento import TelaAlimento

from DAO.dao_filme import daoFilme
from DAO.dao_alimento import daoAlimentos


class ControladorPrincipal():
    def __init__(self) -> None:
        self.__ctrl_relatorio = ControladorRelatorio()
        self.__ctrl_cinema = ControladorCinema()
        self.__ctrl_filme = ControladorFilme(
            daoFilme('filmes.pkl'),
            TelaFilme(),
            self.__ctrl_relatorio,
            'Filme'
        )
        self.__ctrl_alimento = ControladorAlimento(daoAlimentos(
            'alimentos.pkl'),
            TelaAlimento(),
            self.__ctrl_relatorio,
            "Alimento"
        )

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
            elif evento == 'Lanchonete':
                self.__ctrl_alimento.gerencia_sistema()
