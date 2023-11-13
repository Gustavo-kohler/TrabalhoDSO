from telas.abstractTelaItens import AbstractTelaItens


class TelaAlimento(AbstractTelaItens):
    def imprime_operacoes(self):
        print('\n1 - Adicionar alimento')
        print('2 - Remover alimento')
        print('3 - Editar alimento')
        print('4 - Listar alimentos')
        print('5 - Vender alimento\n')

    def escolhe_operacao(self):
        return input('Escolha uma operação: ')

    def mostra_itens(self, codigo, nome, adicionais, preco):
        print(f"\n{codigo}: {nome} ({adicionais}) -> {preco}")

    def nenhum_alimento(self):
        print("\nNenhum alimento cadastrado.\n")

    def escolhe_codigo(self):
        return int(input('Insira um código: '))

    def escolhe_nome(self):
        return input('Insira um nome: ')

    def escolhe_preco(self):
        return float(input('Insira um preço: '))

    def escolhe_quantidade(self):
        return int(input('Insira uma quantidade: '))

    def mostra_edicao(self):
        print('\n1 - Editar preço')
        print('2 - Adiciona adicional\n')

    def informa_remocao(self):
        print('Item removido com sucesso!')
