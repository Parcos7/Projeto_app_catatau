from DadosItens import DadosItens
estoque = []
def VerDados():
    for itens in estoque:
        itens.ApDados()

def cadastro():
    while True:
        sabor = input("Escolha o sabor a ser cadastrado: ").strip().lower()
        qnt = int(input("Escolha a quantidade: "))
        valor = float(input("Valor unitario?: "))
        item = DadosItens(sabor, qnt, valor, saldo = 0)
        estoque.append(item)
        escolha = input("Deseja cadastrar algo mais? (s/n): ").strip().lower()
        if escolha != "s":
            break
        
def v_total():
    vTotal =  0
    for itens in estoque:
        vTotal += itens.saldo
    return vTotal

def venda():
    while True:
        itemVenda = input("Qual item foi vendido? ").strip().lower()
        for itens in estoque:
            if itens.sabor == itemVenda:
                qntVendida = int(input("Qual a quantidade a ser vendida? "))
                itens.venda(qntVendida)
                VerDados()
                break
        break

def addItem():
    while True:    
        addI = input("Qual item deseja adicionar? ").strip().lower()
        for itens in estoque: 
            if itens.sabor == addI:
                qntADD = int(input("Quantidade que será Adcionado? "))
                itens.ADD(qntADD)
                break
        break

while True:
    x = int(input("Escolha:\n 1 - Cadastrar item\n 2 - Ver Dados\n 3 - Cadastrar Venda\n 4 - Adicionar item existente\n 5 - Valor Total\n"))
    match x:
        case 1:    
            cadastro()
        case 2:   
            VerDados()
        case 3: 
            venda()
        case 4:
            addItem()
        case 5:
            print(f"\nValor total vendido: R$ {v_total()}\n")
