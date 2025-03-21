from DadosItens import DadosItens

estoque = []

def cadastro():
    while True:
        sabor = input("Escolha o sabor a ser cadastrado: ")
        qnt = int(input("Escolha a quantidade: "))
        valor = float(input("Valor unitario?: "))
        item = DadosItens(sabor, qnt, valor)
        estoque.append(item)
        escolha = input("Deseja cadastrar algo mais? (s/n)\n").strip().lower()
        if escolha != "s":
            break

def VerDados():
    for itens in estoque:
        itens.ApDados()

def venda():
    while True:
        itemVenda = input("Qual item foi vendido? ")
        for itens in estoque:
            if itens.sabor.lower() == itemVenda:
                qntVendida = int(input("Qual a quantidade a ser vendida? "))
                itens.venda(qntVendida)
                break

def addItem():
    while True:    
        addI = input("Qual item deseja adicionar? ")
        for itens in estoque: 
            if itens.sabor.lower() == addI:
                qntADD = int(input("Quantidade que será Adcionado? "))
                itens.ADD(qntADD)
                break

while True:
    x = int(input("Escolha:\n 1 - Cadastrar item\n 2 - Ver Dados\n 3 - Cadastrar Venda\n 4 - Adicionar item existente\n"))
    match x:
        case 1:    
            cadastro()
        case 2:   
            VerDados()
        case 3: 
            venda()
        case 4:
            addItem()
