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

                    if (nome.isspace()):
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

    def run_tela_vender_filme(self, filmes):
        sg.theme('DarkAmber')
        layout = [
            [sg.Text('VENDA DE FILME')],
            [sg.Listbox(values=filmes, size=(40, 10))],
            [sg.Text('Por favor, insira o código do filme.')],
            [sg.Text('Código'), sg.InputText()],
            [sg.Text('Quantidade'), sg.InputText()],
            [sg.Button('Vender Filme'), sg.Button('Cancelar')]
        ]

        window = sg.Window('CineFalcão').Layout(layout)

        vendendo_filme = True
        while vendendo_filme:
            try:
                event, values = window.read()
                if (event == sg.WIN_CLOSED) or (event == 'Cancelar'):
                    window.close()
                    return None
                elif event == 'Vender Filme':
                    print(values)
                    codigo = int(values[1])
                    quantidade = int(values[2])

                    window.close()
                    return {'codigo': codigo, 'quantidade': quantidade}

            except ValueError:
                print('Valor inválido para o código.')

    def run_tela_edita_filme(self, filmes_existentes):
        sg.theme('DarkAmber')
        layout = [
            [
                sg.Text('EDIÇÃO DE FILME')
            ],
            [
                sg.Listbox(values=filmes_existentes, size=(40, 10))
            ],
            [
                sg.Text(
                    'Insira o código do filme que deseja editar.')
            ],
            [
                sg.Text('Código'), sg.InputText()
            ],
            [
                sg.Text('Além disso, insira um novo nome e o novo preço do filme.')
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

        editando_filme = True
        while editando_filme:
            try:
                event, values = window.read()
                if (event == sg.WIN_CLOSED) or (event == 'Cancelar'):
                    window.close()
                    return None
                elif event == 'Editar':
                    print(values)
                    codigo_filme = int(values[1])
                    novo_nome = values[2]
                    novo_preco = float(values[3])

                    if novo_nome.isspace():
                        raise TypeError

                    window.close()
                    return {
                        'codigo_filme': codigo_filme,
                        'novo_nome': novo_nome,
                        'novo_preco': novo_preco
                    }

            except ValueError:
                print('Valor inválido para o código.')

    def run_tela_inclui_genero(self, filmes_existentes, generos_existentes):
        sg.theme('DarkAmber')
        layout = [
            [
                sg.Text('EDIÇÃO DE FILME')
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
                    return None
                elif event == 'Incluir Gênero':
                    print(values)
                    codigo_filme = int(values[2])
                    codigo_genero = int(values[3])

                    window.close()
                    return {
                        'codigo_filme': codigo_filme,
                        'codigo_genero': codigo_genero
                    }

            except ValueError:
                print('Valor inválido para o código.')
