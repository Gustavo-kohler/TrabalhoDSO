import PySimpleGUI as sg


class TelaCinema():
    def run_tela_principal(self):
        categorias = ['Lanchonete', 'Filmes', 'Relatório']

        sg.theme('DarkAmber')
        layout = list()
        for categoria in categorias:
            botao = [sg.Button(categoria)]
            layout.append(botao)
        window = sg.Window('CineFalcão').Layout(layout)

        event, not_used_values = window.read()
        if event == sg.WIN_CLOSED:
            return None
        else:
            return categoria
