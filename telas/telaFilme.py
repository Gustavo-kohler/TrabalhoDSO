from telas.abstractTelaItens import AbstractTelaItens
import PySimpleGUI as sg
from exceptions.valor_vazio_exception import ValorVazioException
from exceptions.valor_negativo_nulo_exception import ValorNegativoExceptionOuNuloException
from exceptions.valor_ausente_em_lista_exception import ValorAusenteEmListaException


class TelaFilme(AbstractTelaItens):
    def run_tela_principal(self):
        sg.theme('DarkAmber')
        layout = [
            [
                sg.Button('Adicionar Filme', size=(18, 1)),
                sg.Button('Remover Filme', size=(18, 1))
            ],
            [
                sg.Button('Editar Filme', size=(18, 1)),
                sg.Button('Vender Filmes', size=(18, 1))
            ],
            [
                sg.Button('Adicionar Gêneros', size=(18, 1)),
                sg.Button('Inclui Gêneros', size=(18, 1))
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

    def run_tela_inclui_genero(self, filmes_existentes, generos_existentes, codigos_filme, codigos_generos):
        sg.theme('DarkAmber')
        layout = [
            [
                sg.Text('Inclusão de Gênero em Filme')
            ],
            [
                sg.Listbox(values=filmes_existentes, size=(40, 10)),
                sg.Listbox(values=generos_existentes, size=(40, 10))
            ],
            [
                sg.Text(
                    'Insira o código do filme que deseja adicionar um gênero')
            ],
            [
                sg.Text('Além disso, insira o código do gênero que será adicionada.')
            ],
            [
                sg.Text('Código do Filme'), sg.InputText()
            ],
            [
                sg.Text('Código do Gênero'), sg.InputText()
            ],
            [
                sg.Button('Incluir Gênero'), sg.Button('Cancelar')
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
                elif event == 'Incluir Gênero':
                    # Convertendo str em int, pode gerar um ValueError
                    codigo_filme = int(values[2])

                    # Convertendo str em int, pode gerar um ValueError
                    codigo_genero = int(values[3])

                    # Verificando se o input código filme é nulo ou negativo
                    self.testa_se_input_negativo(
                        codigo_filme, 'Código de filme nulo ou negativo não é válido.')

                    # Verificando se o input código gênero é nulo ou negativo
                    self.testa_se_input_negativo(
                        codigo_genero, 'Código de gênero nulo ou negativo não é válido.')

                    # Verifica se o código gênero informado consta no banco
                    self.teste_se_input_no_banco(
                        codigo_filme, codigos_filme, 'O código informado em filme não consta nos registros.')

                    # Verifica se o código filme informado consta no banco
                    self.teste_se_input_no_banco(
                        codigo_genero, codigos_generos, 'O código informado em gênero não consta nos registros.')

                    window.close()
                    return {
                        'codigo_filme': codigo_filme,
                        'codigo_genero': codigo_genero
                    }

            except ValueError:
                self.popup_nao_funcionou(
                    'Pelo menos um dos valores inseridos para código e para quantidade não é válido.')

            except ValorNegativoExceptionOuNuloException as error:
                self.popup_nao_funcionou(error)

            except ValorAusenteEmListaException as error:
                self.popup_nao_funcionou(error)
