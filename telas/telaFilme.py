from telas.abstractTelaItens import AbstractTelaItens


class TelaFilme(AbstractTelaItens):
    def imprime_operacoes(self):
        print('1 - Adicionar filme')
        print('2 - Remover filme')
        print('3 - Editar filme')
        print('4 - Listar filmes')
        print('5 - Vender ingresso')
        print('6 - Adicionar gêneros')
        print('7 - Lista gêneros')

    def escolhe_operacao(self):
        print('Escolha uma operação.')
        return int(input())

    def mostra_itens(self, codigo, nome, generos):
        print(f"\n{codigo}: {nome} ({generos})")

    def nenhum_filme(self):
        print("\nNenhum filme cadastrado.\n")

    def escolhe_codigo(self):
        return int(input('Insira um código: '))

    def escolhe_nome(self):
        return input('Insira um nome: ')

    def escolhe_quantidade(self):
        return int(input('Insira uma quantidade: '))

    def imprime_edicao(self):
        print('Edite o filme adicionando um gênero.')
