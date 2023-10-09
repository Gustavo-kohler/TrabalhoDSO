

class TelaCinema():
    def chama_bem_vindo(self, nome, cidade):
        print("Cinema {nome} da cidade {cidade}")
        print("Selecione uma operação:")
        print("1 - Lanchonete\n2 - Filmes\n3 - Desliga sistema")

    def escolhe_operacao(self):
        return input("operação: ")
