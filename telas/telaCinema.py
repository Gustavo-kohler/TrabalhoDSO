

class TelaCinema():
    def chama_bem_vindo(self, nome, cidade):
        print(f"\nCinema {nome} da cidade {cidade}")
        print("Selecione uma operação:")
        print("1 - Lanchonete\n2 - Filmes\n3 - Relatório\n4 - Desliga sistema")

    def escolhe_operacao(self):
        return input("operação: ")
