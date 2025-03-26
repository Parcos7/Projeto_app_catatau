class DadosItens:
    def __init__(self, sabor, qnt, valor, saldo):
        self.sabor = sabor
        self.qnt = qnt
        self.valor = valor
        self.saldo = saldo
        
    def ApDados(self):
        print(f"\nNome: {self.sabor}\nQnt: {self.qnt}\nValor total por qnt: R$ {self.valor*self.qnt}\n ")

    def venda(self, qntVendida):
        if self.qnt >= qntVendida:
            self.qnt -= qntVendida
            self.saldo += self.valor * qntVendida
            print(f"\nVenda realizada! Agora restam {self.qnt} unidades de {self.sabor}.\n")
        else:
            print("\nEstoque insuficiente!")

    def ADD(self, qntADD):
        self.qnt += qntADD
        print("\nQuantidade adicionada!\n")
    
