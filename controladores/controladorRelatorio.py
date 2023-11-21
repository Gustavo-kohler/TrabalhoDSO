from telas.telaRelatorio import TelaRelatorio
from DAO.dao_relatorio import daoRelatorio


class ControladorRelatorio():
    def __init__(self) -> None:
        self.__tela = TelaRelatorio()
        self.__daoRelatorio = daoRelatorio('relatorios.pkl')

    def gera_relatorio(self):
        relatorios_existentes = []
        total = 0
        if (len(self.__daoRelatorio.get_all()) == 0):
            motivo = 'Não há relatórios cadastrados.'
            self.__tela.popup_nao_funcionou(motivo)
        else:
            for relatorio in self.__daoRelatorio.get_all():

                relatorio_existente = f"({relatorio.codigo}) {relatorio.objeto.nome}: vendida(s) {relatorio.quantidade} unidades(s)."
                relatorios_existentes.append(relatorio_existente)

                total += relatorio.objeto.preco * relatorio.quantidade

            self.__tela.run_tela_gera_relatorio(relatorios_existentes, total)

    def adiciona_relatorio(self, objeto, quantidade):
        self.__daoRelatorio.add(
            len(self.__daoRelatorio.get_all()), objeto, quantidade)
