from telas.telaRelatorio import TelaRelatorio
from entidades.relatorio import Relatorio


class ControladorRelatorio():
    def __init__(self) -> None:
        self.__tela = TelaRelatorio()
        self.__relatorios = []  # type: list

    def lista_relatorio(self):
        if len(self.__relatorios) > 0:
            for relatorio in self.__relatorios:
                self.__tela.mostra_relatorio(
                    relatorio.codigo, relatorio.nome, relatorio.quantidade)
        else:
            self.__tela.nunhum_relatorio()

    def adiciona_relatorio(self, nome, quantidade):
        self.__relatorios.append(
            Relatorio(len(self.__relatorios), nome, quantidade))
