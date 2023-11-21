from telas.abstractTelaItens import AbstractTelaItens
import PySimpleGUI as sg


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

    def run_tela_inclui_adicional(self, alimentos_existentes):
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
                    return None
                elif event == 'Incluir Adicional':
                    print(values)
                    codigo_alimento = int(values[1])
                    adicional_nome = values[2]

                    if (adicional_nome.isspace()):
                        raise TypeError

                    window.close()

                    return {
                        'codigo_alimento': codigo_alimento,
                        'adicional_nome': adicional_nome
                    }

            except ValueError:
                print('Valor inválido para o código.')
