import PySimpleGUI as sg
from telas.abstractTelaItens import AbstractTelaItens
from exceptions.valor_vazio_exception import ValorVazioException
from exceptions.valor_negativo_nulo_exception import ValorNegativoExceptionOuNuloException
from exceptions.valor_ausente_em_lista_exception import ValorAusenteEmListaException


class TelaAlimento(AbstractTelaItens):
    def run_tela_principal(self):
        sg.theme('DarkAmber')
        layout = [
            [
                sg.Button('Adicionar Alimento', size=(18, 1)),
                sg.Button('Remover Alimento', size=(18, 1))
            ],
            [
                sg.Button('Editar Alimento', size=(18, 1)),
                sg.Button('Vender Alimentos', size=(18, 1))
            ],
            [
                sg.Button('Inclui Adicionais', size=(18, 1))
            ]
        ]

        window = sg.Window('CineFalcão').Layout(layout)

        event, not_used_values = window.read()
        if event == sg.WIN_CLOSED:
            window.close()
            return None
        else:
            window.close()
            return event

    def run_tela_inclui_adicional(self, alimentos_existentes, codigos_existentes):
        sg.theme('DarkAmber')
        layout = [
            [
                sg.Text('Inclusão de Adicionais em Alimentos')
            ],
            [
                sg.Listbox(values=alimentos_existentes, size=(40, 10))
            ],
            [
                sg.Text(
                    'Insira o código do alimento que deseja adicionar um adicional.')
            ],
            [
                sg.Text('Além disso, insira o nome de um adicional.')
            ],
            [
                sg.Text('Código do Alimento'), sg.InputText()
            ],
            [
                sg.Text('Adicional'), sg.InputText()
            ],
            [
                sg.Button('Incluir Adicional'), sg.Button('Cancelar')
            ]
        ]

        window = sg.Window('CineFalcão').Layout(layout)

        editando_filme = True
        while editando_filme:
            try:
                event, values = window.read()
                if (event == sg.WIN_CLOSED) or (event == 'Cancelar'):
                    window.close()
                    self.popup_fecha_tela()

                    return None
                elif event == 'Incluir Adicional':
                    # Convertendo str em int, pode gerar um ValueError
                    codigo_alimento = int(values[1])

                    adicional_nome = values[2]

                    # Verificando se o input código é nulo ou negativo
                    self.testa_se_input_negativo(
                        codigo_alimento, 'Código nulo ou negativo não é válido.')

                    # Verificando se o input nome é vazio
                    self.testa_se_input_vazio(
                        adicional_nome, 'Adicional vazio ou com espaços não é válido.')

                    # Verifica se o código informado consta no banco
                    self.teste_se_input_no_banco(
                        codigo_alimento, codigos_existentes, 'O código informado não consta nos registros.')

                    window.close()

                    return {
                        'codigo_alimento': codigo_alimento,
                        'adicional_nome': adicional_nome
                    }

            except ValueError:
                self.popup_nao_funcionou(
                    'Pelo menos um dos valores inseridos para código e para adicional não é válido.')

            except ValorAusenteEmListaException as error:
                self.popup_nao_funcionou(error)

            except ValorVazioException as error:
                self.popup_nao_funcionou(error)

            except ValorNegativoExceptionOuNuloException as error:
                self.popup_nao_funcionou(error)
