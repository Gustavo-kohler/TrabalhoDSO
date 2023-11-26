from controladores.abstractControladoritens import AbstractControladorItens

from DAO.dao import DAO


class ControladorAlimento(AbstractControladorItens):
    def __init__(self, dao, tela, controlador_relatorio, label):
        super().__init__(dao, tela, controlador_relatorio, label)

    def gerencia_sistema(self):
        rodando_alimentos = True
        while rodando_alimentos:
            categoria = self.tela.run_tela_principal()

            print(categoria)

            if categoria == 'Adicionar Alimento':
                self.adiciona_item()
            elif categoria == 'Remover Alimento':
                self.remove_item()
            elif categoria == 'Editar Alimento':
                self.edita_item()
            elif categoria == 'Vender Alimentos':
                self.vende_item()
            elif categoria == 'Inclui Adicionais':
                self.inclui_adicional()
            else:
                rodando_alimentos = False

    def inclui_adicional(self):
        alimentos_existentes = []
        codigos_existentes = []

        if (len(self.dao.get_all()) == 0):
            motivo = 'Não há alimentos cadastrados.'
            self.tela.popup_nao_funcionou(motivo)
        else:
            for alimento in self.dao.get_all():
                adicionais = [
                    adicional.nome for adicional in alimento.adicionais]

                alimento_existente = f'({alimento.codigo}) {alimento.nome} {adicionais}'

                codigos_existentes.append(alimento.codigo)

                alimentos_existentes.append(alimento_existente)

            inputs = self.tela.run_tela_inclui_adicional(
                alimentos_existentes, codigos_existentes)

            if not (inputs is None):
                alimento = self.dao.get(inputs['codigo_alimento'])
                adicional = inputs['adicional_nome']

                alimento.inclui_adicional(adicional)
                self.dao._DAO__dump()
                self.tela.popup_funcionou()
