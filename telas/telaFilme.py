from telas.abstractTelaItens import AbstractTelaItens
import PySimpleGUI as sg


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

    def run_tela_inclui_genero(self, filmes_existentes, generos_existentes):
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
