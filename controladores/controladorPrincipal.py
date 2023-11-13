from controladores.controladorCinema import ControladorCinema
from controladores.controladorFilme import ControladorFilme
from controladores.controladorAlimento import ControladorAlimento
from controladores.controladorRelatorio import ControladorRelatorio


class ControladorPrincipal():
    def __init__(self) -> None:
        self.__ctrl_cinema = ControladorCinema()
        self.__ctrl_filme = ControladorFilme()
        self.__ctrl_alimento = ControladorAlimento()
        self.__ctrl_relatorio = ControladorRelatorio()

        self.inicia_sistema()

    def inicia_sistema(self):
        rodando = True

        while rodando:
            try:
                operacao = self.__ctrl_cinema.bem_vindo()

                operacao = int(operacao)

                if operacao == 1:
                    self.gera_relatorio(self.__ctrl_alimento.lista_operacoes())
                elif operacao == 2:
                    self.gera_relatorio(self.__ctrl_filme.lista_operacoes())
                elif operacao == 3:
                    self.__ctrl_relatorio.lista_relatorio()
                elif operacao == 4:
                    self.__ctrl_relatorio.total_vendas()
                elif operacao == 5:
                    rodando = False
                else:
                    print('Valor inserido não condiz com os disponíveis.')
                    print('Tente novamente.')
            except ValueError:
                print('Valor inserido apresenta incompatibilidade de tipo.')
                print('Tente novamente.')
            except EOFError:
                print('Não foi encontrado o valor.')
            except KeyboardInterrupt:
                print('\nHouve uma tentativa de interromper o programa.')
                print('Retornando ao menu principal...')

    def fornece_relatorio(self):
        self.__ctrl_relatorio.lista_relatorio()

    def gera_relatorio(self, metodo):
        retorno = metodo
        if isinstance(retorno, list):
            self.__ctrl_relatorio.adiciona_relatorio(retorno[0], retorno[1])
