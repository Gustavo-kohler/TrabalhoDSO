import PySimpleGUI as sg
from exceptions.valor_vazio_exception import ValorVazioException
from exceptions.valor_negativo_nulo_exception import ValorNegativoExceptionOuNuloException
from exceptions.valor_ausente_em_lista_exception import ValorAusenteEmListaException


class TelaGenero():
    def testa_se_input_vazio(self, input, message):
        if input.isspace() or input == '':
            raise ValorVazioException(message)

    def retira_espaco_input(self, input):
        return input.lstrip()

    def run_tela_genero(self, generos):
        sg.theme('DarkAmber')
        layout = [
            [sg.Text('ADIÇÃO DE GÊNERO')],
            [sg.Listbox(values=generos, size=(40, 10))],
            [sg.Text('Por favor, insira o nome do gênero.')],
            [sg.Text('Nome'), sg.InputText()],
            [sg.Button('Adicionar genero'), sg.Button('Cancelar')]
        ]

        window = sg.Window('CineFalcão').Layout(layout)

        adicionando_genero = True
        while adicionando_genero:
            try:
                event, values = window.read()
                if (event == sg.WIN_CLOSED) or (event == 'Cancelar'):
                    window.close()
                    self.popup_fecha_tela()

                    return None
                elif event == 'Adicionar genero':
                    nome = values[1]

                    # Verificando se o input nome é vazio
                    self.testa_se_input_vazio(
                        nome, 'Nome vazio ou com espaços não é válido.')

                    # Retirando espaços do início do nome, caso tenha
                    if nome[0] == ' ':
                        nome = self.retira_espaco_input(nome)

                    window.close()
                    return {'nome': nome}

            except ValueError:
                self.popup_nao_funcionou(
                    'O valor inserido em preço não é valido.')

            except ValorVazioException as error:
                self.popup_nao_funcionou(error)

    def popup_nao_funcionou(self, motivo: str):
        sg.theme('DarkAmber')
        layout = [
            [sg.Text('Sua operação teve problemas.')],
            [sg.Text(motivo)],
        ]

        window = sg.Window('CineFalcão').Layout(layout)

        event, values = window.read()
        if (event == sg.WIN_CLOSED):
            window.close()

    def popup_funcionou(self):
        sg.theme('DarkAmber')
        layout = [
            [sg.Text('Sua operação teve sucesso!')],
        ]

        window = sg.Window('CineFalcão').Layout(layout)

        event, values = window.read()
        if (event == sg.WIN_CLOSED):
            window.close()

    def popup_fecha_tela(self):
        sg.theme('DarkAmber')
        layout = [
            [sg.Text('Operação cancelada.')],
        ]

        window = sg.Window('CineFalcão').Layout(layout)

        event, values = window.read()
        if (event == sg.WIN_CLOSED):
            window.close()
