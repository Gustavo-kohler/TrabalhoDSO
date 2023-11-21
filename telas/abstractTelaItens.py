from abc import ABC, abstractmethod
import PySimpleGUI as sg


class AbstractTelaItens(ABC):
    @abstractmethod
    def run_tela_principal(self):
        pass

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
                    return None
                elif event == 'Cadastrar':
                    nome = values[0]
                    preco = values[1]

                    if (nome.isspace()):
                        raise TypeError

                    preco = float(preco)

                    window.close()
                    return {'nome': nome, 'preco': preco}

            except TypeError:
                print('Strings vazias ou com espaços não são válidas.')

            except ValueError:
                print('Valor inválido para o preço.')

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
                    return None
                elif event == 'Remover':
                    codigo = int(values[1])

                    window.close()
                    return {'codigo': codigo}

            except ValueError:
                print('Valor inválido para o código.')

    def run_tela_edita_item(self, itens_existentes, label):
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
                    return None
                elif event == 'Editar':
                    print(values)
                    codigo_item = int(values[1])
                    novo_nome = values[2]

                    if values[3] != '-':
                        novo_preco = float(values[3])
                    else:
                        novo_preco = values[3]

                    if novo_nome.isspace():
                        raise TypeError

                    window.close()
                    return {
                        'codigo_item': codigo_item,
                        'novo_nome': novo_nome,
                        'novo_preco': novo_preco
                    }

            except ValueError:
                print('Valor inválido para o código.')

    def run_tela_vender_item(self, itens, label):
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
                    return None
                elif event == 'Vender':
                    print(values)
                    codigo = int(values[1])
                    quantidade = int(values[2])

                    window.close()
                    return {'codigo': codigo, 'quantidade': quantidade}

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
