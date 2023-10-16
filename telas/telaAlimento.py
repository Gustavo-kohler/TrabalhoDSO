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

    def mostra_itens(self, alimentos):
        if len(alimentos):
            print('\nCódigo: Alimento (Adicionais) -> preco\n')
            for alimento in alimentos:

                adicionais_str = ''
                if len(alimento.adicionais) > 0:
                    for adicionais in alimento.adicionais:
                        adicionais_str += adicionais.nome + ' '
                else:
                    adicionais_str = '-'
                print(
                    f"{alimento.codigo}: {alimento.nome} ({adicionais_str}) -> {alimento.preco}\n")
            return True
        else:
            print("\nNenhum alimento cadastrado\n")
            return False

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
