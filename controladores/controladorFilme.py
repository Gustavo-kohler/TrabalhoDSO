from telas.telaFilme import TelaFilme
from controladores.controladorGenero import ControladorGenero
from DAO.dao_filme import daoFilme as DAO


class ControladorFilme():
    def __init__(self, controlador_relatorio):
        self.__dao_filmes = DAO('filmes.pkl')
        self.__tela = TelaFilme()
        self.__contrlador_relatorio = controlador_relatorio
        self.__controlador_genero = ControladorGenero()

    def gerencia_sistema(self):
        rodando_filmes = True
        while rodando_filmes:
            categoria = self.__tela.run_tela_principal()

            print(categoria)

            if categoria == 'Adicionar Filme':
                self.adiciona_filme()
            elif categoria == 'Remover Filme':
                self.remove_filme()
            elif categoria == 'Editar Filme':
                self.edita_filme()
            elif categoria == 'Vender Filmes':
                self.vende_filme()
            elif categoria == 'Adicionar Gêneros':
                self.adiciona_genero()
            elif categoria == 'Inclui Gêneros':
                self.inclui_genero()
            else:
                rodando_filmes = False

    def adiciona_filme(self):
        inputs = self.__tela.run_tela_adicionar_filme()
        print(inputs)

        if not (inputs is None):
            nome = inputs['nome']
            preco = inputs['preco']
            codigo = None

            todos_filmes = self.__dao_filmes.get_all()

            todos_codigos = [filme.codigo for filme in todos_filmes]

            if len(todos_codigos) == 0:
                codigo = 1
            else:
                codigo = max(todos_codigos) + 1

            self.__dao_filmes.add(codigo, nome, preco)

            self.__tela.popup_funcionou()

        else:
            motivo = 'Você interrompeu o cadastro.'
            self.__tela.popup_nao_funcionou(motivo)

    def remove_filme(self):
        filmes_existentes = []

        for filme in self.__dao_filmes.get_all():
            filme_existente = f'({filme.codigo}) {filme.nome}'

            filmes_existentes.append(filme_existente)

        inputs = self.__tela.run_tela_remover_filme(filmes_existentes)
        print(inputs)

        if inputs is None:
            motivo = 'Você interrompeu o cadastro.'
            self.__tela.popup_nao_funcionou(motivo)
        else:
            codigo = inputs['codigo']
            todos_codigos = [
                filme.codigo for filme in self.__dao_filmes.get_all()]
            if not (codigo in todos_codigos):
                motivo = 'Não existe filme cadastrado com o código informado.'
                self.__tela.popup_nao_funcionou(motivo)
            else:
                self.__dao_filmes.remove(codigo)

                self.__tela.popup_funcionou()

    def edita_filme(self):
        filmes_existentes = []

        for filme in self.__dao_filmes.get_all():
            filme_existente = f'({filme.codigo}) {filme.nome}, R$ {filme.preco}'

            filmes_existentes.append(filme_existente)

        inputs = self.__tela.run_tela_edita_filme(
            filmes_existentes)

        if inputs is None:
            motivo = 'Você interrompeu o cadastro.'
            self.__tela.popup_nao_funcionou(motivo)
        else:
            codigo_filme = inputs['codigo_filme']
            novo_nome = inputs['novo_nome']
            novo_preco = inputs['novo_preco']

            filme = self.__dao_filmes.get(codigo_filme)
            print(type(filme))
            if novo_nome != '-':
                filme.nome = novo_nome
                print(novo_nome)
            if novo_preco != '-':
                filme.preco = novo_preco

    def vende_filme(self):
        filmes_existentes = []

        for filme in self.__dao_filmes.get_all():
            filme_existente = f'({filme.codigo}) {filme.nome}'

            filmes_existentes.append(filme_existente)

        inputs = self.__tela.run_tela_vender_filme(filmes_existentes)
        print(inputs)

        if inputs is None:
            motivo = 'Você interrompeu o cadastro.'
            self.__tela.popup_nao_funcionou(motivo)
        else:
            codigo = inputs['codigo']
            todos_codigos = [
                filme.codigo for filme in self.__dao_filmes.get_all()]
            if not (codigo in todos_codigos):
                motivo = 'Não existe filme cadastrado com o código informado.'
                self.__tela.popup_nao_funcionou(motivo)
            else:
                objeto = self.__dao_filmes.get(codigo)
                quantidade = inputs['quantidade']
                self.__contrlador_relatorio.adiciona_relatorio(
                    [objeto, quantidade])
                self.__tela.popup_funcionou()

    def adiciona_genero(self):
        self.__controlador_genero.adiciona_genero()
        self.__tela.popup_funcionou()

    def inclui_genero(self):
        filmes_existentes = []
        generos_existentes = []

        for filme in self.__dao_filmes.get_all():
            generos = [genero.nome["nome"] for genero in filme.generos]
            filme_existente = f'({filme.codigo}) {filme.nome} {generos}'

            filmes_existentes.append(filme_existente)

        for genero in self.__controlador_genero.generos():
            genero_existente = f'({genero.codigo}) {genero.nome["nome"]}'

            generos_existentes.append(genero_existente)

        inputs = self.__tela.run_tela_inclui_genero(
            filmes_existentes, generos_existentes)

        if inputs is None:
            motivo = 'Você interrompeu o cadastro.'
            self.__tela.popup_nao_funcionou(motivo)
        else:
            filme = self.__dao_filmes.get(inputs['codigo_filme'])
            genero = self.__controlador_genero.get(
                inputs['codigo_genero'])

            filme.inclui_genero(genero)
            self.__dao_filmes._DAO__dump()
            self.__tela.popup_funcionou()
