from abc import ABC, abstractmethod


class AbstractControladorItens(ABC):
    @abstractmethod
    def __init__(self, dao, tela, controlador_relatorio, label):
        self.__dao = dao
        self.__tela = tela
        self.__controlador_relatorio = controlador_relatorio
        self.__label = label

    @property
    def dao(self):
        return self.__dao

    @property
    def tela(self):
        return self.__tela

    @property
    def controlador_relatorio(self):
        return self.__controlador_relatorio

    @property
    def label(self):
        return self.__label

    @abstractmethod
    def gerencia_sistema(self):
        pass

    def adiciona_item(self):
        inputs = self.__tela.run_tela_adicionar_item(self.__label)

        if not (inputs is None):
            nome = inputs['nome']
            preco = inputs['preco']
            codigo = None

            todos_itens = self.__dao.get_all()

            todos_codigos = [item.codigo for item in todos_itens]

            if len(todos_codigos) == 0:
                codigo = 1
            else:
                codigo = max(todos_codigos) + 1

            self.__dao.add(codigo, nome, preco)

            self.__tela.popup_funcionou()

    def remove_item(self):
        itens_existentes = []
        todos_codigos = []

        for item in self.__dao.get_all():
            item_existente = f'({item.codigo}) {item.nome}'

            itens_existentes.append(item_existente)
            todos_codigos.append(item.codigo)

        inputs = self.__tela.run_tela_remover_item(
            itens_existentes, self.__label, todos_codigos)

        if not (inputs is None):
            codigo = inputs['codigo']

            self.__dao.remove(codigo)

            self.__tela.popup_funcionou()

    def edita_item(self):
        itens_existentes = []
        codigos_existentes = []

        for item in self.__dao.get_all():
            item_existente = f'({item.codigo}) {item.nome}, R$ {item.preco}'

            itens_existentes.append(item_existente)
            codigos_existentes.append(item.codigo)

        inputs = self.__tela.run_tela_edita_item(
            itens_existentes, self.__label, codigos_existentes)

        if not (inputs is None):
            codigo_item = inputs['codigo_item']
            novo_nome = inputs['novo_nome']
            novo_preco = inputs['novo_preco']

            item = self.__dao.get(codigo_item)

            alteracoes = False

            if novo_nome != '-':
                item.nome = novo_nome
                alteracoes = True
            if novo_preco != '-':
                item.preco = novo_preco
                alteracoes = True

            if alteracoes:
                self.__dao._DAO__dump()

            self.__tela.popup_funcionou()

    def vende_item(self):
        itens_existentes = []
        codigos_existentes = []

        for item in self.__dao.get_all():
            item_existente = f'({item.codigo}) {item.nome}, R$ {item.preco}'

            itens_existentes.append(item_existente)
            codigos_existentes.append(item.codigo)

        inputs = self.__tela.run_tela_vender_item(
            itens_existentes, self.__label, codigos_existentes)

        if not (inputs is None):
            codigo = inputs['codigo']
            objeto = self.__dao.get(codigo)
            quantidade = inputs['quantidade']

            self.__controlador_relatorio.adiciona_relatorio(objeto, quantidade)
            self.__tela.popup_funcionou()
