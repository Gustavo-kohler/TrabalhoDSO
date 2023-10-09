from telas.telaAlimento import TelaAlimento
from entidades.alimento import Alimento
from controladores.abstractControladoritens import AbstractControladorItens


class ControladorAlimento(AbstractControladorItens):
    def __init__(self) -> None:
        self.__tela = TelaAlimento()
        self.__alimentos = []

    def lista_operacoes(self):
        self.__tela.imprime_operacoes()
        operacao = self.__tela.escolhe_operacao()

        if operacao == 1:
            self.adiciona_item()
        elif operacao == 2:
            self.remove_item()
        elif operacao == 3:
            self.edita_item()
        elif operacao == 4:
            self.lista_itens()
        elif operacao == 5:
            self.vende_alimento()

    def __busca_alimento(self, codigo: int):
        for alimento in self.__alimentos:
            if alimento.codigo == codigo:
                return alimento

    def adiciona_item(self):
        nome = self.__tela.escolhe_nome()
        preco = self.__tela.escolhe_preco()

        lista_codigos = [alimento.codigo for alimento in self.__alimentos]
        codigo = max(lista_codigos) + 1

        self.__alimentos.append(Alimento(nome, codigo, preco))

    def remove_item(self):
        codigo = self.__tela.escolhe_codigo()
        alimento = self.__busca_alimento(codigo)

        self.__alimentos.remove(alimento)

    def edita_item(self):
        codigo = self.__tela.escolhe_codigo()

        self.__tela.mostra_edicao()
        operacao = self.__tela.escolhe_operacao()

        if operacao == 1:
            self.__busca_alimento(codigo).preco(self.__tela.escolhe_preco)
        elif operacao == 2:
            self.__busca_alimento(codigo).adiciona_adicional(
                self.__tela.escolhe_nome)

    def lista_item(self):
        for alimento in self.__alimentos:
            self.__tela.mostra_iten(
                alimento.codigo(), alimento.nome(), alimento.preco())

    def vende_alimento(self):
        codigo = self.__tela.escolhe_codigo()
        quantidade = self.__tela.escolhe_quantidade()

        alimento = self.__busca_alimento(codigo)

        return alimento.nome(), quantidade
