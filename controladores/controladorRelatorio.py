from telas.telaRelatorio import TelaRelatorio
from entidades.relatorio import Relatorio


class ControladorRelatorio():
    def __init__(self) -> None:
        self.__tela = TelaRelatorio()
        self.__relatorios = []

    def lista_relatorio(self):
        for relatorio in self.__relatorios:
            self.__tela.mostra_relatorio(
                relatorio.codigo(), relatorio.nome(), relatorio.quantidade())

    def adiciona_relatorio(self, nome, quantidade):
        self.__relatorios.append(
            Relatorio(self.__relatorios.len(), nome, quantidade))
