from telas.telaAlimento import TelaAlimento
from entidades.alimento import Alimento
from controladores.abstractControladoritens import AbstractControladorItens


class ControladorAlimento(AbstractControladorItens):
    def __init__(self) -> None:
        self.__tela = TelaAlimento()
        self.__alimentos = []

    def lista_operacoes(self):
        self.__tela.imprime_operacoes()

        operacao = int(self.__tela.escolhe_operacao())

        if operacao == 1:
            self.adiciona_item()
        elif operacao == 2:
            self.remove_item()
        elif operacao == 3:
            self.edita_item()
        elif operacao == 4:
            self.lista_itens()
        elif operacao == 5:
            return self.vende_alimento()
        else:
            print('Valor inserido não condiz com os disponíveis.')
            print('Tente novamente.')

    def busca_alimento(self, codigo: int):
        for alimento in self.__alimentos:
            if alimento.codigo == codigo:
                return alimento
        raise EOFError

    def adiciona_item(self):
        nome = self.__tela.escolhe_nome()
        preco = self.__tela.escolhe_preco()

        lista_codigos = [alimento.codigo for alimento in self.__alimentos]
        if len(lista_codigos) == 0:
            codigo = 1
        else:
            codigo = max(lista_codigos) + 1

        self.__alimentos.append(Alimento(nome, codigo, preco))

    def remove_item(self):
        codigo = self.__tela.escolhe_codigo()
        alimento = self.busca_alimento(codigo)

        self.__alimentos.remove(alimento)
        self.__tela.informa_remocao()

    def edita_item(self):
        tem_alimento = self.lista_itens()
        if not tem_alimento:
            print('Não há alimentos. Adicione um para usar essa função.')
            return False
        codigo = self.__tela.escolhe_codigo()

        alimento = self.busca_alimento(codigo)

        self.__tela.mostra_edicao()
        operacao = int(self.__tela.escolhe_operacao())

        if operacao == 1:
            novo_preco = self.__tela.escolhe_preco()
            alimento.preco = novo_preco
        elif operacao == 2:
            novo_nome = self.__tela.escolhe_nome()
            alimento.adiciona_adicional(novo_nome)

    def lista_itens(self):
        if len(self.__alimentos) > 0:
            for alimento in self.__alimentos:
                adicionais_str = ''
                if len(alimento.adicionais) > 0:
                    for adicionais in alimento.adicionais:
                        adicionais_str += adicionais.nome + ' '
                else:
                    adicionais_str = '-'

                self.__tela.mostra_itens(
                    alimento.codigo, alimento.nome, adicionais_str, alimento.preco)
        else:
            self.__tela.nenhum_alimento()

    def vende_alimento(self):
        codigo = self.__tela.escolhe_codigo()
        quantidade = self.__tela.escolhe_quantidade()

        alimento = self.busca_alimento(codigo)

        return [alimento, quantidade]
