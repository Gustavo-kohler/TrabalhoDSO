import PySimpleGUI as sg


class TelaGenero():
    def run_tela_genero(self, generos):
        sg.theme('DarkAmber')
        layout = [
            [sg.Text('ADIÇÃO DE GÊNERO')],
            [sg.Listbox(values=generos, size=(40, 10))],
            [sg.Text('Por favor, insira o nome do genero.')],
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
                    return None
                elif event == 'Adicionar genero':
                    print(values)
                    nome = values[1]

                    window.close()
                    return {'nome': nome}

            except ValueError:
                print('Valor inválido para o código.')
