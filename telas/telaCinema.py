import PySimpleGUI as sg


class TelaCinema():
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.theme('DarkAmber')
        layout = [
            [sg.Button('Lanchonete')]
            [sg.Button('Filmes')]
            [sg.Button('Relatório')]
        ]
        self.__window = sg.Window('CineFalcão').Layout(layout)

    def run_view(self):
        running = True
        events = ('Lanchonete', 'Filmes', 'Relatórios')
        while running:
            event, values = self.__window.read()
            if event == sg.WIN_CLOSED:
                running = False
            elif event in events:
                return values
        self.__window.close()
