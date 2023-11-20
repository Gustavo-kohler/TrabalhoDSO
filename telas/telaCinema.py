import PySimpleGUI as sg


class TelaCinema():
    def run_tela_principal(self):
        sg.theme('DarkAmber')

        layout = [
            [sg.Button('Lanchonete')],
            [sg.Button('Filmes')],
            [sg.Button('Relatório')]
        ]

        window = sg.Window('CineFalcão').Layout(layout)

        event, not_used_values = window.read()
        if event == sg.WIN_CLOSED:
            window.close()
            return None
        else:
            window.close()
            return event
