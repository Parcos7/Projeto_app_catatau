class DadosItens:
    def __init__(self, sabor, qnt, valor, saldo):
        self.sabor = sabor
        self.qnt = qnt
        self.valor = valor
        self.saldo = saldo
        
    def ApDados(self):
        print(f"\bNome: {self.sabor}\nQnt: {self.qnt}\nValor total por qnt: R$ {self.valor*self.qnt}\n ")

    def venda(self, qntVendida):
        if self.qnt >= qntVendida:
            self.qnt -= qntVendida
            self.saldo += self.valor * qntVendida
            print(f"Venda realizada! Agora restam {self.qnt} unidades de {self.sabor}.\n")
        else:
            print("Estoque insuficiente!")

    def ADD(self, qntADD):
        self.qnt += qntADD
        print("Quantidade adicionada!")
    
