class DadosItens:
    def __init__(self, sabor, qnt, valor):
        self.sabor = sabor
        self.qnt = qnt
        self.valor = valor
    
    def ApDados(self):
        print(f"\bNome: {self.sabor}\nQnt: {self.qnt}\nValor Total: {self.valor*self.qnt}\n")

    def venda(self, resul):
        if self.qnt >= resul:
            self.qnt -= resul
            print(f"Venda realizada! Agora restam {self.qnt} unidades de {self.sabor}.")
        else:
            print("Estoque insuficiente!")

    def ADD(self, resul):
        self.qnt += resul
        print("Quantidade adicionada!")