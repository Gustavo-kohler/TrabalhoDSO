from abstractTelaItens import AbstractTelaItens


class TelaFilme(AbstractTelaItens):
    def __imprime_operacoes(self):
        print('1 - Adicionar filme')
        print('2 - Remover filme')
        print('3 - Editar filme')
        print('4 - Listar filmes')
        print('5 - Vender ingresso')
        print('6 - Adicionar gêneros')
        print('7 - Lista gêneros')

    def escolhe_operacao(self):
        print('Escolha uma operação.')
        self.__imprime_operacoes()
        return int(input())

    def mostra_itens(self):
        print('Código: Filme')
        for filme in self.__filmes:
            print(f'{filme.codigo}: {filme.nome}')

    def escolhe_codigo(self):
        return int(input('Insira um código: '))

    def escolhe_nome(self):
        return input('Insira um nome: ')

    def imprime_edicao(self):
        print('Edite o filme adicionando um gênero.')
