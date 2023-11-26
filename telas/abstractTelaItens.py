from abc import ABC, abstractmethod
import PySimpleGUI as sg
from exceptions.valor_vazio_exception import ValorVazioException
from exceptions.valor_negativo_nulo_exception import ValorNegativoExceptionOuNuloException
from exceptions.valor_ausente_em_lista_exception import ValorAusenteEmListaException


class AbstractTelaItens(ABC):
    @abstractmethod
    def run_tela_principal(self):
        pass

    def testa_se_input_vazio(self, input, message):
        if input.isspace() or input == '':
            raise ValorVazioException(message)

    def testa_se_input_negativo(self, input, message):
        if input <= 0:
            raise ValorNegativoExceptionOuNuloException(message)

    def retira_espaco_input(self, input):
        return input.lstrip()

    def teste_se_input_no_banco(self, input, banco, message):
        if input not in banco:
            raise ValorAusenteEmListaException(message)

    def run_tela_adicionar_item(self, label):
        sg.theme('DarkAmber')
        layout = [
            [sg.Text(f'Cadastro de {label}')],
            [sg.Text(f'Por favor, insira o Nome e Preço do {label}.')],
            [sg.Text('OBS: para preço, insira um valor no formato: "12.1",')],
            [sg.Text('do contrário, o sistema não irá computar.')],
            [sg.Text('Nome'), sg.InputText()],
            [sg.Text('Preço'), sg.InputText()],
            [sg.Button('Cadastrar'), sg.Button('Cancelar')]
        ]

        window = sg.Window('CineFalcão').Layout(layout)

        adicionando_item = True
        while adicionando_item:
            try:
                event, values = window.read()
                if (event == sg.WIN_CLOSED) or (event == 'Cancelar'):
                    window.close()
                    self.popup_fecha_tela()

                    return None
                elif event == 'Cadastrar':
                    nome = values[0]
                    preco = values[1]

                    # Verificando se o input nome é vazio
                    self.testa_se_input_vazio(
                        nome, 'Nome vazio ou com espaços não é válido.')

                    # Verificando se o input preço é vazio
                    self.testa_se_input_vazio(
                        preco, 'Preço vazio ou com espaços não é válido.')

                    # Fazendo a conversão de str para float (pode gerar um ValueError)
                    preco = float(preco)

                    # Verificando se o input preço é negativo
                    self.testa_se_input_negativo(
                        preco, 'Preço é nulo ou negativo não é válido.')

                    # Retirando espaços do início do nome, caso tenha
                    if nome[0] == ' ':
                        nome = self.retira_espaco_input(nome)

                    print(nome)

                    window.close()
                    return {'nome': nome, 'preco': preco}

            except ValueError:
                self.popup_nao_funcionou(
                    'O valor inserido em preço não é valido.')

            except ValorVazioException as error:
                self.popup_nao_funcionou(error)

            except ValorNegativoExceptionOuNuloException as error:
                self.popup_nao_funcionou(error)

    def run_tela_remover_item(self, itens, label):
        sg.theme('DarkAmber')
        layout = [
            [sg.Text(f'Remoção de {label}')],
            [sg.Listbox(values=itens, size=(40, 10))],
            [sg.Text(f'Por favor, insira o código do {label}.')],
            [sg.Text('Código'), sg.InputText()],
            [sg.Button('Remover'), sg.Button('Cancelar')]
        ]

        window = sg.Window('CineFalcão').Layout(layout)

        removendo_item = True
        while removendo_item:
            try:
                event, values = window.read()
                if (event == sg.WIN_CLOSED) or (event == 'Cancelar'):
                    window.close()
                    self.popup_fecha_tela()

                    return None
                elif event == 'Remover':
                    # Convertendo str em int, pode gerar um ValueError
                    codigo = int(values[1])

                    # Verificando se o input código é nulo ou negativo
                    self.testa_se_input_negativo(
                        codigo, 'Código nulo ou negativo não é válido.')

                    window.close()
                    return {'codigo': codigo}

            except ValueError:
                print('Valor inválido para o código.')

            except ValorNegativoExceptionOuNuloException as error:
                self.popup_nao_funcionou(error)

    def run_tela_edita_item(self, itens_existentes, label, codigos_existentes):
        sg.theme('DarkAmber')
        layout = [
            [
                sg.Text(f'Edição de {label}')
            ],
            [
                sg.Listbox(values=itens_existentes, size=(40, 10))
            ],
            [
                sg.Text(
                    f'Insira o código do {label} que deseja editar.')
            ],
            [
                sg.Text('Código'), sg.InputText()
            ],
            [
                sg.Text(
                    f'Além disso, insira um novo nome e o novo preço do {label}.')
            ],
            [
                sg.Text(
                    'Caso não queira alterar algum, coloque um hífen no input: "-"')
            ],
            [
                sg.Text('Novo nome '), sg.InputText()
            ],
            [
                sg.Text('Novo preço'), sg.InputText()
            ],
            [
                sg.Button('Editar'), sg.Button('Cancelar')
            ]
        ]

        window = sg.Window('CineFalcão').Layout(layout)

        editando_item = True
        while editando_item:
            try:
                event, values = window.read()
                if (event == sg.WIN_CLOSED) or (event == 'Cancelar'):
                    window.close()
                    self.popup_fecha_tela()

                    return None
                elif event == 'Editar':
                    # Converte str em int, pode gerar um ValueError
                    codigo_item = int(values[1])

                    novo_nome = values[2]
                    novo_preco = values[3]

                    # Verificando se o input nome é vazio
                    self.testa_se_input_vazio(
                        novo_nome, 'Nome vazio ou com espaços não é válido.')

                    # Retirando espaços do início do nome, caso tenha
                    if novo_nome[0] == ' ':
                        novo_nome = self.retira_espaco_input(novo_nome)

                    # Verificando se o input nome é vazio
                    self.testa_se_input_vazio(
                        novo_preco, 'Preço vazio ou com espaços não é válido.')

                    # Retirando espaços do início do preço, caso tenha
                    if novo_preco[0] == ' ':
                        self.retira_espaco_input(novo_preco)

                    # Verifica se o código informado consta no banco
                    self.teste_se_input_no_banco(
                        codigo_item, codigos_existentes, 'O código informado não consta nos registros.')

                    if values[3] != '-':
                        # Converte str em float, pode gerar um ValueError
                        novo_preco = float(values[3])

                        # Verificando se o input preço é negativo
                        self.testa_se_input_negativo(
                            novo_preco, 'Preço nulo ou negativo não é válido.')

                    window.close()
                    return {
                        'codigo_item': codigo_item,
                        'novo_nome': novo_nome,
                        'novo_preco': novo_preco
                    }

            except ValueError:
                self.popup_nao_funcionou(
                    'Pelo menos um dos valores inseridos para código e para novo preço não é válido.')

            except ValorAusenteEmListaException as error:
                self.popup_nao_funcionou(error)

            except ValorVazioException as error:
                self.popup_nao_funcionou(error)

            except ValorNegativoExceptionOuNuloException as error:
                self.popup_nao_funcionou(error)

    def run_tela_vender_item(self, itens, label, codigos_banco):
        sg.theme('DarkAmber')
        layout = [
            [sg.Text(f'Venda de {label}')],
            [sg.Listbox(values=itens, size=(40, 10))],
            [sg.Text(f'Por favor, insira o código do {label}.')],
            [sg.Text('Código'), sg.InputText()],
            [sg.Text('Quantidade'), sg.InputText()],
            [sg.Button('Vender'), sg.Button('Cancelar')]
        ]

        window = sg.Window('CineFalcão').Layout(layout)

        vendendo_item = True
        while vendendo_item:
            try:
                event, values = window.read()
                if (event == sg.WIN_CLOSED) or (event == 'Cancelar'):
                    window.close()
                    self.popup_fecha_tela()

                    return None
                elif event == 'Vender':
                    # Convertendo str em int, pode gerar um ValueError
                    codigo = int(values[1])

                    # Convertendo str em int, pode gerar um ValueError
                    quantidade = int(values[2])

                    # Verificando se o input código é nulo ou negativo
                    self.testa_se_input_negativo(
                        codigo, 'Código nulo ou negativo não é válido.')

                    # Verificando se o input quantidade é nulo ou negativo
                    self.testa_se_input_negativo(
                        quantidade, 'Quantidade nula ou negativa não é válida.')

                    # Verifica se o código informado consta no banco
                    self.teste_se_input_no_banco(
                        codigo, codigos_banco, 'O código informado não consta nos registros.')

                    window.close()
                    return {'codigo': codigo, 'quantidade': quantidade}

            except ValueError:
                self.popup_nao_funcionou(
                    'Pelo menos um dos valores inseridos para código e para quantidade não é válido.')

            except ValorNegativoExceptionOuNuloException as error:
                self.popup_nao_funcionou(error)

            except ValorAusenteEmListaException as error:
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
