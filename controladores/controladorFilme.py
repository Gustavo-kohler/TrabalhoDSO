from telas.telaFilme import TelaFilme
from controladores.controladorGenero import ControladorGenero
from entidades.filme import Filme
from DAO.dao import DAO


class ControladorFilme():
    def __init__(self):
        self.__dao_filmes = DAO('filmes.pkl')
        self.__dao_generos = DAO('generos.pkl')
        self.__tela = TelaFilme()

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
                pass
            elif categoria == 'Listar Filmes':
                pass
            elif categoria == 'Vender Filmes':
                pass
            elif categoria == 'Adicionar Gêneros':
                pass
            elif categoria == 'Listar Gêneros':
                pass
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

            novo_filme = Filme(nome, codigo, preco)

            self.__dao_filmes.add(codigo, novo_filme)

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
        generos_existentes = []

        for filme in self.__dao_filmes.get_all():
            filme_existente = f'({filme.codigo}) {filme.nome}'

            filmes_existentes.append(filme_existente)

        for genero in self.__dao_generos.get_all():
            genero_existente = f'({genero.codigo}) {genero.nome}'

            generos_existentes.append(genero_existente)

        inputs = self.__tela.run_tela_remover_filme(
            filmes_existentes, generos_existentes)

        if inputs is None:
            pass
