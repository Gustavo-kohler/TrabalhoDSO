from PySimpleGUI import PySimpleGUI as sg


class TelaRelatorio():
    def run_tela_gera_relatorio(self, relatorios_existentes, total_vendas):
        sg.theme('DarkAmber')
        layout = [
            [sg.Text('Relatórios existentes:')],
            [sg.Listbox(values=relatorios_existentes, size=(40, 10))],
            [sg.Text(f'Total de vendas: R${total_vendas:.2f}')],
            [sg.Button('Voltar')]
        ]
        print(relatorios_existentes)
        window = sg.Window('CineFalcão', layout)

        window.read()
        window.close()
        return None

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
            return None
