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
                    relatorio.codigo, relatorio.objeto.nome, relatorio.quantidade)
        else:
            self.__tela.nenhum_relatorio()

    def adiciona_relatorio(self, objeto, quantidade):
        self.__relatorios.append(
            Relatorio(len(self.__relatorios), objeto, quantidade))

    def total_vendas(self):
        total = 0
        for relatorio in self.__relatorios:
            total += (relatorio.objeto.preco * relatorio.quantidade)
        self.__tela.mostra_total(total)
