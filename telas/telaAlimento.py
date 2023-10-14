from telas.abstractTelaItens import AbstractTelaItens


class TelaAlimento(AbstractTelaItens):
    def imprime_operacoes(self):
        print('1 - Adicionar alimento')
        print('2 - Remover alimento')
        print('3 - Editar alimento')
        print('4 - Listar alimentos')
        print('5 - Vender alimento')

    def escolhe_operacao(self):
        print('Escolha uma operação.')
        return int(input())

    def mostra_itens(self, codigo, nome, preco):
        print(f'{codigo}: {nome} -> {preco}')

    def escolhe_codigo(self):
        return int(input('Insira um código: '))

    def escolhe_nome(self):
        return input('Insira um nome: ')

    def escolhe_preco(self):
        return float(input('Insira um preço: '))

    def escolhe_quantidade(self):
        return int(input('Insira uma quantidade: '))

    def mostra_edicao(self):
        print('1 - Editar preço')
        print('2 - Adiciona adicional')
