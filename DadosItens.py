class DadosItens:
    def __init__(self, sabor, qnt, valor, saldo):
        self.sabor = sabor
        self.qnt = qnt
        self.valor = valor
        self.saldo = saldo

    def ApDados(self):
        print(f"\bNome: {self.sabor}\nQnt: {self.qnt}\nValor Total: {self.valor*self.qnt}\nValor Vendidos: {self.saldo}\n")

    def venda(self, resul):
        if self.qnt >= resul:
            self.qnt -= resul
            self.saldo += self.valor * self.qnt
            print(f"Venda realizada! Agora restam {self.qnt} unidades de {self.sabor}.")
        else:
            print("Estoque insuficiente!")

    def ADD(self, resul):
        self.qnt += resul
        print("Quantidade adicionada!")
