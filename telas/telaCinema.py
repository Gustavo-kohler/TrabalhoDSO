import PySimpleGUI as sg


class TelaCinema():
    def run_tela_principal(self):
        sg.theme('DarkAmber')

        layout = [
            [sg.Text('CineFalcão', font=('Arial', 35))],
            [sg.Text('Seja bem-vindo(a).', font=('Arial', 20))],
            [sg.Button('Lanchonete', size=(30, 3))],
            [sg.Button('Filmes', size=(30, 3))],
            [sg.Button('Relatório', size=(30, 3))]
        ]

        window = sg.Window('CineFalcão', size=(270, 300)).Layout(layout)

        event, not_used_values = window.read()
        if event == sg.WIN_CLOSED:
            window.close()
            return None
        else:
            window.close()
            return event
