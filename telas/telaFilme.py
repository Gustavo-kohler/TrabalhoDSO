from telas.abstractTelaItens import AbstractTelaItens
import PySimpleGUI as sg


class TelaFilme():
    def run_tela_principal(self):
        # categorias = [
        #     'Adicionar Filme',
        #     'Remover Filme',
        #     'Editar Filme',
        #     'Listar Filmes',
        #     'Vender Filmes',
        #     'Adicionar Gêneros',
        #     'Listar Gêneros'
        # ]

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
                sg.Button('Adicionar Gêneros', size=(18, 1))
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

    def run_tela_adicionar_filme(self):
        sg.theme('DarkAmber')
        layout = [
            [sg.Text('CADASTRO DE FILME')],
            [sg.Text('Por favor, insira o Nome e Preço do Ingresso.')],
            [sg.Text('OBS: para preço, insira um valor no formato: "12.1",')],
            [sg.Text('do contrário, o sistema não irá computar.')],
            [sg.Text('Nome'), sg.InputText()],
            [sg.Text('Preço'), sg.InputText()],
            [sg.Button('Cadastrar'), sg.Button('Cancelar')]
        ]

        window = sg.Window('CineFalcão').Layout(layout)

        adicionando_filme = True
        while adicionando_filme:
            try:
                event, values = window.read()
                if (event == sg.WIN_CLOSED) or (event == 'Cancelar'):
                    window.close()
                    return None
                elif event == 'Cadastrar':
                    nome = values[0]
                    preco = values[1]

                    print(nome)
                    print(preco)

                    big_string = ' ' * 1000

                    if (nome in big_string):
                        raise TypeError

                    preco = float(preco)

                    window.close()
                    return {'nome': nome, 'preco': preco}

            except TypeError:
                print('Strings vazias ou com espaços não são válidas.')

            except ValueError:
                print('Valor inválido para o preço.')

    def run_tela_remover_filme(self, filmes):
        sg.theme('DarkAmber')
        layout = [
            [sg.Text('REMOÇÃO DE FILME')],
            [sg.Listbox(values=filmes, size=(40, 10))],
            [sg.Text('Por favor, insira o código do filme.')],
            [sg.Text('Código'), sg.InputText()],
            [sg.Button('Remover Filme'), sg.Button('Cancelar')]
        ]

        window = sg.Window('CineFalcão').Layout(layout)

        removendo_filme = True
        while removendo_filme:
            try:
                event, values = window.read()
                if (event == sg.WIN_CLOSED) or (event == 'Cancelar'):
                    window.close()
                    return None
                elif event == 'Remover Filme':
                    print(values)
                    codigo = int(values[1])

                    window.close()
                    return {'codigo': codigo}

            except ValueError:
                print('Valor inválido para o código.')

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
