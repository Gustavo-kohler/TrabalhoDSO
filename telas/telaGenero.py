

class TelaGenero():
    def mostra_generos(self, generos):
        print('Código: Gênero')
        if len(generos) == 0:
            print('Não há gêneros.')
            return False
        for genero in generos:
            print(f'{genero.codigo}: {genero.nome}')
        return True

    def escolhe_nome(self):
        return input('Insira um nome: ')
