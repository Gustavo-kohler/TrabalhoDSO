

class TelaGenero():
    def mostra_generos(self, generos):
        print('Código: Gênero')
        for genero in generos:
            print(f'{genero.codigo}: {genero.nome}')

    def escolhe_nome(self):
        return input('Insira um nome: ')
