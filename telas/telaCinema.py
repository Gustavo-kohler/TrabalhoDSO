

class TelaCinema():
    def chama_bem_vindo(self, nome, cidade):
        print("Bem vindo ao cinema {nome} da cidade {cidade}")
        print("Selecione uma operação:")
        print("1 - Lanchonete\n2 - Filmes")

    def escolhe_operacao(self):
        return input("operação: ")
