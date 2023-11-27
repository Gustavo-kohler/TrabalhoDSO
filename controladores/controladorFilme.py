from controladores.controladorGenero import ControladorGenero
from controladores.abstractControladoritens import AbstractControladorItens


class ControladorFilme(AbstractControladorItens):
    def __init__(self, dao, tela, controlador_relatorio, label):
        super().__init__(dao, tela, controlador_relatorio, label)
        self.__controlador_genero = ControladorGenero()

    def gerencia_sistema(self):
        rodando_filmes = True
        while rodando_filmes:
            categoria = self.tela.run_tela_principal()

            if categoria == 'Adicionar Filme':
                self.adiciona_item()
            elif categoria == 'Remover Filme':
                self.remove_item()
            elif categoria == 'Editar Filme':
                self.edita_item()
            elif categoria == 'Vender Filmes':
                self.vende_item()
            elif categoria == 'Adicionar Gêneros':
                self.adiciona_genero()
            elif categoria == 'Inclui Gêneros':
                self.inclui_genero()
            else:
                rodando_filmes = False

    def adiciona_genero(self):
        self.__controlador_genero.adiciona_genero()

    def inclui_genero(self):
        filmes_existentes = []
        filmes_codigos = []
        generos_existentes = []
        generos_codigos = []

        if ((len(self.dao.get_all()) == 0) or (len(self.__controlador_genero.generos()) == 0)):
            motivo = 'Não há filmes e/ou não há gêneros cadastrados.'
            self.tela.popup_nao_funcionou(motivo)
        else:
            for filme in self.dao.get_all():
                generos = [genero.nome["nome"] for genero in filme.generos]
                filme_existente = f'({filme.codigo}) {filme.nome} {generos}'

                filmes_existentes.append(filme_existente)
                filmes_codigos.append(filme.codigo)

            for genero in self.__controlador_genero.generos():
                genero_existente = f'({genero.codigo}) {genero.nome["nome"]}'

                generos_existentes.append(genero_existente)
                generos_codigos.append(genero.codigo)

            inputs = self.tela.run_tela_inclui_genero(
                filmes_existentes, generos_existentes, filmes_codigos, generos_codigos)

            if inputs is not None:
                filme = self.dao.get(inputs['codigo_filme'])
                genero = self.__controlador_genero.get(
                    inputs['codigo_genero'])

                filme.inclui_genero(genero)
                self.dao._DAO__dump()
                self.tela.popup_funcionou()
