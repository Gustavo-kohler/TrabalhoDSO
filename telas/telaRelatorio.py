

class TelaRelatorio():
    def mostra_relatorio(self, codigo, nome, quantidade):
        print(f"\n({codigo}) {nome}: vendida(s) {quantidade} unidades(s).")

    def nenhum_relatorio(self):
        print("\nNenhum relatorio.\n")

    def mostra_total(self, total):
        print(f"\nTotal de vendas: R${total:.2f}")
